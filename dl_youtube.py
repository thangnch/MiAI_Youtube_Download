from pytube import YouTube
from moviepy.editor import *
import os

video_url = "https://www.youtube.com/watch?v=xcJtL7QggTI"

# Tạo class mới
yt = YouTube(video_url)

streams = yt.streams
print(streams)

# Tải video
video = yt.streams.get_by_itag(137)
video_file = video.download(output_path=".", filename="video.mp4")

# Tải audio
audio = yt.streams.get_by_itag(139)
audio_file = audio.download(output_path=".", filename="audio.mp3")

# Merge audio và video vào 1 file
output_file = "export.mp4"

new_clip = VideoFileClip("video.mp4")
new_clip = new_clip.without_audio()

new_audio = AudioFileClip("audio.mp3")
new_clip = new_clip.set_audio(new_audio)
new_clip.write_videofile(output_file)
