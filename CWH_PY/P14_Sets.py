# Sets
# Don't consider repeated values. Unique set of values
# These are unorderd
# They are immutable
# Don't contain duplicate values
# Same as set in Mathematics
s = {2, 3, 4, 2, 5, 3}
s.add(9)
s.remove(4)
s.pop() # random val pop
s.discard(4)
del s # to delete set from memory
print(s)

info = {"cola", "coca", 3.9, 5}
print(info)

# harry = {}
# to create empty set
harry = set()
print(type(harry))

for val in info:
    print(val)

# Set Methods

s1 = {1, 3, 7, 11}
s2 = {17, 23, 11, 88}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
s1.update(s2) # update will not return anything. Makes changes in s1 itself
print(s1)

