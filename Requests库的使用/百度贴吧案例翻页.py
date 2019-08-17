# -*- coding:utf-8 -*-
import re
import requests
# 百度贴吧数据获取
#要获取的数据 标题 发贴时间 作者
key = input('请输入要获取的贴吧：')
page = input('请输入要获取的页数:')
for pn in range(int(page)):
    resp = requests.get('http://tieba.baidu.com/f?kw={}&pn={}'.format(key,pn*50)).text
    # print(resp.text)
    #P匹配出每一个帖子的url
    article_urls = re.findall(r'<a rel="noreferrer" href="(/p/\d+)"',resp,re.S)
    # print(article_urls)#查看
    #URL拼接
    article_urls = ['http://tieba.baidu.com'+ url for url in article_urls] #第一种方法：利用列表推导式
    print(article_urls)
    #对帖子的详情页发起请求

    for  url in article_urls:

        article_resp = requests.get(url).text
        # print(article_resp)
        #解析出想要的具体的数据

        # title = re.findall(r'<title>(.*?).*?_百度贴吧</title><',article_resp,re.S)[0]
        try:
            title = re.findall(r"'threadTitle': '(.*?)'",article_resp,re.S)[0]
        except IndexError as e:
            title = '数据异常'
        print('第{}页，第{}个帖子：'.format(pn,article_urls.index(url)+1))

        print('名字：',title)
        #异常处理
        try:
            author = re.findall(r'author:"(.*?)"',article_resp,re.S)[0]
        except IndexError as e:
            author = '数据异常'
        print('作者:',author)
        try:
            create_time = re.findall(r'quot;(\d+-\d+-\d+ \d+:\d+)&quot',article_resp,re.S)#后面不加[0],因为如果加了[0],没有匹配不到，那么就不会往下进行匹配了
            if not create_time:
                print('第二次匹配时间：')
                create_time = re.findall(r'<span class="now_date">(.*?)</span>',article_resp,re.S)
        except IndexError as e:
            create_time = '数据异常'
        print('时间:',create_time[0])
        print('===================')




