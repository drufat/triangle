import numpy
from distutils.core import setup, Extension

setup(name='triangle',
      packages=['triangle'],
      version='0.3',
      description='Python binding to the triangle library',
      author='Dzhelil Rufat',
      author_email='drufat@caltech.edu',
      url='https://github.com/drufat/triangle',
      requires = ['numpy'],
      ext_modules=[Extension('triangle.core', ['c/triangle.c', 'c/triangle_ext.c'],
                             include_dirs = ['c', numpy.get_include()],
                             define_macros = [('NO_TIMER', 1), ('TRILIBRARY', 1)]) 
              ]
      )
