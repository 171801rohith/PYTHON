# Step 1: Create a method
# Step 2: Declare 2 variable
# Step 3: Create Try Catch
# Step 4: Inside try to divide num1/num2
# Step 5: Create except, else and finally
# Step 6: handle ZeroDivisionError, TypeError
# Step 7: Test cases (10 ,2), (10,0), (10, 'a')


def TryCatch(num1, num2):
    try:
        result = num1 / num2

    except TypeError:
        print("Error invalid input type. Enter a integer")

    except ZeroDivisionError:
        print("Error invalid denominator. Can't divide by zero")

    else:
        print("The result is :", result)

    finally:
        print("Execution of the divide_numbers is complete")


num1 = 10
# num2 = 'a'
# num2 = 0
num2 = 2
TryCatch(num1, num2)
