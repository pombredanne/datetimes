#!/usr/bin/env python

import os
import sys

import datetimes

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'datetimes',
]

requires = []

setup(
    name='datetimes',
    description='Extended Python Datetime',
    long_description=open('README.md').read(),
    author='Soshio',
    author_email='tech@getsoshio.com',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'datetimes': ['*.pem']},
    package_dir={'datetimes': 'datetimes'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',

    ),
)