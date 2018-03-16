#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import bringbuf

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='bringbuf',
    version=bringbuf.__version__,
    description='A simple circular buffer to handle byte streams (for instance from a serial port), heavily based on enque.',
    long_description=read('README.rst'),
    author='Andreas Gschossmann',
    author_email='ghandi_84@hotmail.com',
    url='http://github.com/ticktronaut/bringbuf',
    license='MIT',
    python_requires='>=3',
    py_modules=['bringbuf.bringbuf'],
    packages=find_packages(exclude=['virtenv'])
    #py_modules=['bringbuf']
    #install_requires=['collections', 'itertools', 'warnings'],
    #include_package_data=True
)
