# Try Catch 
num1 = 50
num2 = "23"
try: # try the below code/operation
    result = num1 / num2

except TypeError:
    print("Error invalid input type. Enter a integer")

else: # if try works this will be executed
    print("The result is :",result)

finally: # will execute no matter what
    print("Execution of the divide_numbers is complete")
