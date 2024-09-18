import os
os.system('cls' if os.name == 'nt' else 'clear')

class Chin:
    def __init__(self):
        self.phase = []

    # ask user for key elements of the diagram
    def user_input(self):
        phases = int(input(f'\nHow many phases will this waterfall diagram consist of? '))

        for i in range(phases):
            phase_name = str(input(f'\nWhat is the name of phase {i+1}? '))
            number_of_tasks = int(input(f'How many tasks are in the {phase_name} phase? '))
            tasks = []
            for j in range(number_of_tasks):
                task_name = str(input(f'Enter task {j+1}: '))
                tasks.append(task_name)
            self.phase.append({"phase_name": phase_name, "tasks": tasks})

    # display diagram
    def display_diagram(self):
        self.user_input()
        print(f'\n\nYour Waterfall diagram')
        for i, name in enumerate(self.phase, 1):
            print(f'\nPhase {i}: {name['phase_name']}')
            for j, task_name in enumerate(name['tasks'], 1):
                print(f'    Tasks {j}: {task_name}')
        print(f'\n')

if __name__ == "__main__":
    model = Chin()
    model.display_diagram()