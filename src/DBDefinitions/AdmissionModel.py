from sqlalchemy import Column, String, DateTime

from .BaseModel import BaseModel, UUIDFKey

class AdmissionModel(BaseModel):
    __tablename__ = "admissions"

    name = Column(String, comment="Name of the admission entry")
    name_en = Column(String, comment="English name of the admission entry")

    program_id = UUIDFKey(nullable=True, comment="Foreign key referencing the associated course")

    startdate = Column(DateTime, comment="Admission validity start date")
    enddate = Column(DateTime, comment="Admission validity end date")

    pass