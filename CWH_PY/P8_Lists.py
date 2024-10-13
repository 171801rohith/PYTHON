#!/usr/bin/env python

# LISTS
lst = [1, 4, 24, 52, 1, 5, "Bro", True]
#      0  1  2   3   4  5   6     7
#     -8 -7 -6  -5  -4 -3  -2    -1

# lst[-3] == lst[len(lst)-3] == lst[8-3]  #negative indexing

print(lst[2])

if 4 in lst:  # Checks whether 7 is in list
    print("T")
else:
    print("F")

print(lst[1:4])
print(lst[1:-1])
print(lst[1:6:2])  # jump by 2

lst1 = [i * i for i in range(10)]
print(lst1)
lst1 = [i * i for i in range(10) if i % 2 == 0]
print(lst1)

# List Methods
l = [11,2,5,6,4,1]
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l.index(2))
print(l.count(2))
print(l)
m = l
# m[0] = 0 # l also changes
# print(l)
m = l.copy()
m[0] = 0 # l doesn't change
print(l)
l.insert(2,900)
print(l)
m = [100,900,300]
l.extend(m)
print(l)
print(m)
k = l + m
print(k)