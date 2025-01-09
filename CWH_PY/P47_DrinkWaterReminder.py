import win32com.client as win32
import time

def speak_out():
    speaker = win32.Dispatch("SAPI.Spvoice")
    while True:
        min = int(time.strftime("%M", time.localtime()))
        print(min)
        if min == 59:
            print("Hello")
            speaker.speak("It's time to drink water.")
            time.sleep(1)
        time.sleep(0.5) 


speak_out()

 