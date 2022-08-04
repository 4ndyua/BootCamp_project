from moviepy.editor import VideoFileClip
import os
import urllib.request
from TikTokApi import TikTokApi
import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Tik  Tok  to  GIF")
print(ascii_banner)
ROOT_DIR = os.path.abspath(os.curdir)
x = random.randint(1, 10000)


def to_gif():
    vc = VideoFileClip(f'out{x}.mp4')
    vc.write_gif(f'gif{x}.gif')
    vc.close()
    print(f'\nGIF FILE : {ROOT_DIR}\gif{x}.gif\n')


def tiktok2gif_from_url(url: str):
    with urllib.request.urlopen(url) as response, \
            open(f'out{x}.mp4', 'wb') as file:
        data = response.read()
        file.write(data)
        file.close()
    to_gif()
    return 'OK'


def tiktok2gif_from_id(id: str):
    with TikTokApi() as api:
        video = api.video(id=id)
        video_data = video.bytes()
        with open(f'out{x}.mp4', "wb") as out_file:
            out_file.write(video_data)
    to_gif()
    return 'OK'



option = ''
while option != 'q':
    option = input('PLEASE CHOOSE YOUR OPTION (type "q" for exit)\n '
                   'Type "1" for GIF FROM URL\n Type "2" for GIF FROM ID\n INPUT HERE: ')
    if option == '1':
        option_url = input('INPUT URL OF VIDEO: ')
        print('PROCESSING...')
        tiktok2gif_from_url(option_url)
    elif option == '2':
        option_id = input('INPUT ID OF VIDEO: ')
        print('PROCESSING...')
        tiktok2gif_from_id(option_id)
    else:
        print('Wrong number. Choose 1 or 2 option')

folder = os.listdir(ROOT_DIR)

for item in folder:
    if item.endswith('.mp4'):
        os.remove(os.path.join(ROOT_DIR, item))
