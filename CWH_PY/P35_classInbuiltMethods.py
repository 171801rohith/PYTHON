# dir, __dict__ and help method

# dir gives the list of all methods and all attributes that can be used
x = [9, 3, 4]
print(dir(x))

print("_" * 171)
x = (9, 3, 4)
print(dir(x))


# __dict__ gives the dictionary of all attributes and methods of an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gender = "Male"
        self.job = False

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


p = Person("John Doe", 30)
print("_" * 171)
print(dir(p))
print("_" * 171)
print(p.__dict__)
print("_" * 171)
print(p.__sizeof__())

# help method gives the documentation of a function or class
print("_" * 171)
print(help(Person))
print("_" * 171)
print(help(print))
