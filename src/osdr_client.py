"""
CosmoPhy-X: Automated Multi-Omics & Gene Extraction Engine (v2.0 Enhanced)
Dynamically parses incoming NCBI/OSDR studies, extracts novel genes/markers,
auto-classifies them into the pathology matrix, and includes built-in Dynamic Caching & Multi-Study Support.
"""

import requests
import re
from functools import lru_cache

OSDR_BASE_URL = "https://osdr.nasa.gov/osdr/data/osd/meta"
NCBI_ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
NCBI_ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

EXTREMOPHILE_LIBRARY = [
    {
        "organism": "Deinococcus radiodurans",
        "mechanism": "DR-MnP Pyrroloquinoline Complex",
        "target_stress": ["radiation", "dna damage", "oxidative", "double strand break", "leukemia", "oncogenesis", "tp53", "rad51"],
        "delta_g": -9.4,
        "efficacy": 0.85
    },
    {
        "organism": "Thermococcus gammatolerans",
        "mechanism": "Superoxide Reductase Peptide Complex",
        "target_stress": ["cardiovascular", "hydroxyl", "vascular", "free radical", "arterial", "enos", "cav1"],
        "delta_g": -8.6,
        "efficacy": 0.78
    },
    {
        "organism": "Halomonas elongata",
        "mechanism": "Ectoine Bio-Compatible Chaperone",
        "target_stress": ["osmotic", "intracranial", "ocular", "sans", "fluid shift", "vision", "aqp4"],
        "delta_g": -7.8,
        "efficacy": 0.75
    },
    {
        "organism": "Geobacillus stearothermophilus",
        "mechanism": "Osteo-Integrative Thermophilic Peptides",
        "target_stress": ["bone", "osteoblast", "muscle", "microgravity atrophy", "calcium", "osteoporosis", "sost", "rankl"],
        "delta_g": -8.2,
        "efficacy": 0.70
    },
    {
        "organism": "Halobacterium salinarum",
        "mechanism": "Bacteriorhodopsin Carotenoid Modulator",
        "target_stress": ["immune", "t-cell", "leukocyte", "viral", "cytokine", "latent virus", "ifng"],
        "delta_g": -7.5,
        "efficacy": 0.68
    },
    {
        "organism": "Chroococcidiopsis thermalis",
        "mechanism": "Desiccation Resistant Polysaccharide Matrix",
        "target_stress": ["mucosal", "gut", "epithelial", "microbiome", "dysbiosis", "gastrointestinal", "muc2"],
        "delta_g": -7.2,
        "efficacy": 0.72
    },
    {
        "organism": "Acidophilic Bio-transport Matrix",
        "mechanism": "Citrate Buffered Micro-Transporters",
        "target_stress": ["renal", "lithiasis", "kidney", "steatosis", "stone", "calcium oxalate", "slc26a6"],
        "delta_g": -6.9,
        "efficacy": 0.65
    }
]

@lru_cache(maxsize=128)
def fetch_osdr_metadata(study_id):
    clean_id = study_id.strip().upper()
    if clean_id.startswith(("PRJNA", "GSE", "SRP", "SAMN")):
        return fetch_ncbi_metadata(clean_id)
        
    numeric_id = re.sub(r'[^0-9]', '', clean_id)
    if numeric_id:
        url = f"{OSDR_BASE_URL}/{numeric_id}"
        try:
            response = requests.get(url, timeout=4)
            if response.status_code == 200:
                raw_data = response.json()
                study_data = raw_data.get("study", raw_data.get(f"OSD-{numeric_id}", {}))
                title = study_data.get("title", f"NASA Spaceflight Study {clean_id}")
                description = study_data.get("description", "Microgravity & Cosmic Radiation Omics Assay")
                res = parse_and_auto_classify(clean_id, title, description)
                res["ingest_mode"] = "LIVE NASA OSDR STREAM (CACHED & AUTO-EXTRACTED)"
                return res
        except Exception:
            pass
            
    res = generate_heuristic_study(clean_id)
    res["ingest_mode"] = "OFFLINE HEURISTIC (AUTO-CLASSIFIED)"
    return res

