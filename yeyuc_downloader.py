import os
import sys

import you_get


class YouGet():

    def __init__(self, path):
        self.path = path  # 存放视频文件的路径

    def rmfile(self, path):
        """
        删除文件
        :param path: 文件路径
        :return: None
        """
        try:
            os.remove(path)
        except Exception as e:
            print(e)

    def download(self, url):
        sys.argv = ['you-get', '-o', self.path, url]
        you_get.main()

        # 下载完成，删除xml文件
        for file in os.listdir(self.path):
            if file[-3:] == 'xml':
                self.rmfile(os.path.join(self.path, file))


if __name__ == "__main__":
    path = r"视频存放路径"
    urls = ["待下载的视频列表"]
    yg = YouGet(path)
    for url in urls:
        yg.download(url)
