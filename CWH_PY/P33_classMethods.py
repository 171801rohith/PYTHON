# class Methods


class Employee:
    company = "Hell"

    def show(self):
        return f"EmployeeName = {self.name}\nCompany = {self.company}"

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Rohith"
print(e1.show())
e2 = Employee()
e2.name = "Shek"
print(e2.show())
print()
e1.changeCompany("APPIL")
e1 = Employee()
e1.name = "Rohith"
print(e1.show())
e2 = Employee()
e2.name = "Shek"
print(e2.show())


# Class methods as Alternate constructors
print()
print("# Class methods as Alternate constructors")


class Dog:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    @classmethod
    def fromStr(cls, str):
        return cls(str.split("-")[0], str.split("-")[1])


d1 = Dog("Boow", "pedi")
print(d1.name)
print(d1.food)

str = "Harry-Meat"
d2 = Dog(str.split("-")[0], str.split("-")[1])
print(d2.name)
print(d2.food)

str = "Shek-camel"
d3 = Dog.fromStr(str)
print(d3.name)
print(d3.food)


