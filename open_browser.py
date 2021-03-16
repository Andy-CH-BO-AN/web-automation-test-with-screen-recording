import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = 'https://www.google.com/'


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
    options.add_argument('window-size=1920x1080')
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
    os.system(r'taskkill /f /im python.exe')
