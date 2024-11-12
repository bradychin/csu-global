import json
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Ensure that json files are in the same folder as this python script
print('\nPlace " personalityTraits.json" and "importantSteps.json" in the same folder as this python script.')
while True:
        try: 
            verify = input(f'\nAre the files in the same folder? \nPress "1" if they are.\nPress "f" to end program.\n>>> ')
            if verify == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif verify == 'f':
                exit()
            else: 
                raise ValueError 
        except ValueError:
            print(f'Place in same directory.\n')

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
    important_step = step['step']
    important_step_description = step['description']
    print(f'Step {important_step}: {important_step_description}')
else: 
    print(f'\n')