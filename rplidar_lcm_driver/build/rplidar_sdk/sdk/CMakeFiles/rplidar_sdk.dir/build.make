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
include rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/compiler_depend.make

# Include the progress variables for this target.
include rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/progress.make

# Include the compile flags for this target's objects.
include rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/flags.make

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/flags.make
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o: /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_serial.cpp
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o -MF CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o.d -o CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o -c /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_serial.cpp

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.i"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_serial.cpp > CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.i

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.s"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_serial.cpp -o CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.s

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/flags.make
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o: /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_socket.cpp
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o -MF CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o.d -o CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o -c /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_socket.cpp

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.i"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_socket.cpp > CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.i

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.s"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/net_socket.cpp -o CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.s

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/flags.make
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o: /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/timer.cpp
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o -MF CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o.d -o CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o -c /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/timer.cpp

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.i"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/timer.cpp > CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.i

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.s"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/arch/linux/timer.cpp -o CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.s

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/flags.make
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o: /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/hal/thread.cpp
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o -MF CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o.d -o CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o -c /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/hal/thread.cpp

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.i"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/hal/thread.cpp > CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.i

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.s"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/hal/thread.cpp -o CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.s

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/flags.make
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o: /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/rplidar_driver.cpp
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o -MF CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o.d -o CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o -c /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/rplidar_driver.cpp

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.i"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/rplidar_driver.cpp > CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.i

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.s"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/rplidar_driver.cpp -o CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.s

# Object files for target rplidar_sdk
rplidar_sdk_OBJECTS = \
"CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o" \
"CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o" \
"CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o" \
"CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o" \
"CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o"

# External object files for target rplidar_sdk
rplidar_sdk_EXTERNAL_OBJECTS =

rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_serial.cpp.o
rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/net_socket.cpp.o
rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/arch/linux/timer.cpp.o
rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/hal/thread.cpp.o
rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/sdk/src/rplidar_driver.cpp.o
rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/build.make
rplidar_sdk/sdk/librplidar_sdk.a: rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mbot/mbot_ws/rplidar_lcm_driver/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking CXX static library librplidar_sdk.a"
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && $(CMAKE_COMMAND) -P CMakeFiles/rplidar_sdk.dir/cmake_clean_target.cmake
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rplidar_sdk.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/build: rplidar_sdk/sdk/librplidar_sdk.a
.PHONY : rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/build

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/clean:
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk && $(CMAKE_COMMAND) -P CMakeFiles/rplidar_sdk.dir/cmake_clean.cmake
.PHONY : rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/clean

rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/depend:
	cd /home/mbot/mbot_ws/rplidar_lcm_driver/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mbot/mbot_ws/rplidar_lcm_driver /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk /home/mbot/mbot_ws/rplidar_lcm_driver/build /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk /home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : rplidar_sdk/sdk/CMakeFiles/rplidar_sdk.dir/depend

