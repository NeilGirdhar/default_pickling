#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='default_pickling',
    version='0.3',
    description=(
        'A base class that provides default pickling and copying method '
        'implementations for use in inheritance.'),
    author='Neil Girdhar',
    author_email='mistersheik@gmail.com',
    project_urls={
        "Bug Tracker":
        "https://github.com/NeilGirdhar/default_pickling/issues",
        "Source Code": "https://github.com/NeilGirdhar/default_pickling",
    },
    download_url = "https://pypi.python.org/pypi/default_pickling",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=['testing', 'logging', 'example'],
    python_requires='>=3.7',
    setup_requires=[],
    tests_require=[],
)
