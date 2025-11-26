cmake_minimum_required(VERSION 3.12)
project(spackexample VERSION 0.3.1)

option(WITH_BOOST "Build with filesystem functionality" OFF)
option(WITH_YAML "Build with YAML parser functionality" OFF)

# ---------------------------------------------------------------------------
# Collect sources and headers conditionally
# ---------------------------------------------------------------------------
set(SRCS "")
if(WITH_BOOST)
set(SRCS
  flatset/flatset.cpp
)

set(PUBLIC_HEADERS
  flatset/flatset.hpp
)
  find_package(Boost 1.65.1 REQUIRED filesystem)
  list(APPEND SRCS filesystem/filesystem.cpp)
  list(APPEND PUBLIC_HEADERS filesystem/filesystem.hpp)
endif()

if(WITH_YAML)
  find_package(yaml-cpp 0.7.0 REQUIRED)
  list(APPEND SRCS yamlParser/yamlParser.cpp)
  list(APPEND PUBLIC_HEADERS yamlParser/yamlParser.hpp)
endif()

# ---------------------------------------------------------------------------
# Define the library (once)
# ---------------------------------------------------------------------------
add_library(spackexamplelib ${SRCS})

set_target_properties(spackexamplelib PROPERTIES
  PUBLIC_HEADER "${PUBLIC_HEADERS}"
)

# ---------------------------------------------------------------------------
# Include directories
# ---------------------------------------------------------------------------
target_include_directories(spackexamplelib
  PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/spackexamplelib>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}/spackexamplelib>
)

# ---------------------------------------------------------------------------
# Link conditional dependencies
# ---------------------------------------------------------------------------
if(WITH_BOOST)
  target_link_libraries(spackexamplelib PUBLIC Boost::filesystem)
endif()

if(WITH_YAML)
  target_link_libraries(spackexamplelib PUBLIC yaml-cpp)
  target_include_directories(spackexamplelib PRIVATE ${YAML_CPP_INCLUDE_DIR})
endif()

# ---------------------------------------------------------------------------
# Executable
# ---------------------------------------------------------------------------
add_executable(spackexample main.cpp)
target_link_libraries(spackexample PRIVATE spackexamplelib)

# ---------------------------------------------------------------------------
# Install targets
# ---------------------------------------------------------------------------
include(GNUInstallDirs)
install(TARGETS spackexample spackexamplelib
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
  INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/spackexample
)
