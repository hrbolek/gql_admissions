import json

def find_types(data, types_dict):
    if isinstance(data, dict):
        # Check if the dictionary has a __typename key
        typename = data.get("__typename")
        if typename:
            # Initialize the type structure in types_dict if not already present
            if typename not in types_dict:
                types_dict[typename] = {"name": typename, "fields": []}
            # Add fields to the typename structure if they don't already exist
            for key, value in data.items():
                if key != "__typename":  # Skip the __typename field itself
                    field_type = derive_type(value)
                    
                    # Check if the field already exists in the list of fields
                    if not any(field['name'] == key for field in types_dict[typename]["fields"]):
                        types_dict[typename]["fields"].append({
                            "name": key,
                            "type": field_type
                        })
        # Recursively search in all values of the dictionary
        for key, value in data.items():
            find_types(value, types_dict)
    elif isinstance(data, list):
        # Recursively search in all elements of the list
        for item in data:
            find_types(item, types_dict)

def derive_type(value):
    """Derive the type of a value."""
    if isinstance(value, dict):
        # Use __typename if available, otherwise mark as generic "Object"
        return {"kind": "OBJECT", "name": value.get("__typename", "Object")}
    elif isinstance(value, list):
        # Derive type of the first element in the list for homogeneity, default to "List[Any]"
        if value:
            return {"kind": "LIST", "ofType": derive_type(value[0])}
        else:
            return {"kind": "LIST", "ofType": {"kind": "SCALAR", "name": "Any"}}
    elif isinstance(value, str):
        return {"kind": "SCALAR", "name": "String"}
    elif isinstance(value, int):
        return {"kind": "SCALAR", "name": "Int"}
    elif isinstance(value, float):
        return {"kind": "SCALAR", "name": "Float"}
    elif isinstance(value, bool):
        return {"kind": "SCALAR", "name": "Boolean"}
    elif value is None:
        return {"kind": "SCALAR", "name": "Null"}
    else:
        return {"kind": "SCALAR", "name": "Unknown"}

def extract_types(json_data):
    types_dict = {}  # Dictionary to store unique types with their fields and types
    find_types(json_data, types_dict)
    # Convert the types_dict to a list as per GraphQL introspection format
    types_list = [{"name": name, "fields": fields["fields"]} for name, fields in types_dict.items()]

    introspection_output = {
        "data": {
            "__schema": {
                "types": types_list
            }
        }
    }    
    return introspection_output

makeschema = extract_types
# # Load the JSON file
# with open('/mnt/data/z2.json') as f:
#     json_data = json.load(f)

# # Extract types
# types_list = extract_types(json_data)

# # Convert the dictionary of types to JSON format
# introspection_output = {
#     "data": {
#         "__schema": {
#             "types": types_list
#         }
#     }
# }

# # Print the introspection-style JSON
# print(json.dumps(introspection_output, indent=2))