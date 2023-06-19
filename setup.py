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

from kanashi import Config, File
from setuptools import find_packages, setup


# Module Requirements
requirements = File.readline( "requirements.txt" )

# Setup Tool
setup(
    name = "kanashi",
    author = Config.AUTHOR,
    author_email = Config.AUTHOR_EMAIL,
    version = Config.VERSION,
    license = Config.LICENSE,
    url = Config.REPOSITORY,
    install_requires = requirements,
    keywords = [
        "instagram",
        "instagram-login", "instagram-image",
        "instagram-video", "instagram-feeds",
        "instagram-story", "instagram-private",
        "instagram-cookie", "instagram-session",
        "linux",
        "termux",
        "android",
    ],
    description = "Kanashi is an open source project that can be used to login to real Instagram accounts via Linux Terminal and Android Termux.",
    packages = find_packages(),
    python_requires = ">=3.10.4",
    include_package_data = True
)