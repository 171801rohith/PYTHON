# Shutil  Module
import shutil, os

shutil.copy("C:\\Users\\rohit\\Desktop\\PYTHON\\CWH_PY\\P24.py", "OS Example\\Tutorial1\\shutilCopy.py")
# shutil.copy("src", "dst") used to copy files

shutil.copytree("OS Example\\Tutorial4", "OS Example\\myCopyTree")
# shutil.copytree("src", "dst") used to copy folders

shutil.move("OS Example\\Tutorial4\\Nothing.png", "OS Example\\Tutorial2\\Nothing.png")
# shutil.move("src", "dst") used to moves files

shutil.rmtree("OS Example\\Tutorial3")
# shutil.rmtree("src") used to delete folders

os.remove("OS Example\\Tutorial1\\3.json")
# os.remove("src") used to delete files