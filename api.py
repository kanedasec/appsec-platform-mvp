from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import SessionLocal
from db import crud
from schemas import FindingCreate, FindingResponse
from schemas import SquadCreate, SquadResponse
from schemas import QuestionResponse, QuestionCreate
from schemas import AssessmentCreate, AssessmentResponse

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/findings", response_model=List[FindingResponse])
def list_findings(db: Session = Depends(get_db)):
    findings = crud.get_all_findings(db)
    return findings

@app.get("/findings/{finding_id}", response_model=FindingResponse)
def find_finding(finding_id: int, db: Session = Depends(get_db)):
    finding = crud.get_finding_by_id(db, finding_id)
    if finding is None:
        raise HTTPException(status_code=404, detail="finding not found")
    return finding

@app.post("/findings", response_model=FindingResponse)
def create_finding_endpoint(finding: FindingCreate, db: Session = Depends(get_db)):
    new_finding = crud.create_finding(
        db,
        title=finding.title,
        severity=finding.severity,
        source=finding.source,
        status=finding.status,
    )
    return new_finding

@app.post("/squads", response_model=SquadResponse)
def create_squad(squad: SquadCreate, db: Session = Depends(get_db)):
    new_squad = crud.create_squad(
        db,
        name=squad.name,
        description=squad.description,
        manager=squad.manager,
        manager_email=squad.manager_email,
        focal_point=squad.focal_point,
        focal_point_email=squad.focal_point_email,
        tech_leader=squad.tech_leader,
        tech_leader_email=squad.tech_leader_email
    )
    return new_squad

@app.get("/squads", response_model=List[SquadResponse])
def list_squads(db: Session = Depends(get_db)):
    squads = crud.get_all_squads(db)
    return squads

@app.post("/questions", response_model=QuestionResponse)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    new_question = crud.create_question(
        db,
        code=question.code,
        text=question.text,
        domain=question.domain,
        weight=question.weight,
        order=question.order,
    )
    return new_question

@app.get("/questions", response_model=List[QuestionResponse])
def list_questions(db: Session = Depends(get_db)):
    questions = crud.get_all_questions(db)
    return questions

@app.post("/assessments", response_model=AssessmentResponse)
def create_assessment_endpoint(payload: AssessmentCreate, db: Session = Depends(get_db)):
    try:
        assessment = crud.create_assessment(
            db,
            squad_id= payload.squad_id,
            assessment_cycle= payload.assessment_cyle,
            answers= payload.answers,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return assessment

@app.get("/assessments", response_model=List[AssessmentResponse])
def list_assessments(db: Session = Depends(get_db)):
    assessments = crud.get_all_assessments(db)
    return assessments

@app.get("/squad/{squad_id}/assessments", response_model=List[AssessmentResponse])
def list_assesments_by_squad(squad_id: int, db: Session = Depends(get_db)):
    assessments = crud.get_assessments_by_squad(db, squad_id)
    if len(assessments) == 0:
        raise HTTPException(status_code=404, detail="No assessments found for this squad")

    return assessments