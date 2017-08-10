 # -*-coding:UTF-8-*-
import urllib
import urllib2
import os
from lxml import etree
import time
def allurl():
    count1 = 1
    count1_max = 57
    while count1 < 57:
        print count1
        if(count1 == 1):
            url = 'https://www.yaoraotu.com/taotu/'
        else:
            url = 'https://www.yaoraotu.com/taotu/list_' + str(count1) + '.html'
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0','Referer': 'http://www.mzitu.com'}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request,timeout=60).read()
        #cate = re.findall('<div class="lb">\[<a href="(.+?)" target="_blank">(.+?)</a>\]</div>', html) 
        #print response
        pattern = etree.HTML(response)
        s = set()
        link_list = pattern.xpath('//a[@target="_blank"]/@href')
        # print link_list
        # c = 0
        for link in link_list:
            #girlurl(link,headers)
            if((link != '/sitemap.html') and (link != 'http://www.miibeian.gov.cn')):
                s.add(link)
        #print s
        for link in s:
            sum1 = 0
            girlurl(link,headers,sum1)
            #break
        count1 = count1 + 1
        #print url
        #c = c +1
        #link = link
    #     girlurl(link,headers)
    #print count1
    # a = 0
    # for link in s:
    #     a = a + 1
    # print a

def girlurl(url,headers,sum1):
    count = 1
    while 1:
        count = count +1
        if(count == 1):
            url1 = url
        else:
            url1 = url[:-5]+'_'+str(count)+'.html'
        try:
            request = urllib2.Request(url1,headers = headers)
            response = urllib2.urlopen(request,timeout=60).read()
        except urllib2.URLError, e:
            break
        #print response
        pattern = etree.HTML(response)
        dirName = pattern.xpath('//div[@class="titlepic"]/h1/text()')
        #print dirName
        for ccc in dirName:
            DIRNAME = ccc.encode('utf-8')
        #print DIRNAME
        #print type(DIRNAME)
        title = DIRNAME.strip()#名称

        #print title
        #pattern = etree.HTML(response)
        #link1 = pattern.xpath('//div[@class="bigpic column_1_arc"]/a/@href')
        link_list = pattern.xpath('//div[@class="bigpic column_1_arc"]/a/img/@src')
        #print link_list
        #print link1
        #print url
        for link in link_list:
            sum1 = sum1 + 1
            print sum1
            #time.sleep(1)
        #     #print num
        #     for Num in range(1,int(num)):
        #         Newurl = url +  '/' + str(Num)
        #         #print Newurl
            saveimg(str(title),link,headers,sum1)

        #for link in link_list:
        #    print link
    print sum1
# def lasturl(url,headers,title):
#     request = urllib2.Request(url,headers = headers)
#     response = urllib2.urlopen(request).read()
#     #print response
#     pattern = etree.HTML(response)
#     link_list = pattern.xpath('//div[@class="main-image"]/p/a/img/@src')
#     maintitle = pattern.xpath('//div[@class="content"]/h2/text()')
#     #print maintitle
#     for title in maintitle:
#         imgname = title.encode('utf-8')
#         #print imgname
#     #dirName = pattern.xpath('//head[1]/title/text()')
#     #print dirName.encode("UTF-8")
#     #for bbb in dirName:
#     #    print bbb.encode("UTF-8")
#     #print link_list
#     for link in link_list:
#         #pass
#         #print link
#         saveimg(imgname,link,headers)
def saveimg(imgname,url,headers,sum1):
    #dir = os.mkdir(imgname)
    if(imgname[-6:-5] == '('):
        title = imgname[:-6]
    else:
        title =  imgname[:-7]
    path= r'/home/liang/Pictures/yaorao'
    #print dir
    i =1
    c = 0
    while i:
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request ,timeout=180).read()
            #print url[-9:]
            #DIR = '/改成自己的目录/' + dir + url[-9]
            #print type(imgname)
            newfiledir=path+'/'+title#确定新的文件路径，此处根据关键词创建新的文件夹
            #print newfiledir
            isexist=os.path.exists(newfiledir)# 判断文件夹是否存在
            if not isexist : # 如果不存在则创建文件路径
                os.mkdir(newfiledir)
            with open(newfiledir+ '/' + title + str(sum1)+'.jpg','wb') as f:
                f.write(response)
            i = 0
        except urllib2.URLError, e:

            i = 1
            if(c>10):
                break
                print url
                print title
            c = c + 1

    


allurl()