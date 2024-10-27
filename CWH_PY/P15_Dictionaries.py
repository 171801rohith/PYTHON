# Dictionaries

dic = {901: "C++", 17: "Java", 42: "Python", "JavaScript": 5}
# {key : values}
print(type(dic))
print(dic)
print(dic[901])  # Two ways of accessing dictionaries
print(dic.get(901))
# 91 doesn't exsist
# print(dic[91])  # will trhow error
print(dic.get(91))  # will print 'None'
print(dic["JavaScript"])

print(dic.values())
# for i in dic.keys():
#     print(dic[i], end=", ")
print(dic.values())
for key in dic.keys():
    print(f"The value of {key} is {dic[key]}")

print(dic.items())

for key, value in dic.items():
    print(f"The value of {key} is {value}")

# Dictionaries Methods
dic1 = {901: "C++", 17: "Java", 42: "Python"}
dic2 = {421: 921, 9: 42321}
# dic1.update(dic2)
# # dic1.clear()
# dic1.pop(9)
# dic1.popitem() # Pops last item
del dic1[901]
print(dic1)
