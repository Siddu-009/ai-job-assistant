KNOWN_SKILLS = [
    "aws",
    "docker",
    "kubernetes",
    "terraform",
    "jenkins",
    "ansible",
    "linux",
    "github actions",
    "git",
    "python",
    "prometheus",
    "grafana",
    "eks",
    "ec2",
    "s3",
    "iam",
    "route53",
    "rds",
    "argocd",
    "helm",
    "devops"
]

def extract_skills(text):

    text = text.lower()

    skills = []

    for skill in KNOWN_SKILLS:

        if skill in text:
            skills.append(skill)

    return skills
