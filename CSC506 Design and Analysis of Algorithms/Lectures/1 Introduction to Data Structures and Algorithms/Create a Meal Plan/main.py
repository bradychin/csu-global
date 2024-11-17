import sys, operator, random
from operator import attrgetter

from nutrition import Food, MealPlan

# Constants to be used by the greedy algorithm.
NUTRIENT_THRESHOLD = 0.001
FRACTION_THRESHOLD = 0.05
CALORIE_THRESHOLD = 0.1
MAX_CALORIES = 2000


def load_nutrient_data(filename):
    # Open file, read food items one line at a time,
    # create Food objects and append them to a list.
    # Return the list once the entire file is processed.
    food_list = []
    with open(filename, 'r') as file:
        for line in file:
            # Split the line at the first colon
            name_part, nutrients_part = line.split(":")
            # Strip quotes and whitespace from the food name
            name = name_part.strip().strip('"')
            # Split nutrient values and convert them to float
            protein, carbs, fat, calories = map(float, nutrients_part.split(","))
            # Create a Food object and add it to the list
            food_item = Food(name, protein, carbs, fat, calories)
            food_list.append(food_item)
    return food_list


def sort_food_list(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    nutrient_calories_attr = f'{nutrient}_calories'
    foods.sort(key=attrgetter(nutrient_calories_attr),reverse=True)

def create_meal_plan(foods, nutrient, goal):
    # A greedy algorithm to create a meal plan that has MAX_CALORIES
    # calories and the goal amount of the nutrient (e.g. 30% protein)
    plan = MealPlan()

    # Sort the food list based on the selected nutrient in descending order
    sort_food_list(foods, nutrient)

    # Convert the goal percentage to a fraction
    goal_fraction = goal / 100.0

    # Remaining calories to be filled in the meal plan
    remaining_calories = MAX_CALORIES

    # Iterate through the sorted food list
    for food in foods:
        # Ensure the food item has enough calories (>= 0.1)
        if food.calories < CALORIE_THRESHOLD:
            continue

        # Ensure the selected nutrient percentage is at least 0.1% in the food
        if getattr(food, f"{nutrient}_calories") / food.calories < NUTRIENT_THRESHOLD:
            continue

        # Check if the food can be added without exceeding the calorie limit
        if remaining_calories - food.calories >= 0:
            # Add the entire food item
            plan.add_food(food)
            remaining_calories -= food.calories
        else:
            # Calculate the fraction of the food that fits within the remaining calories
            fraction = plan.fraction_to_fit_calorie_limit(food, remaining_calories)
            if fraction >= FRACTION_THRESHOLD:
                food.set_fraction(fraction)
                plan.add_food(food)
                remaining_calories -= food.calories

        # Check if the current plan meets the calorie and nutrient goals
        if plan.meets_calorie_limit(MAX_CALORIES, 0.1) and plan.meets_nutrient_goal(nutrient, goal_fraction, 0.001):
            break

    return plan


def print_menu():
    print()
    print("\t1 - Set maximum protein")
    print("\t2 - Set maximum carbs")
    print("\t3 - Set maximum fat")
    print("\t4 - Exit program")
    print()


if __name__ == "__main__":
    # 1. Load the food data from the file (change this to a user
    # prompt for the filename)
    filename = input('Enter name of food data file: ')
    foods = load_nutrient_data(filename)

    # 2. Display menu and get user's choice. Repeat menu until a
    # valid choice is entered by the user (1-4, inclusive).
    while True:
        try:
            print_menu()
            choice = int(input('Enter choice (1-4): '))
            if choice > 4 or choice < 1:
                raise ValueError
            elif choice == 1:
                nutrient = 'protein'
                break
            elif choice == 2:
                nutrient = 'carbs'
                break
            elif choice == 3:
                nutrient = 'fat'
                break
            elif choice == 4:
                break
        except ValueError:
            print('Invalid choice! Enter an integer from 1-4!')

    # 3. Prompt user for goal nutrient percent value. Repeat prompt
    # until a valid choice is entered by the user (0-100, inclusive)
    while True:
        try:
            goal = int(input('What percentage of calories from protein is the goal? What percentage of calories from protein is the goal?'))
            if goal > 100 or goal < 0:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid choice! Enter an integer from 0-100!')

    # 4. Run greedy algorithm to create the meal plan.
    plan = create_meal_plan(foods, nutrient, goal)

    # 5. Display plan.
    print(plan)