"""
CosmoPhy-X: Astronaut Health Monitoring & CosmoPhy-X Bio-Defense Dossier
Executive Clinical Mission Dossier Generator
Includes End-to-End Biosynthetic & Nano-Medicine Delivery Protocol.
"""

from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Dashboard-matched Bi-color / Taupe Palette
COLOR_CANVAS_BG = colors.HexColor('#f7f4ee')     # Soft Cream / Off-White Background
COLOR_CARD_BEIGE = colors.HexColor('#eae4de')   # Soft Taupe Panel Background
COLOR_BORDER = colors.HexColor('#c5bac1')       # Subtle Lavender-Tinted Border
COLOR_HEADER_BG = colors.HexColor('#e2dcd5')    # Header & Table Head Background
COLOR_PRIMARY = colors.HexColor('#7b4f85')      # Cosmic Lavender / Deep Purple Accent
COLOR_SECONDARY = colors.HexColor('#d48c98')    # Soft Peach / Rose Pink Accent
COLOR_TEXT_DARK = colors.HexColor('#36283b')    # Deep Dark Plum Text
COLOR_TEXT_MUTED = colors.HexColor('#6e5873')   # Secondary Muted Text
COLOR_RISK_HIGH = colors.HexColor('#b33939')    # Clinical Red
COLOR_RISK_SAFE = colors.HexColor('#218c74')    # Mitigated Green

def draw_beige_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(COLOR_CANVAS_BG)
    canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], stroke=0, fill=1)
   
    canvas.setStrokeColor(COLOR_BORDER)
    canvas.setLineWidth(1)
    canvas.rect(16, 16, doc.pagesize[0] - 32, doc.pagesize[1] - 32, stroke=1, fill=0)
    canvas.restoreState()

