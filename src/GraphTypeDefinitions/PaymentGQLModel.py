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
PaymentInfoGQLModel = typing.Annotated["PaymentInfoGQLModel", strawberry.lazy(".PaymentInfoGQLModel")]

@strawberry.type(description="one (in one year) admission linked to program")
class PaymentGQLModel(BaseGQLModel):

    @classmethod
    def get_table_resolvers(cls):
        return {
            "id": lambda row: row.id, 
            "payment_info_id": lambda row: row.payment_info_id,
            "bank_unique_data": lambda row: row.bank_unique_data,
            "variable_symbol": lambda row: row.variable_symbol,
            "student_id": lambda row: row.student_id,
            "amount": lambda row: row.amount
        }
    
    @classmethod
    def getloader(cls, info: strawberry.types.Info):
        return getLoadersFromInfo(info).PaymentModel
    
    id: uuid.UUID = strawberry.field()
    payment_info_id: typing.Optional[uuid.UUID] = strawberry.field(description="Generální platební podmínky")
    bank_unique_data: typing.Optional[str] = strawberry.field(description="unikátní identifikátor platby vystavený bankou (link do banky)")
    variable_symbol: typing.Optional[str] = strawberry.field(description="uvedený variabilní symbol")
    student_id: typing.Optional[uuid.UUID] = strawberry.field(description="identifikovaná přihláška / student")
    amount: typing.Optional[int] = strawberry.field(description="zaplacená částka")
    
    @strawberry.field(description="")
    async def payment_info(self, info: strawberry.types.Info) -> typing.Optional["PaymentInfoGQLModel"]:
        from .PaymentInfoGQLModel import PaymentInfoGQLModel
        result = await PaymentInfoGQLModel.resolve_reference(info=info, id=self.payment_info_id)
        return result
    pass
