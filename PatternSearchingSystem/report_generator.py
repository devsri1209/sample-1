from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def generate_pdf_report(results, pattern):

    pdf = SimpleDocTemplate("Pattern_Search_Report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    # TITLE
    title = Paragraph("Pattern Searching Analysis Report", styles['Title'])

    elements.append(title)
    elements.append(Spacer(1, 20))

    # SEARCH PATTERN
    pattern_text = Paragraph(f"<b>Search Pattern:</b> {pattern}", styles['BodyText'])

    elements.append(pattern_text)
    elements.append(Spacer(1, 20))

    # TABLE DATA
    data = [
        ["Algorithm", "Matches", "Execution Time", "Comparisons"]
    ]

    for algo in results:

        data.append([
            algo,
            str(len(results[algo]["positions"])),
            str(round(results[algo]["time"], 6)),
            str(results[algo]["comparisons"])
        ])

    # CREATE TABLE
    table = Table(data)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)

    elements.append(table)
    elements.append(Spacer(1, 20))

    # MATCH POSITIONS
    for algo in results:

        text = f"<b>{algo} Match Positions:</b> {results[algo]['positions']}"

        para = Paragraph(text, styles['BodyText'])

        elements.append(para)
        elements.append(Spacer(1, 10))

    # BUILD PDF
    pdf.build(elements)

    print("PDF Report Generated Successfully")