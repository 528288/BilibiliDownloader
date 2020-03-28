import datetime
import itertools
import os
import time

import numpy as np
import pandas as pd


class Common():

    def mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def rmdir(self, path):
        """
        删除目录（允许非空）
        :param path: 目录路径
        :return: None
        """
        import shutil
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(e)

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

    def date_convert(self, value):
        """
        string, format -> new datetime parsed from a string (like time.strptime()).
        :param value: 带转换字符串
        :return: date
        注：仅支持"%Y-%m-%d"格式
        """
        try:
            # create_date = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            create_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
            return create_date
        except Exception as e:
            print(e)

    def get_md5(self, url):
        """
        将url转换成固定长度的字符串
        :param url:
        :return: 固定长度的字符串
        """
        import hashlib
        if isinstance(url, str):
            url = url.encode("utf-8")
        m = hashlib.md5()
        m.update(url)
        return m.hexdigest()

    def order_dict(self, data, index, **kwargs):
        """
        将字典按key/value排序
        :param data: 待排序的字典
        :param index: 0/1, 0: 按key，1：按value
        :param kwargs: reverse: bool, 是否降序, 默认False
        :return: dict
        """
        _ = sorted(data.items(), key=lambda x: x[index], reverse=kwargs.get('reverse', True))
        return {item[0]: item[1] for item in _}

    def normlize(self, x, index=0):
        """
        归一化
        :param x: list/numpy array
        :param index: 方法
        :return: numpy array
        """
        if index == 0:
            return (x - np.min(x)) / (np.max(x) - np.min(x))
        elif index == 1:
            return np.arctan(x) * 2 / np.pi
        else:
            return x / np.sum(x)

    def norm_dict(self, data, index=0):
        """
        将字典按value归一化
        :param data: 待归一化的字典
        :param index: 方法
        :return: dict
        """
        x = list(data)
        y = self.normlize(list(data.values()), index=index)
        return {i: j for (i, j) in zip(x, y)}

    def flatten(self, x, **kwargs):
        """
        a.flatten(order='C')

            Return a copy of the array collapsed into one dimension.

            Parameters
            ----------
            order : {'C', 'F', 'A', 'K'}, optional
                'C' means to flatten in row-major (C-style) order.
                'F' means to flatten in column-major (Fortran-
                style) order. 'A' means to flatten in column-major
                order if `a` is Fortran *contiguous* in memory,
                row-major order otherwise. 'K' means to flatten
                `a` in the order the elements occur in memory.
                The default is 'C'.

            Returns
            -------
            y : ndarray
                A copy of the input array, flattened to one dimension.

            See Also
            --------
            ravel : Return a flattened array.
            flat : A 1-D flat iterator over the array.

            Examples
            --------
            >>> a = np.array([[1,2], [3,4]])
            >>> a.flatten()
            array([1, 2, 3, 4])
            >>> a.flatten('F')
            array([1, 3, 2, 4])
        """
        return np.array(x).flatten(kwargs.get('order', 'C'))

    def cumsum(self, x, **kwargs):
        """
        累计和
        :param x: list/numpy array
        :param kwargs: axis: None; 0/1
        :return: numpy array
        """
        return np.cumsum(x, axis=kwargs.get('axis'))

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

    def list2str(self, ls, seq=''):
        """
        将列表元素拼接成字符串
        :param ls: list/numpy
        :param seq: 拼接符，默认无
        :return: str
        """
        return seq.join([str(i) for i in ls])

    def combinations(self, ls, r, **kwargs):
        """
        combinations(iterable, r) --> combinations object
        Return successive r-length combinations of elements in the iterable.
        combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

        combinations_with_replacement(iterable, r) --> combinations_with_replacement object
        Return successive r-length combinations of elements in the iterable
        allowing individual elements to have successive repeats.
        combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC

        :kwargs replacement:是否允许重复
        """
        if kwargs.get('replacement'):
            return itertools.combinations_with_replacement(ls, r)
        else:
            return itertools.combinations(ls, r)

    def permutations(self, ls, r):
        """
        permutations(iterable[, r]) --> permutations object
        Return successive r-length permutations of elements in the iterable.
        permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
        """
        return itertools.permutations(ls, r)

    def product(self, ls, r):
        """
        product(*iterables, repeat=1) --> product object

        Cartesian product of input iterables.  Equivalent to nested for-loops.

        For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
        The leftmost iterators are in the outermost for-loop, so the output tuples
        cycle in a manner similar to an odometer (with the rightmost element changing
        on every iteration).

        To compute the product of an iterable with itself, specify the number
        of repetitions with the optional repeat keyword argument. For example,
        product(A, repeat=4) means the same as product(A, A, A, A).

        product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
        product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...
        """
        return itertools.product(ls, r)

    def entropy(self, x):
        import math
        """
        :param x: 数据矩阵，dataframe
        :return: 权值，list
        """
        """
        熵值法介绍：
        熵值法是计算指标权重的经典算法之一，它是指用来判断某个指标的离散程度的数学方法。
        离散程度越大，即信息量越大，不确定性就越小，熵也就越小；信息量越小，不确定性越大，熵也越大。
        根据熵的特性，我们可以通过计算熵值来判断一个事件的随机性及无序程度，
        也可以用熵值来判断某个指标的离散程度，指标的离散程度越大，该指标对综合评价的影响越大。
        """

        # 标准化
        x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))

        # 求k
        rows = x.index.size  # 行
        cols = x.columns.size  # 列
        k = 1.0 / math.log(rows)

        lnf = [[None] * cols for i in range(rows)]

        # 矩阵计算--
        # 信息熵
        x = np.array(x)
        lnf = [[None] * cols for i in range(rows)]
        lnf = np.array(lnf)
        for i in range(0, rows):
            for j in range(0, cols):
                if x[i][j] == 0:
                    lnfij = 0.0
                else:
                    p = x[i][j] / x.sum(axis=0)[j]
                    lnfij = math.log(p) * p * (-k)
                lnf[i][j] = lnfij
        lnf = pd.DataFrame(lnf)
        E = lnf

        # 计算冗余度
        d = 1 - E.sum(axis=0)
        # 计算各指标的权重
        w = [[None] * 1 for i in range(cols)]
        for j in range(0, cols):
            wj = d[j] / sum(d)
            w[j] = wj
            # 计算各样本的综合得分,用最原始的数据
        return w

    def timestamp(self, date=(2018, 6, 19, 20, 55, 00)):
        # 本地时间 转换 为时间戳
        date_ = datetime.datetime(*date)
        timestamp2 = time.mktime(date_.timetuple())  # date_.timetuple() 将datetime格式的转化为time模块的tuple格式
        return timestamp2

    def localtime(self, timestamp=1529112900):
        # 时间戳转换为本地时间
        ltime = time.localtime(
            timestamp)  # time.struct_time(tm_year=2018, tm_mon=6, tm_mday=16, tm_hour=9, tm_min=35, tm_sec=0, tm_wday=5, tm_yday=167, tm_isdst=0)
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        return timeStr

    def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
        # UTCS时间转换为时间戳 2018-07-13T16:00:00Z

        import pytz
        local_tz = pytz.timezone('Asia/Chongqing')  # 定义本地时区
        utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)  # 讲世界时间的格式转化为datetime.datetime格式
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(
            local_tz)  # 想将datetime格式添加上世界时区，然后astimezone切换时区：世界时区==>本地时区
        # local_format = "%Y-%m-%d %H:%M:%S"              #定义本地时间format
        # time_str = local_dt.strftime(local_format)                         #将datetime格式转化为str—format格式
        # return int(time.mktime(time.strptime(time_str, local_format)))     #运用mktime方法将date—tuple格式的时间转化为时间戳;time.strptime()可以得到tuple的时间格式
        return int(time.mktime(local_dt.timetuple()))  # 返回当地时间戳

    def local_to_utc(local_ts, utc_format='%Y-%m-%dT%H:%MZ'):
        # 本地时间转换为UTC  传入的本地时间戳 1531411200
        import pytz

        local_tz = pytz.timezone('Asia/Chongqing')  # 定义本地时区
        local_format = "%Y-%m-%d %H:%M:%S"  # 定义本地时间format

        time_str = time.strftime(local_format, time.localtime(local_ts))  # 首先将本地时间戳转化为时间元组，用strftime格式化成字符串
        dt = datetime.datetime.strptime(time_str, local_format)  # 将字符串用strptime 转为为datetime中 datetime格式
        local_dt = local_tz.localize(dt, is_dst=None)  # 给时间添加时区，等价于 dt.replace(tzinfo=pytz.timezone('Asia/Chongqing'))
        utc_dt = local_dt.astimezone(pytz.utc)  # astimezone切换时区
        return utc_dt.strftime(utc_format)  # 返回世界时间格式

    def movie_py(self, video_path, audio_path):
        """
        将视频转成音频
        :param video: 视频地址
        :param audio: 音频地址
        :return: None
        """

        from moviepy.editor import VideoFileClip

        try:
            video = VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(audio_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pass
