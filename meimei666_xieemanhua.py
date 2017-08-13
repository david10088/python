 # -*-coding:UTF-8-*-
import urllib
import urllib2
import os
import random 
import multiprocessing
from lxml import etree
import time

def getHead():
    my_headers=["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)" ,
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',  
    'Opera/9.25 (Windows NT 5.1; U; en)',  
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',  
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',  
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',  
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',  
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",  
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ", 
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", 
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"     
    ] 
    return random.choice(my_headers)

def allurl():
    count1 = 1
    c = 1
    count1_max = 92
    while count1 < count1_max:
        print 'dijikun'+str(count1)
        if(count1 == 1):
            url = 'http://www.27270.com/game/cosplaymeitu/'
        else:
            url = 'http://www.27270.com/game/cosplaymeitu/list_20_' + str(count1) + '.html'
        headers = {'User-Agent': getHead()}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request,timeout=160).read()
        #cate = re.findall('<div class="lb">\[<a href="(.+?)" target="_blank">(.+?)</a>\]</div>', html) 
        #print response
        #return 0
        pattern = etree.HTML(response)
        s = set()
        link_list = pattern.xpath('//div[@class="pic_list_box w1200"]/ul/li/a/@href')
        # print link_list
        # c = 0
        for link in link_list:
            #girlurl(link,headers)
            if((link != '/sitemap.html') and (link != 'http://www.miibeian.gov.cn')):
                s.add(link)
        # print s
        # return 0

        for link in s:
            print 'dijirenrenrenren' + str(c)
            
            sum1 = 0
            link1 =  link
            #print link1
            girlurl(link1,headers,c)
            c =c + 1
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

def girlurl(url,headers,sum12):
    count = 0
    sum1 = 0
    caocao = 1
    headers = {'User-Agent': getHead()}
    while caocao:
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
        dirName = pattern.xpath('//div[@class="warp oh"]/h1/text()')
        #print dirName
        for ccc in dirName:
            DIRNAME = ccc.encode('utf-8')
        #print DIRNAME
        #print type(DIRNAME)
        title = DIRNAME.strip()#名称
        path= r'/home/liang/Pictures/meimei666/cosplay'
        newfiledir=path+'/'+str(sum12)#确定新的文件路径，此处根据关键词创建新的文件夹
            #print newfiledir
        isexist=os.path.exists(newfiledir)# 判断文件夹是否存在
        if not isexist : # 如果不存在则创建文件路径
            os.mkdir(newfiledir)
            file_object = open(newfiledir + '/title.txt', 'a')
            file_object.write(title)
            file_object.close( )
        #pattern = etree.HTML(response)
        #link1 = pattern.xpath('//div[@class="bigpic column_1_arc"]/a/@href')
        link_list = pattern.xpath('//div[@class="articleV4Body"]/p/a/img/@src')
        #print link_list
        next1 = pattern.xpath('//div[@class="warp oh"]/h1/text()')
        if(next1 == []):
            caocao = 0
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
            saveimg(newfiledir,link,headers,sum1)

        #for link in link_list:
        #    print link
    #print sum1
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
    #print dir
    headers = {'User-Agent': getHead()}
    i =1
    c = 0
    while i:
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request ,timeout=180).read()
            #print url[-9:]
            #DIR = '/改成自己的目录/' + dir + url[-9]
            #print type(imgname)
            
            with open(imgname+ '/' + str(sum1)+'.jpg','wb') as f:
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