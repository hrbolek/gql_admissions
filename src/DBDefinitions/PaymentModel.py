from sqlalchemy import Column, String, DateTime, Float, ForeignKey

from .BaseModel import BaseModel, UUIDFKey

class PaymentModel(BaseModel):
    __tablename__ = "admission_payments"

    payment_info_id = Column(ForeignKey("admission_payment_infos.id"), comment="Generální platební podmínky")
    bank_unique_data = Column(String, comment="unikátní identifikátor platby vystavený bankou (link do banky)")
    variable_symbol = Column(String, comment="uvedený variabilní symbol")
    student_id = UUIDFKey(comment="identifikovaná přihláška / student")
    amount = Column(Float, comment="zaplacená částka")

    pass