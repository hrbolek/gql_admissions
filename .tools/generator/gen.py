from src import gatherTypes, makeschema

import json
with open("z4.result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

types = gatherTypes(data)

# output = json.dumps(types, indent=4)
# print(output)

types = makeschema(data)

with open("z_.json", "w", encoding="utf-8") as f:
    json.dump(types, f, indent=4)

output = json.dumps(types, indent=4)
print(output)

