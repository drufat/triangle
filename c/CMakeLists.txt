cmake_minimum_required(VERSION 2.6)

add_definitions( 
    -DVOID=int
    -DREAL=double
    -DNO_TIMER
    -DANSI_DECLARATORS
)

add_executable(tricall tricall.c triangle.c)
target_link_libraries(tricall m)
set_target_properties (tricall PROPERTIES COMPILE_DEFINITIONS "TRILIBRARY")

add_executable(triangle triangle.c)
target_link_libraries(triangle m)
