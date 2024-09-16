"""
扮演UDP访问的客户端
"""
import socket  # 导包

# 创建一个套接字,用来接收和发送数据
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 定位服务器的ip和端口号
addr = ('127.0.0.1', 8083)  # 这里的端口，ip一定要与服务器的保持一致

# 输入要发送的数据
data = input("请输入你想要发送的数据:")

# 调用套接字的sendto方法发送， 并传入服务器的ip和端口
# ！！！别忘记编码
client_socket.sendto(data.encode('utf-8'), addr)

# 发送后关闭套接字
client_socket.close()