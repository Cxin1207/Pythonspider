import urllib.request
# urlopen 发起请求
# req = urllib.request.urlopen('http://www.baidu.com')
# req = urllib.request.urlopen('http://httpbin.org/post',data=b'username=CX')# 当data不传值，默认，get请求，传值后，为post请求
# req = urllib.request.urlopen('http://httpbin.org/post',data='username=中文'.encode(),timeout=2)# 当data不传值，默认，get请求，传值后为post请求; timeout请求超时
# print(req.read().decode())

# print(req) #这个个对象
# print(dir(req))#查看源代码
# print(req.read().decode())#查看源代码
# print(req.info())#头信息
#做测试的网站 httpbin.org/get


##================================================================================================
#Request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

req = urllib.request.Request('https://www.jianshu.com',headers=headers)# Request是类，headers是字典
r = urllib.request.urlopen(req)
print(r.read().decode())