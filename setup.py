#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages
# use the same encoding in python 3 and 2
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# ref: https://pypi.python.org/pypi/pytest-runner
# Because it uses Setuptools setup_requires, pytest-runner will install itself on every invocation of setup.py.
# In some cases, this causes delays for invocations of setup.py that will never invoke pytest-runner.
# Avoid this contingency, by requiring pytest-runner only when pytest is invoked
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner >=2.0, <3',] if needs_pytest else []
setup_requires = [] + pytest_runner

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
    install_requires=['pexpect >=4, <5'],
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
    setup_requires=setup_requires,
    tests_require=[
        'pytest >=3.0.6, <4',
        'pytest-cov >=2.4.0, <3'
    ],
)
