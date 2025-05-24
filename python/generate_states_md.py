import os

# List of all 50 US states (lowercase, underscores for spaces)
all_states = [
    'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware',
    'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky',
    'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi',
    'missouri', 'montana', 'nebraska', 'nevada', 'new_hampshire', 'new_jersey', 'new_mexico',
    'new_york', 'north_carolina', 'north_dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania',
    'rhode_island', 'south_carolina', 'south_dakota', 'tennessee', 'texas', 'utah', 'vermont',
    'virginia', 'washington', 'west_virginia', 'wisconsin', 'wyoming'
]

# Exclude Idaho and Montana
states_to_create = [s for s in all_states if s not in ('idaho', 'montana')]

base_dir = os.path.join(os.path.dirname(__file__), '..', 'content', 'states')

for state in states_to_create:
    state_dir_name = state.replace('_', '-')  # Use hyphens for directory and slug
    state_dir = os.path.join(base_dir, state_dir_name)
    os.makedirs(state_dir, exist_ok=True)
    index_md = os.path.join(state_dir, '_index.md')
    if not os.path.exists(index_md):
        with open(index_md, 'w') as f:
            f.write(f"""---
title: "{state.replace('_', ' ').title()}"
layout: "States"
state: "{state_dir_name}"
---
""")
        print(f"Created {index_md}")
    else:
        print(f"{index_md} already exists, skipping.")