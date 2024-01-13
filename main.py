import eel
import os
from pytube import YouTube
eel.init("web")
@eel.expose
def download_video(link):
    print("Download Started")
    eel.set_loading_cursor()
    yt = YouTube(link)
    audio_stream = yt.streams.get_lowest_resolution()
    if os.path.isdir("downloads") == True:
        pass
    else:
        os.mkdir("downloads")
    audio_stream.download("downloads/")
    url = f'../downloads/{yt.title}.mp4'
    eel.reset_cursor()
    return url
eel.start("index.html")