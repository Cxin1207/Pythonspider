## 模拟请求百度首页
import socket
#创建客户端
client = socket.socket()
#连接百度服务端
client.connect(('www.baidu.com',80))
#构造HTTP请求报文
# request = b'GET / HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'#注意空格，否则会失败

request = b'GET /s?wd=python HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'#注意空格，否则会失败  请求百度搜索python


#发送请求
client.send(request)
#接受服务端返回的数据
res = b''
data = client.recv(1024)

while data:
    res = res + data
    data = client.recv(1024)

print(res.decode())
