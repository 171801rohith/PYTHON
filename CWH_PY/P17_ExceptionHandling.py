# Error or Exception Handling
# Try catch

a = input("Enter a number :")
print(f"Multiplication table of {a} :")
try:
    for i in range(1, 11):
        print(f"{a} x {i} =", int(a) * i)
except Exception as e:
    print("Sorry, something went wrong 404 error")
    print(e)


print("Some important Lines of Code")
print("End of Code")

try:
    print(4 / 0)
except Exception as e:
    print("Error Occurred:", e)

try:
    print(4 / 0)
except Exception:
    print("Error Occurred:")

# Some Errors
# Value error
# Divide by zero error
# Index error

# Finally Clause

def fun1():
    try:
        l = [2,45,6]
        i = int(input("a num :"))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    print("I'm not executed finally")

def fun2():
    try:
        l = [2,45,6]
        i = int(input("a num :"))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("I'm executed finally")

print(fun1())
print(fun2())

# Custom error

a = 3 # A num btwn 5 - 9
# a = 6 # A num btwn 5 - 9
if a < 5 or a > 9:
    raise ValueError("Enter a num between 5 and 9")
else:
    print(a)