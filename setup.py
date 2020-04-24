from setuptools import setup, Extension

version = {}
with open('triangle/version.py') as f:
    exec(f.read(), version)

define_macros = [
    ('VOID', 'void'),
    ('REAL', 'double'),
    ('NO_TIMER', 1),
    ('TRILIBRARY', 1),
    ('ANSI_DECLARATORS', 1),
]

ext_modules = [
    Extension(
        'triangle.core',
        ['c/triangle.c', 'triangle/core.c'],
        include_dirs=['c'],
        define_macros=define_macros,
        # extra_compile_args=['-g'],
    ),
]

setup(
    name='triangle',
    version=version['__version__'],
    description='Python binding to the triangle library',
    author='Dzhelil Rufat',
    author_email='d@rufat.be',
    url='https://rufat.be/triangle',
    packages=['triangle'],
    package_data={
        'triangle': [
            'data/*.node',
            'data/*.ele',
            'data/*.poly',
            'data/*.area',
            'data/*.edge',
            'data/*.neigh',
        ]
    },
    install_requires=[
        'numpy',
    ],
    ext_modules=ext_modules,
    license='LGPLv3',
)
