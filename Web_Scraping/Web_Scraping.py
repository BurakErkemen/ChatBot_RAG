
from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By
import requests
import pandas as pd 

browser = webdriver.Edge()

duyuru1 = "https://yazilimtf.firat.edu.tr/tr/announcements-all"

browser.get(duyuru1)


sleep(3)

