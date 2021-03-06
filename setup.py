#!/usr/bin/env python

import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(name='rhea',
      version='0.3.6',
      description='Efficient environment variables management and typing for python.',
      maintainer='Mourad Mourafiq',
      maintainer_email='mourad.mourafiq@gmail.com',
      author='Mourad Mourafiq',
      author_email='mourad.mourafiq@gmail.com',
      url='https://github.com/polyaxon/rhea',
      license='MIT',
      platforms='any',
      packages=find_packages(),
      keywords=[
          'polyaxon',
          'dotenv',
          'environ',
          'environment',
          'env-vars',
          '.env',
          'django',
      ],
      install_requires=[
          'PyYAML==3.13',
          'six==1.11.0',
      ],
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP',
      ],
      tests_require=[
          "pytest",
      ],
      cmdclass={'test': PyTest})
