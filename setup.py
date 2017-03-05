#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
# use the same encoding in python 3 and 2
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='raspyemu',
    version='0.1.0.dev0',
    description='raspyemu',
    long_description=long_description,
    url='https://github.com/pypa/raspyemu',
    author='Dennis Bing Yu',
    author_email='fall7standup8@gmail.com',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Emulators',
        'Topic :: Utilities',
    ],
    keywords='RaspberryPi rpi qemu emulator',
    packages=find_packages(exclude=['tests']),
    # external packages
    install_requires=['pexpect >= 4, <5'],
    # eg:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'raspyemu=raspyemu.cli:main',
        ],
    },
)
