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
