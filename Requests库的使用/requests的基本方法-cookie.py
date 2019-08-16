import requests
import json
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
resp = requests.get(url='http://www.baidu.com',headers=headers)
# print(resp.headers)
# print(resp.cookies)查看coolie
cookies = {}
for items in resp.cookies.items():
    # print(items[0])
    cookies[items[0]] = items[1]
#
# print(cookies)
#利用json将cookie转成字符串，存到数据库，下次使用直接从数据库调用
# requests.get('http://www.jianshu.com',cookies={从另外文件中取出直接用})

### 代理
# proxy = {
#     'https':'http://112.114.124:50',
#     'http':'http://112.114.124:50',
# }
# print(requests.get('http://httpbin.org/ip',proxies=proxy))
## 重定向
r = requests.get('http://github.com',allow_redirects=False)#默认的是重定向，关闭后allow_redirects=False，显示301
print(r.status_code)
print(r.headers)

### ssl  解决verify = False 关闭证书验证
