#!/usr/bin/env bash

VERSION=`python -c "exec(open('triangle/version.py').read()); print(__version__)"`
echo v$VERSION

echo v$VERSION
git push --version
python setup.py sdist
twine upload dist/*