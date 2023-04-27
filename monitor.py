import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os
import hashlib
import csv
from numpy import genfromtxt

malwaredb = []

def init():
    global malwaredb
    print("Hello user! Do not close this window!")
    print("This is what is keeping you safe!")
    print("Setting up C:\\Secure_Torrent...")
    command = 'rmdir /s /q C:\\Secure_Torrent'
    os.system(command)
    command = 'mkdir C:\\Secure_Torrent'
    os.system(command)
    print("Downloading malware database...")
    command = 'curl -o C:\\Users\\4675\\Documents\\MWDB.csv http://5.161.188.76/project/MWDB.csv'
    os.system(command)
    print("Malware database downloaded to C:\\Users\\4675\\Documents\\MWDB.csv!")
    malwaredbfile = open("C:\\Users\\4675\\Documents\\MWDB.csv")
    malwaredb = list(csv.reader(malwaredbfile))
    print("Malware database ready to go!")
    malwaredbfile.close()

def scan(path):
    command = 'C:\\"Program Files\\Windows Defender"\\MpCmdRun.exe -Scan -ScanType 3 -File ' + path
    os.system(command)

def compare(path):
    print("Checking malware database for match")
    f = open(path, 'r')
    filein = f.read().encode("utf-8")
    sha256hash = hashlib.sha256(filein).hexdigest()
    f.close()
    for x in malwaredb:
        xr = "Null"
        try:
            xr = str(x).replace("[","").replace("]","").replace("'","")
        except:
            xr = "Null"
        if sha256hash == xr:
            print("Blacklisted malware detected, deleting file!")
            os.remove(path)
            return False
    print("File not contained in blacklisted malware, forwarding to defender")
    return True

class Watcher:
    DIRECTORY_TO_WATCH = "C:\\Secure_Torrent"

    def __init__(self):
        self.observer = Observer()
        print("Waiting for files to be downloaded to scan...")

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
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
            time.sleep(1)
            new = '"' + str(event.src_path).replace("\\", r"/")
            new += '"'
            print ("Received created event - %s." % new)
            try:
                if compare(str(event.src_path)):
                   scan(new)
            except:
                print("Checksum error: Rely on Windows Defender")
                scan(new)


        #elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
        #    time.sleep(1)
        #    new = '"' + str(event.src_path).replace("\\", r"/")
        #    new += '"'
        #    print ("Received modified event - %s." % new)
        #    compare(str(event.src_path))
        #    scan(new)

if __name__ == '__main__':
    init()
    w = Watcher()
    w.run()

    # pythonw.exe
