import strawberry
import uuid
import datetime
import typing

import strawberry.types

from uoishelpers.resolvers import getLoadersFromInfo, getUserFromInfo

from .BaseGQLModel import BaseGQLModel

AcProgramGQLModel = typing.Annotated["AcProgramGQLModel", strawberry.lazy(".AcProgramGQLModel")]

@strawberry.type(description="")
class AdmissionGQLModel(BaseGQLModel):

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
        return getLoadersFromInfo(info).AdmissionModel
    

    id: uuid.UUID = strawberry.field()
    start_date: datetime.datetime = strawberry.field()
    end_date: datetime.datetime = strawberry.field()

    program_id: uuid.UUID = strawberry.field()

    @strawberry.field(description="")
    async def program(self, info: strawberry.types.Info) -> typing.Optional["AcProgramGQLModel"]:
        from .AcProgramGQLModel import AcProgramGQLModel
        result = await AcProgramGQLModel.resolve_reference(info=info, id=self.program_id)
        return result

    pass


@strawberry.field(description="")
async def admission_by_id(self, info: strawberry.types.Info, id: uuid.UUID) -> typing.Optional[AdmissionGQLModel]:
    result = await AdmissionGQLModel.load_with_loader(info=info, id=id)
    return result