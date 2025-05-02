import strawberry
import uuid
import typing

import strawberry.types

from uoishelpers.gqlpermissions import RBACObjectGQLModel

PaymentGQLModel = typing.Annotated["PaymentGQLModel", strawberry.lazy(".PaymentGQLModel")]

# from .BaseGQLModel import _BaseGQLModel as BaseGQLModel
from .BaseGQLModel import BaseGQLModel, BaseGQLModelEx, IDType

@strawberry.federation.type(keys=["id"], extend=True) #, description="An user in system")
class StudentGQLModel(BaseGQLModelEx):
    
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
    async def payment(self, info: strawberry.types.Info) -> typing.Optional[PaymentGQLModel]:
        from .AdmissionGQLModel import AdmissionGQLModel
        from .PaymentGQLModel import PaymentGQLModel
        loader = PaymentGQLModel.getLoader(info)
        rows = await loader.filter_by(student_id=self.id)
        row = next(rows, None)
        return PaymentGQLModel.from_dataclass(row) if row else None
    
    @strawberry.field(description="Platby za přijímací řízení")
    async def my_id(self, info: strawberry.types.Info) -> typing.Optional[IDType]:
        return self.id
    