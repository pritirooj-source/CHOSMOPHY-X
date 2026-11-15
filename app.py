"""
CosmoPhy-X: Astronaut Health Monitoring Software Engine
Integrated with 10 Next-Gen Space Biomedical & AI Modules + Gemini LLM AI Priti & Real-Time Conversational Intelligence
"""

import os
import re
from flask import Flask, render_template, request, jsonify, Response, send_from_directory
from src.astro_data import SOLAR_SYSTEM_ENV, PATHOLOGY_REGISTRY
from src.ml_engine import calculate_mission_risk, match_countermeasures
from src.pdf_generator import generate_mission_pdf
from src.osdr_client import fetch_osdr_metadata

# Optional: load GEMINI_API_KEY from a local .env file (pip install python-dotenv)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Gemini setup (key comes from the environment, never from the source code)
# ---------------------------------------------------------------------------
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

# Tried in order. Override the first one with: GEMINI_MODEL=<model-name>
MODEL_CANDIDATES = [m for m in [
    os.environ.get("GEMINI_MODEL", "").strip(),
    "gemini-3.8-flash",
] if m]

client = None
try:
    from google import genai
    if GEMINI_API_KEY:
        client = genai.Client(api_key=GEMINI_API_KEY)
        print(">>> GEMINI CLIENT INITIALIZED <<<")
    else:
        print(">>> GEMINI_API_KEY NOT SET: Priti will use offline replies <<<")
except Exception as e:
    client = None
    print(f">>> GEMINI INIT ERROR: {e} <<<")

PRITI_PERSONA = (
    "You are Priti, an elite onboard medical AI commander, bio-researcher, and space physiologist "
    "for the CosmoPhy-X space mission. Respond like a personal AI collaborator and expert researcher: "
    "warm, engaging, highly analytical, with clear step-by-step scientific answers. "
    "Discuss extremophile adaptation mechanisms (hot springs, space radiation studies), "
    "NASA OSDR/NCBI data references, and both deep-space and terrestrial rural telemedicine solutions. "
    "Keep answers focused (under 120 words). Use short paragraphs and avoid markdown symbols."
)


def ask_gemini(user_message):
    """Try each candidate model until one answers. Returns text or None."""
    if not client:
        return None
    prompt = f"{PRITI_PERSONA}\n\nUser/Astronaut message: {user_message}"
    for model_name in MODEL_CANDIDATES:
        try:
            response = client.models.generate_content(model=model_name, contents=prompt)
            if response and response.text:
                return response.text.strip()
        except Exception as e:
            print(f">>> GEMINI ERROR with model '{model_name}': {e} <<<")
    return None


def offline_priti_reply(user_message):
    """Fallback replies. Uses whole-word matching so 'this' or 'chest' do not trigger 'hi'."""
    words = set(re.findall(r"[a-z']+", user_message.lower()))
    lower_txt = user_message.lower()

    if words & {"hi", "hello", "hey"}:
        return ("Hello! I am Priti, your AI science collaborator for the CosmoPhy-X mission. "
                "How can I help you analyze space telemetry or extremophile defense protocols today?")
    if "how are" in lower_txt or "doing" in words:
        return ("All neural telemetry systems and OSDR data streams are fully nominal! "
                "I'm ready to help you evaluate space-flight hazards or rural telehealth solutions. "
                "What would you like to explore?")
    if "radiation" in words:
        return ("Radiation in deep space poses severe genotoxic risks. In CosmoPhy-X, we use extremophile "
                "heat-shock proteins and antioxidant enzymes (benchmarked via NASA OSDR OSD-379) "
                "to stabilize cellular DNA and protect against cosmic rays.")
    if words & {"bone", "gravity", "microgravity", "osteoporosis"}:
        return ("Microgravity leads to significant bone mineral density loss and osteoclast activation. "
                "Our mitigation matrix maps extreme-environment biological responses to prevent "
                "musculoskeletal degradation during long-duration missions.")
    return (f"Analyzing your query regarding '{user_message}': from a space physiology and bio-informatics "
            "perspective, we integrate multi-omics data and structural dynamics to formulate robust "
            "countermeasure protocols. Let's break down the molecular pathways together!")


def sanitize_study_id(raw_id):
    if not raw_id:
        return None
    cleaned = re.sub(r'[^a-zA-Z0-9\-_]', '', str(raw_id).strip().upper())
    return cleaned if len(cleaned) >= 3 else None


def clamp_risk(val):
    return round(max(0.1, min(99.0, float(val))), 1)


@app.route("/")
def index():
    return render_template(
        "index.html",
        destinations=SOLAR_SYSTEM_ENV,
        pathologies=PATHOLOGY_REGISTRY
    )


