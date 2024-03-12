import socket

def main():
    # 创建一个客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接服务器
    server_address = ('localhost', 6666)  # 使用localhost表示连接到本机
    client_socket.connect(server_address)
    
    # 向服务器发送信息
    message = input("输入你要发送的信息")
    client_socket.sendall(message.encode())
    
    # 接收服务器的响应
    response = client_socket.recv(1024)
    print('服务器响应：', response.decode())
    
    # 关闭客户端套接字
    client_socket.close()

if __name__ == '__main__':
    main()