import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Finding(Base):
    __tablename__ = 'findings'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    severity = Column(String)
    source = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Squad(Base):
    __tablename__ = 'squads'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    manager = Column(String)
    manager_email = Column(String)
    focal_point = Column(String)
    focal_point_email = Column(String)
    tech_leader = Column(String)
    tech_leader_email = Column(String)

    assessments = relationship("Assessment", back_populates="squad")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    text = Column(String)
    domain = Column(String)
    weight = Column(Integer)
    order = Column(Integer)

    answers = relationship("AssessmentAnswer", back_populates="question")

class Assessment(Base):
    __tablename__ = 'assessments'
    id = Column(Integer, primary_key=True, index=True)
    squad_id = Column(Integer, ForeignKey('squads.id'))
    assessment_cycle = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    total_score = Column(Float)
    level = Column(String)

    squad = relationship("Squad", back_populates="assessments")
    answers = relationship("AssessmentAnswer", back_populates="assessments")

class AssessmentAnswer(Base):
    __tablename__ = 'assessment_answers'
    id = Column(Integer, primary_key=True, index=True)
    assessment_id = Column(Integer, ForeignKey('assessments.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    value = Column(Integer)
    score = Column(Float)

    assessments = relationship("Assessment", back_populates="answers")
    question = relationship("Question", back_populates="answers")


