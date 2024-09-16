"""
扮演TCP访问的客户端，请求服务端的照片数据
"""
import socket  # 导包

# 创建一个套接字,用来接收和发送数据!!! TCP协议的套接字的第二个参数要变SOCK_DGRAM >> SOCK_STREAM
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定位服务器的ip和端口号
addr = ('127.0.0.1', 8084)  # 这里的端口，ip一定要与服务器的保持一致

# 尝试来连接服务端，并捕获异常
try:
    client_socket.connect(addr)
except Exception as e:
    print(e)
    print("连接失败！请重新尝试！")

# 输入要发送的数据
data = input("请输入需要文件名:")

# 向服务端发送请求数据,别忘了编码！！！
client_socket.send(data.encode('utf-8'))
# 提前打开要存放文件的相对位置
with open('./client/'+data, 'wb') as f:
    # 服务端传来的数据是一段一段的，要循环接收
    while True:
        # 接收服务端传来的二进制图片数据
        pic_data = client_socket.recv(1024)
        # 定义一个判断，没数据的时候逃离循环
        if pic_data:
            f.write(pic_data)
        else:
            break

# 断开连接
client_socket.close()