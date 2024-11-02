import typing
import strawberry
import uuid

@strawberry.federation.type(keys=["id"], extend=True, description="user linked with study program")
class AcProgramStudentGQLModel:
    id: uuid.UUID = strawberry.field()
    program_id: uuid.UUID = strawberry.federation.field(external=True)
    user_id: uuid.UUID = strawberry.federation.field(external=True)
    state_id: uuid.UUID = strawberry.federation.field(external=True)

    @strawberry.field(description="unique number for student (user) and program")
    async def register_number(self) -> uuid.UUID:
        return self.id
    
    @strawberry.field(description="Zaplaceno za přijímací řízení")
    async def admission_payed(self) -> typing.Optional[bool]:
        raise NotImplementedError()
        return self.id    