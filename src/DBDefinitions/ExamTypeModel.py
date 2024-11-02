from sqlalchemy import Column, String, DateTime

from .BaseModel import BaseModel, UUIDFKey


class ExamTypeModel(BaseModel):
    __tablename__ = "admission_exam_types"

    name = Column(String, comment="Name of the admission entry")
    name_en = Column(String, comment="English name of the admission entry")

    pass