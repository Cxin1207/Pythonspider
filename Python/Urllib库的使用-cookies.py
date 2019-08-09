
##==================================================================================
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

##==================================================================================

#第二种方法  将cookie保存文本  很少用，没必要保存成文本

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

