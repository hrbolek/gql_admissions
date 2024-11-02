import strawberry
import uuid
import datetime
import typing

import strawberry.types

from uoishelpers.resolvers import getLoadersFromInfo, getUserFromInfo

from .BaseGQLModel import BaseGQLModel

AcProgramGQLModel = typing.Annotated["AcProgramGQLModel", strawberry.lazy(".AcProgramGQLModel")]
AdDisciplineGQLModel = typing.Annotated["AdDisciplineGQLModel", strawberry.lazy(".AdDisciplineGQLModel")]
PaymentInfoGQLModel = typing.Annotated["PaymentInfoGQLModel", strawberry.lazy(".PaymentInfoGQLModel")]
AcProgramStudentGQLModel = typing.Annotated["AcProgramStudentGQLModel", strawberry.lazy(".AcProgramStudentGQLModel")]

@strawberry.type(description="one (in one year) admission linked to program")
class AdmissionGQLModel(BaseGQLModel):

    @classmethod
    def get_table_resolvers(cls):
        return {
            "id": lambda row: row.id, 
            "state_id": lambda row: row.state_id,
            "program_id": lambda row: row.program_id,
            "payment_info_id": lambda row: row.payment_info_id,

            "application_start_date": lambda row: row.application_start_date,
            "application_last_date": lambda row: row.application_last_date,
            "end_date": lambda row: row.end_date,
            "condition_date": lambda row: row.condition_date,
            "payment_date": lambda row: row.payment_date,
            "condition_extended_date": lambda row: row.condition_extended_date,
            "request_condition_extend_date": lambda row: row.request_condition_extend_date,
            "request_extra_conditions_date": lambda row: row.request_extra_conditions_date,
            "request_extra_date_date": lambda row: row.request_extra_date_date,
            "exam_start_date": lambda row: row.exam_start_date,
            "exam_last_date": lambda row: row.exam_last_date,
            "student_entry_date": lambda row: row.student_entry_date,
        }
    
    @classmethod
    def getloader(cls, info: strawberry.types.Info):
        return getLoadersFromInfo(info).AdmissionModel

    id: uuid.UUID = strawberry.field()
    state_id: typing.Optional[uuid.UUID] = strawberry.field(description="stav přijímacího řízení")
    program_id: typing.Optional[uuid.UUID] = strawberry.field(description="Program, pro který je přijímací řízení vypsáno")
    payment_info_id: typing.Optional[uuid.UUID] = strawberry.field(description="platební podmínky")

    application_start_date: typing.Optional[datetime.datetime] = strawberry.field(description="Od kdy lze podávat přihlášky")
    application_last_date: typing.Optional[datetime.datetime] = strawberry.field(description="Poslední možnost podání přihlášky")
    end_date: typing.Optional[datetime.datetime] = strawberry.field(description="Konec přijímacího řízení")
    condition_date: typing.Optional[datetime.datetime] = strawberry.field(description="Do kdy lze doložit splnění podmínek")
    payment_date: typing.Optional[datetime.datetime] = strawberry.field(description="Do kdy lze zaplatit poplatek")
    condition_extended_date: typing.Optional[datetime.datetime] = strawberry.field(description="Prodloužená lhůta pro doložení splnění podmínek")
    request_condition_extend_date: typing.Optional[datetime.datetime] = strawberry.field(description="Lhůta do kdy lze požádat o proudloužení pro doložení splnění podmínek")
    request_extra_conditions_date: typing.Optional[datetime.datetime] = strawberry.field(description="Lhůta do kdy lze požádat o specifické podmínky přijímacího řízení")
    request_extra_date_date: typing.Optional[datetime.datetime] = strawberry.field(description="Lhůta do kdy lze požádat o extra termín přijímacích zkoušek")
    exam_start_date: typing.Optional[datetime.datetime] = strawberry.field(description="První možný den přijímacích zkoušek")
    exam_last_date: typing.Optional[datetime.datetime] = strawberry.field(description="Poslední možný den přijímacích zkoušek")
    student_entry_date: typing.Optional[datetime.datetime] = strawberry.field(description="Den zápisu")

    @strawberry.field(description="")
    async def program(self, info: strawberry.types.Info) -> typing.Optional["AcProgramGQLModel"]:
        from .AcProgramGQLModel import AcProgramGQLModel
        result = await AcProgramGQLModel.resolve_reference(info=info, id=self.program_id)
        return result

    @strawberry.field(description="")
    async def disciplines(self, info: strawberry.types.Info) -> typing.List["AdDisciplineGQLModel"]:
        from .AdDisciplineGQLModel import AdDisciplineGQLModel
        loader = AdDisciplineGQLModel.getloader(info=info)
        rows = await loader.filter_by(admission_id=self.id)
        results = (AdDisciplineGQLModel.from_sqlalchemy(row) for row in rows)
        return results
        # raise NotImplementedError()
        from .AdDisciplineGQLModel import AdDisciplineGQLModel
        result = await AdDisciplineGQLModel.resolve_reference(info=info, id=self.program_id)
        return result

    @strawberry.field(description="")
    async def payment_info(self, info: strawberry.types.Info) -> typing.Optional["PaymentInfoGQLModel"]:
        from .PaymentInfoGQLModel import PaymentInfoGQLModel
        result = await PaymentInfoGQLModel.load_with_loader(info=info, id=self.payment_info_id)
        return result

    @strawberry.field(description="")
    async def applications(self, info: strawberry.types.Info) -> typing.List["AcProgramStudentGQLModel"]:
        raise NotImplementedError()
        from .PaymentInfoGQLModel import PaymentInfoGQLModel
        result = await PaymentInfoGQLModel.resolve_reference(info=info, id=self.program_id)
        return result

    pass


@strawberry.field(description="")
async def admission_by_id(self, info: strawberry.types.Info, id: uuid.UUID) -> typing.Optional[AdmissionGQLModel]:
    result = await AdmissionGQLModel.load_with_loader(info=info, id=id)
    return result