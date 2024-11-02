import strawberry
import uuid

@strawberry.federation.type(keys=["id"], extend=True)
class AcProgramStudentGQLModel:
    id: uuid.UUID = strawberry.field()
