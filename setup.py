# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "tinker_partner_api"
VERSION = "0.2.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.10",
    "six >= 1.9",
    "certifi",
    "python-dateutil"
]

setup(
    name=NAME,
    version=VERSION,
    description="Tinker Partner API Client",
    author_email="",
    url="",
    keywords=["tinker", "api-client"],
    install_requires=REQUIRES,
    packages=find_packages("tinker_partner_api"),
    include_package_data=True,
    long_description="""\
        This is a handcrafted wrapper around the swagger generated code for the Tinker Partner API.

        Works with version 3.2+ and `python2` with an up to date pyOpenSSL.
    """
)


