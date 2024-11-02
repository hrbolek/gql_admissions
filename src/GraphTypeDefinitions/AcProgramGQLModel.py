import strawberry
import uuid

import strawberry.types

@strawberry.federation.type(keys=["id"], extend=True)
class AcProgramGQLModel:
    id: uuid.UUID = strawberry.field()

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        result = cls(**data)
        return result