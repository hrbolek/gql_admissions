import strawberry
import uuid

import strawberry.types

@strawberry.federation.type(keys=["id"], extend=True) #, description="study program (accreditation)")
class AcProgramGQLModel:
    id: uuid.UUID = strawberry.field()

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        result = cls(**data)
        return result