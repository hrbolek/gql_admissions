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

    description = Column(String, comment="Poznámka k přezkoušení")
    score = Column(Float, comment="Bodové ohodnocení výkonu")
    user_id = UUIDFKey(comment="Kdo přezkoušení absolvoval")
    examiner_id = UUIDFKey(comment="Kdo přezkoušel")
    discipline_id = Column(ForeignKey("admission_disciplines.id"), comment="Která disciplína (část předmětu)")
    exam_planed_date = Column(DateTime, comment="Naplánované datum")

    pass