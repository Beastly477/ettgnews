import os
import yaml

# Path to the YAML file
yaml_file = "./data/states/montana.yaml"

# Path to the output directory for Markdown files
output_dir = "./content/states/montana/counties"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load the YAML data
with open(yaml_file, "r") as file:
    data = yaml.safe_load(file)

# Iterate over the counties and create Markdown files
for county in data.get("counties", []):
    slug = county["slug"]
    name = county["name"]

    # Create the Markdown content
    markdown_content = f"""---
title: "{name}"
county: "{slug}"
type: "county"
---
"""

    # Write the Markdown file
    output_path = os.path.join(output_dir, f"{slug}.md")
    with open(output_path, "w") as md_file:
        md_file.write(markdown_content)

    print(f"Created: {output_path}")