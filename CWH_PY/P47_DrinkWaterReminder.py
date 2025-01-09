import win32com.client as win32
import time

def speak_out():
    speaker = win32.Dispatch("SAPI.Spvoice")
    while True:
        sec = int(time.strftime("%S", time.localtime()))
        print(sec)
        if sec == 59:
            print("Hello")
            speaker.speak("It's time to drink water.")
            time.sleep(1)
        time.sleep(0.5) 


speak_out()

 