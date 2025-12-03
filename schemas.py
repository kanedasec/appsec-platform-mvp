from datetime import datetime
from pydantic import BaseModel

class FindingCreate(BaseModel):
    title: str
    severity: str
    source: str
    status: str

class FindingResponse(BaseModel):
    id: int
    title: str
    severity: str
    source: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class SquadCreate(BaseModel):
    name: str
    description: str | None = None
    manager: str | None = None
    manager_email: str | None = None
    focal_point: str | None = None
    focal_point_email: str | None = None
    tech_leader: str | None = None
    tech_leader_email: str | None = None

class SquadResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    manager: str | None = None
    manager_email: str | None = None
    focal_point: str | None = None
    focal_point_email: str | None = None
    tech_leader: str | None = None
    tech_leader_email: str | None = None

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    code: str
    text: str
    domain: str
    weight: int
    order: int

class QuestionResponse(BaseModel):
    id: int
    code: str
    text: str
    domain: str
    weight: int
    order: int

    class Config:
        orm_mode = True

class AssessmentAnswerInput(BaseModel):
    question_id: int
    value: int

class AssessmentCreate(BaseModel):
    squad_id: int
    assessment_cyle: str
    answers: list[AssessmentAnswerInput]

class AssessmentAnswerResponse(BaseModel):
    question_id: int
    value: int
    score: float

class AssessmentResponse(BaseModel):
    id: int
    squad: SquadResponse
    assessment_cycle: str
    created_at: datetime
    total_score: float
    level: str
    answers: list[AssessmentAnswerResponse]

    class Config:
        orm_mode = True