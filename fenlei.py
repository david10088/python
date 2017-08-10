# -*-coding:UTF-8-*-
# This Python file uses the following encoding: utf-8
import os
import glob
import shutil
path= r'/home/liang/Pictures/mzitu'
filelist=os.listdir(path)

def a():#创建文件夹
    
    for files in filelist:#遍历所有文件
        #print files
        Olddir=os.path.join(path,files)#匹配路径和文件名
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue
        filename=os.path.splitext(files)[0]#将文件名和后缀名分离
        
        if(filename[-4:-3] == '（'):
            filename_key = filename[:-4]# 截取文件名中的关键字符串
        elif(filename[-1:] == '）'):
            filename_key = filename[:-3]
        else:
            filename_key = filename# 截取文件名中的关键字符串
        #print(filename_key)
        newfiledir=path+'/'+filename_key#确定新的文件路径，此处根据关键词创建新的文件夹
        isexist=os.path.exists(newfiledir)# 判断文件夹是否存在
        if not isexist : # 如果不存在则创建文件路径
            os.mkdir(newfiledir)
        oldfiles = path +'/'+ files
        shutil.move(oldfiles,newfiledir)# 移动文件

a()