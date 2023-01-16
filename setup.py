from setuptools import setup, Extension


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

# see pyproject.toml for other metadata
setup(
    name='triangle',
    ext_modules=ext_modules,
)
