# Looping Statements
# In Python by default all variables are set to 0 or '\0' 


# For Loops
# in Strings
name = "Kritharth"
for i in name:
    print(i, end = ', ')
    
# in Lists
colors = ['red', 'blue', 'green']
for color in colors:
    print('Color :',color) 
    for i in color:
        print(i, end=' ')
    print()

# in Range
for i in range(8):
    print(i) # 0 to 7
for i in range(1, 8):
    print(i) # 1 to 7
        #range(start, stop, step)
for i in range(0, 20, 2): 
    print(i) # 0 to 19 but here i increments by step value = 2

n = int(input('=>'))
for i in range(1, 11):
    print(n, 'x', i, '=', i * n)


# While Loops
i = 0
while(i < 7):
    print(i)
    i += 1
    
# We can use else along side while
count = 5
while(count > 0):
    print(count) 
    count -= 1
else:
    print("I'm inside else")

while(i <= 38):
    i = int(input('=>'))
    
# Do-While Emulation in Python 
# Emulating becoz there is no do-while in Python
while True:
    i = int(input('=>'))
    if(i <= 38):
        break
    print("Try again")
    

# Continue and Break Statements
for i in range(12):
    if(i == 10):
        print("Loop as been broken")
        break
    print("5 x", i, '=', 5 * i)
    
for i in range(12):
    if(i == 5):
        print("Iteration as been skipped")
        continue
    print("5 x", i, '=', 5 * i)
    