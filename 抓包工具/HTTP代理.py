import re
import socket
server = socket.socket()
#服务端
server.bind(('0.0.0.0',8181))
server.listen(5)#监听
#客户端
client = socket.socket()

while True:
    conn, addr = server.accept()#等待接受连接  addr客户端地址
    data = conn.recv(1024)#接受数据
    print(data)
    # 将接受的数据转发出去
    url = re.findall(rb'Host: (.*?)\r',data)[0]
    client.connect((url,80))
    client.send(data)#数据发出去
    while True:
        res = client.recv(1024)
        if res:
            conn.send(res)
        else:
            break


