# python-ffmpeg-youtube-live
Simple code to stream from a python program using opencv to Youtube Live using ffmpeg 


* Run with: 
 `python capture.py <video path/camera device> <YOUTUBE_KEY>`

* The python code streams to stdout buffer, which ffmpeg reads in as a pipe input.
* Change the ffmpeg parameters in the program to suit your requirements
* The `-f lavfi -i anullsrc -acodec libmp3lame -ar 44100` adds dummy audio to be able to stream to YouTube Live. 
* Pipe breaks without the cv2.imencode. I don't fully understand why
