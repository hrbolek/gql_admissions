import datetime
import strawberry
import uuid
import typing

import strawberry.types
from uoishelpers.gqlpermissions import RBACObjectGQLModel

# from .BaseGQLModel import _BaseGQLModel as BaseGQLModel
from .BaseGQLModel import BaseGQLModel, IDType, BaseGQLModelEx

UserGQLModel = typing.Annotated["UserGQLModel", strawberry.lazy(".UserGQLModel")]

@strawberry.federation.type(keys=["id"], extend=True) # , description="An user in system")
class StateGQLModel(BaseGQLModelEx, BaseGQLModel):
    
    # from .BaseGQLModel import (
    #     id,
    #     lastchange,
    #     created,
    #     createdby_id,
    #     changedby_id,
    #     createdby,
    #     changedby,
    #     rbacobject_id,
    #     rbacobject
    # )

    id: uuid.UUID = strawberry.field()
    lastchange: typing.Optional[datetime.datetime] = strawberry.federation.field(external=True, default=None)
    created: typing.Optional[datetime.datetime] = strawberry.federation.field(external=True, default=None)
    createdby_id: typing.Optional[IDType] = strawberry.federation.field(external=True, default=None)
    changedby_id: typing.Optional[IDType] = strawberry.federation.field(external=True, default=None)
    rbacobject_id: typing.Optional[IDType] = strawberry.federation.field(external=True, default=None)
    createdby: typing.Optional["UserGQLModel"] = strawberry.federation.field(external=True, default=None)
    changedby: typing.Optional["UserGQLModel"] = strawberry.federation.field(external=True, default=None)
    rbacobject: typing.Optional["RBACObjectGQLModel"] = strawberry.federation.field(external=True, default=None)
