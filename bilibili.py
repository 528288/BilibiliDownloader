from yeyuc_multicore import MultiCore
from yeyuc_spider import RequestsSpider

if __name__ == "__main__":
    rs = RequestsSpider(pages=3, selenium=True)
    urls = rs.spider()
    rs.browser.close()
    urls = ["https://www.bilibili.com/video/av" + item for item in urls]

    # path = r"你想要的下载位置"
    path = r"./data/video"
    mc = MultiCore(path)
    data = mc.split_list(urls, 8)  # 将urls分成8份
    mc.process(param=data)