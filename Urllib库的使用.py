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

##================================================================================================


##==================================================================================
#Cookie使用
#第一种方法
# import urllib.request
# from http import cookiejar
# #创建一个cookie对象
# cookie = cookiejar.CookieJar()
# #创建一个cookie处理器
# cookies = urllib.request.HTTPCookieProcessor(cookie)
# # 创建一个opener对象
# opener = urllib.request.build_opener((cookies))
#
# res = opener.open('http://www.baidu.com')
#
# print(cookies.cookiejar)



# 第二种方法  将cookie保存文本  很少用，没必要保存成文本
#
# import urllib.request
# from http import cookiejar
# filename = 'cookie.txt'
# #创建一个cookie对象
# cookie = cookiejar.MozillaCookieJar(filename)
# #创建一个cookie处理器
# cookies = urllib.request.HTTPCookieProcessor(cookie)
# # 创建一个opener对象
# opener = urllib.request.build_opener((cookies))
#
# res = opener.open('http://www.baidu.com')
#
# print(cookies.cookiejar)
##==================================================================================
##==================================================================================
#代理
