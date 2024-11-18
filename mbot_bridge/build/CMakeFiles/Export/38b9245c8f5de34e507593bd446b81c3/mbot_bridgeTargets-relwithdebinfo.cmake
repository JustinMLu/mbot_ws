#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mbot_bridge_cpp" for configuration "RelWithDebInfo"
set_property(TARGET mbot_bridge_cpp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(mbot_bridge_cpp PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libmbot_bridge_cpp.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libmbot_bridge_cpp.so"
  )

list(APPEND _cmake_import_check_targets mbot_bridge_cpp )
list(APPEND _cmake_import_check_files_for_mbot_bridge_cpp "${_IMPORT_PREFIX}/lib/libmbot_bridge_cpp.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
