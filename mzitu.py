 # -*-coding:UTF-8-*-
import urllib
import urllib2
import os
from lxml import etree
def allurl():
    url = 'http://www.mzitu.com/all'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0','Referer': 'http://www.mzitu.com'}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request).read()
    #print response
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//a[@target="_blank"]/@href')
    for link in link_list:
        #girlurl(link,headers)
        link = link
        girlurl(link,headers)

def girlurl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    #print response
    pattern = etree.HTML(response)
    #dirName = pattern.xpath('//head[1]/title/text()')
    #for ccc in dirName:
    #DIRNAME = ccc.encode('utf-8')
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//div[@class="pagenavi"]/a[5]/span/text()')
    for num in link_list:
        #print num
        for Num in range(1,int(num)):
            Newurl = url +  '/' + str(Num)
            #print Newurl
            lasturl(Newurl,headers)

    #for link in link_list:
    #    print link
def lasturl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    #print response
    pattern = etree.HTML(response)
    link_list = pattern.xpath('//div[@class="main-image"]/p/a/img/@src')
    maintitle = pattern.xpath('//div[@class="content"]/h2/text()')
    #print maintitle
    for title in maintitle:
        imgname = title.encode('utf-8')
        #print imgname
    #dirName = pattern.xpath('//head[1]/title/text()')
    #print dirName.encode("UTF-8")
    #for bbb in dirName:
    #    print bbb.encode("UTF-8")
    #print link_list
    for link in link_list:
        #pass
        #print link
        saveimg(imgname,link,headers)
def saveimg(imgname,url,headers):
    #dir = os.mkdir(imgname)
    #print dir
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    #print url[-9:]
    #DIR = '/改成自己的目录/' + dir + url[-9]
    #print DIR
    with open('/home/liang/Pictures/mzitu/' + imgname + '.jpg','wb') as f:
        f.write(response)




allurl()