import sys
import threading
from notification_service import NotificationService
from ethacts_gui import EthActsApp
import wx

def run_notification_service():
    service = NotificationService()
    service.start_service()

def run_gui():
    app = wx.App(False)
    frame = EthActsApp()
    app.MainLoop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        run_gui()
    else:
        run_notification_service()
