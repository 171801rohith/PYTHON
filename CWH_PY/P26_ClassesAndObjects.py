# Class and Object
# Constructor

class Details:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is {self.occupation}")

a = Details("rohith", "engineer")
a.info()

b = Details("srinivas", "dentist")
b.info()
