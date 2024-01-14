import eel
import os
from pytube import YouTube

eel.init("web")


@eel.expose
def download_video(link: str) -> str:
    print("Download Started")
    eel.set_loading_cursor()
    yt = YouTube(link)
    audio_stream = yt.streams.get_lowest_resolution()
    if os.path.isdir("web/downloads/") != True:
        os.mkdir("web/downloads/")
    audio_stream.download("web/downloads/")
    url = f"{yt.title}.mp4"
    eel.reset_cursor()
    return url


eel.start("index.html")
