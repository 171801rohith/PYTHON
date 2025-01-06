# Instance  variables & Class variables

class MyEmployee:
    # Class variable
    companyName = "Apple"
    noOfEmployees = 0

    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
        MyEmployee.noOfEmployees += 1

    def show(self):
        print("-" * 30)
        return f"noOfEmployees = {self.noOfEmployees}\ncompanyName = {self.companyName}\nname = {self.name}\nsalary = {self.salary}"


emp1 = MyEmployee("Rohith", 89000)
emp1.companyName = "Apple INDIA"
emp1.noOfEmployees = 10
print(emp1.show())
emp2 = MyEmployee("Shek", 79000)
print(emp2.show())
emp3 = MyEmployee("Shek", 79000)
print(emp3.show())
