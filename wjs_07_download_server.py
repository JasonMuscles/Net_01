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

    # 接受客户端发送过来需要下载的文件名称

    file_name = new_client_socket.recv(1024).decode("gbk")
    print("客户端:%s \n请求下载的文件名为：%s\n" % (str(client_addr), file_name))

    # 发送文件数据给客户端
    new_client_socket.send("服务器文件内容发送中...".encode("gbk"))

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
