import cv2
import numpy as np 
import sys
import subprocess as sp 

FFMPEG_BIN = "ffmpeg" # on Linux ans Mac OS

video_path=sys.argv[1]
youtube_live_key = sys.argv[2]

command = [ FFMPEG_BIN,
        '-i', '-', #input from pipe
        '-f', 'lavfi',
        '-i','anullsrc', #Youtube Live needs some audio, so create fake audio src
        '-acodec', 'libmp3lame', 
        '-ar', '44100',
        '-deinterlace', 
        '-vcodec', 'nvenc_h264', #Use libx264 if no nvidia GPU available
        '-pix_fmt', 'yuv420p',
        '-s', '1280x720',
        '-preset', 'ultrafast',
    '-tune', 'fastdecode',
    '-r', '30', #Frame rate
    '-g', '120', 
    '-b:v', '2500k',
    '-threads:6', 
    '-qscale:3',
    '-b:a:712000',
    '-buffsize:512k',
    '-f' , 'flv',
    'rtmp://a.rtmp.youtube.com/live2/{}'.format(youtube_live_key),
        ]

pipe = sp.Popen( command, stdin=sp.PIPE, stderr=sp.PIPE)

cap = cv2.VideoCapture(video_path)
ret2=True   
i=1
ret=None
frame=None
while True:
    ret, frame = cap.read()
    if ret:
        ret2,frame_out = cv2.imencode('.jpg',frame) #Breaks without this for some reason
        if ret2:
	        pipe.stdin.write( frame_out.tobytes() )
            
