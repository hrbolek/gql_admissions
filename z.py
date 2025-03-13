import uuid
def analyze_dict_attributes(d: dict):
    basic_attributes = {}
    dict_attributes = {}
    list_attributes = {}
    for key, value in d.items():
        if isinstance(value, dict):
            dict_attributes[key] = type(value)
        elif isinstance(value, list):
            list_attributes[key] = type(value)
        else:
            basic_attributes[key] = type(value)
    return {
        "basic": basic_attributes,
        "scalars": dict_attributes,
        "vectors": list_attributes
    }

def iterate_list(l: list, level=0):
    attributes = {}
    for item in l:
        assert isinstance(item, dict)
        stop_yielding = False
        for t, t_level in iterate_dict(l[0], level=level+1):
            if t_level == level + 1:
                attributes["__typename"] = t["__typename"]
                for key, value in t.items():
                    attributes[key] = value
                stop_yielding = True
            elif not stop_yielding:
                yield t, t_level
        
    yield attributes, level

def iterate_dict(d: dict, level=0):
    knowntypes = set()
    basic_attributes = {}
    dict_attributes = {}
    list_attributes = {}
    __typename = d.get("__typename", f"T_{uuid.uuid4()}")
    for key, value in d.items():
        if key == "__typename":
            # __typename = value
            continue
        if isinstance(value, dict):
            for t, t_level in iterate_dict(value, level=level+1):
                __typename = t["__typename"]
                if __typename not in knowntypes:
                    knowntypes.add(__typename)
                    yield t, t_level
                if t_level == level + 1:
                    dict_attributes[key] = f"Optional[{__typename}]"
        elif isinstance(value, list):
            for t, t_level in iterate_list(value, level=level+1):
                __typename = t["__typename"]
                if __typename not in knowntypes:
                    knowntypes.add(__typename)
                    yield t, t_level
                if t_level == level + 1 :
                    list_attributes[key] = f"List[{__typename}]"
        else:
            basic_attributes[key] = type(value)

    result = {
        "__typename": __typename, 
        **basic_attributes,
        **dict_attributes,
        **list_attributes
    }
    yield result, level

