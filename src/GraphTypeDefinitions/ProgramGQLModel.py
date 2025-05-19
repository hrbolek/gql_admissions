import typing
import strawberry
import uuid

import strawberry.types

from uoishelpers.gqlpermissions import RBACObjectGQLModel, OnlyForAuthentized
from uoishelpers.resolvers import VectorResolver
# from .BaseGQLModel import _BaseGQLModel as BaseGQLModel
from .BaseGQLModel import BaseGQLModel, BaseGQLModelEx

from .AdmissionGQLModel import AdmissionGQLModel, AdmissionInputFilter
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

    admissions: typing.List["AdmissionGQLModel"] = strawberry.field(
        description="Admissions for this program",
        permission_classes=[
            OnlyForAuthentized
        ],
        resolver=VectorResolver["AdmissionGQLModel"](fkey_field_name="program_id", whereType=AdmissionInputFilter),
    )
    