import strawberry
import uuid
import datetime
import typing

import strawberry.file_uploads
import strawberry.types

from uoishelpers.resolvers import getLoadersFromInfo, getUserFromInfo

from .BaseGQLModel import BaseGQLModel

AcProgramGQLModel = typing.Annotated["AcProgramGQLModel", strawberry.lazy(".AcProgramGQLModel")]
AdmissionGQLModel = typing.Annotated["AdmissionGQLModel", strawberry.lazy(".AdmissionGQLModel")]
PaymentGQLModel = typing.Annotated["PaymentGQLModel", strawberry.lazy(".PaymentGQLModel")]

@strawberry.type(description="one (in one year) admission linked to program")
class PaymentInfoGQLModel(BaseGQLModel):

    @classmethod
    def get_table_resolvers(cls):
        return {
            "id": lambda row: row.id, 
            "account_number": lambda row: row.account_number,
            "specific_symbol": lambda row: row.specific_symbol,
            "constant_symbol": lambda row: row.constant_symbol,
            "IBAN": lambda row: row.IBAN,
            "SWIFT": lambda row: row.SWIFT,
            "amount": lambda row: row.amount,
        }
    
    @classmethod
    def getloader(cls, info: strawberry.types.Info):
        return getLoadersFromInfo(info).PaymentInfoModel
    

    id: uuid.UUID = strawberry.field()
    # admission_id: uuid.UUID = strawberry.field()
    account_number: typing.Optional[str] = strawberry.field(description="číslo účtu s kódem banky za lomítkem")
    specific_symbol: typing.Optional[str] = strawberry.field(description="specifický symbol")
    constant_symbol: typing.Optional[str] = strawberry.field(description="konstantní symbol")
    IBAN: typing.Optional[str] = strawberry.field(description="IBAN code")
    SWIFT: typing.Optional[str] = strawberry.field(description="SWIFT bank code")
    amount: typing.Optional[float] = strawberry.field(description="Částka k zaplacení")
    
    @strawberry.field(description="")
    async def admission(self, info: strawberry.types.Info) -> typing.Optional["AdmissionGQLModel"]:
        from .AdmissionGQLModel import AdmissionGQLModel
        result = await AdmissionGQLModel.resolve_reference(info=info, id=self.admission_id)
        return result
    
    @strawberry.field(description="")
    async def payments(self, info: strawberry.types.Info) -> typing.List["PaymentGQLModel"]:
        from .PaymentGQLModel import PaymentGQLModel
        loader = PaymentGQLModel.getloader(info=info)
        rows = await loader.filter_by(payment_info_id=self.id)
        results = (PaymentGQLModel.from_sqlalchemy(row) for row in rows)
        return results
        # raise NotImplementedError()
        # from .AdmissionGQLModel import AdmissionGQLModel
        # result = await AdmissionGQLModel.resolve_reference(info=info, id=self.admission_id)
        # return result
    
        
    pass
