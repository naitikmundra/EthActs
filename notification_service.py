import win10toast_click
import random
import time
from playsound import playsound
import threading
import stoicquote as q

class NotificationService:
    def __init__(self):
        self.quote_file = "quotes.txt"

    def onclick(self):
        # run_ethacts.py

        from ethacts_gui import EthActsApp
        
        EthActsApp(initial_tab=1).run()

    # Example: Open the Quiz tab (tab 2)
    # EthActsApp(initial_tab=2).run()
    def play_sound(self):
        playsound("notify.wav")
    

    def show_notification(self):
        try:
            toaster = win10toast_click.ToastNotifier()
            quote = q.get_random_quote()[0]
            self.save_quote(quote)

            toaster.show_toast(
                "EthActs", quote, icon_path="notification.ico", callback_on_click=self.onclick
            )
            print("Notification showed")
        except Exception as e:
            print(f"Exception in show_notification: {e}")

    def save_quote(self, quote):
        

        # Write the new quote at the beginning of the file
        with open(self.quote_file, "a") as file:
            file.write("\n" + quote + "\n")  # Write the new quote

    def start_service(self):
        while True:
            sound_thread = threading.Thread(target=self.play_sound)
            notification_thread = threading.Thread(target=self.show_notification)

            sound_thread.start()
            notification_thread.start()

            sound_thread.join()
            notification_thread.join()

            time_to_wait = random.randint(30, 180)
            print(f"Waiting for {time_to_wait} seconds before the next notification.")
            time.sleep(time_to_wait)

if __name__ == "__main__":
    service = NotificationService()
    service.start_service()
