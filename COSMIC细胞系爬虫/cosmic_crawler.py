import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import os
os.chdir("C:\\Users\\杨谷婴\\Desktop\\陈帅宇临时工作\\爬虫")
cwd = os.getcwd()
print(cwd)
url='https://cancer.sanger.ac.uk/cell_lines/cbrowse/all'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = []
for span in soup.find_all('span', class_='sample'):
  try:
    a = span.find('a')
    links.append(a['href'])
  except:
    pass
with open('links.csv','w',newline='') as csvfile:
  writer = csv.writer(csvfile,delimiter=',',quoting=csv.QUOTE_MINIMAL)

  for link in links:
    writer.writerow([link])
    
csvfile.close()
print(links)