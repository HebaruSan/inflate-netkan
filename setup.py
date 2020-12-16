#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='InflateNetkan',
    version='0.1',
    description='Submits a Netkan to the queue for inflation',
    author='HebaruSan',
    package_data={
        "": ["*.txt"],
    },
    entry_points={
        'console_scripts': [
            'inflate-netkan=inflate_netkan:inflate_netkan',
        ],
    },
    packages=find_packages(),
    install_requires=[
        'gitpython',
        'exitstatus',
    ],
    extras_require={
        'development': [
            'pylint',
            'autopep8',
            'mypy',
        ]
    },
)
