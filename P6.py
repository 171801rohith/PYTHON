# Step 1: Create 3 class Fruit, Mango, Apple
# Step 2: make Mango and Apple as Sub Classes
# Step 3: Define a method saying I am Fruit in the Fruit class
# Step 4: Access the method given in the Fruit class
# Step 5: Override the method both in Mango and Apple saying I am Mango and I am Apple respectively


class Fruit:
    def say(self):
        print("I am a Fruit")


class Mango(Fruit):
    def say(self):
        print("I am a Mango")


class Apple(Fruit):
    def say(self):
        print("I am a Apple")


fruit = Fruit()
fruit.say()

mango = Mango()
mango.say()

apple = Apple()
apple.say()
