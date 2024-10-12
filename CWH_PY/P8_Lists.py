# LISTS
lst = [1, 4, 24, 52, 1, 5, 'Bro', True]
#      0  1  2   3   4  5   6     7
#     -8 -7 -6  -5  -4 -3  -2    -1

# lst[-3] == lst[len(lst)-3] == lst[8-3]  #negative indexing

print(lst[2])

if 4 in lst:  # Checks whether 7 is in list
    print('T')
else:
    print('F')
    
print(lst[1:4])
print(lst[1:-1])
print(lst[1:6:2]) # jump by 2 

lst1 = [i*i for i in range(10)]
print(lst1)
lst1 = [i*i for i in range(10) if i%2 == 0]
print(lst1)
