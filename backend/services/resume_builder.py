from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def build_resume(
    name,
    email,
    phone,
    summary,
    skills,
    projects,
    education,
    output_file
):

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"<b>{name}</b>",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            f"{email} | {phone}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>PROFESSIONAL SUMMARY</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            summary,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>TECHNICAL SKILLS</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            skills,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>PROJECTS</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            projects,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>EDUCATION</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            education,
            styles["Normal"]
        )
    )

    doc.build(content)
