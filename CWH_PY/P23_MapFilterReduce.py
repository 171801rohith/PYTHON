# Map
# Filter
# Reduce
from functools import reduce

cube = lambda x: x * x * x
sqr = lambda x: x * x 

l = [1, 2, 3, 4, 5, 6, 7]
nl = []
# for i in l:
#     nl.append(cube(i))

# MAP
# map(cube, l) returns a object
nl =list(map(cube, l))
print(nl)
nl =list(map(sqr, l))
print(nl)

# FILTER
# filter(filter_func, l) returns a object
filter_func = lambda x: x > 4
nl = list(filter(filter_func, l))
print(nl)

# REDUCE
sum = reduce(lambda x, y: x - y, l)
print(sum)
