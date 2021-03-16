import threading
import screen_record
import open_browser


def run_screen_record():
    screen_record.screen_record()


def run_open_browser():
    open_browser.open_browser()


thread = [threading.Thread(target=run_screen_record), threading.Thread(target=run_open_browser)]

if __name__ == '__main__':

    for t in thread:
        t.start()
