# Decorator 

def greet(func):
    def mFunc():
        print("Good morning!")
        func()
    return mFunc

@greet
def hello():
    print("Hello, World!")

hello()

# Passing Arguments

def great(func):
    def mfunc(*args, **kwargs):
        func(*args, **kwargs)
        print("Have an Excellent day!")
    return mfunc

@great
def add(a, b, c):
    print(a+b+c)

add(1, 2, 3)

@great 
def multi(a, b):
    print(a*b)

multi(4,5)

