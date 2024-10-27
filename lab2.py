# Lab 2:
# 1. Update the Employee class:
#    o Extend the Employee class from Lab 1 by adding attributes for role, basic salary, and HRA.
# 2. Create an array of Employee objects:
#    o Create an list of 4 Employee objects and store the data using the store_data() method.
# 3. Create an EmployeeReport class:
#    o Create a class EmployeeReport to hold a report_date and implement a display_employees() method that takes the employee list as input.
# 4. Code the RoleBuilder and SalaryCalculator classes:
#    o RoleBuilder.get_role_description(role_id) should return a description based on
# role_id (1-4).
#    o SalaryCalculator.get_allowance(basic, percentage) computes allowance.
#    o SalaryCalculator.get_salary(basic, hra, allowance) computes the total salary.
# 5. Implement display_employees():
#    o Loop through the list of employees.
#    o Use a RoleBuilder class to fetch the role description.
#    o Use a SalaryCalculator class to calculate the allowances and salary for each employee.
#    o Display the employee data in the format:
# EMP_ID NAME ROLE BASIC ALLOW SALARY


class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code


class Employee:
    def __init__(self, name, emp_id, basic_salary, role, hra, address: Address):
        self.name = name
        self.emp_id = emp_id
        self.address = address
        self.hra = hra
        self.basic_salary = basic_salary
        self.role = role


class EmployeeReport:
    def __init__(self, date):
        self.report_date = date

    def display_employees(self, emp):
        show_data(emp)
        print("Employee ReportDate:", self.report_date)


class RoleBuilder:
    def __init__(self):
        pass


class SalaryCalculator:
    def __init__(self):
        pass


def store_data():
    name = input("Enter your name : ")
    emp_id = input("Enter your emp_id : ")
    basic_salary = input("Enter your salary : ")
    hra = input("Enter your HRA : ")
    role = input("Enter your role : ")
    address = Address(
        input("Enter your street : "),
        input("Enter your city : "),
        input("Enter your zipcode :"),
    )
    employee.append(Employee(name, emp_id, basic_salary, role, hra, address))


def addRepotDate():
    date = input("Enter in DD/MM/YYYY format : ")
    reportDate.append(EmployeeReport(date))


def show_data(empy: Employee):
    print("Employee Name      :", empy.name)
    print("Employee Emp_id    :", empy.emp_id)
    print("Employee Role      :", empy.role)
    print("Employee Salary    :", empy.basic_salary)
    print("Employee HRA       :", empy.hra)
    print("Employee Address   :", empy.address.street)
    print("Employee City      :", empy.address.city)
    print("Employee Zip_code  :", empy.address.zip_code)


employee = []
reportDate = []
numberOfEmployess = int(input("Enter number of Employess : "))

for i in range(numberOfEmployess):
    print(f"------------------Enter Employee {i + 1} Details---------------")
    store_data()
    addRepotDate()


for i in range(numberOfEmployess):
    print(f"------------------Employee {i + 1} Details---------------")
    reportDate[i].display_employees(employee[i])
