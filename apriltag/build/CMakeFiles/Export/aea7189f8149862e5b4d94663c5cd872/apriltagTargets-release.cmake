#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "apriltag::apriltag" for configuration "Release"
set_property(TARGET apriltag::apriltag APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(apriltag::apriltag PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libapriltag.so.3.4.2"
  IMPORTED_SONAME_RELEASE "libapriltag.so.3"
  )

list(APPEND _cmake_import_check_targets apriltag::apriltag )
list(APPEND _cmake_import_check_files_for_apriltag::apriltag "${_IMPORT_PREFIX}/lib/libapriltag.so.3.4.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
