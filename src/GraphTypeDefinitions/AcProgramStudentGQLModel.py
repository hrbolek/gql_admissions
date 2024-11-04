import typing
import strawberry
import uuid

@strawberry.federation.type(keys=["id"], extend=True) # , description="user linked with study program")
class AcProgramStudentGQLModel:
    id: uuid.UUID = strawberry.field()

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        result = cls(**data)
        return result


    program_id: typing.Optional[uuid.UUID] = strawberry.federation.field(external=True, default=None)
    user_id: typing.Optional[uuid.UUID] = strawberry.federation.field(external=True, default=None)
    state_id: typing.Optional[uuid.UUID] = strawberry.federation.field(external=True, default=None)

    @strawberry.field(description="unique number for student (user) and program")
    async def register_number(self) -> uuid.UUID:
        return self.id
    
    @strawberry.field(description="Zaplaceno za přijímací řízení")
    async def admission_paid(self) -> typing.Optional[bool]:
        raise NotImplementedError()
        return self.id    