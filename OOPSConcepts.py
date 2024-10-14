class Dog:  # Brackets are optional
    # One parameter is compalsory so we use 'self' everytime when we define a Method. Don't ever miss 'self'
    def __init__(self, name):
        # self ='this' in java
        print('Hey bro aadithya is the "GreatAssGaint"', name)
        self.dog_name = name

    def bark(self):
        print(self.dog_name, "says, Wooff!!")
    
    def walk(self, location = 'park'):
        print(self.dog_name,"is walking towards",location)


#  Funciton when defined inside a class then they are called 'Methods'

dog1 = Dog("John")  # Objects/Instances of class Dog
dog1.bark()
dog1.walk("a car wheel")
dog1.walk()
