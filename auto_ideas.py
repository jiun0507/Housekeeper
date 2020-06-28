import sys
import time
import json
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if ".png" in filename:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/screenshots/" \
                    + filename
                os.rename(src, new_destination)
            elif ".py" in filename:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/pythonfiles/" \
                    + filename
                os.rename(src, new_destination)
            elif ".jpg" in filename or "jpeg" in filename:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/photos/" \
                    + filename
                os.rename(src, new_destination)                
            elif ".key" in filename:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/keynotes/" \
                    + filename
                os.rename(src, new_destination)  
            elif ".key" in filename:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/keynotes/" \
                    + filename
                os.rename(src, new_destination)  
            if ".zip" in filename:
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/zipfiles/" \
                    + filename
                os.rename(src, new_destination)  


folder_to_track = "/Users/bob/Desktop"
folder_destination = "/Users/bob/Desktop/automated_organization/"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop()
observer.join()
