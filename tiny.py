import strawberry
from strawberry.schema_directive import schema_directive, Location

@schema_directive(
    locations=[Location.INPUT_FIELD_DEFINITION],
    repeatable=True,
)
class Relation:
    to: str
    field: str = "id"

@strawberry.input
class FooInput:
    bar_id: strawberry.ID = strawberry.field(
        directives=[Relation(to="Bar")]
    )

@strawberry.type
class Query:
    @strawberry.mutation
    def do_thing(self, input: FooInput) -> bool:
        return True

schema = strawberry.Schema(
    query=Query,
    schema_directives=[Relation],        # ← make sure this is here
)

if __name__ == "__main__":
    print(schema.as_str())
