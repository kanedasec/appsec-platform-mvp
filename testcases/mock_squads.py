import requests

squads = [
    {
        "name": "Squad Auth Services",
        "description": "Responsável pelos serviços de autenticação e gestão de identidades.",
        "manager": "Mariana Oliveira",
        "manager_email": "mariana.oliveira@empresa.com",
        "focal_point": "Daniel Souza",
        "focal_point_email": "daniel.souza@empresa.com",
        "tech_leader": "Rafael Lima",
        "tech_leader_email": "rafael.lima@empresa.com"
    },
    {
        "name": "Squad Payments API",
        "description": "Implementa e mantém APIs de pagamentos e integrações financeiras.",
        "manager": "Lucas Almeida",
        "manager_email": "lucas.almeida@empresa.com",
        "focal_point": "Patrícia Fernandes",
        "focal_point_email": "patricia.fernandes@empresa.com",
        "tech_leader": "João Matos",
        "tech_leader_email": "joao.matos@empresa.com"
    },
    {
        "name": "Squad Customer Portal",
        "description": "Desenvolve e mantém o portal do cliente e suas funcionalidades.",
        "manager": "Carolina Mendes",
        "manager_email": "carolina.mendes@empresa.com",
        "focal_point": "Gustavo Teixeira",
        "focal_point_email": "gustavo.teixeira@empresa.com",
        "tech_leader": "Fernanda Prado",
        "tech_leader_email": "fernanda.prado@empresa.com"
    },
    {
        "name": "Squad Mobile App",
        "description": "Responsável pelo aplicativo mobile e integrações nativas.",
        "manager": "Roberto Braga",
        "manager_email": "roberto.braga@empresa.com",
        "focal_point": "Larissa Pinto",
        "focal_point_email": "larissa.pinto@empresa.com",
        "tech_leader": "Eduardo Teles",
        "tech_leader_email": "eduardo.teles@empresa.com"
    },
    {
        "name": "Squad Data Platform",
        "description": "Constrói pipelines de dados, lakes e plataformas analíticas.",
        "manager": "Juliana Castro",
        "manager_email": "juliana.castro@empresa.com",
        "focal_point": "Hugo Ferreira",
        "focal_point_email": "hugo.ferreira@empresa.com",
        "tech_leader": "Tatiana Viana",
        "tech_leader_email": "tatiana.viana@empresa.com"
    },
    {
        "name": "Squad Observability",
        "description": "Responsável por métricas, logs, tracing e plataformas de SRE.",
        "manager": "Felipe Moreira",
        "manager_email": "felipe.moreira@empresa.com",
        "focal_point": "Camila Rocha",
        "focal_point_email": "camila.rocha@empresa.com",
        "tech_leader": "Vinícius Torres",
        "tech_leader_email": "vinicius.torres@empresa.com"
    },
    {
        "name": "Squad Fraud Detection",
        "description": "Desenvolve soluções de prevenção e detecção de fraude em tempo real.",
        "manager": "Ana Paula Ribeiro",
        "manager_email": "ana.ribeiro@empresa.com",
        "focal_point": "Marcus Silva",
        "focal_point_email": "marcus.silva@empresa.com",
        "tech_leader": "Bianca Duarte",
        "tech_leader_email": "bianca.duarte@empresa.com"
    },
    {
        "name": "Squad Infrastructure as Code",
        "description": "Automação de infraestrutura, pipelines IaC e práticas DevSecOps.",
        "manager": "Rodrigo Carvalho",
        "manager_email": "rodrigo.carvalho@empresa.com",
        "focal_point": "Isabela Cunha",
        "focal_point_email": "isabela.cunha@empresa.com",
        "tech_leader": "Paulo Henrique",
        "tech_leader_email": "paulo.henrique@empresa.com"
    },
    {
        "name": "Squad Notification Services",
        "description": "Serviços de envio de e-mail, push notifications e SMS.",
        "manager": "Clara Rodrigues",
        "manager_email": "clara.rodrigues@empresa.com",
        "focal_point": "Leonardo Almeida",
        "focal_point_email": "leonardo.almeida@empresa.com",
        "tech_leader": "Sabrina Lopes",
        "tech_leader_email": "sabrina.lopes@empresa.com"
    },
    {
        "name": "Squad API Gateway",
        "description": "Gerencia gateways, roteamento de APIs e políticas de segurança.",
        "manager": "Diego Marques",
        "manager_email": "diego.marques@empresa.com",
        "focal_point": "Helena Moraes",
        "focal_point_email": "helena.moraes@empresa.com",
        "tech_leader": "André Barbosa",
        "tech_leader_email": "andre.barbosa@empresa.com"
    }
]

for squad in squads:
    response = requests.post("http://localhost:8000/squads", headers={"Content-Type": "application/json"}, json=squad)
    print(response.status_code)