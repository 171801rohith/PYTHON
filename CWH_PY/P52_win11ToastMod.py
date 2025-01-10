# Display Notifications

from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Welcome to Python ", "This is cool!", duration=4, icon_path= None)
