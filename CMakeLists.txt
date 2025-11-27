cmake_minimum_required(VERSION 3.12)
project(spackexample VERSION 0.3.1 LANGUAGES CXX)

option(WITH_BOOST "build with filesystem functionality" OFF)
option(WITH_YAML  "build with YAML parser functionality" OFF)

set(SOURCE_FILES main.cpp)

if(WITH_BOOST)
  find_package(Boost 1.65.1 REQUIRED COMPONENTS filesystem)
  list(APPEND SOURCE_FILES
       filesystem/filesystem.cpp
       flatset/flatset.cpp)
endif()

if(WITH_YAML)
  find_package(yaml-cpp 0.7.0 REQUIRED)
  list(APPEND SOURCE_FILES
       yamlParser/yamlParser.cpp)
endif()

add_executable(spackexample ${SOURCE_FILES})

if(WITH_BOOST)
  target_link_libraries(spackexample PRIVATE Boost::filesystem)
  target_compile_definitions(spackexample PRIVATE WITH_BOOST)
endif()

if(WITH_YAML)
  target_link_libraries(spackexample PRIVATE yaml-cpp::yaml-cpp)
  target_compile_definitions(spackexample PRIVATE WITH_YAML)
endif()

include(GNUInstallDirs)
install(TARGETS spackexample RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
