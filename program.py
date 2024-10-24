# Lab 1:
# 1. File Creation:
#    o Create a file called as program.py
# 2. Code the Address class:
#    o Create a class Address with attributes such as street, city, and zip code.
# 3. Code the Employee class:
#    o Create a class Employee with attributes like name, emp_id, and address (which
# should be an instance of Address).
# 4. Implement store_data method:
#    o Write a function store_data(employee) to accept user input and store the employee
# and address information inside the Employee object passed as an argument.
# 5. Implement show_data method:
#    o Write a function show_data(employee) to display the employee and address
# information using the Employee object passed as an argument.

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

class Employee:
    def __init__(self, name, emp_id, address:Address):
        self.name = name
        self.emp_id = emp_id
        self.address = address
    
def store_data(employee):
    employee.name = input("Enter your name : ")
    employee.emp_id = input("Enter your emp_id : ")

def show_data(empy:Employee):
    print("------------Employee Details------------")
    print("Employee Name\t:\t",empy.name)
    print("Employee Emp_id\t:\t",empy.emp_id)
    print("Employee Address\t:\t",empy.address.street)
    print("Employee City\t:\t",empy.address.city)
    print("Employee Zip_code\t:\t",empy.address.zip_code)


add = Address(input("Enter your street : "), input("Enter your city : "),input("Enter your zip_code : "))
emp = Employee("", "", add)
store_data(emp)
show_data(emp)


