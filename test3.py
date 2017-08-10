
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Liang'

import urllib.request
import numpy as np
import time
import matplotlib.pyplot as plt
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei']   #有效的方法
 
# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='123456', database='db_pms')
cursor = conn.cursor()

sql = "SELECT id, user_id, paymoney, created FROM `pms_order` WHERE status = 20 AND user_id != 24610 AND user_id != 37 AND created BETWEEN 1493568000 AND 1501516800"

   # 执行SQL语句
cursor.execute(sql)
values = cursor.fetchall()

count1 = [0,0,0,0,0,0,0]

for row in values:
	day = int(time.strftime('%w',time.localtime(row[3])))
	if(day == 1):
		count1[0] += 1
	elif(day == 2):
		count1[1] += 1
	elif(day == 3):
		count1[2] += 1
	elif(day == 4):
		count1[3] += 1
	elif(day == 5):
		count1[4] += 1
	elif(day == 6):
		count1[5] += 1
	elif(day == 0):
		count1[6] += 1







labels = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
x = range(len(labels))
y = count1
zhfont = mpl.font_manager.FontProperties(fname='/usr/share/fonts/msyh/msyh.ttf')
# plt.xlabel('周几',fontproperties=zhfont)
# plt.ylabel('订单数',fontproperties=zhfont)
plt.title('图像的标题',fontproperties=zhfont)
plt.plot(x, y, 'ro-')
plt.xticks(x, labels,fontproperties=zhfont)

# plt.show()     #生成并显示整个图像

plt.bar(range(len(count1)), count1, tick_label=labels)
plt.show()