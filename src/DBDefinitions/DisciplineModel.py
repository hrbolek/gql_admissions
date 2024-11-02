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
    __tablename__ = "admission_discipline"

    result_max = Column(Float)
    result_min = Column(Float)
    discipline_type_id = Column(ForeignKey(""), index=True)
    
    pass