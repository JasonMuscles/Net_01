import socket


def main():
    # 1.买个手机（创建套接字 socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息 bind）

    tcp_server_socket.bind(("", 7788))

    # 3.手机设置为正常接听状态 （让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    # 4.等待别人的电话到来（等待客户端的链接 accept）
    new_client_socket, client_addr = tcp_server_socket.accept()

    print(client_addr)

    # 接收客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data.decode("gbk"))

    new_client_socket.send("哈哈哈".encode("gbk"))

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
