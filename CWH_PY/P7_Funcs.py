#  User-Define-Functions in Python

def CalcMean(a, b):
    mean = (a * b)/(a + b)
    print(mean)

def CalcGreat(a, b):
    if(a > b):
        print(a,"is greater")
    else:
        print(b,"is greater")
        
def CalcSomething():
    pass
        
a = 4
b = 10
CalcMean(a, b)
CalcGreat(a, b)
c = 4
d = 19
CalcMean(a, d)
CalcGreat(c, d)


# Function Arguments and Return statements

# Default Arguments
def avg(a = 9, b = 8):
    print("Avg is", (a + b)/2)

avg()
avg(12, 30) # It will overwrite 9 and 8 
avg(a = 30) # It will overwrite only 9 we can also do vice-versa

# Required Arguments
def avg(a, b):
    print("Avg is", (a + b)/2)

# avg() # Error
# avg(a = 30) #Error
avg(12, 30) # We have to pass to arguments in Required Arguments 

# Variable Length Arguments
def avg(*nums):
    sum = 0
    # print(type(nums))
    for i in nums:
        sum += i
    print("avg is", sum / len(nums))
    
avg(4, 5, 5, 7, 9) # We can give any number of args

# Returning values
def avg(*nums):
    sum = 0
    # print(type(nums))
    for i in nums:
        sum += i
    return sum / len(nums)
    
a = avg(4, 5, 5, 7, 9) 
print("avg is", a)