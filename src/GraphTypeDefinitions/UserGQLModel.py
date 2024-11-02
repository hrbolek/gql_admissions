import strawberry
import uuid

import strawberry.types

@strawberry.federation.type(keys=["id"], extend=True, description="An user in system")
class UserGQLModel:
    id: uuid.UUID = strawberry.field()

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        result = cls(**data)
        return result