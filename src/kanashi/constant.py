#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
# Follow, Unfollow, Media downloader, etc.
#
# Kanashi Copyright (c) 2024 - hxAri <hxari@proton.me>
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

from builtins import str as Str
from os import getenv
from sys import path as paths
from typing import MutableSequence


__all__ = (
	"BasePath",
	"BaseVenv",
	"HomePath",
	"SelfPath"
)


BaseParts:MutableSequence[Str] = paths[0].split( "\x2f" )
BasePath:Str = "\x2f".join( BaseParts[:BaseParts.index( "src" )] )
""" The Base Path of Application """

BaseParts:MutableSequence[Str] = paths[4].split( "\x2f" )
BaseVenv:Str = "\x2f".join( BaseParts[:BaseParts.index( "lib" )] )
""" The Base Path of Virtual Environment """

HomePath:Str = getenv( "HOME" )
""" The Home Path of User Previlege """

SelfPath:Str = "\x34\x62\x36\x31\x36\x65\x36\x31\x37\x33\x36\x38\x36\x39"
""" The Self Path Application """

del BaseParts
