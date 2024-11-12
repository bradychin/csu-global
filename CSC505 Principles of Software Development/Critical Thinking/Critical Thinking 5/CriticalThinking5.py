def intro():
    print('''\nThis script will do the following:
    1. Display intro.
    2. Display use cases.
    3. Display uml info.
    ''')

def use_cases():
    # Define actor and use cases
    actor_info = [
        {'actor_name': 'Department of Public Works (DoPW)', 'use_case': 'Develop a web-based pothole tracking and repair system (PHTRS). Continues to maintain system\'s performance and security.'},
        {'actor_name': 'Public Works Staff', 'use_case': 'Manages pothole information. Assigns repair crew. Tracks repairs and updates system.'},
        {'actor_name': 'Citizens', 'use_case': 'Logs onto website, reports pothole information such as location and severity.'},
        {'actor_name': 'Repair Crew', 'use_case': 'Repair holes. Logs work hours and updates status of potholes.'}
    ]

    print('Use Cases:')
    # Print actor and use cases
    for item in actor_info:
        name = item['actor_name']
        use_case = item['use_case']
        print(f'    Actor: {name}')
        print(f'    Use Case: {use_case}\n')

def uml_description():
    print('UML Description:')
    print('''    The UML use case diagram illustrates the interactions between the Pothole Tracking and Repair System (PHTRS) \b
    and the four main actors: Department of Public Works (DoPW), the Public Works Staff, the Citizens, and the Repair Crew. \b
    The diagram highlights use cases for each actor showing a clear and organized structure that represents the overall workflow \b
    of the system, from pothole reporting to repair completion.
    ''')

if __name__ == "__main__":
    intro()
    use_cases()
    uml_description()