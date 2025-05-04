import os
import yaml

# Path to the YAML file
yaml_file = "./data/states/montana.yaml"

# Path to the output directory for Markdown files
output_dir = "./data/states/montana/"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load the YAML data
with open(yaml_file, "r") as file:
    data = yaml.safe_load(file)

# Iterate over the counties and create Markdown files
for county in data.get("counties", []):
    slug = county["slug"]
    name = county["name"]

    # Prepare the YAML content for the county
    county_data = {
        "name": name,
        "slug": slug
    }

    # Write the YAML file
    output_path = os.path.join(output_dir, f"{slug}.yaml")
    with open(output_path, "w") as yaml_file:
        yaml.dump(county_data, yaml_file, default_flow_style=False)

    print(f"Created: {output_path}")