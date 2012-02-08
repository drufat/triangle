import numpy
from distutils.core import setup, Extension

setup(name='triangle',
      version='0.1',
      requires = ['numpy'],
      description='Python binding to the triangle library',
      author='Dzhelil Rufat',
      author_email='drufat@caltech.edu',
      packages=['triangle'],
      ext_modules=[Extension('triangle.core', ['c/triangle.c', 'c/triangle_ext.c'],
                             include_dirs = (numpy.get_include(), 'c'),
                             define_macros = [('NO_TIMER', 1), ('TRILIBRARY', 1)]) 
              ],
     )