def generate_mission_pdf(dest_key, duration_days, dest_info, countermeasures):
    buffer = BytesIO()
   
    doc = SimpleDocTemplate(
        buffer,
        pagesize=landscape(letter),
        rightMargin=30,
        leftMargin=30,
        topMargin=18,
        bottomMargin=18
    )

    story = []
    styles = getSampleStyleSheet()

    total_rows = len(countermeasures)

    if total_rows <= 8:
        f_size, f_lead, v_pad = 6.5, 8.0, 2.5
    elif total_rows <= 16:
        f_size, f_lead, v_pad = 5.5, 6.8, 1.0
    else:
        f_size, f_lead, v_pad = 4.8, 5.8, 0.5

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=COLOR_PRIMARY
    )

    sub_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.2,
        leading=7.8,
        textColor=COLOR_TEXT_MUTED
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=5.8,
        leading=7.5,
        alignment=2,
        textColor=COLOR_TEXT_MUTED
    )

    cell_bold_style = ParagraphStyle('CB', fontName='Helvetica-Bold', fontSize=f_size, leading=f_lead, textColor=COLOR_TEXT_DARK)
    cell_regular_style = ParagraphStyle('CR', fontName='Helvetica', fontSize=f_size - 0.2, leading=f_lead, textColor=COLOR_TEXT_DARK)
    cell_italic_style = ParagraphStyle('CI', fontName='Helvetica-Oblique', fontSize=f_size - 0.2, leading=f_lead, textColor=COLOR_TEXT_MUTED)
    cell_high_risk = ParagraphStyle('CHR', fontName='Helvetica-Bold', fontSize=f_size, leading=f_lead, alignment=1, textColor=COLOR_RISK_HIGH)
    cell_mitigated_risk = ParagraphStyle('CMR', fontName='Helvetica-Bold', fontSize=f_size, leading=f_lead, alignment=1, textColor=COLOR_RISK_SAFE)
    cell_center_style = ParagraphStyle('CC', fontName='Helvetica', fontSize=f_size - 0.2, leading=f_lead, alignment=1, textColor=COLOR_TEXT_DARK)

    # 1. Header Section (Removed verification text and left blank)
    header_data = [
        [
            Paragraph("<b>COSMOPHY-X: ASTRONAUT DOSSIER</b>", title_style),
            Paragraph("", meta_style)
        ]
    ]

    header_table = Table(header_data, colWidths=[500, 232])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 2))

    # 2. Mission Parameter Telemetry Strip
    total_rad = dest_info.get('radiation_msv_day', 0.5) * duration_days
    param_data = [
        ["TARGET VECTOR:", "DURATION:", "GRAVITY FLUX:", "RADIATION FLUX:", "EST. TOTAL DOSE:"],
        [dest_info.get('name', dest_key), f"{duration_days} Sol Days", f"{dest_info.get('gravity_g', 0.0)} g", f"{dest_info.get('radiation_msv_day', 0.5)} mSv/day", f"{total_rad:.1f} mSv"]
    ]

    param_table = Table(param_data, colWidths=[146, 146, 146, 146, 148])
    param_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_CARD_BEIGE),
        ('TEXTCOLOR', (0,0), (-1,0), COLOR_TEXT_MUTED),
        ('TEXTCOLOR', (0,1), (-1,1), COLOR_TEXT_DARK),
        ('TEXTCOLOR', (4,1), (4,1), COLOR_RISK_HIGH),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTNAME', (0,1), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 5.5),
        ('FONTSIZE', (0,1), (-1,1), 7.0),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LINEBELOW', (0,-1), (-1,-1), 1.0, COLOR_PRIMARY),
    ]))
    story.append(param_table)
    story.append(Spacer(1, 2))

    # 3. Dynamic Formulation Matrix
    col_widths = [155, 48, 205, 145, 65, 54]

    headers = [
        Paragraph("<b>PATHOLOGY FOCUS</b>", ParagraphStyle('TH1', fontName='Helvetica-Bold', fontSize=f_size + 0.2, leading=f_lead, textColor=COLOR_PRIMARY)),
        Paragraph("<b>BASELINE</b>", ParagraphStyle('TH2', fontName='Helvetica-Bold', fontSize=f_size + 0.2, leading=f_lead, alignment=1, textColor=COLOR_PRIMARY)),
        Paragraph("<b>TARGET THERAPEUTIC SOLUTION</b>", ParagraphStyle('TH3', fontName='Helvetica-Bold', fontSize=f_size + 0.2, leading=f_lead, textColor=COLOR_PRIMARY)),
        Paragraph("<b>MODEL EXTREMOPHILE</b>", ParagraphStyle('TH4', fontName='Helvetica-Bold', fontSize=f_size + 0.2, leading=f_lead, textColor=COLOR_PRIMARY)),
        Paragraph("<b>ΔG AFFINITY</b>", ParagraphStyle('TH5', fontName='Helvetica-Bold', fontSize=f_size + 0.2, leading=f_lead, alignment=1, textColor=COLOR_PRIMARY)),
        Paragraph("<b>MITIGATED</b>", ParagraphStyle('TH6', fontName='Helvetica-Bold', fontSize=f_size + 0.2, leading=f_lead, alignment=1, textColor=COLOR_PRIMARY))
    ]

    table_content = [headers]

    for cm in countermeasures:
        table_content.append([
            Paragraph(cm['pathology'], cell_bold_style),
            Paragraph(f"{cm['baseline_risk']}%", cell_high_risk),
            Paragraph(cm['solution'], cell_regular_style),
            Paragraph(cm['organism'], cell_italic_style),
            Paragraph(f"{cm['delta_g_kcal']} kcal/mol", cell_center_style),
            Paragraph(f"{cm['mitigated_risk']}%", cell_mitigated_risk)
        ])

    matrix_table = Table(table_content, colWidths=col_widths)
    matrix_style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_HEADER_BG),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), v_pad),
        ('BOTTOMPADDING', (0,0), (-1,-1), v_pad),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.35, COLOR_BORDER),
    ])

    for i in range(1, len(table_content)):
        bg = colors.HexColor('#f7f4ee') if (i % 2 != 0) else COLOR_CARD_BEIGE
        matrix_style.add('BACKGROUND', (0, i), (-1, i), bg)

    matrix_table.setStyle(matrix_style)
    story.append(matrix_table)
    story.append(Spacer(1, 2))

    # 4. End-to-End Biosynthetic & Nano-Medicine Protocol Strip
    protocol_text = (
        "<b>COSMOPHY-X BIOSYNTHETIC PROTOCOL:</b> 1. <i>Mining &amp; In-Silico Identification:</i> Isolate extremophilic radiotolerant/thermophilic genes. "
        "2. <i>Molecular Mimicry &amp; Docking:</i> Optimize human receptor binding affinity (ΔG) via AlphaFold/RFdiffusion. "
        "3. <i>Nano-Encapsulation:</i> Protect via PLGA nano-particles against protease degradation. "
        "4. <i>Administration:</i> Zero-gravity targeted μM Inhalable Aerosol Spray or Subcutaneous Nano-Patch Delivery."
    )
    protocol_style = ParagraphStyle(
        'ProtocolStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=5.2,
        leading=6.6,
        textColor=COLOR_TEXT_DARK
    )
    protocol_table = Table([[Paragraph(protocol_text, protocol_style)]], colWidths=[732])
    protocol_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_CARD_BEIGE),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('LINEABOVE', (0,0), (-1,-1), 0.5, COLOR_PRIMARY),
    ]))
    story.append(protocol_table)
    story.append(Spacer(1, 2))

    # 5. Clean Clinical Validation Footer
    footer_data = [
        [
            Paragraph("<b>STATUS:</b> VERIFIED BIO-CERTIFIED", sub_style),
            Paragraph("<b>SPECIALIST:</b> PRITI ROOJ", meta_style)
        ]
    ]

    footer_table = Table(footer_data, colWidths=[532, 200])
    footer_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEABOVE', (0,0), (-1,-1), 0.6, COLOR_PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(footer_table)

    doc.build(story, onFirstPage=draw_beige_background)
    buffer.seek(0)
    return buffer.getvalue()
