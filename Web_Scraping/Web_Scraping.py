
from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
import requests
import pandas as pd 

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


browser = webdriver.Edge()
dizi=[]
duyurular = "https://yazilimtf.firat.edu.tr/tr/announcements-all"

browser.get(duyurular)
sleep(5)

height = 0 
for i in range(1,13):
    git_button = browser.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div[1]/a[{i}]")
    sleep(3)
    git_button.click()
    sleep(3)
    browser.execute_script("window.scrollTo(0,200)")
    title = browser.find_element(By.CSS_SELECTOR,"new-section-detail-title")
    date = browser.find_element(By.CSS_SELECTOR,"new-section-detail-date")
    context = browser.find_element(By.CSS_SELECTOR,"new-section-detail-explanation")
    item = {
        'baslık': title,
        'icerik': context,
        'tarih': date
    }
    dizi.append(item)
    browser.back()
    height +=192
    browser.execute_script(f"window.scrollTo(0,{height})") #3267
    sleep(3)

sleep(25)

print(dizi)

sleep(25)
browser.quit()
