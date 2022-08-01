from moviepy.editor import VideoFileClip
import os
import urllib.request

ROOT_DIR = os.path.abspath(os.curdir)


def tiktok2gif(url: str):
    with urllib.request.urlopen(url) as response, \
            open('out.mp4', 'wb') as file:
        data = response.read()
        file.write(data)

    vc = VideoFileClip("out.mp4")
    vc.write_gif("gif-out.gif")

    # print(f'{ROOT_DIR}\gif-out.gif')

    return f'{ROOT_DIR}\gif-out.gif'


s = "Python Bootcamp"
s_hashed = hash(s)

# print(s_hashed)
