"""
CosmoPhy-X: Comprehensive Solar System Planetary Environments & Astronaut Vital Signs Matrix
"""

SOLAR_SYSTEM_ENV = {
    "LEO_ISS": {
        "name": "Low Earth Orbit (ISS Station)",
        "gravity_g": 0.0,
        "radiation_msv_day": 0.50,
        "atmosphere_psi": 14.7
    },
    "GEO_STATION": {
        "name": "Geostationary High Orbit (GEO)",
        "gravity_g": 0.0,
        "radiation_msv_day": 1.20,
        "atmosphere_psi": 0.0
    },
    "LUNAR_BASE": {
        "name": "Moon - Shackleton Polar Base",
        "gravity_g": 0.166,
        "radiation_msv_day": 1.37,
        "atmosphere_psi": 0.0
    },
    "MERCURY_POLAR": {
        "name": "Mercury - Polar Crater Base",
        "gravity_g": 0.38,
        "radiation_msv_day": 2.10,
        "atmosphere_psi": 0.0
    },
    "VENUS_ATMOSPHERE": {
        "name": "Venus - Cloud Colony (55 km Altitude)",
        "gravity_g": 0.90,
        "radiation_msv_day": 0.40,
        "atmosphere_psi": 14.2
    },
    "MARS_SURFACE": {
        "name": "Mars - Jezero Surface Outpost",
        "gravity_g": 0.38,
        "radiation_msv_day": 0.70,
        "atmosphere_psi": 0.09
    },
    "PHOBOS_BASE": {
        "name": "Phobos - Martian Orbital Waystation",
        "gravity_g": 0.00057,
        "radiation_msv_day": 1.75,
        "atmosphere_psi": 0.0
    },
    "CERES_BASE": {
        "name": "Ceres - Main Asteroid Belt Hub",
        "gravity_g": 0.028,
        "radiation_msv_day": 1.45,
        "atmosphere_psi": 0.0
    },
    "JUPITER_ORBIT": {
        "name": "Jupiter - High Radiation Exclusion Orbit",
        "gravity_g": 2.528,
        "radiation_msv_day": 12.50,
        "atmosphere_psi": 0.0
    },
    "EUROPA_SUBSURFACE": {
        "name": "Europa - Ice-Crust Marine Research Post",
        "gravity_g": 0.134,
        "radiation_msv_day": 5.40,
        "atmosphere_psi": 0.0
    },
    "GANYMEDE_BASE": {
        "name": "Ganymede - Magnetic Outpost",
        "gravity_g": 0.146,
        "radiation_msv_day": 0.80,
        "atmosphere_psi": 0.0
    },
    "CALLISTO_BASE": {
        "name": "Callisto - Low-Radiation Jovian Platform",
        "gravity_g": 0.126,
        "radiation_msv_day": 0.35,
        "atmosphere_psi": 0.0
    },
    "TITAN_EXPEDITION": {
        "name": "Titan - Hydrocarbon Coast Outpost",
        "gravity_g": 0.138,
        "radiation_msv_day": 0.25,
        "atmosphere_psi": 21.3
    },
    "ENCELADUS_BASE": {
        "name": "Enceladus - Cryovolcanic Vent Lab",
        "gravity_g": 0.011,
        "radiation_msv_day": 0.65,
        "atmosphere_psi": 0.0
    },
    "PLUTO_OUTPOST": {
        "name": "Pluto - Kuiper Belt Rim Observatory",
        "gravity_g": 0.063,
        "radiation_msv_day": 1.95,
        "atmosphere_psi": 0.0001
    },
    "DEEP_SPACE_TRANSIT": {
        "name": "Interplanetary Heliocentric Transit (Mars/Jupiter Corridors)",
        "gravity_g": 0.0,
        "radiation_msv_day": 1.84,
        "atmosphere_psi": 10.2
    }
}

