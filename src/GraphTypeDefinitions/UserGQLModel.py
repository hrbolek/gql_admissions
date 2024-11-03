import strawberry
import uuid
import typing

import strawberry.types

AdDisciplineResultGQLModel = typing.Annotated["AdDisciplineResultGQLModel", strawberry.lazy(".AdDisciplineResultGQLModel")]
AdmissionGQLModel = typing.Annotated["AdmissionGQLModel", strawberry.lazy(".AdmissionGQLModel")]
PaymentGQLModel = typing.Annotated["PaymentGQLModel", strawberry.lazy(".PaymentGQLModel")]

@strawberry.federation.type(keys=["id"], extend=True, description="An user in system")
class UserGQLModel:
    id: uuid.UUID = strawberry.field()

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        result = cls(**data)
        return result
    
    @strawberry.field(description="Výsledky zkoušek (disciplín) v přijímacím řízení")
    async def admission_discipline_results(self, info: strawberry.types.Info) -> typing.List[AdDisciplineResultGQLModel]:
        from .AdDisciplineResultGQLModel import AdDisciplineResultGQLModel
        loader = AdDisciplineResultGQLModel.getloader(info=info)
        rows = await loader.filter_by(user_id=self.id)
        results = (AdDisciplineResultGQLModel.from_sqlalchemy(row) for row in rows)
        return results
        
    @strawberry.field(description="Přijímací řízení")
    async def admissions(self, info: strawberry.types.Info) -> typing.List[AdmissionGQLModel]:
        from .AdDisciplineResultGQLModel import AdDisciplineResultGQLModel
        from .AdmissionGQLModel import AdmissionGQLModel

        loader = AdDisciplineResultGQLModel.getloader(info=info)
        rows = await loader.filter_by(user_id=self.id)
        results = (AdmissionGQLModel.from_sqlalchemy(row.discipline.admission) for row in rows)
        return results
                
    @strawberry.field(description="Platby za přijímací řízení")
    async def admission_payments(self, info: strawberry.types.Info) -> typing.List[PaymentGQLModel]:
        from .AdDisciplineResultGQLModel import AdDisciplineResultGQLModel
        from .AdmissionGQLModel import AdmissionGQLModel
        from .PaymentGQLModel import PaymentGQLModel

        raise NotImplementedError()
        loader = AdDisciplineResultGQLModel.getloader(info=info)
        rows = await loader.filter_by(user_id=self.id)
        results = (AdmissionGQLModel.from_sqlalchemy(row.discipline.admission) for row in rows)
        return results
                
            