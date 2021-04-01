#!/bin/sh

# make list of video to concat
ls video/*.mp4 | sed "s/\(.*\)/file '\1'/g" > vidlist.txt

# concat
ffmpeg -f concat -safe 0 -i vidlist.txt -c copy eval/video.mp4
