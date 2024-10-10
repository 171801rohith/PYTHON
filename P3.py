numbers = [1,2,3,4,5]

# num = []
# print("Enter list elemnts :")
# for i in range(1,5):
#     num.append(int(input()))
# print(num)

# 1
numbers.append(6)
numbers.append(7)
numbers.pop(3)
# print(numbers)

# 2
# print("SUM of List :",sum(numbers))
# print("MIN of List :",min(numbers))
# print("MAX of List :",max(numbers))

# 3
names = ["Shek","Kithath","Sarthick","Chomith","Ass"]
age = [17,19,18,20,70]
stud_details ={}
for i in range(0,len(names)):
    stud_details[names[i]] = age[i] 
#   dict_details[key] = value  # syntax
print(stud_details)