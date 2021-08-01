from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


regurl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(regurl)

time.sleep(10)

def scrapedate():
    headers=["Name", "Distance", "Mass", "Radius"]
    