import strawberry
import uuid
import datetime
import typing

import strawberry.types

from uoishelpers.resolvers import getLoadersFromInfo, getUserFromInfo

from .BaseGQLModel import BaseGQLModel

AcProgramStudentGQLModel = typing.Annotated["AcProgramStudentGQLModel", strawberry.lazy(".AcProgramStudentGQLModel")]
UserGQLModel = typing.Annotated["UserGQLModel", strawberry.lazy(".UserGQLModel")]
AdDisciplineGQLModel = typing.Annotated["AdDisciplineGQLModel", strawberry.lazy(".AdDisciplineGQLModel")]
AdmissionGQLModel = typing.Annotated["AdmissionGQLModel", strawberry.lazy(".AdmissionGQLModel")]

@strawberry.type(description="single result reached by an user")
class AdDisciplineResultGQLModel(BaseGQLModel):

    @classmethod
    def get_table_resolvers(cls):
        return {
            "id": lambda row: row.id, 
            "start_date": lambda row: row.startdate,
            "end_date": lambda row: row.enddate,
            "program_id": lambda row: row.program_id
        }
    
    @classmethod
    def getloader(cls, info: strawberry.types.Info):
        return getLoadersFromInfo(info).DisciplineResulModel
    

    id: uuid.UUID = strawberry.field()
    description: typing.Optional[str] = strawberry.field(description="Poznámka k přezkoušení")
    score: typing.Optional[float] = strawberry.field(description="Bodové ohodnocení výkonu")
    user_id: typing.Optional[uuid.UUID] = strawberry.field(description="Kdo přezkoušení absolvoval")
    examiner_id: typing.Optional[uuid.UUID] = strawberry.field(description="Kdo přezkoušel")
    discipline_id: typing.Optional[uuid.UUID] = strawberry.field(description="Která disciplína (část předmětu)")
    exam_planed_date: typing.Optional[datetime.datetime] = strawberry.field(description="Naplánované datum")
    # program_id: uuid.UUID = strawberry.field()

    @strawberry.field(description="")
    async def student(self, info: strawberry.types.Info) -> typing.Optional["AcProgramStudentGQLModel"]:
        raise NotImplementedError()
        from .AcProgramStudentGQLModel import AcProgramStudentGQLModel
        result = await AcProgramStudentGQLModel.resolve_reference(info=info, id=self.program_id)
        return result

    @strawberry.field(description="")
    async def user(self, info: strawberry.types.Info) -> typing.Optional["UserGQLModel"]:
        from .UserGQLModel import UserGQLModel
        result = await UserGQLModel.resolve_reference(info=info, id=self.user_id)
        return result

    @strawberry.field(description="")
    async def examiner(self, info: strawberry.types.Info) -> typing.Optional["UserGQLModel"]:
        from .UserGQLModel import UserGQLModel
        result = await AcProgramStudentGQLModel.resolve_reference(info=info, id=self.examiner_id)
        return result

    @strawberry.field(description="")
    async def discipline(self, info: strawberry.types.Info) -> typing.Optional["AdDisciplineGQLModel"]:
        from .AdDisciplineGQLModel import AdDisciplineGQLModel
        result = await AdDisciplineGQLModel.resolve_reference(info=info, id=self.discipline_id)
        return result

    @strawberry.field(description="")
    async def admission(self, info: strawberry.types.Info) -> typing.Optional["AdmissionGQLModel"]:
        raise NotImplementedError()
        from .AdmissionGQLModel import AdmissionGQLModel
        result = await AdmissionGQLModel.resolve_reference(info=info, id=self.examiner_id)
        return result

