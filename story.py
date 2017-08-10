#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding='utf-8'
        return r.text
    except:
        return 'error!'

def get_content(url):

    url_list = []
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')

    category_list = soup.find_all('div',class_='index_toplist mright mbottom')
    history_list = soup.find_all('div',class_='index_toplist mbottom')

    for cate in category_list:
        name = cate.find('div',class_='toptab').span.text
        with open('novel_list.csv','a+') as f:
            f.write('\n小说种类：{} \n'.format(name))

        book_list = cate.find('div',class_='topbooks').find_all('li')

        # 循环遍历出每一个小说的的名字，以及链接
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            url_list.append(link)

            # 这里使用a模式写入，防止清空文件
            with open('novel_list.csv','a') as f:
                f.write('小说名:{} \t 小说地址:{} \n'.format(title,link))

    for cate in history_list:
        name = cate.find('div',class_='toptab').span.text
        with open('novel_list.csv','a') as f:
            f.write('\n小说种类: {} \n'.format(name))

        book_list = cate.find('div',class_='topbooks').find_all('li')

        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            url_list.append(link)

            with open('novel_list.csv','a') as f:
                f.write('小说名:{} \t 小说地址:{} \n'.format(title,link))

    return url_list


 # 获取单本小说的所有章节链接
def get_txt_url(url):

    url_list = []
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    list_a = soup.find_all('dd')
    txt_name = soup.find('dt').text

    with open('C:/Users/Administrator/Desktop/小说/{}.txt'.format(txt_name),'a+') as f:
        f.write('小说标题：{} \n'.format(txt_name))

    for url in list_a:
        url_list.append('http://www.qu.la/' + url.a['href'])

    return url_list,txt_name


def get_one_txt(url,txt_name):

    html = get_html(url).replace('<br/>','\n')
    soup = BeautifulSoup(html,'lxml')
    try:
        txt = soup.find('div',id='content').text
        title = soup.find('h1').text

        with open('C:/Users/Administrator/Desktop/小说/{}.txt'.format(txt.name),'a') as f:
            f.write(title + '\n\n')
            f.write(txt)
            print('当前小说：{}当前章节{}已经下载完毕'.format(txt_name,title))
    except:
        print('ERROR!')



def get_all_txt(url_list):
    
    for url in url_list:
        # 遍历获取当前小说的所有章节的目录，并且生成小说头文件

        page_list,txt_name = get_txt_url(url)

def main():
    # 小说排行榜地址
    base_url = 'http://www.qu.la/paihangbang/'
    # 获取排行榜中所有小说的url链接
    url_list = get_content(base_url)
    # 除去重复的小说
    url_list = list(set(url_list))
    get_all_txt(url_list)

if __name__ == '__main__':
    main()