#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashi Copyright (c) 2022 - Ari Setiawan <ari160824@gmail.com>
# Kanashi Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Kanashi is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from setuptools import find_packages, setup

# Module Requirements
requirements = [
	"requests>=2.28.1"
]

# Setup Tool
setup(
    name = "kanashi",
    author = "Ari Setiawan",
    author_email = "ari160824@gmail.com",
    version = "1.1.4",
    license = "GNU General Public License v3",
    url = "https://github.com/hxAri/Kanashi",
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
