from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os
import easygui
import time

title = "EasyConcat v0.2"
validExt = [".mp4",".avi",".ogv",".webm",".mkv"]

folders = ["C:\\\\Users\\\\hi\\\\Videos\\\\TestFiles"]

for folder in folders:
    clips = []
    files = os.listdir(folder)
    yee = folder + ".txt"
    with open(yee, 'w') as f:
        for file in files:
            f.write("file ")
            f.write(folder + "\\\\" + file)
            f.write('\n')
    
    command = "ffmpeg -f concat -safe 0 -i " + yee + " -r 25 -c copy " + folder + ".mp4"
    print(command)
    os.system(command)
