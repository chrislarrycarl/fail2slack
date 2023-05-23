#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fail2slack',
    version='0.4.0',
    description='Send fail2ban jail status updates to Slack.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPL-2.0',
    packages=find_packages(),
    author='Chris Carlevato',
    author_email='hello@asdf.dev',
    keywords=['fail2ban', 'slack'],
    url='https://github.com/asdfdotdev/fail2slack',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security",
        "Topic :: System",
        "Topic :: Utilities",
    ],
    install_requires=[
        'argparse==1.4.0',
        'requests==2.31.0',
        'validators==0.18.2',
    ],
)
