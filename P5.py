# Step 1: Define a class called car
# Step 2: Define a class attribute called 'wheels
# Step 3: In the constructor define 1: Make of car 2: Model of car
# Step 4: Print the maker and model

class car():
    wheels = 4
    def __init__(self, maker, model):
        print("1. Maker of the car :", maker)
        print("2. Model of the car :", model)

McQueen = car('Audi', 'R8')
print(McQueen.wheels)