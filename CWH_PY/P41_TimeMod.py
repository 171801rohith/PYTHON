# Time Module
import time

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("Hello")
time.sleep(5)
print("World") # It's printed after 5 seconds

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)