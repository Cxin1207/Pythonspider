import socket
server = socket.socket()
# 绑定ip地址和端口
server.bind(('',8888))
#开始监听
server.listen(5) #同一时间最多接受五个请求

# 和客户端建立连接
conn,addr = server.accept()  #返回的是一个元祖

#接受信息
data = conn.recv(1024)  #一次最多只能接受1024字节
print(data)





