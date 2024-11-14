import os
if(not os.path.exists("OS Example")):
    os.mkdir("OS Example")

# for i in range(1, 5):
#     os.mkdir(f"OS Example/Day{i}")

# for i in range(1, 5):
#     os.rename(f"OS Example/Day{i}", f"OS Example/Tutorial{i}")

folders  = os.listdir("OS Example")
for folder in folders:
    print(folder)
    print(os.listdir(f"OS Example/{folder}"))

print(os.getcwd()) # prints the current working directory
# os.chdir("/User")
print(os.getcwd()) # prints the current working directory