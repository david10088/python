 # -*-coding:UTF-8-*-
import urllib2
import re
from lxml import etree
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

global NUM 
NUM = 0
#获取所有需要爬取的美女html页面
def allurl(url,headers):
    for a in range(2,1608):
        Newurl = url + str(a) + '.html' 
        #print Newurl
        request = urllib2.Request(Newurl, headers=headers)
        response = urllib2.urlopen(request).read()
        pattern = etree.HTML(response)
        link_list = pattern.xpath('//div[@class="post-inner post-hover"]/div[@class="post-thumbnail"]/a/@href')
        for link in link_list:
            #print link
            alllink = "http://www.360meimei.com" + link
            #print alllink
            allgirlurl(alllink,headers = headers)
#获取所有美女的图片每一个html页面
def allgirlurl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    #print pattern
    img_Link = pattern.xpath('//div[@class="link_pages"]/a[last()-1]/span/text()')
    #print img_Link
    for pageNum in img_Link:
    	if len(pageNum)==1:
    	    #print img
	    #print url
	    #print "-----+++_____"
	    for N in range(2,int(pageNum)):
		Newurl = url[:-5] + '_' + str(N) + '.html'
		print Newurl
	    	allgirl(Newurl,headers)
    		#allgirl(url,headers)
	else:
	    #continue
	    print  "单页"
	    allgirl(url,headers)
    #print img_Link
#获取所有美女的图片url
def allgirl(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    pattern = etree.HTML(response)
    img_Link = pattern.xpath('//div[@class="entry-inner"]/p/img[@class="lazy lazy-hidden"]/@src')
    #print img_Link
    for aa in  img_Link:
        #saveimg(num,img_name.encode("utf-8"),headers)
        saveimg(aa,headers)
	#print num[-21:-14]
        #print num
	#pass 
    #print link_list

def saveimg(url,headers):
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request).read()
    global NUM
    NUM += 1
    print NUM
    #img_name = range(1,30000)
    #print img_name
    with open('/home/liang/Pictures/360meimei/' +str(NUM) + '.jpg','wb') as f:
        f.write(response)




if __name__ == "__main__":
    url = "http://www.360meimei.com/index_"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0","Referer":"http://www.360meimei.com/"}

allurl(url,headers)