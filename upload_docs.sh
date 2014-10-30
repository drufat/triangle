#!/usr/bin/env bash

repo=`mktemp -d`
git clone git@github:drufat/triangle.git ${repo}

(
    cd ${repo}
    git checkout gh-pages
    git rm -rf .
)

sphinx-build -b html doc ${repo}

(
    cd ${repo}
    touch .nojekyll
    git add .
    git commit -a -m "Update documents."
    git push origin gh-pages
)

rm -rf ${tmp}
