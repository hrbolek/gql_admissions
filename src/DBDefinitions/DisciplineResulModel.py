from sqlalchemy import (
    Column, 
    
    String, 
    DateTime,
    Float,

    ForeignKey
)
from sqlalchemy.orm import relationship

from .BaseModel import BaseModel, UUIDFKey


class DisciplineResulModel(BaseModel):
    __tablename__ = "admission_discipline_results"

    student_id = UUIDFKey(comment="user + program")
    score = Column(Float)
    discipline_id = Column(ForeignKey("admission_discipline.id"), index=True)

    examiner_id = UUIDFKey(comment="who proves result")

    pass