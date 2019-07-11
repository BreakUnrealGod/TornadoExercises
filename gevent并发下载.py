import os

import gevent
import urllib.request
from gevent import monkey

from settings import BASE_DIR

monkey.patch_all()  # 猴子补丁  将标准库中涉及的IO切换成gevent的


def download(url, filename):
    print("GET %s" % url)

    response = urllib.request.urlopen(url)  # 获取响应对象

    data = response.read()  # 读取响应对象的中数据

    with open(os.path.join(BASE_DIR,'download',filename), 'wb') as fw:
        fw.write(data)

    print("下载了 %d bytes from %s" % (len(data), url))


def main():
    g1 = gevent.spawn(download, "http://www.baidu.com", 'baidu.txt')
    g2 = gevent.spawn(download, "http://www.qq.com", 'qq.txt')
    g3 = gevent.spawn(download, "http://www.163.com", '163.txt')

    gevent.joinall([g1, g2, g3])


if __name__ == "__main__":
    main()
