import random

from parsy import string

class Report:
    def __init__(self, id_num, street_address, pothole_size, pothole_location):
        self.id_num = id_num
        self.street_address = street_address
        self.district = random.randint(1, 10)
        self.pothole_size = pothole_size
        self.pothole_location = pothole_location
        if pothole_size <= 3:
            self.priority = 'Low priority'
        elif 3 < pothole_size < 8:
            self.priority = 'Medium priority'
        else:
            self.priority = 'High priority'

class WorkOrder:
    def __init__(self, pothole_location, pothole_size, crew_id, num_of_crew_people, hours, status, filler_used):
        self.pothole_location = pothole_location
        self.pothole_size = pothole_size
        self.crew_id = crew_id
        self.num_of_crew_people = num_of_crew_people
        self.equipment = 'Patchers, filler, compactors, seals'
        self.hours = hours
        if status == 1:
            self.status = 'Work in progress.'
        elif status == 2:
            self.status = 'Repaired.'
        elif status == 3:
            self.status = 'Temporary repair.'
        elif status == 4:
            self.status = 'Not repaired.'
        self.filler_used = filler_used
        # Assuming $2 per square foot of filler used and $50 for equipment
        self.repair_cost = (hours*num_of_crew_people) + (filler_used*2) + 50

class DamageFile:
    def __init__(self, name, street_address, phone_number, type_of_damage, dollar_amount):
        self.name = name
        self.street_address = street_address
        self.phone_number = phone_number
        self.type_of_damage = type_of_damage
        self.dollar_amount = dollar_amount

def PHTRS():
    # Get pothole information from user for report
    print('\n##############################################')

    print('Welcome to the Pothole Tracking and Repair System.\n')
    pothole_street = input('Enter the street where pothole is located: ')
    pothole_size = enter_int('Enter the size of the pothole (1-10): ', 10)
    pothole_location = input('Enter the pothole location (middle, curb, etc): ')
    id_num = random.randint(1, 1000)

    report = Report(id_num, pothole_street, pothole_size, pothole_location)

    print(f'\nThank you. Here is the info you submitted:')
    print(f'  Case ID: {report.id_num}')
    print(f'  Address: {report.street_address}, District: {report.district}')
    print(f'  Pothole Size: {report.pothole_size}')
    print(f'  Pothole Location: {report.pothole_location}')
    print(f'  Repair Priority: {report.priority}')

    print('##############################################')

    # Work order data
    print('\n##############################################')

    print('FOR CREW ONLY')
    crew_id = enter_int('Enter your crew id: ', 1000)
    num_of_crew_people = enter_int('Enter the number of people in your crew: ', 100)
    hours = enter_int('Hours applied to repair: ', 100)
    status = enter_int('''What is the status of the repair (enter a number)?
    1. Work in progress.
    2. Repaired.
    3. Temporary repair.
    4. Not Repaired
    >>> ''',
        4)
    filler_used = enter_int('Enter filler material used in square feet: ', 1000)

    work_order = WorkOrder(report.pothole_location, report.pothole_size, crew_id, num_of_crew_people, hours, status, filler_used)

    print(f'\nWork Order Submitted')
    print(f'  Pothole details.\n    Size: {work_order.pothole_size}\n    Location: {work_order.pothole_location}')
    print(f'  Crew ID: {work_order.crew_id}')
    print(f'  Crew Size: {work_order.num_of_crew_people}')
    print(f'  Equipment: {work_order.equipment}')
    print(f'  Total hours: {work_order.hours}')
    print(f'  Current Status: {work_order.status}')
    print(f'  Filler used: {work_order.filler_used}')
    print(f'  Cost: ${work_order.repair_cost}')

    print('##############################################')

    # Damage file
    print('\n##############################################')

    print('Please fill out the information to submit a damage file.')
    name = input('Enter your name: ')
    address = input('Enter your address: ')
    phone_number = input('Enter your phone number: ')
    type_of_damage = input('Enter damage done to your vehicle: ')
    damage_cost = enter_int('Enter the estimated cost of the damage to your vehicle: ', 1000000)

    damage_file = DamageFile(name, address, phone_number, type_of_damage, damage_cost)

    print('\nDamage file submitted. Please allow for 3-5 business days to process your file.')
    print('##############################################')

def enter_int(string, max_int):
    while True:
        try:
            int_input = int(input(f'{string}'))
            if int_input <= 0:
                print(f'Enter a number above 0')
            elif int_input > max_int:
                print(f'Enter a number less than {max_int}')
            else:
                break
        except ValueError:
            print('Please enter a number')
    return int_input

if __name__ == '__main__':
    PHTRS()



















