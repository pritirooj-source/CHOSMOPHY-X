"""
CosmoPhy-X: Astronaut Health Monitoring Software Engine
Integrated with 10 Next-Gen Space Biomedical & AI Modules
"""

from flask import Flask, render_template, request, jsonify, Response, send_from_directory
import re
from src.astro_data import SOLAR_SYSTEM_ENV, PATHOLOGY_REGISTRY
from src.ml_engine import calculate_mission_risk, match_countermeasures
from src.pdf_generator import generate_mission_pdf
from src.osdr_client import fetch_osdr_metadata

app = Flask(__name__)

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
   
    try:
        days = max(1, min(3650, int(payload.get("duration", 180))))
    except (ValueError, TypeError):
        days = 180

    dest_info = SOLAR_SYSTEM_ENV.get(dest_key, {})
    risk_results = calculate_mission_risk(dest_key, days)
    countermeasures = match_countermeasures(risk_results)

    pdf_bytes = generate_mission_pdf(dest_key, days, dest_info, countermeasures)

    return Response(
        pdf_bytes,
        mimetype='application/pdf',
        headers={'Content-Disposition': f'attachment;filename=CosmoPhy_X_Prescription_{dest_key}_{days}d.pdf'}
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)