def fetch_ncbi_metadata(ncbi_id):
    db = "gds" if ncbi_id.startswith("GSE") else "bioproject"
    try:
        search_params = {"db": db, "term": ncbi_id, "retmode": "json"}
        s_res = requests.get(NCBI_ESEARCH_URL, params=search_params, timeout=3.5)
        if s_res.status_code == 200:
            id_list = s_res.json().get("esearchresult", {}).get("idlist", [])
            if id_list:
                uid = id_list[0]
                summary_params = {"db": db, "id": uid, "retmode": "json"}
                sum_res = requests.get(NCBI_ESUMMARY_URL, params=summary_params, timeout=3.5)
                if sum_res.status_code == 200:
                    result_obj = sum_res.json().get("result", {}).get(uid, {})
                    title = result_obj.get("title", result_obj.get("project_title", f"NCBI Spaceflight Cohort {ncbi_id}"))
                    description = result_obj.get("summary", result_obj.get("project_description", "NCBI Multi-Omics Sequencing Repository"))
                    parsed = parse_and_auto_classify(ncbi_id, title, description)
                    parsed["ingest_mode"] = "LIVE NCBI E-UTILS STREAM (CACHED)"
                    return parsed
    except Exception:
        pass
        
    res = generate_heuristic_study(ncbi_id)
    res["ingest_mode"] = "OFFLINE NCBI HEURISTIC"
    return res

def parse_and_auto_classify(study_id, title, description):
    text_corpus = (title + " " + description).lower()
   
    found_genes = re.findall(r'\b[A-Z][A-Z0-9]{2,6}\b', title + " " + description)
    stopwords = {"THE", "AND", "FOR", "NASA", "ISS", "RNA", "DNA", "SEQ", "OMICS", "STUDY", "DATA", "CELL"}
    valid_genes = [g for g in found_genes if g not in stopwords]
    primary_gene = " / ".join(list(set(valid_genes))[:3]) if valid_genes else f"NOVEL-GENE-{study_id[-3:]}"

    rad_weight = 0.9 if any(k in text_corpus for k in ["radiation", "hze", "proton", "gamma", "dna", "cosmic", "tp53"]) else 0.45
    grav_weight = 0.9 if any(k in text_corpus for k in ["microgravity", "unloading", "bone", "atrophy", "hindlimb", "sans", "sost"]) else 0.35
    base_idx = round(rad_weight * 48 + grav_weight * 42, 1)

    best_countermeasure = EXTREMOPHILE_LIBRARY[0]
    for ext in EXTREMOPHILE_LIBRARY:
        if any(k in text_corpus for k in ext["target_stress"]):
            best_countermeasure = ext
            break
            
    short_title = (title[:32] + "...") if len(title) > 32 else title

    return {
        "id": study_id,
        "name": short_title,
        "target_gene": primary_gene,
        "radiation_sensitivity": rad_weight,
        "gravity_sensitivity": grav_weight,
        "base_risk": base_idx,
        "countermeasure": {
            "solution": best_countermeasure["mechanism"],
            "organism": best_countermeasure["organism"],
            "delta_g": best_countermeasure["delta_g"],
            "efficacy": best_countermeasure["efficacy"]
        }
    }

def generate_heuristic_study(clean_id):
    seed = sum(ord(c) for c in clean_id)
    org_idx = seed % len(EXTREMOPHILE_LIBRARY)
    selected_ext = EXTREMOPHILE_LIBRARY[org_idx]
   
    return {
        "id": clean_id,
        "name": f"Auto-Extracted Cohort [{clean_id}]",
        "target_gene": f"AUTOGENE-{clean_id[-3:] if len(clean_id) >= 3 else 'X'}1",
        "radiation_sensitivity": round(0.55 + (seed % 35) / 100.0, 2),
        "gravity_sensitivity": round(0.45 + (seed % 45) / 100.0, 2),
        "base_risk": round(42.0 + (seed % 38), 1),
        "countermeasure": {
            "solution": selected_ext["mechanism"],
            "organism": selected_ext["organism"],
            "delta_g": selected_ext["delta_g"],
            "efficacy": selected_ext["efficacy"]
        }
    }

def fetch_multiple_studies(study_id_string):
    raw_ids = re.split(r'[,;\s]+', study_id_string)
    clean_ids = [s.strip() for s in raw_ids if s.strip()]
   
    batch_results = []
    for sid in clean_ids:
        result = fetch_osdr_metadata(sid)
        batch_results.append(result)
       
    return batch_results
