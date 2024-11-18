cmake_minimum_required(VERSION 3.12 FATAL_ERROR)
project(mbot_bridge)

set(CMAKE_BUILD_TYPE RelWithDebInfo)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

find_package(websocketpp REQUIRED)
find_package(mbot_lcm_msgs REQUIRED)
find_package(Threads REQUIRED)

add_library(mbot_bridge_cpp SHARED
  src/robot.cpp
)

# Set library include directories
target_include_directories(mbot_bridge_cpp PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

target_link_libraries(mbot_bridge_cpp
  ${CMAKE_THREAD_LIBS_INIT}
)

# Test executable.
add_executable(mbot_cpp_test test/test_mbot_api.cpp
)
target_link_libraries(mbot_cpp_test
  mbot_bridge_cpp
)
target_include_directories(mbot_cpp_test PRIVATE
)

# Install the library and header files
install(TARGETS mbot_bridge_cpp
    EXPORT ${PROJECT_NAME}Targets
    LIBRARY DESTINATION lib${LIB_SUFFIX}
    ARCHIVE DESTINATION lib${LIB_SUFFIX}
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(DIRECTORY include/ DESTINATION include)

# Configure this as a CMake package

install(EXPORT ${PROJECT_NAME}Targets
  FILE ${PROJECT_NAME}Targets.cmake
  DESTINATION lib/cmake/${PROJECT_NAME}
)

include(CMakePackageConfigHelpers)
# generate the config file that is includes the exports
configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/Config.cmake.in
  "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
  INSTALL_DESTINATION "lib/cmake"
  NO_SET_AND_CHECK_MACRO
  NO_CHECK_REQUIRED_COMPONENTS_MACRO
)

install(FILES
  ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
  DESTINATION lib/cmake/${PROJECT_NAME}
)

export(PACKAGE ${PROJECT_NAME})
