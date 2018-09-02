#!/usr/bin/env python
from distutils.core import setup

VERSION = 0.0.0.a

setup(
    name='pyjsutils',
    version=VERSION,
    packages=['pyjsutils'],
    url='https://github.com/abdulmoizeng/pyjsutils',
    license='MIT',
    author='Muhammad AbdulMoiz',
    author_email='abdulmoizeng@gmail.com',
    description='Javascript like python utilities.',
    long_description=open('README').read(),
    keywords=['python', 'js', 'utilities']
)