# Inheritence


class Vehicle():  # Super-class

    def start_engine(self):
        print("Engine Started")
    
    def drive(self):
        print("Lets roll !!")

class Car(Vehicle):  # Sub-Class
    pass

class Truck(Vehicle):  # Sub-Class
    def __init__(self):
        print("I'm a truck")
    
    # We are overriding the method
    def start_engine(self):
          print("I'm a truck I roar when started")


my_car = Car()
my_car.start_engine()

my_truck = Truck()
my_truck.start_engine()
my_truck.drive()