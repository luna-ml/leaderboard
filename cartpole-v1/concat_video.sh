#!/bin/sh

# download font
cd video
wget "https://fonts.google.com/download?family=Roboto" -O roboto.zip
unzip roboto.zip
cd -

# add episode # on the video

for f in video/*.mp4; do
    episode=`echo $f |  sed 's/.*video\([0-9]*\).mp4$/\1/g'`
    episodeN=`expr "$episode" + 1`

    ffmpeg -i $f -vf drawtext="fontfile=video/Roboto-Medium.ttf: text='#$episodeN': fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5: boxborderw=5: x=5: y=5" -codec:a output video/episode-$episode.mp4
done

# make list of video to concat
ls video/episode-*.mp4 | sed "s/.*\(episode-.*\)/file '\1'/g" > video/vidlist.txt

# concat
ffmpeg -f concat -safe 0 -i video/vidlist.txt -c copy eval/video.mp4
