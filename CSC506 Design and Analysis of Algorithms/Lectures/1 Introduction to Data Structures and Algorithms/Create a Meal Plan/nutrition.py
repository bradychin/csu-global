class Food:
    def __init__(self, name, protein, fat, carbs, calories):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.calories = calories
        self.set_fraction(1.0)

    def set_fraction(self, fraction):
        self.fraction = fraction
        self.protein_calories = 4 * fraction * self.protein
        self.carbs_calories = 4 * fraction * self.carbs
        self.fat_calories = 9 * fraction * self.fat
        self.calories = fraction * self.calories

    def __str__(self):
        return "[%0.4f] %s (P=%s,C=%s,F=%s,E=%s)" % (
        self.fraction, self.name, self.protein, self.carbs, self.fat, self.calories)


class MealPlan:
    def __init__(self):
        self.foods = []
        self.total_calories = 0.0
        self.total_protein_calories = 0.0
        self.total_carbs_calories = 0.0
        self.total_fat_calories = 0.0

    def add_food(self, food):
        self.foods.append(food)
        self.total_protein_calories += food.protein_calories
        self.total_carbs_calories += food.carbs_calories
        self.total_fat_calories += food.fat_calories
        self.total_calories += food.calories

    def percent_nutrient(self, nutrient):
        if self.total_calories > 0.0:
            return getattr(self, "total_%s_calories" % nutrient) / self.total_calories
        else:
            return 0.0

    def calories_with_food(self, food):
        return self.total_calories + food.calories

    def percent_nutrient_with_food(self, food, nutrient):
        if self.total_calories + food.calories > 0.0:
            return (getattr(self, "total_%s_calories" % nutrient) + getattr(food, "%s_calories" % nutrient)) / (
                        self.total_calories + food.calories)
        else:
            return 0.0

    def fraction_to_fit_calories_limit(self, food, calorie_limit):
        # Returns the fraction (0.0-1.0) of the food required to get the calorie limit.
        remaining_calories = calorie_limit - self.total_calories
        if remaining_calories <= 0:
            return 0.0
        fraction = remaining_calories/food.calories
        return max(0.0, min(fraction,  1.0))

    def fraction_to_fit_nutrient_goal(self, food, nutrient, goal):
        # Returns the fraction (0.0-1.0) of the food required to get the nutrient goal.
        if getattr(food, f"{nutrient}_calories") / food.calories < 0.001:
            return 0.0

            # Calculate the current nutrient content of the food
        current_nutrient_percent = getattr(self, f"total_{nutrient}_calories") / self.total_calories

        # Calculate the fraction needed to meet the nutrient goal
        required_fraction = goal / current_nutrient_percent

        # Ensure the fraction is between 0.05 and 1.0
        return max(0.05, min(required_fraction, 1.0))

    def meets_calorie_limit(self, calorie_limit, threshold):
        # Returns True if the total calories of the current meal plan
        # is within the specified threshold of the given calorie limit.
        lower_bound = calorie_limit - 0.1  # 2000.0 - 0.1 = 1999.9
        upper_bound = calorie_limit + 0.1  # 2000.0 + 0.1 = 2000.1

        # Ensure that all foods considered have at least 0.1 calorie
        valid_foods = [food for food in self.foods if food.calories >= 0.1]

        # Calculate the total calories from valid foods
        total_valid_calories = sum(food.calories for food in valid_foods)

        return lower_bound <= total_valid_calories <= upper_bound

    def meets_nutrient_goal(self, nutrient, goal, threshold):
        # Returns True if the total calorie contribution (by percent) of the
        # given nutrient ('protein', 'carbs' or 'fat') for the current
        # meal plan is within the specified threshold of the given goal.
        current_percent = self.percent_nutrient(nutrient)

        # Calculate the acceptable range for the nutrient composition
        lower_bound = goal * (1 - threshold)
        upper_bound = goal * (1 + threshold)

        # Check if the current percent falls within the range
        return lower_bound <= current_percent <= upper_bound

    def __str__(self):
        s = ""
        if len(self.foods) == 0: return "Empty Plan"
        item = 1
        for food in self.foods:
            s += "%d: %s\n" % (item, food)
            item += 1

        s += "Total Calories: %s\n" % self.total_calories
        s += "\tProtein: %s\n" % self.percent_nutrient("protein")
        s += "\tCarbs: %s\n" % self.percent_nutrient("carbs")
        s += "\tFat: %s" % self.percent_nutrient("fat")

        return s
