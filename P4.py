# Step 1: Use the Class keyword and type the name of your class tht you are going to define. Please use a person's name.
# Step 2: Use the init constuctor to create teh initial behaviour of this person. This person needs 2 places of info 1) Name 2) age
# Step 3: Print the 2 peices of info


class Rohith:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Display(self):
        print("Name :", self.name)
        print("Age :", self.age)


name = input("Enter name : ")
age = input("Enter age : ")
roh = Rohith(name, age)
#                  Alternatives
# roh = Rohith(input("Enter name : "), input("Enter age : "))
# roh = Rohith("Aadithya", 90)
roh.Display()
