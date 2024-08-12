import yt_dlp

URL = 'https://youtu.be/QL0LUaxWUOI?si=XM0sdEOohJ-wxo2B'

DIR = 'C:\\Youtube'


ydl_opts = {
    'format':'bestaudio/best',
    'outtmpl': f'{DIR}/%(title)s.%(ext)s',   
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info_dict = ydl.extract_info(URL,download=True)

        downloaded_format = next((f for f in info_dict['formats'] if f['ext'] == 'm4a'), None)
        if downloaded_format:
            downloaded_itag = downloaded_format.get("format_id", None)
            print(f"Downloaded format itag: {downloaded_itag}")
        else:
            print("Failed to retrieve itag for the downloaded format.")

    print(f"Audio download successfully to {DIR}")
    
except Exception as e:
    print(f"An unexpected error occured:{e}")