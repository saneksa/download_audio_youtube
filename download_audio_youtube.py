import youtube_dl
import os

url_download = input('Введите ссылку на видео: ')

options = {
    'format':'bestaudio/best',
    'extractaudio':True,
    'audioformat':'ogg',
    'outtmpl': u'%(title)s.%(ext)s',     #name the file the ID of the video
    'noplaylist':True,
    'nocheckcertificate':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
        'preferredquality': '32',
    }]
}

if ('watch' in url_download):
    id_download = str(url_download.split('watch?v=')[1])
else:
    id_download = str(url_download.split('youtu.be/')[1])
with youtube_dl.YoutubeDL(options) as ydl:
    f = ydl.extract_info(url_download)['title']
ext = str(options['postprocessors'][0]['preferredcodec'])
#os.rename(id_download+'.'+ext,f + '.'+ext)
