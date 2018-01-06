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
    version='1.0.0',
    description='Python Bindings for OpenNebula XML-RPC API',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/privazio/pyone',

    # Author details
    author='Rafael del Valle',
    author_email='rvalle@privaz.io',

    # Choose your license
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='cloud opennebula xmlrpc bindings',
    packages=['pyone'],
    install_requires=['PyXB', 'dicttoxml'],

    package_data={
        'pyone': ['xsd/*.xsd'],
    },

    test_suite="tests"
)
