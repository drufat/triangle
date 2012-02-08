cmake_minimum_required(VERSION 2.6)

add_definitions( 
	-DNO_TIMER
	-DNDEBUG
	-DTRILIBRARY
)

include_directories(
    ../c
    ${PYTHON_INCLUDE_DIRS}
    ${NUMPY_INCLUDE_DIR}
)

add_python_module(core ../c/triangle_ext.c ../c/triangle.c)
