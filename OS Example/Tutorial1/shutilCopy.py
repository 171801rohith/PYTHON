# is v/s '==
# both are comparison operators

a = [1, 23, 34]
b = [1, 23, 34]
print(a is b) # Compares the exact location of object in memory
print(a == b) # Compares the value
print()
a = 2
b = 2
print(a is b) 
print(a == b)
print()
a = (1, 2)
b = (1, 2)
print(a is b) 
print(a == b)
print()
a = None
b = None
print(a is b) 
print(a is None) 
print(a == b)
print(a == None)
print()