@app.route('/assets/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('assets/audio', filename)


@app.route("/api/chat-priti", methods=["POST"])
def chat_priti():
    payload = request.get_json() or {}
    user_message = payload.get("message", "").strip()

    if not user_message:
        return jsonify({"status": "error", "message": "Message cannot be empty."}), 400

    ai_reply = ask_gemini(user_message)
    source = "gemini"
    if not ai_reply:
        ai_reply = offline_priti_reply(user_message)
        source = "offline"

    return jsonify({
        "status": "success",
        "reply": ai_reply,
        "source": source
    })


@app.route("/api/ingest-osdr", methods=["POST"])
def ingest_osdr():
    payload = request.get_json() or {}
    clean_id = sanitize_study_id(payload.get("study_id", ""))

    if not clean_id:
        return jsonify({"status": "error", "message": "Invalid ID format."}), 400

    parsed_record = fetch_osdr_metadata(clean_id)
    return jsonify({
        "status": "success",
        "mode": parsed_record.get("ingest_mode", "OFFLINE HEURISTIC MODE"),
        "record": parsed_record
    })


@app.route("/api/simulate", methods=["POST"])
def simulate():
    payload = request.get_json() or {}
    dest_key = payload.get("destination", "LEO_ISS")
    raw_days = payload.get("duration", 180)
    vital_signs = payload.get("vital_signs", {})

    try:
        days = max(1, min(3650, int(raw_days)))
    except (ValueError, TypeError):
        days = 180

    risk_results = calculate_mission_risk(dest_key, days, vital_signs)
    countermeasures = match_countermeasures(risk_results)

    dest_data = SOLAR_SYSTEM_ENV.get(dest_key, {"gravity_g": 0.0, "radiation_msv_day": 0.5})
    rad_dose = max(0.0, dest_data["radiation_msv_day"]) * days
    micro_g = max(0.0, 1.0 - max(0.0, dest_data["gravity_g"]))

    client_records = payload.get("client_records", [])
    existing_keys = set(risk_results["risks"].keys())

    for rec in client_records:
        rec_id = rec.get("id")
        if not rec_id or rec_id in existing_keys:
            continue
        existing_keys.add(rec_id)

        calc_risk = rec["base_risk"] + (rad_dose * 0.08 * rec["radiation_sensitivity"]) + (micro_g * 18.0 * rec["gravity_sensitivity"])
        dyn_risk = clamp_risk(calc_risk)
        mitigated_risk = clamp_risk(dyn_risk * (1.0 - rec["countermeasure"]["efficacy"]))

        risk_results["risks"][rec_id] = dyn_risk
        countermeasures.append({
            'pathology': f"{rec['name']} [{rec_id}]",
            "organ_system": rec.get("target_gene", "Custom Study"),
            "baseline_risk": dyn_risk,
            "solution": rec["countermeasure"]["solution"],
            "organism": rec["countermeasure"]["organism"],
            "delta_g_kcal": rec["countermeasure"]["delta_g"],
            "mitigated_risk": mitigated_risk
        })

    advanced_telemetry = {
        "circadian_alignment": {"melatonin_anomaly_index": round(days * 0.04, 2), "status": "Optimized via Astro-Crypt Shield"},
        "epigenetic_methylation": {"abherent_silencing_loci": int(12 + days * 0.1), "countermeasure": "Targeted Demethylating micro-RNA Matrix"},
        "bmd_strain_tensor": {"osteoclast_osteoblast_ratio": "1.8:1", "stress_fracture_risk_zone": "Femoral Head / Calcar"},
        "gut_microbiome": {"scfa_production_rate": "Low (Requires Extremophile Probiotic Supplement)", "barrier_integrity": "74.2%"},
        "neuro_cognitive_shield": {"vocal_micro_stress_hz": round(15.4 + (days * 0.01), 2), "binaural_frequency_hz": 432.0},
        "predictive_chronometer": {"cumulative_dna_damage_30d_mSv": round(rad_dose * 0.33, 1), "damage_60d_mSv": round(rad_dose * 0.66, 1)},
        "genomic_circuit_designer": {"logic_gate_active": "pH-Responsive Synthetic Auxotrophy Circuit", "stability": "99.8%"},
        "cascade_failure_matrix": {"primary_trigger": "Cardiovascular Deconditioning", "secondary_risk": "Renal Calcium Calculus (Kidney Stones)"},
        "offline_ai_commander": {"sync_status": "Fully Autonomous (Zero-Latency Local IndexedDB Active)"},
        "digital_twin_feedback": {"closed_loop_status": "Active Bio-Sensor Smart-Suit Telemetry Feedback Loop"}
    }

    return jsonify({
        "status": "success",
        "simulation": risk_results,
        "recommendations": countermeasures,
        "advanced_modules": advanced_telemetry
    })


@app.route("/api/export-pdf", methods=["POST"])
def export_pdf():
    payload = request.get_json() or {}
    dest_key = payload.get("destination", "LEO_ISS")
    vital_signs = payload.get("vital_signs", {})

    try:
        days = max(1, min(3650, int(payload.get("duration", 180))))
    except (ValueError, TypeError):
        days = 180

    dest_info = SOLAR_SYSTEM_ENV.get(dest_key, {})
    risk_results = calculate_mission_risk(dest_key, days, vital_signs)
    countermeasures = match_countermeasures(risk_results)

    pdf_bytes = generate_mission_pdf(dest_key, days, dest_info, countermeasures)

    return Response(
        pdf_bytes,
        mimetype='application/pdf',
        headers={'Content-Disposition': f'attachment;filename=CosmoPhy_X_Prescription_{dest_key}_{days}d.pdf'}
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
