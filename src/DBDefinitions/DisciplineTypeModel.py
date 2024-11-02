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


class DisciplineTypeModel(BaseModel):
    __tablename__ = "admission_discipline_types"

    name = Column(String)
    name_en = Column(String)
    description = Column(String, comment="")
    description_en = Column(String, comment="")
    weight = Column(Float, comment="")
    min_score = Column(Float, comment="")

    pass