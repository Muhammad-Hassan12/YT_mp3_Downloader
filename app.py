from pytube import YouTube

def download_audio(url, output_path='./'):
    try:
        yt = YouTube(url)

        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)

        print(f"Audio downloaded successfully to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

video_url = 'https://www.youtube.com/'
download_audio(video_url, output_path='./')