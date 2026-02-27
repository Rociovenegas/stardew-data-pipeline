
import xml.etree.ElementTree as ET
from pathlib import Path


def generate_first_level_dict(node):
    # Generates a dictionary ONLY for the node's first level. 
    # Ignores elements that have children.

    fields_dict = {}

    for child in node:
        # If you have children, ignore
        if len(child) > 0:
            continue
        
        # If you have text, save it.
        if child.text and child.text.strip():
            field_name = child.tag.lower()
            field_path = child.tag
            fields_dict[field_name] = field_path

    return fields_dict


def find_node_by_path(save_path, element=None):

    tree = ET.parse(save_path)
    root = tree.getroot()
    if element is None:
        return root
    else:
        node = root.find(element)
        if node is None:
            print("No node found. Check the structure of your save file.")
            return None
        return node

def generate_from_save_file(node):
    # Read an XML file and generate the dictionary.    
    fields = generate_first_level_dict(node)
    return fields


def save_as_python_dict(fields, output_file="generated_fields_2.txt"):

    # Save as Python code that you can copy and paste.

    with open(output_file, "w") as f:
        f.write("FIELDS = {\n")
        for key, path in sorted(fields.items()):
            f.write(f'    "{key}": "{path}",\n')
        f.write("}\n")
    print(f"Saving in: {output_file}")


if __name__ == "__main__":
    # Usa TU save file
    user_home = Path.home()
    save_path = user_home / "StardewValleyDashboard" / "Saves" / "test_430986684" / "test_430986684_20260219_161921_193927"
    node = find_node_by_path(save_path, "player")
    
    if node is not None:
        fields = generate_from_save_file(node)
        
        if fields:
            print(f"Total campos encontrados: {len(fields)}\n")
            save_as_python_dict(fields)


