# -*- coding:utf-8 -*-
import re
import requests
# 百度贴吧数据获取
#要获取的数据 标题 发贴时间 作者
resp = requests.get('http://tieba.baidu.com/f?kw=%E5%B0%8F%E8%AF%B4%E5%90%A7&pn=4').text
# print(resp.text)
#P匹配出每一个帖子的url
article_urls = re.findall(r'<a rel="noreferrer" href="(/p/\d+)"',resp,re.S)
# print(article_urls)#查看
#URL拼接
# 运行一次后整体
# article_urls = ['http://tieba.baidu.com'+ url for url in article_urls] #第一种方法：利用列表推导式
# print(article_urls)
# #对帖子的详情页发起请求
# article_resp = requests.get(article_urls[0]).text
# # print(article_resp)
# #解析出想要的具体的数据
#
# title = re.findall(r'<title>(.*?)【小说吧吧】_百度贴吧</title><',article_resp,re.S)[0]
# print('名字：',title)
# author = re.findall(r'author:"(.*?)"',article_resp,re.S)[0]
# print('作者:',author)
# create_time = re.findall(r'quot;(\d+-\d+-\d+ \d+:\d+)&quot',article_resp,re.S)[0]
# print('时间:',create_time)

article_urls = ['http://tieba.baidu.com'+ url for url in article_urls] #第一种方法：利用列表推导式
print(article_urls)
#对帖子的详情页发起请求

for  url in article_urls:

    article_resp = requests.get(url).text
    # print(article_resp)
    #解析出想要的具体的数据

    title = re.findall(r'<title>(.*?)【小说吧吧】_百度贴吧</title><',article_resp,re.S)[0]
    print('第{}个帖子：'.format(article_urls.index(url)+1))

    print('名字：',title)
    author = re.findall(r'author:"(.*?)"',article_resp,re.S)[0]
    print('作者:',author)
    create_time = re.findall(r'quot;(\d+-\d+-\d+ \d+:\d+)&quot',article_resp,re.S)[0]
    print('时间:',create_time)
    print('===================')




