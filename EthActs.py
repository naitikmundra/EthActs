import sys
import threading
from notification_service import NotificationService

def run_notification_service():
    service = NotificationService()
    service.start_service()



if __name__ == "__main__":
  
        run_notification_service()
