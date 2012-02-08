cmake_minimum_required(VERSION 2.6)

add_definitions( 
	-DNO_TIMER
	-DNDEBUG
	-DTRILIBRARY
)

add_library(triangle triangle.c)

add_executable(tricall tricall)
target_link_libraries(tricall triangle)
if (UNIX)
    target_link_libraries(tricall m)
endif(UNIX)
