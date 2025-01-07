# Write a program to pronounce t ist of names using win32 API.
# If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce:
# Shoutout to Rahul
# Shoutout to Nishant

import win32com.client as win32

class ShoutOut:
    speaker = win32.Dispatch("SAPI.SpVoice")
    def __init__(self, names):
        self.names = names
    
    def pronounce(self):
        for name in names:
            shoutout = f"Shoutout to {name}"
            print(shoutout)
            self.speaker.speak(shoutout)



names = ["Rohith", "Shek", "Aadithya", "Karthik"]
shout = ShoutOut(names)
shout.pronounce()