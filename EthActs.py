import win10toast_click
import random
import time
from playsound import playsound
import threading
import stoicquote as q
def onclick():
    print("notification clicked")

def play_sound():
    playsound("notify.wav")

def show_notification():
    toaster = win10toast_click.ToastNotifier()
    toaster.show_toast(
        " ",q.get_random_quote()[0], icon_path="notification.ico", callback_on_click=onclick
    )

while True:
    # Start both the sound and notification in separate threads
    sound_thread = threading.Thread(target=play_sound)
    notification_thread = threading.Thread(target=show_notification)

    sound_thread.start()
    notification_thread.start()

    # Ensure both threads have completed before continuing
    sound_thread.join()
    notification_thread.join()

    time_to_wait = random.randint(30, 180)
    print(time_to_wait)
    time.sleep(time_to_wait)
