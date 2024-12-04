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

f.close()

# ReadLines method
f = open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/mymarks.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    m0 = line.split(",")[0]
    m1 = line.split(",")[1]
    m2 = line.split(",")[2]
    print(line)
    print(f"M0 : {m0}\tM1 : {m1}\tM2 : {m2}")

f.close()

# WriteLines method
f = open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/myfile.txt", "w")
lines = ["line1\n", "line2\n", "line3\n"]
f.writelines(lines)
f.truncate(8)
f.close()

# Seek & Tell method
with open("C:/Users/rohit/Desktop/PYTHON/CWH_PY/myfile.txt", "r") as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print(data)
