import gevent
from gevent import monkey, socket

monkey.patch_all()


def do_service(new_socket):
    while True:
        content = new_socket.recv(1024)
        if len(content) == 0:
            print("下线啦")
            break
        print("接收到:%s" % content.decode("utf-8"))


def main():
    server_socket = socket.socket()  # 使用的是gevent中的socket
    server_socket.bind(("", 8989))
    server_socket.listen(5)

    while True:
        new_socket, new_addr = server_socket.accept()
        # 创建一个协程
        g1 = gevent.spawn(do_service, new_socket)


if __name__ == "__main__":
    main()
