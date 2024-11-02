from sqlalchemy import (
    Column, 
    
    String, 
    DateTime,
    Integer,
    Float,

    ForeignKey
)
from sqlalchemy.orm import relationship

from .BaseModel import BaseModel, UUIDFKey


class DisciplineModel(BaseModel):
    __tablename__ = "admission_disciplines"

    max_score = Column(Float, comment="Maximální počet bodů, které lze v disciplíne dosáhnout")
    min_score = Column(Float, comment="Minimální počet bodů, kdy lze ještě splnit disciplínu")
    discipline_type_id = Column(ForeignKey("admission_discipline_types.id"), comment="Fakticky předmět přijímacího řízení")
    admission_id = Column(ForeignKey("admissions.id"), comment="")
    
    pass