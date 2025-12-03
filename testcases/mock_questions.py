import requests
questions = [
    {
        "code": "SDLC_01",
        "text": "Os pipelines de CI/CD da squad possuem etapas automatizadas de verificação de segurança (por exemplo, SAST, SCA ou secrets scanning) configuradas e ativas?",
        "domain": "SDLC",
        "weight": 1,
        "order": 1,
    },
    {
        "code": "SDLC_02",
        "text": "A squad possui um processo definido para tratar findings de ferramentas de segurança (priorização, triagem, correção e revalidação)?",
        "domain": "SDLC",
        "weight": 1,
        "order": 2,
    },
    {
        "code": "APPSEC_01",
        "text": "A squad realiza revisões de código com foco em segurança (code review com checklist ou critérios mínimos de segurança)?",
        "domain": "AppSec",
        "weight": 1,
        "order": 3,
    },
    {
        "code": "APPSEC_02",
        "text": "A squad mantém um inventário atualizado das aplicações, APIs e componentes sob sua responsabilidade (incluindo dependências críticas)?",
        "domain": "AppSec",
        "weight": 1,
        "order": 4,
    },
    {
        "code": "THREAT_01",
        "text": "A squad já realizou pelo menos um exercício de threat modeling para as principais aplicações ou serviços que mantém?",
        "domain": "ThreatModeling",
        "weight": 1,
        "order": 5,
    },
    {
        "code": "THREAT_02",
        "text": "Os riscos identificados em threat modeling influenciam decisões de backlog (histórias técnicas, débitos de segurança, priorização de correções)?",
        "domain": "ThreatModeling",
        "weight": 1,
        "order": 6,
    },
    {
        "code": "DEVSECOPS_01",
        "text": "A squad trata configurações de infraestrutura e segurança (por exemplo, security groups, policies, roles) como código, com versionamento e revisão?",
        "domain": "DevSecOps",
        "weight": 1,
        "order": 7,
    },
    {
        "code": "DEVSECOPS_02",
        "text": "A squad monitora vulnerabilidades em imagens de container, bibliotecas e componentes usados em produção de forma recorrente?",
        "domain": "DevSecOps",
        "weight": 1,
        "order": 8,
    },
    {
        "code": "INCIDENT_01",
        "text": "A squad saberia como agir em caso de incidente de segurança envolvendo sua aplicação (quem acionar, quais passos seguir, onde registrar)?",
        "domain": "IncidentResponse",
        "weight": 1,
        "order": 9,
    },
    {
        "code": "AWARE_01",
        "text": "Os membros da squad receberam algum tipo de treinamento ou capacitação em segurança de aplicações nos últimos 12 meses?",
        "domain": "Awareness",
        "weight": 1,
        "order": 10,
    },
]

for question in questions:
    response = requests.post("http://localhost:8000/questions", headers={"Content-Type": "application/json"}, json=question)
    print(response.status_code)