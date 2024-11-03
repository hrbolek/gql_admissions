import strawberry
import uuid
import typing

import strawberry.types

AdDisciplineResultGQLModel = typing.Annotated["AdDisciplineResultGQLModel", strawberry.lazy(".AdDisciplineResultGQLModel")]
AdmissionGQLModel = typing.Annotated["AdmissionGQLModel", strawberry.lazy(".AdmissionGQLModel")]
PaymentGQLModel = typing.Annotated["PaymentGQLModel", strawberry.lazy(".PaymentGQLModel")]

@strawberry.federation.type(keys=["id"], extend=True, description="An user in system")
class StateGQLModel:
    id: uuid.UUID = strawberry.field()

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        result = cls(**data)
        return result
    