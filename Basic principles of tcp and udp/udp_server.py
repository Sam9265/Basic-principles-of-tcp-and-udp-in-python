"""
扮演UDP访问的服务端
"""

import socket

# 创建一个套接字,用来接收和发送数据
service_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 定位服务器自身的ip和端口号
local_addr = ('127.0.0.1', 8083)

# 调用套接字的bind()方法,将端口和ip绑定到套接字本身
service_socket.bind(local_addr)

# 开始循环等待客户端数据的发送
while True:
    print("等待客户端的连接......")
    # 捕获异常
    try:
        # 调用套接字的方法recvfrom()来接收客户端，并返回(客户端发送的数据, 客户端的地址)的一个元组
        # recvfrom()中的参数为接收的最大字节数，多余则丢弃
        client_data, client_addr = service_socket.recvfrom(1024)
        # !!!别忘了解码!!!
        print("客户端数据：", client_data.decode('utf-8'))
        print("客户端的地址：", client_addr)
    except Exception as e:
        print(e)
        # 如果出现异常就会中断监听，并退出
        break

service_socket.close()
