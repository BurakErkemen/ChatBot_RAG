from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
import requests
import pandas as pd 
from fpdf import FPDF

browser = webdriver.Edge()
dizi = []

sleep(5)

def clean_text(text):
    return ''.join(char for char in text if char.isprintable())

pdf = FPDF()
pdf.add_page()
pdf.add_font("ArialUnicode", fname=r"C:\Users\burak\Downloads\ArialUnicodeMSRegular\ArialUnicodeMSRegular.ttf")
pdf.set_font("ArialUnicode", size=12)  # Bu satır eklenmiş
"""
for i in range(1):
    height = 0 
    new_url = f"https://yazilimtf.firat.edu.tr/tr/announcements-all/{i}"
    browser.get(new_url)
    sleep(3)
    for j in range(1, 2):
        try:
            git_button = browser.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div[1]/a[{j}]")
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
            cleaned_title = clean_text(title)
            cleaned_content = clean_text(context)
            cleaned_date = clean_text(date)

            text = f"baslık: {cleaned_title}\Content: {cleaned_content}\nDate: {cleaned_date}\n\n"
            pdf.cell(200, 10, txt=text, ln=True)
            
            browser.back()
            height += 192
            browser.execute_script(f"window.scrollTo(0,{height})") #3267
            sleep(3)
        except IndexError:
            print(f"IndexError: {i} numaralı eleman bulunamadı.")

"""
akademisyen = "https://yazilimtf.firat.edu.tr/academic-staffs"
browser.get(akademisyen)
for k in range(20):
    try:
        Ad = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-name")[k].text
        Mail = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-contact-mail")[k].text
        CalısmaAlan = browser.find_elements(By.CSS_SELECTOR, ".personnel-card-info-work-places")[k].text
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
        print(f"IndexError: {k} numaralı eleman bulunamadı.")

pdf.output("output1.pdf", "F")
print("PDF oluşturuldu.")


browser.quit()
