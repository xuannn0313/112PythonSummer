import yt_dlp

Playlist_URL = 'https://youtube.com/playlist?list=PLLCtoR8-d2p3K6wW124IZg6IZpFi1vREj&si=sGx8DSXSrUdvNIiJ'

DIR = 'C:\\Youtube'

ydl_opts = {
    'format':'worst',
    'outtmpl': f'{DIR}/%(playlist_title)s/%(title)ss/%(ext)s'
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

       ydl.download([Playlist_URL])
    print(f"Playlist download successfully to {DIR}")
    

except Exception as e:
    print(f"An unexpected error occured:{e}")