import json

personality_trait_file = 'Principles of Software Development/Critical Thinking/Critical Thinking 4/personalityTraits.json'
important_steps = 'Principles of Software Development/Critical Thinking/Critical Thinking 4/importantSteps.json'

with open(personality_trait_file) as file1:
    personality_data = json.load(file1)

with open(important_steps) as file2:
    important_steps_data = json.load(file2)

print(f'\nPersonality Traits:\n')
for i, item in enumerate(personality_data):
    print(f'Trait {i+1}: {item['trait']}')
    print(f'Description: {item['description']}\n')

print(f'Important steps in the program:')
for i, step in enumerate(important_steps_data):
    print(f'Step {step['step']}: {step['description']}')
else: 
    print(f'\n')