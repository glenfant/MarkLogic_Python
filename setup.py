# -*- coding: utf-8 -*-
#
# Copyright 2015 MarkLogic Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0#
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Note that this code was taken from an example on using PyPi.
#
from __future__ import unicode_literals, print_function, absolute_import

import io
import os
from setuptools import setup, find_packages

__author__ = 'phoehne'
__version__ = '0.0.1.dev1'

_this_directory = os.path.abspath(os.path.dirname(__file__))


def _read(*names):
    return io.open(os.path.join(_this_directory, *names), 'r').read().strip()

_long_description = '\n\n'.join(
    [_read(*names) for names in (('README.rst',), ('CHANGES.rst',))]
    )

setup(
    name="marklogic",
    version=__version__,

    packages=find_packages(exclude=["tests", "examples"]),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'requests>=2.5.0'
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',

    # metadata for upload to PyPI
    description="MarkLogic package for maintaining servers",
    long_description=_long_description,
    author="Paul Hoehne",
    author_email="paul.hoehne@marklogic.com",
    license="Apache",
    keywords="MarkLogic rest management",
    url="http://github.com/paul-hoehne/MarkLogic_Python/",   # project home page, if any
    classifiers=[
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: Apache Software License"
    ]
)
