import strawberry
import uuid
import datetime
import typing

import strawberry.types

from uoishelpers.resolvers import getLoadersFromInfo, getUserFromInfo

from .BaseGQLModel import BaseGQLModel

AcProgramStudentGQLModel = typing.Annotated["AcProgramStudentGQLModel", strawberry.lazy(".AcProgramStudentGQLModel")]
AdmissionGQLModel = typing.Annotated["AdmissionGQLModel", strawberry.lazy(".AdmissionGQLModel")]
AdDisciplineGQLModel = typing.Annotated["AdDisciplineGQLModel", strawberry.lazy(".AdDisciplineGQLModel")]

@strawberry.type(description="this is exam, it groups disciplines")
class AdDisciplineTypeGQLModel(BaseGQLModel):

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
        return getLoadersFromInfo(info).DisciplineTypeModel
    

    id: uuid.UUID = strawberry.field()
    name: typing.Optional[str] = strawberry.field(description="Název předmětu")
    name_en: typing.Optional[str] = strawberry.field(description="Anglický název předmětu")
    description: typing.Optional[str] = strawberry.field(description="Popis - zaměření přezkoušení")
    description_en: typing.Optional[str] = strawberry.field(description="Anglický popis - zaměření přezkoušení")
    weight: typing.Optional[float] = strawberry.field(description="Váha výsledku pro výpočet celkového hodnocení")
    min_score: typing.Optional[float] = strawberry.field(description="Minimální počet bodů, kdy lze ještě splnit předmět")

    @strawberry.field(description="")
    async def disciplines(self, info: strawberry.types.Info) -> typing.Optional["AdDisciplineGQLModel"]:
        from .AdDisciplineGQLModel import AdDisciplineGQLModel
        result = await AdDisciplineGQLModel.resolve_reference(info=info, id=self.program_id)
        return result


