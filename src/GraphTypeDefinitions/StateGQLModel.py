import strawberry
import uuid
import typing

import strawberry.types
from uoishelpers.gqlpermissions import RBACObjectGQLModel

# from .BaseGQLModel import _BaseGQLModel as BaseGQLModel
from .BaseGQLModel import BaseGQLModel, BaseGQLModelEx

@strawberry.federation.type(keys=["id"], extend=True) # , description="An user in system")
class StateGQLModel(BaseGQLModel, BaseGQLModelEx):
    
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