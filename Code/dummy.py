import os
import re
import requests
import youtube_dl

url = 'https://www.youtube.com/watch?v=u1U4Ux7dfy0'

SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'

if url.startswith("https://tviplayer.iol.pt"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    x = requests.get(url=url, headers=headers).text

    between_script_tags = re.search('\"videoUrl\":\"(.*)\",\"videoType\"', x)
    url = between_script_tags.group(1)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(
            url,
            download=True
        )
