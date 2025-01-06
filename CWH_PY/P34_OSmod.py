# OS Module 
# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from l.png all the way till n.png where n is the number of png files in that folder. 
# Do the same for other file formats
import os

dir = "C:\\Users\\rohit\\Desktop\\PYTHON\\OS Example\\Tutorial1"

print(os.listdir(dir))
i = 0

for file in os.listdir(dir):
    if file.endswith(".json"):
        i += 1
        old_path = os.path.join(dir, file)
        new_file = f"{i}.json"
        new_path = os.path.join(dir, new_file)

        os.rename(old_path, new_path)

print(os.listdir(dir))
        

