from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd

regurl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(regurl)

Name=[]
Distance=[]
Mass=[]
Radius=[]

print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')


temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    Name.append(temp_list[i][1]) 
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

headers=['Name','Distance','Mass','Radius']
#Zip=putting it all together, list will make it as a list
planetdata=pd.DataFrame(list(zip(Name,Distance,Mass,Radius)),columns=["Name", "Distance", "Mass", "Radius"])
planetdata.to_csv("planetdata.csv")


