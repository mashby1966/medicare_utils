from setuptools import setup, find_packages
import os
import re

def get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "medicare_utils", "__init__.py")) as f:
        content = f.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="medicare_utils",
    version=get_version(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'medicareutil=medicare_utils.cli:main'
        ]
    },
    install_requires=[],
    author="Your Name",
    description="Utilities for handling Australian Medicare numbers",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
