#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "rplidar_sdk::rplidar_sdk" for configuration ""
set_property(TARGET rplidar_sdk::rplidar_sdk APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(rplidar_sdk::rplidar_sdk PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "CXX"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/librplidar_sdk.a"
  )

list(APPEND _cmake_import_check_targets rplidar_sdk::rplidar_sdk )
list(APPEND _cmake_import_check_files_for_rplidar_sdk::rplidar_sdk "${_IMPORT_PREFIX}/lib/librplidar_sdk.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
