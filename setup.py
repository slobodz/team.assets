import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# Sample setup.py

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='team.assets',
    version='1.0',
    author='team-polska',
    author_email='build.teamexport@gmail.com',
    description='Team asstes sync',
    dependency_links=['https://teampypi.herokuapp.com/'],
    install_requires=required,
    url='https://github.com/slobodz/team.assets'
)