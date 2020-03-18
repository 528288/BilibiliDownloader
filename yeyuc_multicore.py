import multiprocessing as mp

from yeyuc_downloader import YouGet


class MultiCore:
    def __init__(self, path):
        self.yg = YouGet(path)

    def job(self, urls):
        for url in urls:
            self.yg.download(url)

    def process(self, param=[], **kwargs):
        """
        :param param:
            self.job()函数的参数配置
        :param kwargs:
            processes: int, 核数，默认全部
        :return: 计算结果，list
        """
        pool = mp.Pool(processes=kwargs.get("processes"))  # 构建进程池
        pool.map(self.job, param)

    def split_list(self, ls, n):
        """
        将列表分成若干个个小列表
        :param ls: init list/numpy list
        :param n: split num
        :return: n small lists
        """
        if n > len(ls):
            print('分片数大于列表长度！')
        else:
            return [ls[i:i + n] for i in range(0, len(ls), n)]


if __name__ == "__main__":
    path = r"你想要的下载位置"
    urls = ["https://www.bilibili.com/video/av18156598?p=" + str(_) for _ in range(1, 107)]  # 目标视频urls列表

    mc = MultiCore()
    data = mc.split_list(urls, 8)  # 将urls分成8份
    mc.process(param=data)
