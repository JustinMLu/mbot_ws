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
CMAKE_SOURCE_DIR = /home/mbot/mbot_ws/rplidar_lcm_driver

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mbot/mbot_ws/rplidar_lcm_driver/build

# Include any dependencies generated for this target.
include CMakeFiles/rplidar_driver.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/rplidar_driver.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/rplidar_driver.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/rplidar_driver.dir/flags.make

CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o: CMakeFiles/rplidar_driver.dir/flags.make
CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o: /home/mbot/mbot_ws/rplidar_lcm_driver/src/rplidar_driver.cpp
CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o: CMakeFiles/rplidar_driver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o -MF CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o.d -o CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o -c /home/mbot/mbot_ws/rplidar_lcm_driver/src/rplidar_driver.cpp

CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mbot/mbot_ws/rplidar_lcm_driver/src/rplidar_driver.cpp > CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.i

CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mbot/mbot_ws/rplidar_lcm_driver/src/rplidar_driver.cpp -o CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.s

# Object files for target rplidar_driver
rplidar_driver_OBJECTS = \
"CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o"

# External object files for target rplidar_driver
rplidar_driver_EXTERNAL_OBJECTS =

rplidar_driver: CMakeFiles/rplidar_driver.dir/src/rplidar_driver.cpp.o
rplidar_driver: CMakeFiles/rplidar_driver.dir/build.make
rplidar_driver: /usr/local/lib/libmbot_lcm_msgs.a
rplidar_driver: rplidar_sdk/sdk/librplidar_sdk.a
rplidar_driver: /usr/local/lib/liblcm.so.1.5.0
rplidar_driver: CMakeFiles/rplidar_driver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable rplidar_driver"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rplidar_driver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/rplidar_driver.dir/build: rplidar_driver
.PHONY : CMakeFiles/rplidar_driver.dir/build

CMakeFiles/rplidar_driver.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/rplidar_driver.dir/cmake_clean.cmake
.PHONY : CMakeFiles/rplidar_driver.dir/clean

CMakeFiles/rplidar_driver.dir/depend:
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mbot/mbot_ws/rplidar_lcm_driver /home/mbot/mbot_ws/rplidar_lcm_driver /home/mbot/mbot_ws/rplidar_lcm_driver/build /home/mbot/mbot_ws/rplidar_lcm_driver/build /home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles/rplidar_driver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/rplidar_driver.dir/depend

