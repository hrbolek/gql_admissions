import strawberry

@strawberry.type(description="")
class Query:
    from .AdmissionGQLModel import admission_by_id

schema = strawberry.federation.Schema(
    query=Query, 
    extensions=[]
)

from uoishelpers.schema import WhoAmIExtension
schema.extensions.append(WhoAmIExtension)
