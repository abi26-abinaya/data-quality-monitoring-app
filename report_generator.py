from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.lib.units import inch

def generate_report(missing, duplicates, quality_score):
    doc = SimpleDocTemplate("reports/quality_report.pdf")
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Data Quality Report", styles['Title']))
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph(f"Total Duplicates: {duplicates}", styles['Normal']))
    elements.append(Paragraph(f"Quality Score: {quality_score:.2f}%", styles['Normal']))

    doc.build(elements)