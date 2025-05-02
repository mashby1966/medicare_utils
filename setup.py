from setuptools import setup, find_packages

setup(
    name="medicare_utils",
    version=__version__,
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
