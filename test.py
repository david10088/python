#!/usr/bin/env python3
# -*- coding: utf-8 _*_

 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
start_url="http://www.mzitu.com/"
def get_mei_channel(url,pages):
    li = []
    for x in range(1,int(pages)+1):
        web_data=requests.get(url+"page/"+str(x)+"/")
        soup=BeautifulSoup(web_data.text,'lxml')
        channel=soup.find(id = 'pins').findAll('li')
        for list in channel:
            li.append(list.find('img').get('data-original'))
    return  li
def get_pages(url):
   html = requests.get(url)
   soup = BeautifulSoup(html.text,'html.parser')
   pages = soup.findAll(class_= 'page-numbers')
   return pages[-2].getText()
def get_pic(url,num):
    html = requests.get(url)
    open(str(num)+'.jpg', 'wb').write(html.content)
pages = get_pages(start_url)
print(pages)
li = get_mei_channel(start_url,pages)
num =1
for x in li:
    get_pic(x,num)
    num = num+1