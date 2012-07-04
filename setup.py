import numpy
from distutils.core import setup, Extension

setup(name='triangle',
      packages=['triangle'],
      version='2012.07.04',
      description='Python binding to the triangle library',
      author='Dzhelil Rufat',
      author_email='drufat@caltech.edu',
      url='http://drufat.github.com/triangle',
      requires = ['numpy'],
      ext_modules=[Extension('triangle.core', ['c/triangle.c', 'c/triangle_ext.c'],
                             include_dirs = ['c', numpy.get_include()],
                             define_macros = [('NO_TIMER', 1),
                                              ('TRILIBRARY', 1),
                                              ('ANSI_DECLARATORS', 1)])])
