# CosmoPhy-X: Cosmic Physiology & Extremophile Defense
**NASA Space Apps Challenge 2026 Submission**

## Overview

**CosmoPhy-X** is an advanced, dual-use space biomedical and physiological simulation engine engineered to safeguard astronaut health during deep-space exploration while providing downscaled, practical telehealth solutions for remote terrestrial populations. 

Operating at the intersection of astrobiology and bioinformatics, CosmoPhy-X integrates real-time telemetry, NASA Open Science Data Repository (OSDR) multi-omics datasets, and biophysical modeling. It maps extreme-environment extremophile defense mechanisms—such as radiotolerant proteins from extremophiles and thermophilic enzymes—to human physiological vulnerabilities across 16 celestial bodies and transit corridors in the solar system.

---.

## Key Features & Architecture

* **Multi-Destination Orbital Simulation:** Evaluates multi-system pathology vulnerability percentages across 16 unique destinations and transit corridors, including Low Earth Orbit (ISS), Lunar Base Shackleton, Mars Jezero Outpost, Europa Subsurface, Titan, and Interplanetary Transit.
* **Real-Time Astronaut Vital Signs Integration:** Dynamically ingests daily clinical metrics (Systolic Blood Pressure, Blood Sugar, Sleep Hours, and Mood Index) to recalculate organ-specific physiological stress and risk indexes on the fly.
* **NASA OSDR & NCBI Data Ingestion Pipeline:** Empowers researchers to dynamically sync, parse, and ingest live multi-omics datasets (such as `OSD-379` or `PRJNA548028`) to generate custom disease models and biomarker targets.
* **AI Medical Commander "Priti":** A conversational, context-aware AI assistant built to deliver step-by-step first-aid protocols, emergency guidance, and biological countermeasures in plain, natural, and human-like language.
* **Dual-Use Earth Telemedicine Mode:** Downscales space-grade cellular defenses (like heat-shock proteins and antioxidant enzyme formulations) into shelf-stable oral capsules, field-deployable telemedicine kits, and rural clinic ORS packets for high-altitude or remote terrestrial communities.
* **Executive Clinical Mission Dossier Generator:** Compiles simulation results, thermodynamic binding affinities ($\Delta G$), and therapeutic solutions into a publication-ready, dashboard-matched landscape PDF prescription dossier.

---

## Technology Stack

* **Backend:** Python, Flask, ReportLab (Dynamic PDF Dossier Generation)
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla ES6), Chart.js (High-Resolution Multi-Omics Visualizations)
* **AI & Data Integration:** Google GenAI SDK (`google-genai` / Gemini 1.5 Flash), NASA OSDR Metadata REST APIs, NCBI E-utilities

---

## Project File Structure

```text
CosmoPhy-X/
│
├── app.py                  # Main Flask application engine & API routing
├── requirements.txt        # Python dependencies (Flask, ReportLab, requests, etc.)
├── README.md               # Project documentation & GitHub guide
│
├── src/
│   ├── astro_data.py       # Solar system environmental matrices & pathology registry
│   ├── ml_engine.py        # Risk calculation & extremophile countermeasure matching engine
│   ├── pdf_generator.py    # ReportLab landscape PDF clinical dossier generator
│   └── osdr_client.py      # NASA OSDR & NCBI automated multi-omics parsing engine
│
├── static/
│   ├── COSMOPHY-X_Main_Pic_2.jpg  # High-resolution mission banner illustration
│   └── audio/
│       └── soundspack.mp3         # UI interaction sound effects
│
└── templates/
    └── index.html          # Single-page interactive HUD dashboard interface

## Installation & Local Execution Guide

1. **Clone or Download the Repository**  
   Ensure all project files are placed in your working directory matching the directory structure outlined above.

2. **Install Dependencies**  
   Open your terminal in the project root folder and install the required Python packages:
   ```bash
   pip install flask reportlab requests python-dotenv
