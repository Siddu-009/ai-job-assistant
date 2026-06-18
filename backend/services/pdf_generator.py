from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(content, output_file):

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):
        story.append(
            Paragraph(line, styles["BodyText"])
        )

        story.append(
            Spacer(1, 6)
        )

    doc.build(story)
