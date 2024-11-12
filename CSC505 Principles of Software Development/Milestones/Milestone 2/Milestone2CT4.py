personality_data = [
    {
        "trait": "Vision",
        "description": [
            "\nExcellent software developers have a vision of what they want achieve and ",
            "what they need to accomplish their objectives. They are goal-oriented and are ",
            "able to develop and innovate on new ideas and techniques that no one else has before."
        ]
    },
    {
        "trait": "Confidence",
        "description": [
            "\nExcellent software developers have a high level of confidence. They are able",
            "to make challenging decisions and are able to operate under stressful situations."
        ]
    },
    {
        "trait": "Knowledge",
        "description": [
            "\nExcellent software developers have complete knowledge in their field. There are many ",
            "different approaches to the same solution in software development and having full knowledge ",
            "of the development tools and technologies allow for the best outcome."
        ]
    }
]

important_steps_data = [
    {
        "step": 1,
        "description": "Import libraries."
    },
    {
        "step": 2,
        "description": "Set current working directory."
    },
    {
        "step": 3,
        "description": "Define json files."
    },
    {
        "step": 4,
        "description": "Open and read json files."
    },
    {
        "step": 5,
        "description": "Display personality traits."
    },
    {
        "step": 6,
        "description": "Display important steps of the program."
    }
]


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