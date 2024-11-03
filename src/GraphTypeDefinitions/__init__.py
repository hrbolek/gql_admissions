import strawberry

@strawberry.type(description="")
class Query:
    from .AdmissionGQLModel import admission_by_id


from .UserGQLModel import UserGQLModel
schema = strawberry.federation.Schema(
    query=Query, 
    extensions=[],
    types=(UserGQLModel, ),
    enable_federation_2=True
)

from uoishelpers.schema import WhoAmIExtension
schema.extensions.append(WhoAmIExtension)
