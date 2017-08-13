 # -*-coding:UTF-8-*-
import re
import urllib
import urllib2
import os
import random 
import multiprocessing
from lxml import etree
from selenium import webdriver
import time
url = 'http://www.mt366.com/youwu/1663.html'
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"}
# request = urllib2.Request(url, headers=headers)
# response = urllib2.urlopen(request,timeout=160).read()
 

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get(url)   #加载网页
data = driver.page_source   #获取网页文本
driver.save_screenshot('1.png')   #截图保存
pattern = etree.HTML(data)
#link_list = pattern.xpath('//div[@class="mod-single"]/div/div/a/img/@src')

p1 = r"onclick=\"this\.blur\(\);\"><img src=\"\n*(.*)\" alt="
p2 = r"http://www\.mt366\.com.*jpg"

pattern1 = re.compile(p1)
data1 = pattern1.findall(data)
for c in data1:
	pattern2 = re.compile(p2)

	print pattern2.findall(c)
driver.quit()