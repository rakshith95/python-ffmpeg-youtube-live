# python-ffmpeg-youtube-live
Simple code to stream from a python program using opencv to Youtube Live using ffmpeg 


* Run with: 
 `python capture.py <video path/camera device> | ffmpeg -i - -f lavfi -i anullsrc -acodec libmp3lame -ar 44100 -deinterlace -vcodec nvenc_h264 -pix_fmt yuv420p -s 1920x1080 -r 30 -g 120 -b:v 2500k -threads:6 -qscale:3 -b:a:712000 -bufsize:512k -f flv "rtmp://a.rtmp.youtube.com/live2/$YOUR_KEY"`

* The python code streams to stdout buffer, which ffmpeg reads in as a pipe input.
* The `-f lavfi -i anullsrc -acodec libmp3lame -ar 44100` adds dummy audio to be able to stream to YouTube Live. 
* Pipe breaks without the cv2.imencode. I don't fully understand why
