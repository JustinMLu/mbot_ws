#!/usr/bin/env bash
cd build
cmake -DMBOT_TYPE=CLASSIC -DENC=48 ..
make
sudo mbot-upload-firmware flash mbot_classic_v1.1.0_enc48.uf2
cd ..