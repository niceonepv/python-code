from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
## import pandas as pd
import requests
import time
from selenium.webdriver.chrome.options import Options
## from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

txt = open("proxy_list.txt","r")
txt_content = txt.read()
## print(txt_content)
prlist = txt_content.split('\n')
## print(prlist[0])
## print(len(prlist))


filename = 'webex.exe'

URL = 'https://bitbucket.org/softvault/vlc/downloads/webex_client_0002b.exe'

for i in range(65,75):
    try:
        option = Options()
        prefs = {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.automatic_downloads': 1,
            'download.prompt_for_download': False,
        }
        print(prlist[i])
        option.add_experimental_option('prefs', prefs)

        option.add_argument("--disable-infobars")
        option.add_argument('--safebrowsing-disable-extension-blacklist')
        option.add_argument('--safebrowsing-disable-download-protection')
        option.add_argument(f'--proxy-server={str(prlist[i])}')

        browser = webdriver.Chrome(options=option)

##    browser.get('https://2ip.ru')
        browser.get('https://bitbucket.org/softvault/trueconf/downloads/')
##    time.sleep(100)
##   file = browser.find_element(By.linkText, )
        file = browser.find_element(By.LINK_TEXT, 'CSPSetup-5.0.11998.exe')
        file.click()
        time.sleep(5)
        pyautogui.moveTo(417,990,duration = 1)
        pyautogui.click(417,990)
##    print(pyautogui.position())
##    req = requests.get(URL)
##    with open(filename,"wb") as f:
##        f.write(req.content)
        time.sleep(5)
        browser.close()
     ##   print(i)
    except:
        pass