data = {
  "data": {
    "admissionById": {
      "__typename": "AdmissionGQLModel",
      "id": "995a0dd2-3697-4e40-ae68-5bc3d9fe8c81",
      "stateId": "cd8ec638-fcfc-4f86-a18f-9adc656fd4a3",
      "programId": "77bb4a23-1003-4dd4-af62-4511fc013e6d",
      "paymentInfoId": "2dd560b8-7c4c-41a5-aaeb-75f9f8e30409",
      "examStartDate": "2025-04-22T00:00:00",
      "applicationStartDate": "2024-11-01T00:00:00",
      "applicationLastDate": "2025-03-31T23:59:59",
      "conditionDate": "2025-06-13T23:59:59",
      "paymentDate": "2025-04-05T23:59:59",
      "conditionExtendedDate": "2025-09-30T23:59:59",
      "requestConditionExtendDate": None,
      "requestExtraConditionsDate": None,
      "requestExtraDateDate": "2025-06-13T23:59:59",
      "examLastDate": "2025-06-03T23:59:59",
      "studentEntryDate": None,
      "endDate": None,
      "program": {
        "__typename": "AcProgramGQLModel",
        "id": "77bb4a23-1003-4dd4-af62-4511fc013e6d"
      },
      "paymentInfo": {
        "__typename": "PaymentInfoGQLModel",
        "accountNumber": "19-26030881/0710",
        "specificSymbol": "299400",
        "constantSymbol": "558",
        "IBAN": "CZ52 0710 0000 1900 2603 0881",
        "SWIFT": "CNBACZPP",
        "amount": 400,
        "payments": [
          {
            "__typename": "PaymentGQLModel",
            "bankUniqueData": "",
            "variableSymbol": "",
            "studentId": "5d36bb38-b29d-44e8-893d-b5e5a3b2591f",
            "amount": 400
          }
        ]
      },
      "disciplines": [
        {
          "__typename": "AdDisciplineGQLModel",
          "id": "c64ec760-7361-4cd2-a879-f867d7a98af0",
          "name": "TSP",
          "minScore": 20,
          "maxScore": 60,
          "disciplineTypeId": "1fe08f56-1a45-4483-9090-0b5d586aed24",
          "type": {
            "__typename": "AdDisciplineTypeGQLModel",
            "id": "1fe08f56-1a45-4483-9090-0b5d586aed24",
            "name": "Písemný test studijních předpokladů",
            "description": "ověření matematických znalostí a dovedností, numerického myšlení a logického uvažování",
            "descriptionEn": ""
          },
          "results": [
            {
              "__typename": "AdDisciplineResultGQLModel",
              "id": "4c57223e-cb53-4e31-9744-27d3637fdade",
              "score": 20,
              "description": "",
              "examPlanedDate": None,
              "student": {
                "id": "15315904-811b-4248-ac96-f670104646d6"
              },
              "examiner": {
                "id": "ccb397ad-0de7-46e7-bff0-42452f11dd5e"
              }
            }
          ]
        },
        {
          "__typename": "AdDisciplineGQLModel",
          "id": "7c81f985-d015-456f-88db-a6f5c711493e",
          "name": "TAJ",
          "minScore": 20,
          "maxScore": 50,
          "disciplineTypeId": "9e081724-27a0-4adc-8cab-f01c592cb174",
          "type": {
            "__typename": "AdDisciplineTypeGQLModel",
            "id": "9e081724-27a0-4adc-8cab-f01c592cb174",
            "name": "Písemný test z anglického jazyka",
            "description": "ověření znalostí a jazykových schopností uchazeče v anglickém jazyce",
            "descriptionEn": ""
          },
          "results": [
            {
              "__typename": "AdDisciplineResultGQLModel",
              "id": "4b1dc28a-fbdb-4a9d-9fb0-187531b4ba19",
              "score": 20,
              "description": "",
              "examPlanedDate": None,
              "student": {
                "id": "15315904-811b-4248-ac96-f670104646d6"
              },
              "examiner": {
                "id": "ccb397ad-0de7-46e7-bff0-42452f11dd5e"
              }
            }
          ]
        },
        {
          "__typename": "AdDisciplineGQLModel",
          "id": "d8f7808b-7ce5-43c8-bfaa-664ba8493766",
          "name": "TIT",
          "minScore": 2,
          "maxScore": 30,
          "disciplineTypeId": "e11ccb73-af79-40e6-b1b6-8d40accd558b",
          "type": {
            "__typename": "AdDisciplineTypeGQLModel",
            "id": "e11ccb73-af79-40e6-b1b6-8d40accd558b",
            "name": "Písemný test znalostí z informačních technologií",
            "description": "ověření všeobecných znalostí z oblasti informačních technologií",
            "descriptionEn": ""
          },
          "results": [
            {
              "__typename": "AdDisciplineResultGQLModel",
              "id": "65a98754-a707-422c-96bf-3fa96a7eb9e7",
              "score": 2,
              "description": "",
              "examPlanedDate": None,
              "student": {
                "id": "15315904-811b-4248-ac96-f670104646d6"
              },
              "examiner": {
                "id": "ccb397ad-0de7-46e7-bff0-42452f11dd5e"
              }
            }
          ]
        },
        {
          "__typename": "AdDisciplineGQLModel",
          "id": "a24f3394-ba8a-4727-aae4-e9b356f7e648",
          "name": "Sedy lehy 1 minuta",
          "minScore": 5,
          "maxScore": 25,
          "disciplineTypeId": "a2b2a61e-a567-4183-b2bb-0b4b9aeba04e",
          "type": {
            "__typename": "AdDisciplineTypeGQLModel",
            "id": "a2b2a61e-a567-4183-b2bb-0b4b9aeba04e",
            "name": "Praktické ověření tělesné zdatnosti",
            "description": "fyzického ověření tělesné zdatnosti",
            "descriptionEn": ""
          },
          "results": [
            {
              "__typename": "AdDisciplineResultGQLModel",
              "id": "0d4ed048-0a3f-4ff7-94fe-e2bca6c663c3",
              "score": 5,
              "description": "",
              "examPlanedDate": None,
              "student": {
                "id": "15315904-811b-4248-ac96-f670104646d6"
              },
              "examiner": {
                "id": "ccb397ad-0de7-46e7-bff0-42452f11dd5e"
              }
            }
          ]
        },
        {
          "__typename": "AdDisciplineGQLModel",
          "id": "ecae0c20-6bed-4344-8941-44ab47dbbf33",
          "name": "Běh 12 minut",
          "minScore": 5,
          "maxScore": 25,
          "disciplineTypeId": "a2b2a61e-a567-4183-b2bb-0b4b9aeba04e",
          "type": {
            "__typename": "AdDisciplineTypeGQLModel",
            "id": "a2b2a61e-a567-4183-b2bb-0b4b9aeba04e",
            "name": "Praktické ověření tělesné zdatnosti",
            "description": "fyzického ověření tělesné zdatnosti",
            "descriptionEn": ""
          },
          "results": [
            {
              "__typename": "AdDisciplineResultGQLModel",
              "id": "31fa4314-c7bd-4cb0-ab14-0bc7066c2469",
              "score": 5,
              "description": "",
              "examPlanedDate": None,
              "student": {
                "id": "15315904-811b-4248-ac96-f670104646d6"
              },
              "examiner": {
                "id": "ccb397ad-0de7-46e7-bff0-42452f11dd5e"
              }
            }
          ]
        }
      ]
    }
  }
}



