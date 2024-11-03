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
            "description": lambda row: row.description,
            "score": lambda row: row.score,
            "user_id": lambda row: row.user_id,
            "examiner_id": lambda row: row.examiner_id,
            "discipline_id": lambda row: row.discipline_id,
            "exam_planed_date": lambda row: row.exam_planed_date
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
        from .AcProgramStudentGQLModel import AcProgramStudentGQLModel
        result = await AcProgramStudentGQLModel.resolve_reference(info=info, id=self.user_id)
        return result
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
        result = await UserGQLModel.resolve_reference(info=info, id=self.examiner_id)
        return result

    @strawberry.field(description="")
    async def discipline(self, info: strawberry.types.Info) -> typing.Optional["AdDisciplineGQLModel"]:
        from .AdDisciplineGQLModel import AdDisciplineGQLModel
        result = await AdDisciplineGQLModel.load_with_loader(info=info, id=self.discipline_id)
        return result

    @strawberry.field(description="")
    async def admission(self, info: strawberry.types.Info) -> typing.Optional["AdmissionGQLModel"]:
        # raise NotImplementedError()
        from .AdmissionGQLModel import AdmissionGQLModel
        result = await AdmissionGQLModel.load_with_loader(info=info, id=self.examiner_id)
        return result

    @strawberry.field(description="")
    async def passed(self, info: strawberry.types.Info) -> typing.Optional[bool]:
        # raise NotImplementedError()
        from .AdDisciplineGQLModel import AdDisciplineGQLModel
        disciple_gql = await AdDisciplineGQLModel.load_with_loader(info=info, id=self.discipline_id)
        result = self.score >= disciple_gql.min_score
        return result
        