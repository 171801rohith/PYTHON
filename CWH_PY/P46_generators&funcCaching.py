# Generators

def myGenerator():
    for i in range(5):
        yield i

# print(next(myGenerator()))
gen = myGenerator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)

# Function Caching
import functools
import time

@functools.lru_cache(maxsize=None)
def func(n):
    time.sleep(5)
    return n * n

print(func(3))
print("done for 3")
print(func(15))
print("done for 15")
print(func(5))
print("done for 5")
print("Now vlaues are stores in cache so we get the output quickly") 
# To store (the result of a computation) so that it can be subsequently retrieved without repeating the computation is called memoize
print(func(3))
print("done for 3")
print(func(15))
print("done for 15")
print(func(5))
print("done for 5")