import strawberry

from .AdmissionGQLModel import AdmissionQuery, AdmissionMutation
from .PaymentGQLModel import PaymentQuery, PaymentMutation
from .PaymentInfoGQLModel import PaymentInfoQuery, PaymentInfoMutation

@strawberry.type(description="")
class Query(
    AdmissionQuery,
    PaymentQuery,
    PaymentInfoQuery
):
    pass

@strawberry.type(description="")
class Mutation(
    AdmissionMutation,
    PaymentMutation,
    PaymentInfoMutation
):
    pass


from .UserGQLModel import UserGQLModel
from .ProgramGQLModel import ProgramGQLModel
from .StateGQLModel import StateGQLModel
from .StudentGQLModel import StudentGQLModel
from .UserGQLModel import UserGQLModel

schema = strawberry.federation.Schema(
    query=Query, 
    mutation=Mutation,
    extensions=[],
    types=(UserGQLModel, ProgramGQLModel, StateGQLModel, StudentGQLModel ),
    # enable_federation_2=True
)

from uoishelpers.schema import WhoAmIExtension
schema.extensions.append(WhoAmIExtension)
