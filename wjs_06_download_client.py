import socket


def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.获取服务器的IP、PORT
    dest_ip = input("请输入下载服务器的IP：")
    dest_port = int(input("请输入下载服务器的PROT："))

    # 3.链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4.获取下载的文件名称
    download_file_name = input("请输入下载的文件名：")

    # 5.将文件名发送到服务器
    tcp_socket.send(download_file_name.encode("gbk"))

    # 6.接受文件中的数据
    recv_data = tcp_socket.recv(1024)  # 1024->1K（1MB = 1014*1024；1GB = 1024*1024*1024）

    # 7.保存接受到的数据到一个文件中
    with open("新_" + download_file_name, "wb") as f:
        f.write(recv_data)

    # 8.关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
