import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os
import csv
import pathlib


def init():
    command = 'echo Booting Up >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
    os.system(command)

def shutdown():
    command = 'shutdown p'
    os.system(command)

def move(path):
    command = 'echo Moving File '+ path +'to Shared Folder >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
    os.system(command)
    command = 'move ' + path + ' C:\\Users\\WDAGUtilityAccount\\Desktop\\Secure_Torrent\\'
    os.system(command)

def scan(path):
    # Need Checksum for file downloaded here
    command = 'echo We are scanning the file' + path + ' >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
    os.system(command)
    command = 'C:\\Users\\WDAGUtilityAccount\\Desktop\\Box\\ClamAV\\clamscan -i --no-summary ' + path
    flag = os.system(command)
    command = 'echo Scan Complete with '+ flag +' flags >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
    os.system(command)

    if flag != 0:
        shutdown()
    else:
        move(path)


class Watcher:
    DIRECTORY_TO_WATCH = "C:\\Users\\WDAGUtilityAccount\\Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        command = 'echo Started Secure Monitoring Successfully in Background >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
        os.system(command)
        try:
            while True:
                time.sleep(3)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            check = str(pathlib.Path(str(event.src_path)).suffix).lower()
            command = 'echo Checking if we need to scan '+ str(event.src_path) +' >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
            os.system(command)
            if check not in ['.tmp', '.crdownload', '.download', '.!bt', '.torrent']:
                new = '"' + str(event.src_path).replace(r"/", "\\")
                new += '"'
                scan(new)
                # print ("Received created event - %s." % new)


        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            check = str(pathlib.Path(str(event.src_path)).suffix).lower()
            command = 'echo Checking if we need to scan '+ str(event.src_path) +' >> C:\\Users\\WDAGUtilityAccount\\Desktop\\Log.txt'
            os.system(command)
            if check not in ['.tmp', '.crdownload', '.download', '.!bt', '.torrent']:
                new = '"' + str(event.src_path).replace(r"/", "\\")
                new += '"'
                scan(new)

if __name__ == '__main__':
    init()
    w = Watcher()
    w.run()

    # pythonw.exe
