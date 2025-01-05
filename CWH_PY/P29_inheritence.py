# Inheritence


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name: {self.name}\tID: {self.id}")


class Programmer(Employee):
    def __init__(self, name, id, language="Python"):
        super().__init__(name, id)
        self.language = language

    def showLanguage(self):
        print(f"Language is {self.language}")


e = Employee("Leo Das", 420)
e.showDetails()

p = Programmer("Anthony Das", 420, "JAVA")
p.showDetails()
p.showLanguage()

p1 = Programmer("Das", 420)
p1.showDetails()
p1.showLanguage()


# Access Specifiers
# There is no private , public, or protected in python Directly. But used indirectly
class MyClass:
    def __init__(self):
        self.__privateVar = "Hello" # '__' it behaves like a private variable


c = MyClass()
# print(c.__privateVar) # Can't access

# Name Mangling
print(c._MyClass__privateVar) # Accessing in using name mangling

print(c.__dir__()) # List of properties which are accessible
