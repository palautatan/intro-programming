# 1. FOOD CLASS
class food:
    def __init__(self, source, name):
        '''
        Create a new food including
            - Where the food is sourced from (restaurant, brand, or generic)
            - A name for the food
        '''
        self.source = source
        self.name = name


    def macros(self, protein, fat, carbs):
        '''
        Add macronutrient attributes to the food, all must be numeric values of grams
        '''

        # DATA CHECK
        # Make sure all the user input is numeric.
        entered_types = [type(x) in [float, int] for x in [protein, fat, carbs]]

        if all(entered_types):
            self.protein = protein
            self.fat = fat
            self.carbs = carbs
        else:
            print('No macronutrients saved for this food. Please enter integer or floats.')


    def calculateCalories(self):
        '''
        Calculate the calories given the macronutrient breakdown
        '''
        total_cals = 4*self.protein + 9*self.fat + 4*self.carbs
        self.total_cals = total_cals
        return(total_cals)


    def calculateServingGrams(self):
        total_grams = self.protein + self.fat + self.carbs
        self.total_grams = total_grams
        return(total_grams)


    def display(self):
        import numpy as np

        output = list()
        output.append(self.source)
        output.append(self.name)

        if type(self.total_cals) in [float, int]:
            output.append(self.total_cals)
        else:
            output.append(np.nan)

        if type(self.total_grams) in [float, int]:
            output.append(self.total_grams)
        else:
            output.append(np.nan)

        return(output)


# 2. DAILY LOG CLASS
class daily_log:
    def __init__(self, date):
        self.date = date
        self.time = []
        self.food = []
        self.num_servings = []

    def add(self, time, food, num_servings):
        self.time.append(time)
        self.food.append(food)
        self.num_servings.append(num_servings)

    def calorieCount(self):

        daily_cals = []
        for this_food in self.food:
            daily_cals.append(this_food.total_cals)

        self.total_calories = sum(daily_cals)

        return(self.total_calories)

    def display(self):
        import numpy as np

        output = list()
        output.append(self.date)

        if type(self.time)==list:
            output.append(self.time)
        else:
            output.append(np.nan)

        if type(self.food)==list:
            output.append(self.food)
        else:
            output.append(np.nan)

        if type(self.num_servings)==list:
            output.append(self.num_servings)
        else:
            output.append(np.nan)

        if type(self.total_calories) in [int, float]:
            output.append(self.total_calories)
        else:
            output.append(np.nan)

        return(output)
