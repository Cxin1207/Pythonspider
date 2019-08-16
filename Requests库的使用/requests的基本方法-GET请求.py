# 请求  GET POST  PUT head
import requests
# requests.get(url, params=None, **kwargs)
# requests.post()
# requests.put()
# 1  requests.get('http://www.baidu.com/s?wd=python')# 第一种方式
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
#第二种方式
#params = {'wd':'python'}
#requests.get('http://www.baidu.com/s?',params=params,headers=headers)# 第二种方式

r = requests.get('http://www.jianshu.com',headers=headers)# 第二种方式
# print(r.text)#z获取相应方式 text 返回的是文本内容

#返回二进制
# print(r.content)#一般获取图片最常用的方法

#编码不一样的话，容易出现乱码 例如下面
r = requests.get('http://www.baidu.com',headers=headers)# 第二种方式
# print(r.text)
#产生乱码的原因，编码不同，首先查看编码，查看网页源代码
#手动设置编码
# print(r.encoding)#查看默认编码
r.encoding = 'utf-8'
print(r.text)

