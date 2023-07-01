cmake_minimum_required (VERSION 3.12)
project(Webnucleo LANGUAGES CXX)

cmake_policy(SET CMP0086 NEW)
cmake_policy(SET CMP0078 NEW)
set (CMAKE_CXX_STANDARD 11)


### import modules
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

include_directories(${CMAKE_SOURCE_DIR} /usr/include/python3.6m)

add_library(tinyxml2 SHARED tinyxml2.h tinyxml2.cpp)

set_property(SOURCE Webnucleo.i PROPERTY CPLUSPLUS ON)
swig_add_library(${PROJECT_NAME}
  TYPE SHARED
  LANGUAGE python
  SOURCES Webnucleo.i webnucleo.cpp
  )
swig_link_libraries(${PROJECT_NAME} tinyxml2)
target_include_directories(${PROJECT_NAME} PUBLIC "")


