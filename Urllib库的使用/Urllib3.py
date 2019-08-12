import urllib3
#与urllib区别，不需要加括号，是属性，urllib是方法需要加括号
# 实例一个PoolManager对象
http = urllib3.PoolManager()
req = http.request('GET','http://www.baidu.com') #http.request('GET','网址',headers={})GET可以换POST.headers可以直接传
print(req.data)#网页源代码
print(req.status)#状态码
print(req.headers)#urllib3的使用，五分四十二秒