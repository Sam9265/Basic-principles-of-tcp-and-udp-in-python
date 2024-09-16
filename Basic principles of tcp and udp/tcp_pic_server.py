"""
扮演TCP访问的服务端,相应客户端并发送照片
"""
# 导包
import os
import socket

# 创建一个套接字,用来接收和发送数据!!! TCP协议的套接字的第二个参数要变SOCK_DGRAM >> SOCK_STREAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定位服务器的ip和端口号
addr = ('127.0.0.1', 8084)  # 这里的端口，ip一定要与服务器的保持一致

# 将IP和端口绑定到套接字上
server_socket.bind(addr)

# 开启监听模式，这里的128为当前服务器最大的请求等待数
server_socket.listen(128)

print("等待客户端的连接.....")
# 循环接收数据
while True:
    try:
        # 接收客户端的套接字和IP地址
        client_socket, client_addr = server_socket.accept()
        print("客户端的地址：", client_addr)
        # 从客户端套接字中获取的文件名
        file_name = client_socket.recv(1024).decode('utf-8')
        # 判断是否文件存在
        if os.path.exists('./tcp_pic/' + file_name):
            # 二进制图片用'rb'打开
            with open('./tcp_pic/' + file_name, 'rb') as f:
                while True:
                    data_read = f.read(1024)
                    # !!!将数据发送给客户端的套接字!!!
                    client_socket.send(data_read)
                    if not data_read:
                        print("传输完毕！")
                        break
        else:
            print("文件并不存在！")
            break
    except Exception as e:
        print(e)
        break

    client_socket.close()

server_socket.close()