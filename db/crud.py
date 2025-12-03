from sqlalchemy.orm import Session
from db.models import Finding, Squad, Question
from db.models import Assessment, AssessmentAnswer


#------Findings
def create_finding(db: Session, title: str, severity: str, source: str, status: str) -> Finding:
    obj = Finding(
        title=title,
        severity=severity,
        source=source,
        status=status,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all_findings(db: Session):
    return db.query(Finding).all()

def get_finding_by_id(db: Session, finding_id: int) -> Finding:
    return db.query(Finding).filter(Finding.id == finding_id).first()

#--------Squads
def create_squad(
        db: Session,
        name: str,
        description: str | None = None,
        manager: str | None = None,
        manager_email: str | None = None,
        focal_point: str | None = None,
        focal_point_email: str | None = None,
        tech_leader: str | None = None,
        tech_leader_email: str | None = None
):
    obj = Squad(
        name = name,
        description = description,
        manager = manager,
        manager_email = manager_email,
        focal_point = focal_point,
        focal_point_email = focal_point_email,
        tech_leader = tech_leader,
        tech_leader_email = tech_leader_email,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all_squads(db: Session):
    return db.query(Squad).all()

def get_squad_by_id(db: Session, squad_id: int):
    return db.query(Squad).filter(Squad.id == squad_id).first()

#--------Questions
def create_question(db: Session, code: str, text: str, domain: str, weight: int, order: int):
    obj = Question(
        code = code,
        text = text,
        domain = domain,
        weight = weight,
        order = order
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all_questions(db: Session):
    return db.query(Question).all()

#------Assessments
def _compute_level(total_score: float) -> str:
    if total_score < 1.5:
        return "Maturidade Crítica"
    elif total_score < 2.4:
        return "Maturidade Baixa"
    elif total_score < 3.5:
        return "Maturidade Moderada"
    elif total_score < 4.5:
        return "Maturidade Boa"
    else:
        return "Maturidade Elevada"

def create_assessment(db: Session, squad_id: str, assessment_cycle: str, answers: list) -> Assessment:
    squad = db.query(Squad).filter(Squad.id == squad_id).first()
    if squad is None:
        raise ValueError(f"Squad {squad_id} not found")

    assessment = Assessment(
        squad_id = squad_id,
        assessment_cycle = assessment_cycle,
        total_score = 0.0,
        level="",
    )

    db.add(assessment)
    db.flush()

    total_score = 0.0

    for answer in answers:
        question_id = getattr(answer, "question_id")
        value = getattr(answer, "value")

        if value > 5 or value < 0:
            raise ValueError(f"value of {value} is out of expected range")

        question = db.query(Question).filter(Question.id == question_id).first()
        if question is None:
            raise ValueError(f"Question {question_id} not found")

        score = float(value) * float(question.weight)

        assessment_answer = AssessmentAnswer(
            assessment_id = assessment.id,
            question_id = question.id,
            value = value,
            score = score,
        )

        db.add(assessment_answer)
        total_score += score

    total_score = total_score / len(answers)
    assessment.total_score = total_score
    assessment.level = _compute_level(total_score)

    db.commit()
    db.refresh(assessment)

    return assessment

def get_all_assessments(db: Session):
    return db.query(Assessment).all()

def get_assessments_by_squad(db: Session, squad_id: int) -> list[Assessment]:
    squad = db.query(Squad).filter(Squad.id == squad_id).first()
    if squad is None:
        return []
    return squad.assessments