import uuid
import strawberry

class BaseGQLModel:
    @classmethod
    def get_table_resolvers(cls):
        raise NotImplementedError()
    
    @classmethod
    def getloader(cls, info: strawberry.types.Info):
        raise NotImplementedError()
    
    @classmethod
    async def load_with_loader(cls, info: strawberry.types.Info, id: uuid.UUID):
        loader = cls.getloader(info=info)
        db_row = await loader.load(id)
        
        keyed_resolvers = cls.get_table_resolvers()
        instance_values = {
            name: resolver(db_row)
            for name, resolver in keyed_resolvers.items()
        }
        print(f"{cls}, {instance_values}", flush=True)
        instance = cls(**instance_values)
        return instance
