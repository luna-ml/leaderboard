#!/bin/bash

# When evaluator runs,
# the current directory is /workspace, which becomes project root.
# /workspace/model is where model is mounted to get evaluated.
cd model
bunzip2 pretrained.tar.bz2
tar -xf pretrained.tar
