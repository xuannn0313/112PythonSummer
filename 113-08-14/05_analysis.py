import yt_dlp

URL = 'https://youtu.be/kd5LJ4r-vEY?si=wpfywv8Dqmuce00w'

DIR = 'C:\\Youtube'

ydl_opts = {
    'format':'all',
    'skip_download' :True,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info_dict = ydl.extract_info(URL,download=True)

        formats = info_dict.get('formats',[])
        for res in formats:

            vcodec = res.get('vcodec','none')
            acodec = res.get('acodec','none')

            is_video_only= vcodec!='none' and acodec =='none'
            is_audio_only= vcodec=='none' and acodec =='none'

            label=""
            if is_video_only:
                label="[video only]"
            elif is_audio_only:
                label="[audio only]"

# 检查是否为 progressive
            is_progressive = vcodec != 'none' and acodec != 'none'
            
            # 设置标注
            label = ""
            if is_video_only:
                label = " [video only]"
            elif is_audio_only:
                label = " [audio only]"
            if is_progressive:
                label += " [progressive]"
            else:
                label += " [non-progressive]"
            label = ""
                          
            print(f"Format ID: {res['format_id']}, Ext: {res['ext']}, Resolution: {res.get('resolution', 'N/A')}, "
                  f"Video Codec: {vcodec}, Audio Codec: {acodec}, Note: {res.get('format_note', 'N/A')}{label}")

except Exception as e:
    print(f"An unexpected error occured:{e}")