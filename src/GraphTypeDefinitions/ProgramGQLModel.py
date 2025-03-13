import strawberry
import uuid

import strawberry.types

from uoishelpers.gqlpermissions import RBACObjectGQLModel

# from .BaseGQLModel import _BaseGQLModel as BaseGQLModel
from .BaseGQLModel import BaseGQLModel, BaseGQLModelEx

@strawberry.federation.type(keys=["id"], extend=True) #, description="study program (accreditation)")
class ProgramGQLModel(BaseGQLModelEx, BaseGQLModel):
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