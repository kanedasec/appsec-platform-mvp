from db.db import engine, Base
from db.models import Finding, Squad, Question, Assessment, AssessmentAnswer

Base.metadata.create_all(bind=engine)