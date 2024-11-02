from sqlalchemy import (
    Column, 
    
    String, 
    DateTime,
    Integer,

    ForeignKey
)
from sqlalchemy.orm import relationship

from .BaseModel import BaseModel, UUIDFKey


class DisciplineTypeModel(BaseModel):
    __tablename__ = "admission_discipline_type"

    name = Column(String)
    name_en = Column(String)

    pass