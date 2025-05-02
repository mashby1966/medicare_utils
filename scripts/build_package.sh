#!/bin/bash
set -e
rm -rf build dist *.egg-info
python setup.py sdist bdist_wheel
ls -lh dist/
echo "\nPackage built successfully. Use: pip install dist/<file>.whl"
