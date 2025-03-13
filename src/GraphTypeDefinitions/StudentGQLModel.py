import strawberry
import uuid
import typing

import strawberry.types

from uoishelpers.gqlpermissions import RBACObjectGQLModel

PaymentGQLModel = typing.Annotated["PaymentGQLModel", strawberry.lazy(".PaymentGQLModel")]

# from .BaseGQLModel import _BaseGQLModel as BaseGQLModel
from .BaseGQLModel import BaseGQLModel, BaseGQLModelEx

@strawberry.federation.type(keys=["id"], extend=True) #, description="An user in system")
class StudentGQLModel(BaseGQLModel, BaseGQLModelEx):
    
    from .BaseGQLModel import (
        id,
        lastchange,
        created,
        createdby_id,
        changedby_id,
        createdby,
        changedby,
        rbacobject_id,
        rbacobject
    )    
               
    @strawberry.field(description="Platby za přijímací řízení")
    async def payments(self, info: strawberry.types.Info) -> typing.List[PaymentGQLModel]:
        from .AdmissionGQLModel import AdmissionGQLModel
        from .PaymentGQLModel import PaymentGQLModel
        return []
    
        raise NotImplementedError()
        loader = AdDisciplineResultGQLModel.getloader(info=info)
        rows = await loader.filter_by(user_id=self.id)
        results = (AdmissionGQLModel.from_sqlalchemy(row.discipline.admission) for row in rows)
        return results
                
            