# Lambda functions
# An anonymous function
# Used for online functions 

def square(x):
    return x * x

def app(func, x, y, z): # passing Function as argument
    return 6 + func(x, y, z)


print("Using method :", square(4))

sqr = lambda x: x * x
print("Using lambda sqr :", sqr(3))

cube = lambda y: y**3
print("Using lambda cube :", cube(2))

avg = lambda x, y, z: (x + y + z) / 3
print("Using lambda avg :", avg(2, 3, 6))

# print("Using App :", app(cube, 2 ))

print("Using App :", app((lambda x, y, z: (x + y + z) / 3), 2, 3, 6 ))
