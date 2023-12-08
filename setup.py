#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashī Copyright (c) 2022 - Ari Setiawan <hxari@proton.me>
# Kanashī Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Kanashī is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#


from setuptools import setup


#[setup.reader( Str fname )]: Str
def reader( fname:str ) -> str:
	with open( fname, "r" ) as fopen:
		fread = fopen.read()
		fopen.close()
	return fread

# Setup Tool
setup(
    name="kanashi",
    version="1.0.0",
    author="Ari Setiawan (hxAri)",
    author_email="hxari@proton.me",
    maintainer="Ari Setiawan (hxAri)",
    maintainer_email="hxari@proton.me",
    description="",
    packages=['kanashi'],
    # package_dir={ "": "src" },
    provides_extra=reader( "requirements.txt" ).split( "\x0a" ),
    long_description=reader( "README.md" ),
    url="https://github.com/hxAri/Kanashi",
    download_url="https://github.com/hxAri/Kanashi/archive/refs/heads/main.zip",
    license="GNU General Public Licence v3",
    license_file="LICENSE",
    classifiers=[
        "Environment :: CLI Environment",
        "Intended Audience :: Developers",
        "Licence :: GNU General Public Licence v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Command Line Interface",
		"Topic :: Social Media :: Instagram Libraries",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only"
    ]
)
