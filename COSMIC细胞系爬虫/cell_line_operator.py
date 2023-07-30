import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import os
import pandas as pd
from lxml import html
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}
My_df = pd.DataFrame(columns=['Sample_name','COSMIC_sample_ID','Tumour_location','Screening_method','Sample_type','Cell_line_source','Sample_source'])
os.chdir("C:\\Users\\杨谷婴\\Desktop\\陈帅宇临时工作\\爬虫")
cwd = os.getcwd()
with open('links.csv') as f:
  links = list(csv.reader(f))
links = [row[0] for row in links]
def add_record(Sample_name, COSMIC_sample_ID, Tumour_location, Screening_method, Sample_type, Cell_line_source, Sample_source):
    global My_df
    My_df = pd.concat([My_df, pd.DataFrame({'Sample_name': [Sample_name],
                                            'COSMIC_sample_ID': [COSMIC_sample_ID],
                                            'Tumour_location': [Tumour_location],
                                            'Screening_method': [Screening_method],
                                            'Sample_type': [Sample_type],
                                            'Cell_line_source': [Cell_line_source],
                                            'Sample_source': [Sample_source]})], ignore_index=True)

def crawl(url):
  r = requests.get(url,headers=headers)
  tree = html.fromstring(r.text)
  Sample_name=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[2]/a')[0].text_content()
  print(Sample_name)
  COSMIC_sample_ID=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[3]')[0].text_content()
  print(COSMIC_sample_ID)
  Tumour_location=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[4]')[0].text_content()
  print(Tumour_location)
  Screening_method=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[5]')[0].text_content()
  print(Screening_method)
  Sample_type=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[6]/dl/dd[1]')[0].text_content()
  print(Sample_type)
  Cell_line_source=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[6]/dl/dd[2]')[0].text_content()
  print(Cell_line_source)
  Sample_source=tree.xpath('/html/body/div[1]/div/div[2]/section[1]/div/div/dl/dd[6]/dl/dd[3]')[0].text_content()
  print(Sample_source)
  add_record(Sample_name,COSMIC_sample_ID,Tumour_location,Screening_method,Sample_type,Cell_line_source,Sample_source)
  print(My_df)
i=1
for link in links:
  crawl(link)
  i=i+1
  output_file = str(i)+"output_data.csv"
  My_df.to_csv(output_file, index=False)
#def add_record(Sample_name,COSMIC_sample_ID,Tumour_location,Screening_method,Sample_type,Cell_line_source,Sample_source):
  #global My_df
  #My_df = My_df.append({'Sample_name':Sample_name, 'COSMIC_sample_ID':COSMIC_sample_ID,'Tumour_location':Tumour_location,'Screening_method':Screening_method,'Sample_type':Sample_type,'Cell_line_source':Cell_line_source,'Sample_source':Sample_source}, ignore_index=True)
