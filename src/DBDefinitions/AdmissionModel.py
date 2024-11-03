from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .BaseModel import BaseModel, UUIDFKey

class AdmissionModel(BaseModel):
    __tablename__ = "admissions"

    name = Column(String, comment="Name of the admission entry")
    name_en = Column(String, comment="English name of the admission entry")

    state_id = UUIDFKey(nullable=True, comment="stav přijímacího řízení")
    program_id = UUIDFKey(nullable=True, comment="Program, pro který je přijímací řízení vypsáno")
    payment_info_id = Column(ForeignKey("admission_payment_infos.id"), nullable=True, comment="platební podmínky")

    application_start_date = Column(DateTime, comment="Od kdy lze podávat přihlášky")
    application_last_date = Column(DateTime, comment="Poslední možnost podání přihlášky")
    end_date = Column(DateTime, comment="Konec přijímacího řízení")
    condition_date = Column(DateTime, comment="Do kdy lze doložit splnění podmínek")
    payment_date = Column(DateTime, comment="Do kdy lze zaplatit poplatek")
    condition_extended_date = Column(DateTime, comment="Prodloužená lhůta pro doložení splnění podmínek")
    request_condition_extend_date = Column(DateTime, comment="Lhůta do kdy lze požádat o proudloužení pro doložení splnění podmínek")
    request_extra_conditions_date = Column(DateTime, comment="Lhůta do kdy lze požádat o specifické podmínky přijímacího řízení")
    request_extra_date_date = Column(DateTime, comment="Lhůta do kdy lze požádat o extra termín přijímacích zkoušek")
    exam_start_date = Column(DateTime, comment="První možný den přijímacích zkoušek")
    exam_last_date = Column(DateTime, comment="Poslední možný den přijímacích zkoušek")
    student_entry_date = Column(DateTime, comment="Den zápisu")

    discipline = relationship("PaymentInfoModel", viewonly=True, uselist=False, lazy="joined") # https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html

    pass