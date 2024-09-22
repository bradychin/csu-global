import os
os.system('cls' if os.name == 'nt' else 'clear')

class Chin:
    def __init__(self):
        self.phases = []
        self.feedback_loops = []

    # ask user for key elements of the diagram
    def user_input(self):
        number_of_phases = enter_number('\nHow many phases will this waterfall diagram consist of?')
        number_of_feedback_loops = enter_number('How many feedback loops will there be?')

        for i in range(number_of_phases):
            phase_name = str(input(f'\nWhat is the name of phase {i+1}? '))
            number_of_tasks = enter_number(f'How many tasks are in the {phase_name} phase?')
            tasks = []
            for j in range(number_of_tasks):
                task_name = str(input(f'Enter task {j+1}: '))
                tasks.append(task_name)
            self.phases.append({"phase_name": phase_name, "tasks": tasks})

        print(f'\n')
        for i in range(number_of_feedback_loops):
            feedback_loop_name = str(input(f'Enter the name of feedback loop {i+1}: '))
            self.feedback_loops.append(feedback_loop_name)

    # display diagram
    def display_diagram(self):
        self.user_input()
        print(f'\n########################################')
        print(f'Your Waterfall diagram')
        for i, name in enumerate(self.phases, 1):
            display_phase_name = name['phase_name']
            print(f'  Phase {i}: {display_phase_name}')
            for j, task_name in enumerate(name['tasks'], 1):
                print(f'    Tasks {j}: {task_name}')
        print(f'\n')
        print(f'Feedback Loops')
        for j, loop in enumerate(self.feedback_loops):
            print(f'  Feedback loop {j+1}: {loop}')
        print(f'\n########################################\n')

def enter_number(prompt):
    while True:
        try:
            user_number_input = int(input(f'{prompt}: '))
            if user_number_input < 0:
                print('Number cannot be negative!')
            else:
                break
        except ValueError:
            print('Please enter a number.\n')
    return user_number_input

if __name__ == "__main__":
    model = Chin()
    model.display_diagram()