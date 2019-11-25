import socket


def send_msg(udp_socket):
    """发送消息
    :param udp_socket: 通过套接字调用sendto方法
    """
    # 获取要发送的内容
    dest_ip = input("请输入对方的IP地址：")
    dest_port = int(input("请输入对方的Port："))
    send_data = input("请输入你要发送的信息：")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收消息并显示"""
    # 接收数据并显示
    recv_data = udp_socket.recvfrom(1024)
    print("%s：%s" % (str(recv_data[1]), recv_data[0].decode("GBK")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("", 7788))

    # while循环来处理事情
    while True:

        op = input("========聊天工具=======\n"
                   "请输入功能：\n"
                   "1-发送消息\n"
                   "2-接收消息\n"
                   "0-退出系统\n")

        if op == "1":
            # 发送信息数据
            send_msg(udp_socket)
        elif op == "2":
            # 接收信息数据并显示
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误，请核对后再次输入。")


if __name__ == "__main__":
    main()