def iterateJson(data: dict):
    def runOnList(data: list):
        for item in data:
            assert isinstance(item, dict)
            yield from runOnDict(item)

    def runOnDict(data: dict):
        for key, value in data.items():
            yield key, value
            if isinstance(value, dict):
                yield from runOnDict(value)
            elif isinstance(value, list):
                yield from runOnList(value)
            else:
                yield key, value
    assert isinstance(data, dict)
    yield from runOnDict(data)

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

import re
def camel_to_snake(name):
    # Find all uppercase letters and replace them with an underscore followed by the lowercase version
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def genGQLfile(typedef):
    lines = [
        f'',
        f'@strawberry.federation.type(description="")',
        f'class {typedef["__typename"]}:',
        # f'    pass'
    ]
    fields = typedef["fields"]
    for name, fielddef in fields.items():
        name = camel_to_snake(name)
        typing = fielddef["typing"]
        __typename = (fielddef["type"]["__typename"])
        
        if typing != "":
            continue
        lines.extend([
            f'    {name}: typing.Optional[{__typename}] = strawberry.field(description="", default=None)',
        ])

    lines.append('')
    for name, fielddef in fields.items():
        name = camel_to_snake(name)
        typing = fielddef["typing"]
        if typing != "OBJECT":
            continue
        __typename = (fielddef["type"]["__typename"])
        lines.extend([
            f'    {__typename}_id: typing.Optional[IDType] = strawberry.field(description="", default=None)',
        ])

    for name, fielddef in fields.items():
        name = camel_to_snake(name)
        typing = fielddef["typing"]
        if typing != "OBJECT":
            continue
        __typename = (fielddef["type"]["__typename"])
        lines.extend([
            '',
            f'    @strawberry.field(description="")',
            f'    async def {name}(self, info: strawberry.types.Info) -> typing.Optional[{__typename}]:',
            f'        from .{__typename} import {__typename} as SCALAR',
            f'        result = await SCALAR.load(info=info, id=self.{__typename}_id)',
            f'        return result',
        ])

    for name, fielddef in fields.items():
        name = camel_to_snake(name)
        typing = fielddef["typing"]
        if typing != "LIST":
            continue
        __typename = (fielddef["type"]["__typename"])
        lines.extend([
            '',
            f'    @strawberry.field(description="")',
            f'    async def {name}(self, info: strawberry.types.Info) -> typing.List[{__typename}]:',
            f'        from .{__typename} import {__typename} as SCALAR',
            f'        loader = SCALAR.getloader(info=info)',
            f'        rows = await loader.filter_by({__typename}_id=self.id)',
            f'        results = (SCALAR.fromsqlalchemy(row) for row in rows)',
            f'        return results',
        ])
    return lines

def genDBfile(typedef):
    lines = [
        f'',
        f'class {typedef["__typename"]}:',
        # f'    pass'
    ]
    fields = typedef["fields"]
    for name, fielddef in fields.items():
        typing = fielddef["typing"]
        __typename = fielddef["type"]["__typename"]
        if typing != "":
            continue
        lines.extend([
            f'    {name}: typing.Optional[{__typename}] = strawberry.field(description="", default=None)',
        ])
    return lines


schema = gatherTypes(data)

for key, value in schema.items():
    print("*"*5, f"{value['__typename']}")
    # print(key, value)
    fields = value.get("fields", None)
    if fields is None:
        print(value)
        continue
    # print(fields)
    for x, v in fields.items():
        print(f"\t{x}: {v['typing']} {v['type']['__typename']}")

            
            
    
import json
with open("z2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

onlytypes = {}
schema = gatherTypes(data)

for key, value in schema.items():
    __typename = value['__typename']
    __typedef = onlytypes.get(__typename, None)
    if __typedef is None:
        __typedef = {}
        onlytypes[__typename] = __typedef

    fields = value.get("fields", None)
    if fields is None:
        continue
    # print(fields)
    for x, v in fields.items():
        fieldtype = v['type']['__typename'] 
        if v['typing'] != "":
            fieldtype = {"kind": v['typing'], "ofType": v['type']['__typename']}

        newfield = {"type": fieldtype}
        xdef = __typedef.get(x, None)
        if xdef is None:
            __typedef[x] = fieldtype

for key, value in onlytypes.items():
    print("*" * 5, key)
    for x, v in value.items():
        print(f"\t{x}: {v}")

output = json.dumps(onlytypes, indent=4)
print(output)

for key, value in schema.items():
    print('\n'.join(genGQLfile(value)))

