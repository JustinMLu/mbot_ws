#!/usr/bin/env bash

echo $PWD
VX_SHADERS_DIR=$(find . -regex '.*vx\/shaders' | head -n 1)
export VX_SHADER_PATH=$PWD/$VX_SHADERS_DIR
echo "VX shades location: {$VX_SHADER_PATH}"

VX_FONTS_DIR=$(find . -regex '.*vx\/fonts' | head -n 1)
export VX_FONT_PATH=$PWD/$VX_FONTS_DIR
echo "VX fonts location: {$VX_FONT_PATH}"

# TODO: This doesn't work with the new install. Need to set this elsewhere.
# LCM_JAVA_FILE_LOCATION=$(find . -regex '.*lcm.*\.jar' | head -n 1)
LCM_JAVA_FILE_LOCATION=/usr/local/share/java/mbot_lcm_msgs.jar
export CLASSPATH=$CLASSPATH:$LCM_JAVA_FILE_LOCATION
echo "Jar file location: {$LCM_JAVA_FILE_LOCATION}"
