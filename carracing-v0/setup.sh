#!/bin/sh

# install gym from source where carracing is not available in pypi released version
pushd
cd /tmp/
git clone https://github.com/openai/gym.git
cd gym
git checkout v0.10.5
pip install -e '.[box2d]'
popd

conda install -y x264=='1!152.20180717' ffmpeg=4.0.2 -c conda-forge
apt-get update
apt-get install -y python-opengl xvfb unzip swig
