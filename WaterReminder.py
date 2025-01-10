import win32com.client as win32
from win10toast import ToastNotifier


def speak_out(name):
    toast = ToastNotifier()
    speaker = win32.Dispatch("SAPI.Spvoice")
    toast.show_toast(
        "Python Reminder",
        f"Hey {name}, It's time to drink water.",
        duration=3,
        icon_path=None,
    )
    speaker.speak(f"It's time to drink water {name}.")

speak_out("Rohith")

