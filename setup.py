from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='coord',
      version=version,
      description="Conversion between different coordinate systems",
      long_description=open('README.md').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='spatial coordinate cartesian spherical cylindrical',
      author='Keith Schulze',
      author_email='keith.schulze@monash.edu',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      )
