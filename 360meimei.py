 # -*-coding:UTF-8-*-
import urllib2
import re
from lxml import etree
import random
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

global NUM 
NUM = 0
global NUM1 
NUM1 = 0
#获取所有需要爬取的美女html页面
def allurl(url,headers):
    for a in range(1015,1608):
        print a
        Newurl = url + str(a) + '.html' 
        #print Newurl
        try:
            request = urllib2.Request(Newurl, headers=headers)
            response = urllib2.urlopen(request,timeout = 180).read()
        except urllib2.URLError, e:
            return 0

        pattern = etree.HTML(response)
        link_list = pattern.xpath('//div[@class="post-inner post-hover"]/div[@class="post-thumbnail"]/a/@href')
        for link in link_list:
            #print link
            alllink = "http://www.360meimei.com" + link
            #print alllink
            allgirlurl(alllink,headers = headers)
#获取所有美女的图片每一个html页面
def allgirlurl(url,headers):
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request,timeout = 180).read()
    except urllib2.URLError, e:
        return 0
    pattern = etree.HTML(response)
    #print pattern
    img_Link = pattern.xpath('//div[@class="link_pages"]/a[last()-1]/span/text()')
    # print url
    # return 0
    count = 1
    global NUM
    global NUM1
    NUM = 0
    while 1:
        
        if(count == 1):
            url1 = url
        else:
            url1 = url[:-5]+'_'+str(count)+'.html'
        try:
            request = urllib2.Request(url1,headers = headers)
            response = urllib2.urlopen(request,timeout=160).read()
        except urllib2.URLError, e:
            print NUM1
            break
        count = count +1
        #print url1
        allgirl(url1,headers)
    
    #print img_Link
#获取所有美女的图片url
def allgirl(url,headers):
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request,timeout = 180).read()
    except urllib2.URLError, e:
        return 0
    #print url
    # return 0
    pattern = etree.HTML(response)
    DIRNAME = pattern.xpath('//div[@class="post-inner group"]/h1/text()')
    #print DIRNAME
    for ccc in DIRNAME:
        title = ccc.encode('utf-8')
        #print DIRNAME
        #print type(DIRNAME)
    title = title.strip()#名称
    path= r'/home/liang/Pictures/360meimei'
    newfiledir=path+'/'+str(title)#确定新的文件路径，此处根据关键词创建新的文件夹
    try:
        isexist=os.path.exists(newfiledir)# 判断文件夹是否存在
        if not isexist : # 如果不存在则创建文件路径
            os.mkdir(newfiledir)
    except :
        return
    
    img_Link = pattern.xpath('//div[@class="entry-inner"]/p/img[@class="lazy lazy-hidden"]/@src')
    #print img_Link
    for aa in  img_Link:
        #saveimg(num,img_name.encode("utf-8"),headers)
        saveimg(aa,headers,newfiledir,title)
	#print num[-21:-14]
        #print num
    
	#pass 
    #print link_list

def saveimg(url,headers,newfiledir,title):
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request,timeout = 180).read()
    except urllib2.URLError, e:
        return 0
    global NUM
    NUM += 1
    global NUM1
    NUM1 += 1
    
    #img_name = range(1,30000)
    #print img_name
    try:
        with open(newfiledir + '/' + title + str(NUM) + '.jpg','wb') as f:
            f.write(response)
    except:
        return 0




if __name__ == "__main__":
    url = "http://www.360meimei.com/index_"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"http://www.360meimei.com/"}

allurl(url,headers)