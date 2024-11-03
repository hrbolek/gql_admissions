from sqlalchemy import (
    Column, 
    String, 
    DateTime, 
    Float,
    ForeignKey
)

from .BaseModel import BaseModel, UUIDFKey

class PaymentInfoModel(BaseModel):
    __tablename__ = "admission_payment_infos"

    account_number = Column(String, comment="číslo účtu s kódem banky za lomítkem")
    specific_symbol = Column(String, comment="specifický symbol")
    constant_symbol = Column(String, comment="konstantní symbol")
    IBAN = Column(String, comment="IBAN code")
    SWIFT = Column(String, comment="SWIFT bank code")
    amount = Column(Float, comment="Částka k zaplacení")
    pass