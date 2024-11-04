# Conditional statements
a = int(input("Enter your age : "))
if(a >= 45):
    print("You can drive and work")
elif(a >= 18 ):
    print("You can drive")
else:
    print("You can't drive")
    
# elif is simply if-else-if

# Short Hand If Else (Similar to Ternary Operator)
    # value_if_true if condition else value_if_false
a = 248
b = 234
print("A") if a > b else print("=") if a == b else print("B")

print(9) if a < b else ""
c = 9 if a < b else 0
print(c)