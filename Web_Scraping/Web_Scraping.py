
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

sleep(2)
"""
for i in range(1,67):
    height = 0 
    new_url = f"https://yazilimtf.firat.edu.tr/tr/announcements-all/{i}"
    browser.get(new_url)
    sleep(3)
    for i in range(1,13):
        git_button = browser.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div[1]/a[{i}]")
        sleep(5)
        git_button.click()
        sleep(5)
        browser.execute_script("window.scrollTo(0,200)")
        title = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div[3]/h3").text
        date = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div[2]/p").text
        context = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div[4]/p[2]").text
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
"""
akademisyen = "https://yazilimtf.firat.edu.tr/academic-staffs"
browser.execute_script("window.scrollTo(0,200)")

browser.get(akademisyen)
sleep(3)
#for i in range(1,21):
link = browser.find_element(By.XPATH,f"/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/a")
height_akademic = 0
link.click()
sleep(5)
unvan = browser.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div[2]/div[1]") 
ad = browser.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div[2]/div[2]/h2")
kurum = browser.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div[2]/p")
uzmanlık = browser.find_element(By.XPATH,'//*[@id="uzmanlik_text"]')
yok_ıd = browser.find_element(By.XPATH,'//*[@id="yok_academic_id_text"]')
browser.execute_script("window.scrollTo(0,3200)")
mail = browser.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/p[3]/a")
item = {
            'unvan': unvan,
            'ad': ad,
            'kurum': kurum,
            'uzmanlık ':uzmanlık,
            'yok_ıd' : yok_ıd,
            'mail':mail
        }
dizi.append(item)

print(dizi)
sleep(5)
browser.quit()
