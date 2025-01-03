# Getter and Setter


class myClass:
    # Getter method
    @property
    def getVal(self):
        return self.val
    
    # Setter method
    @getVal.setter
    def setVal(self, val):
        self.val = val

obj = myClass()
obj.setVal = 80
# print("value is ", obj.getVal()) # without using @property decrator
print("value is ", obj.getVal)  # with using @property decrator


class Employee:
    name = None
    salary = None
    role = None

    @property
    def getDetails(self):
        return f"NAME = {self.name} SALARY = {self.salary} ROLE = {self.role}"

    @getDetails.setter
    def setDetails(self, details):
        self.name, self.salary, self.role = details
    

emp = Employee()
emp.setDetails = ("Shek", 3000, "HR")
print(emp.getDetails)

# OR
print("\nNORMAL\n")

class Employees:
    name = None
    salary = None
    role = None

    # Getter
    def getDetails(self):
        return f"NAME = {self.name} SALARY = {self.salary} ROLE = {self.role}"

    # Setter
    def setDetails(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    

emp = Employees()
emp.setDetails("Shek", 3000, "HR")
print(emp.getDetails())
    