"""
CosmoPhy-X: Universal Multi-Omics & Vital Signs Dynamic Simulation Engine
"""

from src.astro_data import SOLAR_SYSTEM_ENV, PATHOLOGY_REGISTRY

def calculate_mission_risk(destination_key, duration_days, vital_signs=None):
    dest = SOLAR_SYSTEM_ENV.get(destination_key, SOLAR_SYSTEM_ENV["LEO_ISS"])
    duration = max(1, min(3650, int(duration_days)))
    
    radiation_dose = max(0.0, dest["radiation_msv_day"]) * duration
    microgravity = max(0.0, 1.0 - max(0.0, dest["gravity_g"]))
    
    risks = {}
    for p_id, data in PATHOLOGY_REGISTRY.items():
        base = data["base_risk"]
        grav_impact = microgravity * (data["gravity_factor"] * 24.0)
        
        # Non-linear exponential/growth penalty for long-duration deep space radiation
        rad_impact = (radiation_dose ** 1.05 * 0.05) * data["radiation_factor"]
        
        # Vital signs penalty integration for health monitoring challenge
        vital_penalty = 0.0
        if vital_signs:
            if p_id == "vital_cardio_bp" and float(vital_signs.get("bp_systolic", 120)) > 140:
                vital_penalty = 15.0
            if p_id == "vital_metabolic_sugar" and float(vital_signs.get("blood_sugar", 100)) > 126:
                vital_penalty = 18.0
            if p_id == "vital_neuro_sleep_mood" and float(vital_signs.get("sleep_hours", 8)) < 6:
                vital_penalty = 20.0

        calc = round(max(0.1, min(99.0, base + grav_impact + rad_impact + vital_penalty)), 1)
        risks[p_id] = calc
        
    return {
        "destination": dest["name"],
        "destination_key": destination_key,
        "duration_days": duration,
        "total_radiation_msv": round(radiation_dose, 2),
        "risks": risks
    }

def match_countermeasures(risk_results):
    recommendations = []
    risks = risk_results.get("risks", {})
    dest_key = risk_results.get("destination_key", "LEO_ISS")
    duration = risk_results.get("duration_days", 180)
    
    high_stress_destinations = ["EUROPA_ORBIT", "DEEP_SPACE_TRANSIT", "MERCURY_ORBIT", "CERES_ASTEROID", "EUROPA_SUBSURFACE"]
    use_intense_tier = (duration >= 300) or (dest_key in high_stress_destinations)
    
    for p_id, r_val in risks.items():
        if p_id in PATHOLOGY_REGISTRY:
            reg = PATHOLOGY_REGISTRY[p_id]
            tiered = reg["countermeasures_tiered"]
            
            tier_key = "intense" if (use_intense_tier or r_val > 55.0) else "standard"
            cm = tiered[tier_key]
            
            mitigated = round(max(0.1, min(99.0, r_val * (1.0 - cm["efficacy"]))), 1)
            recommendations.append({
                "pathology": reg["label"],
                "organ_system": reg.get("organ_system", "Systemic"),
                "baseline_risk": r_val,
                "solution": cm["solution"],
                "organism": cm["organism"],
                "delta_g_kcal": cm["delta_g"],
                "mitigated_risk": mitigated,
                "tier": tier_key.upper()
            })
    return recommendations
