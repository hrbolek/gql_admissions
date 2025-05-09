import uuid
import datetime
import typing
import strawberry
import dataclasses

from uoishelpers.gqlpermissions import OnlyForAuthentized, RBACObjectGQLModel

IDType = uuid.UUID
UserGQLModel = typing.Annotated["UserGQLModel", strawberry.lazy(".UserGQLModel")]

# @classmethod
# async def resolve_reference(cls, info: strawberry.types.Info, id: IDType, **otherData):
#     _id = IDType(id) if isinstance(id, str) else id
#     return None if id is None else cls(id=_id, **otherData)
import strawberry

from strawberry.federation.schema_directive import schema_directive, Location
from strawberry.directive import DirectiveLocation
@schema_directive(
    repeatable=True,
    compose=True,
    description="Description for foreign keys",
    locations=[Location.INPUT_FIELD_DEFINITION, Location.FIELD_DEFINITION, DirectiveLocation.FIELD],
)
class Relation:
    """
    @relation(to: Typ, field: 'id')
    říká, že pole inputu je cizí klíč na zadaný typ.
    """
    to: str
    field: str = "id"

@strawberry.interface(
    # keys=["id"], 
    description="""Entity representing an interface"""
)
class BaseGQLModel:
    
    # @classmethod
    # def getLoader(cls, info: strawberry.types.Info):
    #     raise NotImplementedError()
    
    @classmethod
    def from_dataclass(cls, db_row):
        db_row_dict = dataclasses.asdict(db_row)
        instance = cls(**db_row_dict)
        return instance

    @classmethod
    async def load_with_loader(cls, info: strawberry.types.Info, 
        id: typing.Annotated[uuid.UUID, strawberry.argument(description="primary key")]
    ):
        if id is None: return None

        _id = IDType(id) if isinstance(id, str) else id
        loader = cls.getLoader(info=info)
        db_row = await loader.load(_id)
        
        return cls(id=id) if db_row is None else cls.from_dataclass(db_row=db_row)
    
    @classmethod
    def resolve_reference(cls, info: strawberry.types.Info, id: uuid.UUID, **otherdata):
        _id = IDType(id) if isinstance(id, str) else id
        return cls.load_with_loader(info=info, id=_id)
       
    id: IDType = strawberry.field(
        description="primary key", 
        # default=None,
        permission_classes=[OnlyForAuthentized]
    )
    lastchange: typing.Optional[datetime.datetime] = strawberry.field(
        description="timestamp", 
        default=None,
        permission_classes=[OnlyForAuthentized]
    )
    created: typing.Optional[datetime.datetime] = strawberry.field(
        description="date & time of unit born", 
        default=None,
        permission_classes=[OnlyForAuthentized]
    )
    createdby_id: typing.Optional[IDType] = strawberry.field(
        description="who created this entity", 
        default=None,
        permission_classes=[OnlyForAuthentized],
        directives=[Relation(to="UserGQLModel")]
    )
    changedby_id: typing.Optional[IDType] = strawberry.field(
        description="who changed this entity", 
        default=None,
        permission_classes=[OnlyForAuthentized],
        directives=[Relation(to="UserGQLModel")]
    )
    rbacobject_id: typing.Optional[IDType] = strawberry.field(
        description="rbac ruling object", 
        default=None,
        permission_classes=[OnlyForAuthentized],
        directives=[Relation(to="GroupGQLModel"), Relation(to="UserGQLModel")]
    )

    @strawberry.field(
        description="who created this entity",
        permission_classes=[OnlyForAuthentized]
        )
    async def createdby(self) -> typing.Optional["UserGQLModel"]:
        from .UserGQLModel import UserGQLModel
        return None if self.changedby_id is None else UserGQLModel(id=self.createdby_id)

    @strawberry.field(
        description="who created this entity",
        permission_classes=[OnlyForAuthentized]
        )
    async def changedby(self) -> typing.Optional["UserGQLModel"]:
        from .UserGQLModel import UserGQLModel
        return None if self.changedby_id is None else UserGQLModel(id=self.changedby_id)

    @strawberry.field(
        description="rbac holds relations of user",
        permission_classes=[OnlyForAuthentized]
        )
    async def rbacobject(self) -> typing.Optional["RBACObjectGQLModel"]:
        return None if self.rbacobject_id is None else RBACObjectGQLModel(id=self.rbacobject_id)


