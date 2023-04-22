import moviepy.editor
from tkinter.filedialog import *

video_file = askopenfilename()
video = moviepy.editor.VideoFileClip(video_file)
audio = video.audio

audio.write_audiofile("PythonVideoAudioConverter.mp3")
print("Completed")