PATHOLOGY_REGISTRY = {
    "vital_cardio_bp": {
        "organ_system": "Cardiovascular & Blood Pressure",
        "label": "Astronaut Vital Sign: Blood Pressure & Arterial Dynamics",
        "target_gene": "eNOS / CAV1 / SOD2",
        "base_risk": 42.0,
        "gravity_factor": 0.85,
        "radiation_factor": 0.35,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Thermococcus gammatolerans",
                "solution": "Targeted Hydroxyl Radical Scavenger Peptides",
                "delta_g": -8.6,
                "efficacy": 0.78
            },
            "intense": {
                "organism": "Pyrococcus yayanosii",
                "solution": "Barophilic Nitric Oxide Synthetase Stabilizer",
                "delta_g": -9.5,
                "efficacy": 0.87
            }
        }
    },
    "vital_metabolic_sugar": {
        "organ_system": "Pancreas & Blood Glucose",
        "label": "Astronaut Vital Sign: Blood Sugar & Glycemic Index",
        "target_gene": "INS / PDX1 / ABCB4",
        "base_risk": 24.0,
        "gravity_factor": 0.55,
        "radiation_factor": 0.35,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Sulfolobus solfataricus",
                "solution": "Thermo-Stable Amylolytic Metabolic Regulators",
                "delta_g": -7.6,
                "efficacy": 0.66
            },
            "intense": {
                "organism": "Thermotoga maritima",
                "solution": "Hyperthermostable Glycemic Glucose-Insulin Transporters",
                "delta_g": -8.6,
                "efficacy": 0.79
            }
        }
    },
    "vital_neuro_sleep_mood": {
        "organ_system": "Brain & CNS (Sleep & Mood)",
        "label": "Astronaut Vital Sign: Daily Sleep Hours & Behavioral Mood Status",
        "target_gene": "BDNF / CLOCK / ARNTL",
        "base_risk": 27.0,
        "gravity_factor": 0.35,
        "radiation_factor": 0.80,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Pyrococcus furiosus",
                "solution": "Hyperthermostable Neuro-Protective Chaperonins",
                "delta_g": -8.9,
                "efficacy": 0.76
            },
            "intense": {
                "organism": "Nostoc punctiforme",
                "solution": "Hypothalamic Neuropeptide Protection Peptide",
                "delta_g": -9.0,
                "efficacy": 0.85
            }
        }
    },
    "musculoskeletal": {
        "organ_system": "Skeletal & Muscular",
        "label": "Space Osteoporosis & Muscle Atrophy",
        "target_gene": "SOST / RANKL / MYOD1",
        "base_risk": 48.0,
        "gravity_factor": 0.95,
        "radiation_factor": 0.15,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Geobacillus stearothermophilus",
                "solution": "Osteoblast-Stimulating Bioactive Peptides",
                "delta_g": -8.2,
                "efficacy": 0.70
            },
            "intense": {
                "organism": "Thermococcus kodakarensis",
                "solution": "Hyper-Mineralizing Calmodulin Chaperone Matrix",
                "delta_g": -9.3,
                "efficacy": 0.82
            }
        }
    },
    "cardiovascular": {
        "organ_system": "Cardiovascular & Heart",
        "label": "Cardiovascular Deconditioning & Arterial Stiffness",
        "target_gene": "eNOS / CAV1 / SOD2",
        "base_risk": 42.0,
        "gravity_factor": 0.85,
        "radiation_factor": 0.35,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Thermococcus gammatolerans",
                "solution": "Targeted Hydroxyl Radical Scavenger Peptides",
                "delta_g": -8.6,
                "efficacy": 0.78
            },
            "intense": {
                "organism": "Pyrococcus yayanosii",
                "solution": "Barophilic Nitric Oxide Synthetase Stabilizer",
                "delta_g": -9.5,
                "efficacy": 0.87
            }
        }
    },
    "ocular": {
        "organ_system": "Ocular (Eye & Optic Nerve)",
        "label": "Neuro-Ocular Syndrome (SANS) & Papilledema",
        "target_gene": "AQP4 / MTHFR / VEGF",
        "base_risk": 45.0,
        "gravity_factor": 0.90,
        "radiation_factor": 0.10,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Halomonas elongata",
                "solution": "Ectoine Bio-Buffer Osmoprotectant",
                "delta_g": -7.8,
                "efficacy": 0.75
            },
            "intense": {
                "organism": "Salinibacter ruber",
                "solution": "Hyper-Halophilic Intracranial Pressure Modulator",
                "delta_g": -8.9,
                "efficacy": 0.84
            }
        }
    },
    "auditory_vestibular": {
        "organ_system": "Inner Ear & Vestibular Balance",
        "label": "Space Motion Sickness & Otolith Deconditioning",
        "target_gene": "OTOG / COCH / KCNQ4",
        "base_risk": 38.0,
        "gravity_factor": 0.92,
        "radiation_factor": 0.08,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Bacillus subtilis",
                "solution": "Endolymph Osmolyte Stabilizing Formulation",
                "delta_g": -7.1,
                "efficacy": 0.65
            },
            "intense": {
                "organism": "Desulfovibrio magneticus",
                "solution": "Magneto-Tactile Stereocilia Mechanical Cushion",
                "delta_g": -8.4,
                "efficacy": 0.79
            }
        }
    },
    "brain_cns": {
        "organ_system": "Brain & Central Nervous System",
        "label": "Cosmic Ray Neuro-Degeneration & Synaptic Decay",
        "target_gene": "BDNF / SYN1 / MAPT",
        "base_risk": 25.0,
        "gravity_factor": 0.30,
        "radiation_factor": 0.88,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Pyrococcus furiosus",
                "solution": "Hyperthermostable Neuro-Protective Chaperonins",
                "delta_g": -8.9,
                "efficacy": 0.76
            },
            "intense": {
                "organism": "Deinococcus geothermalis",
                "solution": "Heavy Ion Synaptic Cleavage Repair Nano-Enzymes",
                "delta_g": -9.8,
                "efficacy": 0.88
            }
        }
    },
    "pulmonary": {
        "organ_system": "Lungs & Respiratory Tract",
        "label": "Alveolar Lunar Dust Toxicity & Pulmonary Fibrosis",
        "target_gene": "SFTPC / TGFB1 / IL6",
        "base_risk": 20.0,
        "gravity_factor": 0.40,
        "radiation_factor": 0.50,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Thermus thermophilus",
                "solution": "Anti-Fibrotic Extremolytic Aerosol Formulation",
                "delta_g": -7.7,
                "efficacy": 0.71
            },
            "intense": {
                "organism": "Metallosphaera sedula",
                "solution": "Heavy-Metal Chelating Bio-Surfactant Inhalant",
                "delta_g": -9.1,
                "efficacy": 0.85
            }
        }
    },
    "gastrointestinal": {
        "organ_system": "Stomach & Intestines",
        "label": "Gastrointestinal Dysbiosis & Mucosal Degradation",
        "target_gene": "MUC2 / TJP1 / CLDN1",
        "base_risk": 32.0,
        "gravity_factor": 0.50,
        "radiation_factor": 0.40,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Chroococcidiopsis thermalis",
                "solution": "Engineered Pre-biotic Mucosal Matrix",
                "delta_g": -7.2,
                "efficacy": 0.72
            },
            "intense": {
                "organism": "Methanothermococcus okinawensis",
                "solution": "Anaerobic Gut Crypt Epithelial Sealant",
                "delta_g": -8.7,
                "efficacy": 0.83
            }
        }
    },
    "hepatic": {
        "organ_system": "Liver & Hepatic Metabolism",
        "label": "Spaceflight Hepatic Steatosis & Phase-I Enzyme Decay",
        "target_gene": "CYP2E1 / PPARG / CD36",
        "base_risk": 30.0,
        "gravity_factor": 0.60,
        "radiation_factor": 0.45,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Methanocaldococcus jannaschii",
                "solution": "Redox-Buffering Coenzyme F420 Analog",
                "delta_g": -7.3,
                "efficacy": 0.67
            },
            "intense": {
                "organism": "Picrophilus torridus",
                "solution": "Acid-Tolerant Lipid Peroxidation Suppressor Complex",
                "delta_g": -8.8,
                "efficacy": 0.80
            }
        }
    },
    "pancreatic_biliary": {
        "organ_system": "Pancreas & Gallbladder",
        "label": "Beta-Cell Insulin Secretory Stress & Biliary Sludge",
        "target_gene": "INS / PDX1 / ABCB4",
        "base_risk": 24.0,
        "gravity_factor": 0.55,
        "radiation_factor": 0.35,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Sulfolobus solfataricus",
                "solution": "Thermo-Stable Amylolytic Metabolic Regulators",
                "delta_g": -7.6,
                "efficacy": 0.66
            },
            "intense": {
                "organism": "Thermotoga maritima",
                "solution": "Hyperthermostable Glycemic Glucose-Insulin Transporters",
                "delta_g": -8.6,
                "efficacy": 0.79
            }
        }
    },
    "splenic_lymphatic": {
        "organ_system": "Spleen & Lymphatic Nodes",
        "label": "Splenic Lymphocyte Depletion & T-Cell Exhaustion",
        "target_gene": "IFNG / IL2 / NFKB1",
        "base_risk": 28.0,
        "gravity_factor": 0.45,
        "radiation_factor": 0.55,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Halobacterium salinarum",
                "solution": "Carotenoid-Derived Immunomodulators",
                "delta_g": -7.5,
                "efficacy": 0.68
            },
            "intense": {
                "organism": "Deinococcus proteolyticus",
                "solution": "Leukocyte Nuclear Clumping Shielding Peptide",
                "delta_g": -9.2,
                "efficacy": 0.86
            }
        }
    },
    "renal": {
        "organ_system": "Kidneys (Renal Parenchyma)",
        "label": "Renal Lithiasis (Kidney Stones) & Calciuria",
        "target_gene": "SLC26A6 / CASR",
        "base_risk": 35.0,
        "gravity_factor": 0.70,
        "radiation_factor": 0.20,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Acidophilic Bio-transport Matrix",
                "solution": "Citrate Buffered Micro-Transporters",
                "delta_g": -6.9,
                "efficacy": 0.65
            },
            "intense": {
                "organism": "Ferroplasma acidiphilum",
                "solution": "Calcium Oxalate Chelation Nano-Carriers",
                "delta_g": -8.5,
                "efficacy": 0.81
            }
        }
    },
    "bladder_urinary": {
        "organ_system": "Bladder & Urinary Tract",
        "label": "Detrusor Hyporeflexia & Microgravity Urinary Stasis",
        "target_gene": "UPK1A / CHRM3",
        "base_risk": 22.0,
        "gravity_factor": 0.65,
        "radiation_factor": 0.15,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Pseudomonas putida",
                "solution": "Urothelial Glycocalyx Protective Exopolysaccharides",
                "delta_g": -6.8,
                "efficacy": 0.63
            },
            "intense": {
                "organism": "Alkaliphilus transvaalensis",
                "solution": "Contractile Myocyte pH Resilient Bio-Stimulants",
                "delta_g": -8.3,
                "efficacy": 0.77
            }
        }
    },
    "hematopoietic": {
        "organ_system": "Bone Marrow & Circulatory Blood",
        "label": "Radiation Oncogenesis, Leukemia & Genomic Instability",
        "target_gene": "TP53 / ATM / RAD51 / H2AX",
        "base_risk": 15.0,
        "gravity_factor": 0.10,
        "radiation_factor": 0.95,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Deinococcus radiodurans",
                "solution": "DR-MnP Manganese Complex Antioxidant",
                "delta_g": -9.4,
                "efficacy": 0.85
            },
            "intense": {
                "organism": "Deinococcus radiodurans R1-Engineered",
                "solution": "High-LET RecA Homologous Recombination Synthesizers",
                "delta_g": -10.4,
                "efficacy": 0.93
            }
        }
    },
    "integumentary": {
        "organ_system": "Skin & Epithelium",
        "label": "Cosmic Epithelial Desquamation & Radiation Dermatitis",
        "target_gene": "COL1A1 / ELN / MMP1",
        "base_risk": 22.0,
        "gravity_factor": 0.15,
        "radiation_factor": 0.80,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Rubrobacter radiotolerans",
                "solution": "Bacterioruberin Carotenoid Dermal Coating",
                "delta_g": -7.9,
                "efficacy": 0.74
            },
            "intense": {
                "organism": "Cyanothece sp. ATCC 51142",
                "solution": "Scytonemin UV/GCR Sunscreen Epithelial Hydrogel",
                "delta_g": -9.0,
                "efficacy": 0.86
            }
        }
    },
    "thyroid_endocrine": {
        "organ_system": "Thyroid & Adrenal Glands",
        "label": "Thyroid Follicular Radiation Damage & Cortisol Flux",
        "target_gene": "TSHR / TG / NR3C1",
        "base_risk": 26.0,
        "gravity_factor": 0.35,
        "radiation_factor": 0.75,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Synechococcus elongatus",
                "solution": "KaiABC Synthetic Circadian Phase Resonator",
                "delta_g": -8.1,
                "efficacy": 0.69
            },
            "intense": {
                "organism": "Gloeocapsa sp. OU_20",
                "solution": "Radio-Protective Thyroglobulin Shielding Scaffolds",
                "delta_g": -9.2,
                "efficacy": 0.83
            }
        }
    },
    "reproductive": {
        "organ_system": "Reproductive (Gonadal Tissue)",
        "label": "Cosmic Ionizing Gametogenesis Damage & Mutagenesis",
        "target_gene": "DAZL / SYCP3 / AMH",
        "base_risk": 18.0,
        "gravity_factor": 0.20,
        "radiation_factor": 0.92,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Acinetobacter radioresistens",
                "solution": "Poly-Radioprotective Radical-Trapping Peptides",
                "delta_g": -8.8,
                "efficacy": 0.81
            },
            "intense": {
                "organism": "Thermococcus kodakarensis KOD1",
                "solution": "Germline Chromatin Condensation & Repair Enzymes",
                "delta_g": -10.1,
                "efficacy": 0.91
            }
        }
    },
    "olfactory_nasal": {
        "organ_system": "Nasal Mucosa & Olfactory Epithelium",
        "label": "Olfactory Receptor Desensitization & Sinusitis",
        "target_gene": "OR5AN1 / GNAL / ANO2",
        "base_risk": 21.0,
        "gravity_factor": 0.30,
        "radiation_factor": 0.50,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Polaromonas vacuolata",
                "solution": "Psychrophilic Mucosal Humectant Spray",
                "delta_g": -7.0,
                "efficacy": 0.66
            },
            "intense": {
                "organism": "Psychromonas ingrahamii",
                "solution": "Ciliated Epithelial Odorant Receptor Stabilizer",
                "delta_g": -8.2,
                "efficacy": 0.78
            }
        }
    },
    "salivary_oral": {
        "organ_system": "Oral Cavity & Salivary Glands",
        "label": "Microgravity Xerostomia & Enamel Demineralization",
        "target_gene": "MUC7 / AMTN / HTN1",
        "base_risk": 24.0,
        "gravity_factor": 0.45,
        "radiation_factor": 0.30,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Streptococcus thermophilus",
                "solution": "Bio-Remineralizing Salivary Buffer Matrix",
                "delta_g": -7.3,
                "efficacy": 0.68
            },
            "intense": {
                "organism": "Lactobacillus hilgardii",
                "solution": "Enamel Hydroxyapatite Nano-Replenisher",
                "delta_g": -8.4,
                "efficacy": 0.80
            }
        }
    },
    "esophageal_gi": {
        "organ_system": "Esophagus & Upper GI Tract",
        "label": "Zero-G Reflux Esophagitis & Mucosal Erosion",
        "target_gene": "TJP2 / OCLN / CASP3",
        "base_risk": 29.0,
        "gravity_factor": 0.70,
        "radiation_factor": 0.25,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Natronomonas pharaonis",
                "solution": "Alkaliphilic Esophageal Acid-Barrier Gel",
                "delta_g": -7.5,
                "efficacy": 0.70
            },
            "intense": {
                "organism": "Natronobacterium gregoryi",
                "solution": "Sub-Mucosal Sphincter Tone Biopolymer",
                "delta_g": -8.6,
                "efficacy": 0.82
            }
        }
    },
    "skin_microbiome": {
        "organ_system": "Cutaneous Microbiome & Dermis",
        "label": "Spaceflight Cutaneous Dysbiosis & Barrier Breakdown",
        "target_gene": "FLG / LCE1A / DEFB4A",
        "base_risk": 23.0,
        "gravity_factor": 0.25,
        "radiation_factor": 0.60,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Staphylococcus epidermidis SP",
                "solution": "Commensal Symbiotic Lipid Restorer",
                "delta_g": -7.1,
                "efficacy": 0.67
            },
            "intense": {
                "organism": "Rubrobacter xylanophilus",
                "solution": "Radio-Resistant Stratum Corneum Shield",
                "delta_g": -8.5,
                "efficacy": 0.81
            }
        }
    },
    "adrenal_stress": {
        "organ_system": "Adrenal Cortex & Medulla",
        "label": "Chronic Hypercortisolemia & Adrenal Exhaustion",
        "target_gene": "CRHR1 / MC2R / POMC",
        "base_risk": 33.0,
        "gravity_factor": 0.40,
        "radiation_factor": 0.65,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Synechocystis sp. PCC 6803",
                "solution": "Adaptogenic Catecholamine Regulation Matrix",
                "delta_g": -7.6,
                "efficacy": 0.71
            },
            "intense": {
                "organism": "Chlorogloeopsis fritschii",
                "solution": "Adrenocortical Redox Homeostasis Enzyme",
                "delta_g": -8.9,
                "efficacy": 0.84
            }
        }
    },
    "pituitary_hypothalamus": {
        "organ_system": "Pituitary & Hypothalamus Axis",
        "label": "Neuroendocrine Circadian Disruption & Axis Suppression",
        "target_gene": "CLOCK / ARNTL / GNRH1",
        "base_risk": 27.0,
        "gravity_factor": 0.35,
        "radiation_factor": 0.70,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Anabaena variabilis",
                "solution": "Suprachiasmatic Nucleus Circadian Enhancer",
                "delta_g": -7.8,
                "efficacy": 0.73
            },
            "intense": {
                "organism": "Nostoc punctiforme",
                "solution": "Hypothalamic Neuropeptide Protection Peptide",
                "delta_g": -9.0,
                "efficacy": 0.85
            }
        }
    },
    "vascular_endothelium": {
        "organ_system": "Vascular Endothelium & Microvasculature",
        "label": "Capillary Rarefaction & Endothelial Nitric Oxide Failure",
        "target_gene": "KDR / FLT1 / VWF",
        "base_risk": 36.0,
        "gravity_factor": 0.75,
        "radiation_factor": 0.45,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Methanococcus maripaludis",
                "solution": "Angiogenic Microvascular Growth Factors",
                "delta_g": -7.9,
                "efficacy": 0.74
            },
            "intense": {
                "organism": "Methanobacterium congolense",
                "solution": "Endothelial Basement Membrane Stabilizer",
                "delta_g": -9.1,
                "efficacy": 0.86
            }
        }
    },
    "thymus_immune": {
        "organ_system": "Thymus & T-Cell Maturation",
        "label": "Thymic Involution & Naive T-Cell Depletion",
        "target_gene": "FOXN1 / IL7R / DNTT",
        "base_risk": 31.0,
        "gravity_factor": 0.30,
        "radiation_factor": 0.80,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Thermus aquaticus",
                "solution": "Thymopoietic Interleukin Signalling Matrix",
                "delta_g": -8.0,
                "efficacy": 0.75
            },
            "intense": {
                "organism": "Pyrococcus abyssi",
                "solution": "Lymphocyte Progenitor Radioprotective Factor",
                "delta_g": -9.4,
                "efficacy": 0.88
            }
        }
    },
    "lymph_nodes_system": {
        "organ_system": "Lymphatic Drainage & Nodes",
        "label": "Interstitial Fluid Redistribution & Lymphedema",
        "target_gene": "PROX1 / VEGFR3 / CCL21",
        "base_risk": 28.0,
        "gravity_factor": 0.80,
        "radiation_factor": 0.25,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Haloferax volcanii",
                "solution": "Lymphangion Contractility Osmolyte",
                "delta_g": -7.4,
                "efficacy": 0.69
            },
            "intense": {
                "organism": "Halorubrum lacusprofundi",
                "solution": "Interstitial Hydrostatic Pressure Balancer",
                "delta_g": -8.7,
                "efficacy": 0.82
            }
        }
    },
    "bone_marrow_niche": {
        "organ_system": "Bone Marrow Stem Cell Niche",
        "label": "Hematopoietic Stem Cell Senescence & Niche Decay",
        "target_gene": "CXCL12 / KITLG / RUNX1",
        "base_risk": 34.0,
        "gravity_factor": 0.60,
        "radiation_factor": 0.70,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Methanothermobacter thermautotrophicus",
                "solution": "Endosteal Niche Stromal Cell Protector",
                "delta_g": -8.2,
                "efficacy": 0.76
            },
            "intense": {
                "organism": "Archaeoglobus fulgidus",
                "solution": "Pluripotent Stem Cell Telomere Preserver",
                "delta_g": -9.6,
                "efficacy": 0.90
            }
        }
    },
    "skeletal_joints": {
        "organ_system": "Cartilage & Synovial Joints",
        "label": "Articular Cartilage Degeneration & Joint Unloading Stress",
        "target_gene": "ACAN / COL2A1 / MMP13",
        "base_risk": 39.0,
        "gravity_factor": 0.88,
        "radiation_factor": 0.15,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Thermomicrobium roseum",
                "solution": "Chondrocyte Extracellular Matrix Lubricant",
                "delta_g": -7.5,
                "efficacy": 0.71
            },
            "intense": {
                "organism": "Hydrogenobacter thermophilus",
                "solution": "Synovial Fluid Viscoelastic Nanoparticle Gel",
                "delta_g": -8.8,
                "efficacy": 0.83
            }
        }
    },
    "lacrimal_tear": {
        "organ_system": "Lacrimal Glands & Tear Film",
        "label": "Microgravity Dry Eye Syndrome & Corneal Desiccation",
        "target_gene": "LTF / LYZ / MUC5AC",
        "base_risk": 26.0,
        "gravity_factor": 0.50,
        "radiation_factor": 0.35,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Spirulina platensis",
                "solution": "Osmoprotective Tear Film Lipid Stabilizer",
                "delta_g": -7.2,
                "efficacy": 0.68
            },
            "intense": {
                "organism": "Dunaliella salina",
                "solution": "Corneal Epithelial Mucin Secretion Inducer",
                "delta_g": -8.5,
                "efficacy": 0.80
            }
        }
    },
    "myocardial_tissue": {
        "organ_system": "Myocardium & Cardiac Muscle",
        "label": "Myocardial Fibrosis & Cardiac Wall Thinning",
        "target_gene": "MYH6 / COL3A1 / TGFBR1",
        "base_risk": 37.0,
        "gravity_factor": 0.70,
        "radiation_factor": 0.50,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Methanococcus voltae",
                "solution": "Cardiomyocyte Mitochondrial ATP Synthase Booster",
                "delta_g": -8.1,
                "efficacy": 0.75
            },
            "intense": {
                "organism": "Methanosarcina barkeri",
                "solution": "Myocardial Collagen Cross-Link Inhibitor",
                "delta_g": -9.3,
                "efficacy": 0.87
            }
        }
    },
    "coagulation_system": {
        "organ_system": "Blood Coagulation & Platelets",
        "label": "Spaceflight Hypercoagulability & Micro-Thrombus Risk",
        "target_gene": "F2 / F5 / SERPIND1",
        "base_risk": 32.0,
        "gravity_factor": 0.55,
        "radiation_factor": 0.40,
        "countermeasures_tiered": {
            "standard": {
                "organism": "Pyrobaculum aerophilum",
                "solution": "Antithrombotic Extremophilic Protease Inhibitor",
                "delta_g": -7.7,
                "efficacy": 0.72
            },
            "intense": {
                "organism": "Aeropyrum pernix",
                "solution": "Platelet Aggregation Regulating Nanopeptides",
                "delta_g": -8.9,
                "efficacy": 0.84
            }
        }
    }
}