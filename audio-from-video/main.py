import moviepy.editor
from tkinter.filedialog import *
vid = askopenfile()
video=moviepy.editor.VideoFileClip("file location")
aud = video.audio
aud.write_audiofile("demo.mp3")