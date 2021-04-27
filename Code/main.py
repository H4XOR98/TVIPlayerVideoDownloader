from tkinter import *
from tkinter import messagebox
import os
import re
import requests
import youtube_dl

SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'


def Ok(url):
    if url == "":
        messagebox.showinfo("", "Nenhum url inserido")
    elif not url.startswith('https://tviplayer.iol.pt'):
        messagebox.showinfo("", "O url inserido não corresponde ao tvi player")
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
               (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }

        x = requests.get(url=url, headers=headers).text

        between_script_tags = re.search('\"videoUrl\":\"(.*)\",\"videoType\"', x)
        url = between_script_tags.group(1)

        ydl_opts = {
            'format': 'best',
            'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(
                url,
                download=True
            )
        messagebox.showinfo("", "Download concluído com sucesso")


def Exit():
    exit(0)


root = Tk()
width = 500
height = 300

# Window
root.title("TVIPlayer Video Downloader")
root['bg'] = "grey"

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

posX = screen_width / 2 - width / 2
posY = screen_height / 2 - height / 2

root.geometry("%dx%d+%d+%d" % (width, height, posX, posY))
root.resizable(False, False)

Label(root, text="TVI Player Url:").place(x=10, y=10)

e1 = Entry(root)
e1.place(x=120, y=10)

Button(root, text="Download", command=lambda: Ok(e1.get())).place(x=10, y=100)

Button(root, text="Sair", command=Exit).place(x=420, y=100)


root.mainloop()
