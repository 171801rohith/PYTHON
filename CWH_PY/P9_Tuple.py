# Tuples

# They are immutable
# Positive / Negative indexing is same everywhere
tup1 = (1, 3, 5, 76, 32, 543, 3, 334)
# tup1[0] = 12 # throws error We can't change a tuple
print(type(tup1), tup1)
if 32 in tup1:
    print(1)
else:
    print(0)

# Tuple Operations
tup2 = ("gern", "leba", "popop")
Stup = tup1 + tup2
print(Stup)
print(tup1.count(3))
print(tup1.index(3))


