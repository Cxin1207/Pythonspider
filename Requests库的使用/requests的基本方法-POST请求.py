import requests
data = {'username':'wangxian'}
r = requests.post(url='http://httpbin.org/post',data=data)
# print(type(r.text))#是字符串类型
# print(r.text)

# print(type(r.json()))#打印的数据是一样的数据，但是是字典类型
# print(r.json())
