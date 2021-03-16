import os
import threading
import time


def run_screen_record():
    os.system('python screen_record.py')


def run_open_browser():
    os.system('python open_browser.py')


thread = [threading.Thread(target=run_screen_record), threading.Thread(target=run_open_browser)]

if __name__ == '__main__':

    for t in thread:
        t.start()
