import urllib3
#与urllib区别，不需要加括号，是属性，urllib是方法需要加括号
# 实例一个PoolManager对象
# http = urllib3.PoolManager()
# req = http.request('GET','http://www.baidu.com') #http.request('GET','网址',headers={})GET可以换POST.headers可以直接传
# print(req.data)#网页源代码
# print(req.status)#状态码
# print(req.headers)

# req = http.request('POST','http://httpbin.org/post',fields={'username':'wangxian'}) #fields 相当于urllib中的data参数
# print(req.data)
#使用代理
# http = urllib3.ProxyManager('http://58.22.210.91:80')#加代理'http://175.44.153.152:80'
# req = http.request('GET','http://httpbin.org/ip') #fields 相当于urllib中的data参数
# print(req.data)
import json
http = urllib3.PoolManager()
data = {'key':'value'}
# print(type(json.dumps(data)))  #将字典转成字符串类型
# print(json.dumps(data))
req = http.request('POST','http://httpbin.org/post',body=json.dumps(data).encode(), headers={'Content-Type':'application/json'}) #添加json 相当于urllib中的data参数
print(req.data)