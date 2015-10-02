"""PySend
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysend',

    version='0.0.4',

    description='Unified interface for sending email',
    long_description=long_description,

    url='https://github.com/growdaisy/pysend',

    author='Pokey Rule',
    author_email='pokey@growdaisy.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Communications :: Email',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='email smtp sendgrid',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['requests'],
)
