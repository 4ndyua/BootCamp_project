from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip
import os

ROOT_DIR = os.path.abspath(os.curdir)


def tiktok2gif(id_: str):
    with TikTokApi() as api:
        video = api.video(id=id_)

        video_data = video.bytes()

        with open("out.mp4", "wb") as out_file:
            out_file.write(video_data)

    vc = VideoFileClip("out.mp4")
    vc.write_gif("gif-out.gif")

    return f'{ROOT_DIR}\gif-out.gif'

# tiktok2gif('7099016777383824646')
