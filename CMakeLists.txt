cmake_minimum_required(VERSION 2.6)
set(CMAKE_MODULE_PATH ~/Dev/cmake)

find_package(Python REQUIRED)
find_package(Numpy REQUIRED)

add_subdirectory(triangle)
