import uuid

def gatherTypes(data: dict):
    queryOrMutation = "query"
    querytype = {"__typename": queryOrMutation, "fields": {}}
    types = {queryOrMutation: querytype}
    def gatherDictTypes(name, data: dict):
        typedef = None
        __typename = data.get("__typename", None)
        if __typename is not None:
            typedef = types.get(__typename, None)
        if typedef is None:
            if __typename is None:
                __typename = f"{name}.{uuid.uuid4()}.GQLModel"
            typedef = {
                "id": f"{uuid.uuid4()}", 
                "__typename": __typename, 
                "fields": {}
            }
            types[__typename] = typedef

        fields = typedef["fields"]
        for key, value in data.items():
            if key in fields:
                continue
            if key == "__typename":
                continue
            field = {
                "name": key,
                "type_id": "",
                "typing": ""
            }
            fields[key] = field
            if isinstance(value, dict):
                t = gatherDictTypes(key, value)
                field["type_id"] = t["id"]
                field["type"] = t
                field["typing"] = "OBJECT"
            elif isinstance(value, list):
                t = gatherListTypes(key, value)
                field["type_id"] = t["id"]
                field["type"] = t
                field["typing"] = "LIST"
            else:
                fields[key] = {
                    "typing": "",
                    "type": {"__typename": f"{type(value).__name__}"}
                }
        # typedef["fields"] = list(typedef["fields"].values())
        return typedef
    
    def gatherListTypes(name, data: list):
        id = f"{uuid.uuid4()}"
        result = {
            "__typename": f"{name}.{id}.GQLModel",
            "id": id
        }       
        for item in data:
            assert isinstance(item, dict)
            result = gatherDictTypes(name, item)
        return result

    assert isinstance(data, dict)
    assert "data" in data, "missing key data"
    responsedata = data["data"]
    gatherDictTypes(queryOrMutation, responsedata)
    return types

