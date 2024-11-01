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


