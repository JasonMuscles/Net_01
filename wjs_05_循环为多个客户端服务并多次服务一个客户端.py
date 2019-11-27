import socket


def main():
    # 1.买个手机（创建套接字 socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入手机卡（绑定本地信息 bind）

    tcp_server_socket.bind(("", 7788))

    # 3.手机设置为正常接听状态 （让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    while True:
        """为多个不同新客户端服务"""

        print("等待一个新客户端接入")
        # 4.等待别人的电话到来（等待客户端的链接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("一个新客户端已接入%s" % str(client_addr))

        while True:
            """为同一个客户端进行多次服务"""
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)

            # 如果recv解堵塞，那么有两种方式
            # 1.客户端发送过来数据
            # 2.客户端调用close导致了，这里的recv解堵塞

            if recv_data:

                # 显示客户端发送的信息
                print("客户端过来的请求是：%s" % recv_data.decode("gbk"))
                # 回复一部分信息给客户端
                new_client_socket.send("哈哈哈婆婆".encode("gbk"))
            else:
                break

        # 关闭套接字
        new_client_socket.close()
        print("已完成这个客户端的服务")

    # 持续监听套接字，不能关闭，如果关闭XXX.accept不能再次接受新新客户端
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
