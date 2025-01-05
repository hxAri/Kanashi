#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Facebook, e.g Login. Logout, Profile Info,
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

from builtins import int as Int, str as Str
from typing import final


__all__ = [
	"Schema"
]


@final
class Schema:
	
	""" Kanashi Graphql Schema """
	
	__api__:Str
	__doc__:Int
	
	def __init__( self, api:Str, doc:Int ):
		
		"""
		Construct method of class Schema
		
		Parameters:
			api (Str):
				Kanashi API request friendly name
			doc (Int):
				Kanashi query doc
		"""
		
		self.__api__ = api
		self.__doc__ = doc
	
	def __str__( self ) -> Str: return f"{self.api}:{self.doc}:"
	
	@property
	def api( self ) -> Str: return self.__api__
	
	@property
	def doc( self ) -> Int: return self.__doc__
	
	...

