import pystache
import re

def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def gen_gql_file(typedef, templateFileName):
    # Preprocess the typedef to match the Mustache template structure
    processed_fields = []
    for name, fielddef in typedef["fields"].items():
        field = {
            "name": camel_to_snake(name),
            "type": fielddef["type"],
            "is_basic": fielddef["type"]["kind"] == "SCALAR",
            "is_object": fielddef["type"]["kind"] == "OBJECT",
            "is_list": fielddef["type"]["kind"] == "LIST"
        }
        processed_fields.append(field)

    # Organize data for Mustache template rendering
    template_data = {
        "typedef": typedef,
        "fields": processed_fields
    }

    # Load the template
    with open(templateFileName, "r") as template_file:
        template = template_file.read()

    # Render the template with pystache
    renderer = pystache.Renderer()
    result = renderer.render(template, template_data)

    return result


import pystache
import typing

def convert_type_with_template(type_def, templateFileName):
    """
    Generate Python class code from an introspection type definition using a Mustache template.

    Parameters:
    - type_def (dict): The introspection type definition.

    Returns:
    - str: The generated Python code for the class.
    """
    # Prepare the data structure for the template
    fields = []
    for field in type_def["fields"]:
        field_data = {
            "name": field["name"],
            "is_basic": field["type"]["kind"] == "SCALAR" or field["type"].get("name") == "Null",
            "is_object": field["type"]["kind"] == "OBJECT",
            "is_list": field["type"]["kind"] == "LIST",
        }
        
        # Set type names based on the field kind
        if field_data["is_basic"]:
            field_data["type_name"] = map_scalar_to_python(field["type"].get("name"))
        elif field_data["is_object"]:
            field_data["type_name"] = field["type"]["name"]
        elif field_data["is_list"]:
            element_type = field["type"]["ofType"]["name"]
            field_data["element_type"] = element_type
        
        fields.append(field_data)

    # Define the data structure for the template
    template_data = {
        "name": type_def["name"],
        "fields": fields
    }

    # Load and render the template
    with open(templateFileName, "r") as template_file:
        template = template_file.read()
    
    renderer = pystache.Renderer()
    return renderer.render(template, template_data)


def map_scalar_to_python(scalar_name):
    """
    Map GraphQL scalar types to Python types.

    Parameters:
    - scalar_name (str): The name of the GraphQL scalar type.

    Returns:
    - str: The corresponding Python type.
    """
    scalar_map = {
        "String": "str",
        "Int": "int",
        "Float": "float",
        "Boolean": "bool",
        "ID": "str",
        "Null": "None"
    }
    return scalar_map.get(scalar_name, "typing.Any")


# Example usage with the provided type definition
introspection_type = {
    "name": "UserGQLModel",
    "fields": [
        {
            "name": "id",
            "type": {
                "kind": "SCALAR",
                "name": "String"
            }
        },
        {
            "name": "firstname",
            "type": {
                "kind": "SCALAR",
                "name": "Null"
            }
        },
        {
            "name": "type",
            "type": {
                "kind": "OBJECT",
                "name": "UserTypeGQLModel"
            }
        },
        {
            "name": "memberships",
            "type": {
                "kind": "LIST",
                "ofType": {
                    "kind": "OBJECT",
                    "name": "MembershipGQLModel"
                }
            }
        }
    ]
}

# Generate the class code
output = convert_type_with_template(introspection_type)
print(output)
