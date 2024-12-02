# Reading a file
f = open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/myfile.txt", "r")
print(f)
text = f.read()
print(text)
f.close()

# Writing to a file
f = open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/myfile.txt", "w")
f.write("hello world, Harry is crazy. ")
f.close()

# Appending to a file
f = open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/myfile.txt", "a")
f.write("Man this is not crazy!")
f.close()

with open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/myfile.txt", "a") as f:
    f.write("Broooo!")