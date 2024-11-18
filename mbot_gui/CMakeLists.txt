cmake_minimum_required(VERSION 3.1 FATAL_ERROR)
project(mbot_gui)

set(CMAKE_BUILD_TYPE RelWithDebInfo)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

add_subdirectory(common_utils)
add_subdirectory(vx)
add_subdirectory(imagesource)


find_package(Threads REQUIRED)
find_package(lcm REQUIRED)
find_package(GTK2 2.6 REQUIRED gtk)
find_package(mbot_lcm_msgs REQUIRED)

include(${LCM_USE_FILE})

add_executable(botgui
    src/botgui_main.cpp
    src/botgui.cpp
    src/drawing_functions.cpp
    src/vx_gtk_window_base.cpp
    src/vx_utils.cpp
)
target_link_libraries(botgui
  lcm
  vx
  ${GTK2_LIBRARIES}
  ${CMAKE_THREAD_LIBS_INIT}
  common_utils
)
target_include_directories(botgui PRIVATE
  include
  ${GTK2_INCLUDE_DIRS}
)