class BaseGQLModelEx:

    @classmethod
    async def resolve_reference(cls, info: strawberry.types.Info, **data):
        id = data.get("id", None)
        id = IDType(id) if isinstance(id, str) else id
        data["id"] = id
        
        return None if id is None else cls(**data)
    
    # @classmethod
    # async def load_with_loader(cls, info: strawberry.types.Info, id: uuid.UUID):
    #     if id is None: return None

    #     _id = IDType(id) if isinstance(id, str) else id
    #     return cls(id=_id) if _id else None
    
    id: uuid.UUID = strawberry.federation.field(external=True)
    # lastchange: typing.Optional[datetime.datetime] = strawberry.federation.field(shareable=True)
    # created: typing.Optional[datetime.datetime] = strawberry.federation.field(shareable=True)
    # createdby_id: typing.Optional[IDType] = strawberry.federation.field(shareable=True)
    # changedby_id: typing.Optional[IDType] = strawberry.federation.field(shareable=True)
    # rbacobject_id: typing.Optional[IDType] = strawberry.federation.field(shareable=True)
    # createdby: typing.Optional["UserGQLModel"] = strawberry.federation.field(shareable=True)
    # changedby: typing.Optional["UserGQLModel"] = strawberry.federation.field(shareable=True)
    # rbacobject: typing.Optional["RBACObjectGQLModel"] = strawberry.federation.field(shareable=True)


id = strawberry.federation.field(external=True, graphql_type=IDType, default=None)
lastchange: typing.Optional[datetime.datetime] = strawberry.federation.field(external=True, graphql_type=typing.Optional[datetime.datetime], default=None)
created: typing.Optional[datetime.datetime] = strawberry.federation.field(external=True, graphql_type=typing.Optional[datetime.datetime], default=None)
createdby_id:typing.Optional[IDType] = strawberry.federation.field(external=True, graphql_type=typing.Optional[IDType], default=None)
changedby_id: typing.Optional[IDType] = strawberry.federation.field(external=True, graphql_type=typing.Optional[IDType], default=None)
rbacobject_id:typing.Optional[IDType] = strawberry.federation.field(external=True, graphql_type=typing.Optional[IDType], default=None)
createdby: typing.Optional["UserGQLModel"] = strawberry.federation.field(external=True, graphql_type=typing.Optional["UserGQLModel"], default=None)
changedby: typing.Optional["UserGQLModel"] = strawberry.federation.field(external=True, graphql_type=typing.Optional["UserGQLModel"], default=None)
rbacobject: typing.Optional["RBACObjectGQLModel"] = strawberry.federation.field(external=True, graphql_type=typing.Optional["RBACObjectGQLModel"], default=None)

# id = strawberry.federation.field(shareable=True, graphql_type=IDType)
# lastchange = strawberry.federation.field(shareable=True, graphql_type=typing.Optional[datetime.datetime])
# created = strawberry.federation.field(shareable=True, graphql_type=typing.Optional[datetime.datetime])
# createdby_id = strawberry.federation.field(shareable=True, graphql_type=IDType)
# changedby_id = strawberry.federation.field(shareable=True, graphql_type=IDType)
# rbacobject_id = strawberry.federation.field(shareable=True, graphql_type=IDType)
# createdby = strawberry.federation.field(shareable=True, graphql_type=typing.Optional["UserGQLModel"])
# changedby = strawberry.federation.field(shareable=True, graphql_type=typing.Optional["UserGQLModel"])
# rbacobject = strawberry.federation.field(shareable=True, graphql_type=typing.Optional["RBACObjectGQLModel"])


