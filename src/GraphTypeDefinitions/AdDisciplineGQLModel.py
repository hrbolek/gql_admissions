import strawberry
import uuid
import datetime
import typing

import strawberry.types

from uoishelpers.resolvers import getLoadersFromInfo, getUserFromInfo

from .BaseGQLModel import BaseGQLModel

AcProgramStudentGQLModel = typing.Annotated["AcProgramStudentGQLModel", strawberry.lazy(".AcProgramStudentGQLModel")]
AdmissionGQLModel = typing.Annotated["AdmissionGQLModel", strawberry.lazy(".AdmissionGQLModel")]
AdDisciplineResultGQLModel = typing.Annotated["AdDisciplineResultGQLModel", strawberry.lazy(".AdDisciplineResultGQLModel")]
AdDisciplineTypeGQLModel = typing.Annotated["AdDisciplineTypeGQLModel", strawberry.lazy(".AdDisciplineTypeGQLModel")]

@strawberry.type(description="discipline as a part of exam")
class AdDisciplineGQLModel(BaseGQLModel):

    @classmethod
    def get_table_resolvers(cls):
        return {
            "id": lambda row: row.id, 
            "name": lambda row: row.name,
            "max_score": lambda row: row.max_score,
            "min_score": lambda row: row.min_score,
            "discipline_type_id": lambda row: row.discipline_type_id,
            "admission_id": lambda row: row.admission_id,
        }
    
    @classmethod
    def getloader(cls, info: strawberry.types.Info):
        return getLoadersFromInfo(info).DisciplineModel
    
    id: uuid.UUID = strawberry.field()
    name: str = strawberry.field(description="Název disciplíny")
    max_score: float = strawberry.field(description="Maximální počet bodů, které lze v disciplíne dosáhnout")
    min_score: float = strawberry.field(description="Minimální počet bodů, kdy lze ještě splnit disciplínu")
    discipline_type_id: uuid.UUID = strawberry.field(description="Fakticky předmět přijímacího řízení")
    admission_id: uuid.UUID = strawberry.field()

    @strawberry.field(description="")
    async def admission(self, info: strawberry.types.Info) -> typing.Optional["AdmissionGQLModel"]:
        from .AdmissionGQLModel import AdmissionGQLModel
        result = await AdmissionGQLModel.load_with_loader(info=info, id=self.admission_id)
        return result

    @strawberry.field(description="")
    async def results(self, info: strawberry.types.Info) -> typing.List["AdDisciplineResultGQLModel"]:
        from .AdDisciplineResultGQLModel import AdDisciplineResultGQLModel
        loader = AdDisciplineResultGQLModel.getloader(info=info)
        rows = await loader.filter_by(discipline_id=self.id)
        results = (AdDisciplineResultGQLModel.from_sqlalchemy(row) for row in rows)
        return results

    @strawberry.field(description="")
    async def type(self, info: strawberry.types.Info) -> typing.Optional["AdDisciplineTypeGQLModel"]:
        from .AdDisciplineTypeGQLModel import AdDisciplineTypeGQLModel
        result = await AdDisciplineTypeGQLModel.load_with_loader(info=info, id=self.discipline_type_id)
        return result

