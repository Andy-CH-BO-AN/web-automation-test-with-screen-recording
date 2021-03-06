import threading
import numpy as np
import cv2
import pyautogui
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from PIL import ImageGrab
# etet
url = 'https://www.google.com/'
cur_screen_resolution = ImageGrab.grab()  # 獲取屏幕對象
height, width = cur_screen_resolution.size
screen_size = (height, width)


def open_browser():
    # 跳過驅動器
    chrome_path = ChromeDriverManager().install()
    options = webdriver.ChromeOptions()
    # 禁用瀏覽器彈窗
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    options.add_experimental_option('prefs', prefs)
    # 設定瀏覽器分辨率(配合無頭模式)
    options.add_argument(f'window-size={height}x{width}')
    # 開啟無頭模式(自行決定是否啟動)
    # options.add_argument('--headless')
    # 去除自動化控制提示
    options.add_argument('--disable-notifications --disable-popup-blocking')
    # 開啟無痕模式
    options.add_argument('--incognito')
    # 文檔提到需要加上這個屬性來規避bug
    options.add_argument('--disable-gpu')
    # 設置開發者模式啟動，該模式下webdriver屬性為正常值
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(chrome_path, options=options)
    driver.get(url)
    time.sleep(5)
    driver.quit()
    shut_down_python()


def screen_record():
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        # cv2.imshow('show',frame)
        if stop:
            break


def shut_down_python():
    global stop
    stop = True


thread = [threading.Thread(target=screen_record), threading.Thread(target=open_browser)]

if __name__ == '__main__':
    stop = False
    for t in thread:
        t.start()
