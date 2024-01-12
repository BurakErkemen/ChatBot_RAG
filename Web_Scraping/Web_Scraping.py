
from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
import requests
import pandas as pd 
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



browser = webdriver.Edge()
dizi=[]

sleep(2)
"""
for i in range(1,6):
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
        context = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div[4]/p[2]").text
        date = browser.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[2]/div[2]/p").text
        
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
#browser.execute_script("window.scrollTo(0,200)")

browser.get(akademisyen)
sleep(5)

def clean_text(text):
    return ''.join(char for char in text if char.isprintable())

pdf = FPDF()
pdf.add_page()
pdf.add_font("ArialUnicode", fname=r"C:\Users\burak\Downloads\ArialUnicodeMSRegular\ArialUnicodeMSRegular.ttf")
pdf.set_font("ArialUnicode", size=12)  # Bu satır eklenmiş

for i in range(20):
    try:
        Ad = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-name")[i].text
        Mail = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-contact-mail")[i].text
        CalısmaAlan = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-work-places")[i].text
        item = {
            'ad': Ad,
            'mail': Mail,
            'calısmalanları': CalısmaAlan
        }
        dizi.append(item)

        cleaned_ad = clean_text(Ad)
        cleaned_mail = clean_text(Mail)
        cleaned_calisma_alanlari = clean_text(CalısmaAlan)

        text = f"Ad: {cleaned_ad}\nMail: {cleaned_mail}\nÇalışma Alanları: {cleaned_calisma_alanlari}\n\n"
        pdf.cell(200, 10, txt=text, ln=True)
    except IndexError:
        print(f"IndexError: {i} numaralı eleman bulunamadı.")

pdf.output("output.pdf", "F")

print("PDF oluşturuldu.")
print(dizi)

browser.quit()