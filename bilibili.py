from yeyuc_multicore import MultiCore
from yeyuc_spider import RequestsSpider

if __name__ == "__main__":
    """
    配置项：
    start_url：投稿页模式，手动配置
    pages：投稿页页数，默认1
    selenium：是否需要动态加载，默认Fasle
    path：保存路径，默认"./data/video"
    slices：分片数，默认8
    """
    start_url = "https://space.bilibili.com/130763764/video?tid=0&page="
    pages = 1
    selenium = True
    path = r"./data/video"
    slices = 2

    rs = RequestsSpider(pages=pages, selenium=selenium)
    urls = rs.spider(start_url)
    rs.browser.close()
    # urls = ["https://www.bilibili.com/video/av" + item for item in urls]
    urls = ["https://www.bilibili.com/video/" + item for item in urls]
    print(urls)

    # path = r"你想要的下载位置"
    mc = MultiCore(path)
    slices = min(slices, len(urls))  # 防止分片数过大
    data = mc.split_list(urls, slices)  # 将urls分成8份
    mc.process(param=data)
