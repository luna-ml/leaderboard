#!/bin/bash

git clone https://github.com/andywu0913/OpenAI-GYM-CarRacing-DQN.git dqn
cd dqn
git checkout 778c83685606ee26d0a7fbfbdfe89ebab2268490
cp *.py ../
pip install -r requirements.txt
pip install 'tensorflow<=2.0.0'
pip install 'h5py==2.10.0' --force-reinstall
