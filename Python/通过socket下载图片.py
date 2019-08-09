#通过socket下载图片
import socket
import re

img_url = 'http://i1.hdslb.com/bfs/archive/aef0c150abfe7b634757300b4e7f2cceca8b3379.jpg'
client = socket.socket()
client.connect(('i1.hdslb.com',80))

# 构造HTTP报文
request = b'GET /bfs/archive/aef0c150abfe7b634757300b4e7f2cceca8b3379.jpg HTTP/1.0\r\nHost: i1.hdslb.com\r\n\r\n'

#发送HTTP请求
client.send(request)
res = b''

#接受第一个1024的数据
data = client.recv(1024)
while data:
    res = res + data
    data = client.recv(1024)
print(re.findall(b'\r\n\r\n(.*)',res,re.S)[0])#.表示匹配任意字符，*表示是匹配任意次，无限次 re.S表示匹配换行符和制表格
with open('index.jpg','wb') as f: #wb写入二进制
    f.write(re.findall(b'\r\n\r\n(.*)',res,re.S)[0])
print(res)

