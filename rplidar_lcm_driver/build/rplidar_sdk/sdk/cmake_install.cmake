# Install script for directory: /home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/include/rplidar.h"
    "/home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/include/rplidar_cmd.h"
    "/home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/include/rplidar_driver.h"
    "/home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/include/rplidar_protocol.h"
    "/home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/include/rptypes.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/hal" TYPE FILE FILES "/home/mbot/mbot_ws/rplidar_lcm_driver/rplidar_sdk/sdk/sdk/src/hal/types.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk/librplidar_sdk.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk" TYPE FILE FILES "/home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk/rplidar_sdkConfig.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk/rplidar_sdk-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk/rplidar_sdk-targets.cmake"
         "/home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk/CMakeFiles/Export/ccaaa3de7b8fa3bdc381ccd9e9e5ef48/rplidar_sdk-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk/rplidar_sdk-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk/rplidar_sdk-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk" TYPE FILE FILES "/home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk/CMakeFiles/Export/ccaaa3de7b8fa3bdc381ccd9e9e5ef48/rplidar_sdk-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/rplidar_sdk" TYPE FILE FILES "/home/mbot/mbot_ws/rplidar_lcm_driver/build/rplidar_sdk/sdk/CMakeFiles/Export/ccaaa3de7b8fa3bdc381ccd9e9e5ef48/rplidar_sdk-targets-noconfig.cmake")
  endif()
endif()

