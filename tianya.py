# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:05:54 2018

@author: zdz
"""
'''
http://bbs.tianya.cn/post-funinfo-7650448-2.shtml
'''
print("爬虫开始")
from urllib import request  
from bs4 import BeautifulSoup   #Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库  
ye =1033  
while ye<1132:    
    ye = ye+1
    url="http://bbs.tianya.cn/post-free-2076777-"+str(ye)+"-1.shtml"  
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
    page = request.Request(url,headers=headers)  
    page_info = request.urlopen(page).read().decode('utf-8')#打开Url,获取HttpResponse返回对象并读取其ResposneBody  
    # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器  
    soup = BeautifulSoup(page_info, 'html.parser')
    titles = soup.find_all('div', class_='bbs-content')
    unames = soup.find_all('div',class_='atl-info' )
#    for uname in unames:
#                print (uname.get_text("|", strip=True)+'\n')
    a=0
    with open(r"D:\pythonproject\spider1\yrqsl2.txt","a",encoding="utf-8") as file: 
        if ye ==1:#由于第一页的排版和后面的不一样，需要单独抓内容
            while a<len(titles):
                if (unames[a].get_text(strip=True).find ("楼主"))==0:#判断是否是楼主的发言，find匹配字符串，找不到返回0，找到返回字符串的位置
                    file.write(unames[a].get_text(" ", strip=True)+'\n')
                    file.write(titles[a].get_text('\n', strip=True)+'\n'+'\n')            
                    a=a+1
                else:
                    a=a+1
            print(ye)#内容写完返回当前页码    
        else:#如果不是第一页，就执行以下代码
            while a<len(titles):
                if (unames[a+1].get_text(strip=True).find ("楼主"))==0:#判断是否是楼主的发言，find匹配字符串，找不到返回0，找到对应返回字符串的位置
                    file.write(unames[a+1].get_text(" ", strip=True)+'\n')
                    file.write(titles[a].get_text('\n', strip=True)+'\n'+'\n')            
                    a=a+1
                else:
                    a=a+1
            print(ye)#内容写完返回当前页码 
print("爬虫结束")

          


