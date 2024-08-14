import yt_dlp
import ffmpeg
import os

URL = 'https://youtu.be/kd5LJ4r-vEY?si=wpfywv8Dqmuce00w'
DIR = 'C:\\Youtube'

ydl_opts_video = {
    'format':'bestvideo[ext=mp4][height<=1080]',
    'outtmpl' :f'{DIR}/video.mp4',
    'merge_output_format':'mp4',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts_video) as ydl:
        info_dict_video = ydl.extract_info(URL,download=True)
        video_itag=info_dict_video.get("format_id",None)
        print(f"Video download:{DIR}\\video.mp4")
        print(f"Video itag: {video_itag}")
              
except Exception as e:
    print(f"An unexpected error occured while download video:{e}")

ydl_opts_audio={
    'format':'bestaudio[ext=mp4]',
    'outtmpl':f'{DIR}/audio.mp4',
}

try:
     with yt_dlp.YoutubeDL(ydl_opts_audio) as ydl:
        info_dict_audio = ydl.extract_info(URL,download=True)
        audio_itag=info_dict_audio.get("format_id",None)
        print(f"Audio download:{DIR}\\audio.mp4")
        print(f"Audio itag: {audio_itag}")

     video_input=ffmpeg.input(os.path.join(DIR,'video.mp4'))
     audio_input=ffmpeg.input(os.path.join(DIR,'audio.mp4'))
     output_path=os.path.join(DIR,'output.mp4')

     ffmpeg.output(video_input, audio_input, output_path, vcodec='copy', acodec='aac', strict='experimental').run()
     print(f"video and audio merged:{output_path}")

except Exception as e:
    print(f"An unexpected error occured while download audio:{e}")          
