# Copyright 2018 www.privaz.io Valletech AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyone',
    version='1.0.3',
    description='Python Bindings for OpenNebula XML-RPC API',
    long_description=long_description,

    # The project's main homepage.
    url='http://privaz.io',

    # Author details
    author='Rafael del Valle',
    author_email='rvalle@privaz.io',

    # Choose your license
    license='http://www.apache.org/licenses/LICENSE-2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='cloud opennebula xmlrpc bindings',
    packages=['pyone', 'pyone.bindings'],
    install_requires=['PyXB', 'dicttoxml'],
    package_data={
        'pyone': ['xsd/*.xsd'],
    },
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    test_suite="tests"
)
