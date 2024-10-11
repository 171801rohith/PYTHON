# Taking User Inputs
a = input("Enetr your name : ")
print("Your name is",a)

x =int( input("Enetr 1st num : "))
y = int(input("Enetr 2nd num : "))
print(x + y)

# Strings in Python
a = 'hello'
b = "hello"
apple = '''Rohith 
this is 
awesome
'''
# We can write a whole paragraphs inside ''' ''' or """ """
print(apple)

print(a[0])
print(a[2])
print("Printing 'a' using for loop")
for character in a:
    print(character) 

# String Slicing 
     #      ......-3,-2,-1
     # 0,1,2,3,4,5,....
# num = [1,2,3,4,5,6,7,8,9]
name = "Harry,Shubham"
print(len(name))
print(name[0:5]) # Slicing means : [n:m] prints from n to m-1
print(name[2:7])  
print(name[:7]) # 0 to 7
print(name[:-3])  # 0 to 13-3 excludes n characters
print(name[-3:])  # Last 3 characters
nm = "harry"
print(nm[-4:-2])

# String Methods 
#  Strings are immutable
a = "abhishek!! !! !shek"
print(a.find("sh")) # if not found -1. First Occurance Index
print(a.index("shhh")) # if not found error. First Occurance Index
print(a.endswith('000')) # bool value is returned
print(a.endswith('!!', 5,13)) # bool value is returned
print(a.startswith('!!', 5,13)) # bool value is returned
print(a.count('shek'))
print(a.center(50))
print(a.capitalize()) # Only 1st letter in caps
print(a.split(' '))
# print(a.split('!'))
print(a.replace("shek", "lash"))
print(a.rstrip('!'))
print(a.upper()) # Works on a copy of str
print(a.lower())
print(len(a))
str = 'rohith171801'
print(str.swapcase())
print(str.istitle()) # if 1st letter caps returns true
# str = 'rohith171801\n' 
print(str.isprintable())
print(a.islower())
print(a.isupper())
print(str.isalpha()) # bool checks alpha 
print(str.isalnum()) # bool checks alpha numeric
print(a.isalnum()) # bool
sp = "      "
print(sp.isspace())