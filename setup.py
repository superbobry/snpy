#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

# Use 2to3 build conversion if required
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

setup(
    name="snpy",
    description="A wrapper-library for working with openSNP data",
    license="WTFPL",
    version="0.1",
    author="Sergei Lebedev",
    author_email="superbobry@gmail.com",
    url="http://github.com/superbobry/snpy/",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        ],
    py_modules=["sn"],
    platforms="any",
    cmdclass={"build_py": build_py}
    )
