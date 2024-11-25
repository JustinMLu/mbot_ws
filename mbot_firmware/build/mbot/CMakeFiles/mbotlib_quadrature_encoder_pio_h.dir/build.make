# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mbot/mbot_ws/mbot_firmware

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mbot/mbot_ws/mbot_firmware/build

# Utility rule file for mbotlib_quadrature_encoder_pio_h.

# Include any custom commands dependencies for this target.
include mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/compiler_depend.make

# Include the progress variables for this target.
include mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/progress.make

mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h: mbot/quadrature_encoder.pio.h

mbot/quadrature_encoder.pio.h: /home/mbot/mbot_ws/mbot_firmware/mbot/include/mbot/encoder/quadrature_encoder.pio
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/mbot/mbot_ws/mbot_firmware/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating quadrature_encoder.pio.h"
	cd /home/mbot/mbot_ws/mbot_firmware/build/mbot && ../pioasm/pioasm -o c-sdk /home/mbot/mbot_ws/mbot_firmware/mbot/include/mbot/encoder/quadrature_encoder.pio /home/mbot/mbot_ws/mbot_firmware/build/mbot/quadrature_encoder.pio.h

mbotlib_quadrature_encoder_pio_h: mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h
mbotlib_quadrature_encoder_pio_h: mbot/quadrature_encoder.pio.h
mbotlib_quadrature_encoder_pio_h: mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/build.make
.PHONY : mbotlib_quadrature_encoder_pio_h

# Rule to build all files generated by this target.
mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/build: mbotlib_quadrature_encoder_pio_h
.PHONY : mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/build

mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/clean:
	cd /home/mbot/mbot_ws/mbot_firmware/build/mbot && $(CMAKE_COMMAND) -P CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/cmake_clean.cmake
.PHONY : mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/clean

mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/depend:
	cd /home/mbot/mbot_ws/mbot_firmware/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mbot/mbot_ws/mbot_firmware /home/mbot/mbot_ws/mbot_firmware/mbot /home/mbot/mbot_ws/mbot_firmware/build /home/mbot/mbot_ws/mbot_firmware/build/mbot /home/mbot/mbot_ws/mbot_firmware/build/mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mbot/CMakeFiles/mbotlib_quadrature_encoder_pio_h.dir/depend

