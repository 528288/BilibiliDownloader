import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class Coder:
    def __init__(self):
        self.table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
        self.tr = {self.table[i]: i for i in range(58)}
        self.s = [11, 10, 3, 8, 4, 6]
        self.xor = 177451812
        self.add = 8728348608

    def dec(self, x):
        r = 0
        for i in range(6):
            r += self.tr[x[self.s[i]]] * 58 ** i
        return (r - self.add) ^ self.xor

    def enc(self, x):
        x = (x ^ self.xor) + self.add
        r = list('BV1  4 1 7  ')
        for i in range(6):
            r[self.s[i]] = self.table[x // 58 ** i % 58]
        return ''.join(r)


# 给定哔哩哔哩up主投稿页链接，爬取所有视频链接
class RequestsSpider:
    def __init__(self, pages, **kwargs):
        self.depth = pages  # CodeSheep 投稿页功79个视频，分成3页
        if kwargs.get('selenium'):
            self.browser = self.selenium(path=kwargs.get("path", r"./data/chromedriver.exe"))

    def selenium(self, path):
        executable_path = path
        chrome_options = webdriver.ChromeOptions()
        """后台运行Chromedriver"""
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

        """全屏显示"""
        browser.maximize_window()
        time.sleep(5)
        return browser

    def downloader1(self, url):
        """
		需动态加载时, 使用selenium加载完整页面再返回
    `"""
        self.browser.get(url)
        self.browser.implicitly_wait(20)
        time.sleep(5)
        return self.browser.page_source

    def downloader(self, url):
        """
            无需动态加载时，直接使用requests.get()获取页面
            """
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""

    def parse(self, info, html):
        """
            网页解析: BeautifulSoup + re
        """
        soup = BeautifulSoup(html, "html.parser")

        nodes = soup.find("ul", {"class": "clearfix cube-list"}).find_all("li")
        aids = [node.get("data-aid") for node in nodes]
        info.extend(aids)

    def spider(self, start_url):
        """
        初始url与调度
        """
        info = []
        # start_url = "https://space.bilibili.com/384068749/video?tid=0&page="  # 投稿页的url

        for i in range(self.depth):
            print("正在爬取第{0}页".format(i + 1))
            try:
                url = start_url + str(i + 1)
                html = self.downloader1(url)
                self.parse(info, html)
            except Exception as e:
                print(e)
        return info


if __name__ == "__main__":
    # client = RequestsSpider(pages=3, selenium=True)
    # urls = client.spider()
    # client.browser.close()

    # coder = Coder()
    # print(coder.dec('BV1bb411N77n'))
    # print(coder.dec('BV17x411w7KC'))
    # print(coder.dec('BV1Q541167Qg'))
    # print(coder.dec('BV1mK4y1C7Bz'))
    # print(coder.enc(170001))
    # print(coder.enc(455017605))
    # print(coder.enc(882584971))

    # urls = ["https://www.bilibili.com/video/av" + coder.dec(item) for item in urls]
    # urls = ["https://www.bilibili.com/video/av" + item for item in urls]
    # print(urls)

    pass
