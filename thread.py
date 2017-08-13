#!/usr/bin/env python
# -*-coding:UTF-8-*-
import urllib
import urllib2
import os
from lxml import etree
import time
import multiprocessing
import random 
global sum1
global sum2
sum1 = 0
sum2 = 0
# url  = 'https://www.uumnt.com/mote/zhaoyitong.html'
# headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Referer': 'http://www.mzitu.com'}
# request = urllib2.Request(url,headers = headers)
# response = urllib2.urlopen(request,timeout=60).read()
# print response
# url  = 'https://www.uumnt.com/mote/yumiyoumei.html'
# headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Referer': 'http://www.mzitu.com'}
# request = urllib2.Request(url,headers = headers)
# response = urllib2.urlopen(request,timeout=60).read()
# print response
# url  = 'https://www.uumnt.com/mote/liuyouqi.html'
# headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Referer': 'http://www.mzitu.com'}
# request = urllib2.Request(url,headers = headers)
# response = urllib2.urlopen(request,timeout=60).read()
# print response



def start(url, headers,path):
	count1 = 1
	sum_meinv = 0
	count1_max = 38
	
	s = set()
	while count1 < count1_max:
		print count1
		print count1
		print count1
		print count1
		if(count1 == 1):
			url = url
		elif(count1 < 11):
			url = url[:-6] + str(count1) + '.html'
		else:
			url = url[:-7] + str(count1) + '.html'
		#print url
		try:
			request = urllib2.Request(url, headers=headers)
			response = urllib2.urlopen(request,timeout=60).read()
		except:
			return 0
        #cate = re.findall('<div class="lb">\[<a href="(.+?)" target="_blank">(.+?)</a>\]</div>', html) 
		#print response
        # return 0
		pattern = etree.HTML(response)
        
		link_list = pattern.xpath('//div[@class="mote-warp mt14 mote-list"]/ul/li/div/a/@href')
        # print link_list
        # c = 0
		for link in link_list:
            #girlurl(link,headers)
			if((link != '/sitemap.html') and (link != 'http://www.miibeian.gov.cn')):
				s.add(link)
            #break
		count1 = count1 + 1
		#print s
		for link in s:
			sum_meinv +=1
			link1 = 'https://www.uumnt.com' + link
			#print link1
			step1(link1, headers,path,sum_meinv)

        #SSSStime.sleep(1)

        #print url
        #c = c +1
        #link = link
    #     girlurl(link,headers)
    #print count1
    # a = 0
    # for link in s:
    #     a = a + 1
    # print a
    #return 0
    
	

def step1(url, headers,path,sum_meinv):
	#return 0
	count = 1
	sum_meinv_c = 0
	while 1:
		if(count == 1):
			url1 = url
		else:
			url1 = url[:-5]+'/'+str(count)+'.html'
		print url1
		try:
			request = urllib2.Request(url1,headers = headers)
			response = urllib2.urlopen(request,timeout=60).read()
		except:
			break 
		if(response == '2'):
			break
		count = count + 1
		pattern = etree.HTML(response)
		name = pattern.xpath('//meta[@name="description"]/@content')
		for ccc in name:
			DIRNAME = ccc.encode('utf-8')
		name = DIRNAME.strip()#名称

		newfiledir=path+'/'+str(sum_meinv) 	#确定新的文件路径，此处根据关键词创建新的文件夹
		isexist=os.path.exists(newfiledir)# 判断文件夹是否存在
		if not isexist:
			os.mkdir(newfiledir)
			s = str(sum_meinv) + '-' + name 
			file_object = open(path + '/title.txt', 'a')
			file_object.write(s +'\n')
			file_object.close( )
		link_list = pattern.xpath('//div[@class="warp mote-list-body clearfix"]/dl/dd/a/@href')
		pool = multiprocessing.Pool(processes = 3)
		for link in link_list:
			sum_meinv_c = sum_meinv_c + 1
			link = 'https://www.uumnt.com' + link
			pool.apply_async(step2, (link, headers,newfiledir,sum_meinv,sum_meinv_c, )) 
			#step2(link, headers,newfiledir,sum_meinv,sum_meinv_c)
		#print link_list
	#step2(url, headers,path)

def step2(url, headers,path,sum_meinv,sum_meinv_c):
	User = getHead()
	headers1 = {'User-Agent':User,
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		}
	try:
		request = urllib2.Request(url,headers = headers1)
		response = urllib2.urlopen(request,timeout=60).read()
	except:
		return 0
	pattern = etree.HTML(response)
	Name = pattern.xpath('//div[@class="warp clearfix mt14"]/div/h1/text()')
	#print response
	
	for ccc in Name:
		DIRNAME = ccc.encode('utf-8')
        #print DIRNAME
        #print type(DIRNAME)
	Name = DIRNAME.strip()#名称
	#print Name
	newfiledir=path+'/'+str(sum_meinv_c)#确定新的文件路径，此处根据关键词创建新的文件夹
	#print newfiledir
	isexist=os.path.exists(newfiledir)# 判断文件夹是否存在
	if not isexist : # 如果不存在则创建文件路径
		os.mkdir(newfiledir)
		
		s = str(sum_meinv_c) + '-' + Name 
		file_object = open(path + '/title.txt', 'a')
		file_object.write(s +'\n')
		file_object.close( )
	link1 = pattern.xpath('//div[@class="warp clearfix mt14"]/div/a/img/@src')
	for link in link1:
		step3(link, headers,newfiledir)

		


def step3(url, headers,path):

	i = 1
	c = 0
	while 1:
		User = getHead()
		headers = {'User-Agent':User,
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		}
		if(i<10):
			url1 = url[:-5]+ str(i)+'.jpg'
		else:
			url1 = url[:-6] + str(i) + '.jpg'
		#print i
		#print url1
		try:
			request = urllib2.Request(url1,headers = headers)
			response = urllib2.urlopen(request,timeout=60).read()
			
            #DIR = '/改成自己的目录/' + dir + url[-9]
            #print type(imgname)
            
			with open(path+ '/' + str(i)+'.jpg','wb') as f:
				f.write(response)
			i = i + 1
			print i
			
		except urllib2.URLError, e:
			if(c>10):
				break
			c = c + 1


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
#print randdom_header


path= r'/home/liang/Pictures/uumnt/mote'
url = 'https://www.uumnt.com/mote/1-0-0-0/1.html'
headers = {'User-Agent':getHead(),
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
start(url, headers,path)