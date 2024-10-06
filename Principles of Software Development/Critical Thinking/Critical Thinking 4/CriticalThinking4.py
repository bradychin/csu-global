import json
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Get current folder path (where script is located).
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Define json files.
personality_trait_file = 'personalityTraits.json'
important_steps = 'importantSteps.json'

# Open and read json files.
with open(personality_trait_file) as file1:
    personality_data = json.load(file1)

with open(important_steps) as file2:
    important_steps_data = json.load(file2)

# Display personality traits.
print(f'\nPersonality Traits:\n')
for i, item in enumerate(personality_data):
    trait = item['trait']
    print(f'Trait {i+1}: {trait}')
    description = ''.join(item['description'])
    print(f'Description: {description}\n')

# Display important steps of the program.
print(f'Important steps in the program:')
for i, step in enumerate(important_steps_data):
    print(f'Step {step['step']}: {step['description']}')
else: 
    print(f'\n')