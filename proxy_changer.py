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

txt = open("proxy_list.txt","r")
txt_content = txt.read()
## print(txt_content)
prlist = txt_content.split('\n')
print(prlist[0])
print(len(prlist))