# Time Module
import time
timestmp = time.strftime('%H:%M:%S')
print(timestmp)
timestmp = time.strftime('%H')
print(timestmp)
timestmp = time.strftime('%M')
print(timestmp)
timestmp = time.strftime('%S')
print(timestmp)

# Exersice 1
timesir = time.strftime('%H')
print(timesir)
if(int(timesir) > 20):
    print("Good Night sir!!!")
elif(int(timesir) > 16):
    print("Good Evening sir!!!")
elif(int(timesir) >12):
    print("Good Afternoon sir!!!")
else:
    print("Good Morning sir!!!")
    
