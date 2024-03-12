import socket

def main():
    # 创建一个服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定监听地址
    server_address = ('', 6666)  # 使用空字符串表示绑定本机所有网络接口
    server_socket.bind(server_address)
    
    # 监听端口
    server_socket.listen(5)
    print('服务器已启动，监听端口 6666...')
    
    while True:
        # 等待客户端连接
        print('等待客户端连接...')
        client_socket, client_address = server_socket.accept()
        print('客户端已连接，地址：', client_address)
        
        # 向客户端发送欢迎信息
        message = "欢迎连接到服务器！"
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print('服务器响应：', response.decode())
        
        # 关闭客户端套接字
        client_socket.close()

if __name__ == '__main__':
    main()