import win32com.client as win32
import time
from win10toast import ToastNotifier


def speak_out(name):
    toast = ToastNotifier()
    speaker = win32.Dispatch("SAPI.Spvoice")
    while True:
        toast.show_toast(
            "Python Reminder",
            f"Hey {name}, It's time to drink water.",
            duration=3,
            icon_path=None,
        )
        speaker.speak(f"It's time to drink water {name}.")
        time.sleep(60 * 60)

speak_out("Rohith")

# try out Plyer module