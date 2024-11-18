cmake_minimum_required(VERSION 3.1 FATAL_ERROR)
project(rplidar_driver)

add_subdirectory(rplidar_sdk/sdk)

set(CMAKE_BUILD_TYPE RelWithDebInfo)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

find_package(Threads REQUIRED)
find_package(lcm REQUIRED)
find_package(mbot_lcm_msgs REQUIRED)

add_executable(rplidar_driver
    src/rplidar_driver.cpp
)

target_link_libraries(rplidar_driver
    ${CMAKE_THREAD_LIBS_INIT}
    lcm
    mbot_lcm_msgs
    pthread
    rplidar_sdk
)

target_include_directories(rplidar_driver PRIVATE include)

# This is needed to find the shared libraries correctly on RPi OS.
set_target_properties(rplidar_driver PROPERTIES
    INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib
    BUILD_WITH_INSTALL_RPATH 1
)

# Install binary to system.
install(
    TARGETS rplidar_driver
    DESTINATION bin
)
