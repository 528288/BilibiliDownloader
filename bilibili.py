import os
from yeyuc_downloader import YouGet


def movie_py(video_path, audio_path):
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

if __name__ == "__main__":
    path = r"C:\Users\yeyuc\Desktop\发音教程"
    video_path = os.path.join(path, r"data/video")
    audio_path = os.path.join(path, r"data/audio")
    urls = ["https://www.bilibili.com/video/BV1a64y167Wf"]

    # 根据url下载所有视频
    yg = YouGet(video_path)
    for url in urls:
        yg.download(url)

    # 将视频转换成音频
    files = os.listdir(video_path)
    videos = [file.split('.')[0] + '.wav' for file in files]
    for v, a in zip(files, videos):
        movie_py(os.path.join(video_path, v), os.path.join(audio_path, a))



    # """
    # 配置项：
    # start_url：投稿页模式，手动配置
    # pages：投稿页页数，默认1
    # selenium：是否需要动态加载，默认Fasle
    # path：保存路径，默认"./data/video"
    # slices：分片数，默认8
    # """
    # start_url = "https://space.bilibili.com/130763764/video?tid=0&page="
    # pages = 1
    # selenium = True
    # path = r"./data/video"
    # slices = 2
    #
    # rs = RequestsSpider(pages=pages, selenium=selenium)
    # urls = rs.spider(start_url)
    # rs.browser.close()
    # # urls = ["https://www.bilibili.com/video/av" + item for item in urls]
    # # urls = ["https://www.bilibili.com/video/" + item for item in urls]
    # coder = Coder()
    # urls = ["https://www.bilibili.com/video/av" + str(coder.dec(item)) for item in urls]
    #
    #
    # mc = MultiCore(path)
    # slices = min(slices, len(urls))  # 防止分片数过大
    # data = mc.split_list(urls, slices)  # 将urls分成8份
    # mc.process(param=data)
    #
    # # slices = 8
    # # urls = ["https://www.bilibili.com/video/av?p=" + str(_) for _ in range(1, 49)]
    # #
    # # mc = MultiCore(path)
    # # slices = min(slices, len(urls))  # 防止分片数过大
    # # data = mc.split_list(urls, slices)  # 将urls分成8份
    # # mc.process(param=data)
    # #
    # client = Common()
    # #
    # # files = os.listdir(path)
    # # videos = [file.split('.')[0] + '.wav' for file in files]
    # # # videos = [file.split('.')[0] + '.mp3' for file in files]
    # # for v, a in zip(files, videos):
    # #     client.movie_py(os.path.join(path, v), os.path.join(path, a))
    #
    # pass
