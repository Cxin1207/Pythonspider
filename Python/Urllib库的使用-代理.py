import urllib.request
proxy = {
    'http':'117.90.0.68:9000',
    'https':'117.90.0.68:9000',  #免费代理网站：快代理，西祠

}## 代理的格式  {'http':'ip地址:端口号','https':'ip地址:端口号'}https是因为有的网站是https
# 创建一个代理处理器
proxies = urllib.request.ProxyHandler(proxy)

#创建open对象
opener = urllib.request.build_opener(proxies,urllib.request.HTTPHandler)
req = opener.open('http://httpbin.org/ip')
print(req.read().decode())