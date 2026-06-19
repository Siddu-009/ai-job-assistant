from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def build_resume(
    name,
    email,
    phone,
    linkedin,
    github,
    summary,
    skills,
    projects,
    certifications,
    education,
    output_file
):

    doc = SimpleDocTemplate(
        output_file,
        topMargin=20,
        bottomMargin=20,
        leftMargin=30,
        rightMargin=30
    )

    styles = getSampleStyleSheet()

    content = []

    # HEADER

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
        Paragraph(
            linkedin,
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            github,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # SUMMARY

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
        Spacer(1, 8)
    )

    # SKILLS

    content.append(
        Paragraph(
            "<b>TECHNICAL SKILLS</b>",
            styles["Heading2"]
        )
    )

    skills_text = """
<b>DevOps & CI/CD:</b> Jenkins, Git, GitHub, Maven, SonarQube, Nexus, ArgoCD<br/><br/>

<b>Cloud Platform:</b> AWS (EC2, S3, IAM, VPC, RDS, Route53, EKS, CloudWatch)<br/><br/>

<b>Containers:</b> Docker, Kubernetes, Helm, Kustomize<br/><br/>

<b>Infrastructure as Code:</b> Terraform, Ansible<br/><br/>

<b>Monitoring:</b> Prometheus, Grafana, CloudWatch<br/><br/>

<b>Operating Systems:</b> Linux (Ubuntu, RHEL), Bash Scripting
"""

    content.append(
        Paragraph(
            skills_text,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 8)
    )

    # PROJECTS

    content.append(
        Paragraph(
            "<b>PROJECTS</b>",
            styles["Heading2"]
        )
    )

    project_1 = """
<b>CI/CD Pipeline for E-Commerce Application</b><br/>
• Built Jenkins CI/CD pipeline for automated deployments<br/>
• Automated AWS infrastructure using Terraform<br/>
• Configured Ansible deployments on Linux servers<br/>
• Implemented Prometheus & Grafana monitoring
"""

    project_2 = """
<b>Kubernetes-based Microservices Deployment</b><br/>
• Provisioned AWS EKS cluster using Terraform<br/>
• Built and deployed Docker-based microservices<br/>
• Implemented Helm and ArgoCD GitOps workflows<br/>
• Configured Kubernetes autoscaling and monitoring
"""

    content.append(
        Paragraph(
            project_1,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 5)
    )

    content.append(
        Paragraph(
            project_2,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 8)
    )

    # EDUCATION

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

    content.append(
        Spacer(1, 8)
    )

    # CERTIFICATIONS

    content.append(
        Paragraph(
            "<b>CERTIFICATIONS</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            certifications,
            styles["Normal"]
        )
    )

    doc.build(content)
