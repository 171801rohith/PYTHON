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
    def __init__(self, name, emp_id, address: Address, basic_salary, role, hra):
        self.name = name
        self.emp_id = emp_id
        self.address = address
        self.hra = hra
        self.basic_salary = basic_salary
        self.role = role


class EmployeeReport:
    def __init__(self, emp:Employee, report_date):
        self.report_date = report_date
        self.emp = emp


class RoleBuilder:
    def __init__(self):
        pass


class SalaryCalculator:
    def __init__(self):
        pass


def store_data(employee: Employee):
    employee.name = input("Enter your name : ")
    employee.emp_id = input("Enter your emp_id : ")
    employee.basic_salary = input("Enter your salary : ")
    employee.hra = input("Enter your HRA : ")
    employee.role = input("Enter your role : ")
    employee.address.street = input("Enter your street : ")
    employee.address.city = input("Enter your city : ")
    employee.address.zip_code = input("Enter your zipcode :")


def show_data(empy: Employee):
    print("Employee Name      :", empy.name)
    print("Employee Emp_id    :", empy.emp_id)
    print("Employee Role      :", empy.role)
    print("Employee Salary    :", empy.basic_salary)
    print("Employee HRA       :", empy.hra)
    print("Employee Address   :", empy.address.street)
    print("Employee City      :", empy.address.city)
    print("Employee Zip_code  :", empy.address.zip_code)


add = Address("", "", "")

emp = [Employee("", "", add, "", "", "")] * 4

for i in range(4):
    store_data(emp[i])

for i in range(4):
    pass

for i in range(4):
    print(f"------------Employee Details{i+1}------------")
    show_data(emp[i])
