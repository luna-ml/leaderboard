#!/bin/sh
apt-get update
apt-get install -y python-opengl xvfb unzip swig

conda install -y x264=='1!152.20180717' ffmpeg=4.0.2 -c conda-forge
