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

from abc import ABC as Abstract, abstractmethod as abstract
from builtins import int as Int, str as Str
from typing import (
	Any, 
	Iterable, 
	MutableMapping, 
	MutableSequence, 
	Tuple, 
	TypeVar as Var, 
	Union
)


__all__ = [
	"Parser"
]


Cursor = Var( "Cursor", bytes, str )
""" Cursor Type """

Params = Var( "Params", dict, MutableMapping )
""" Params Type """

Result = Var( "Result", dict, list, MutableMapping, MutableSequence )
""" Result Type """


class Parser( Abstract ):
	
	""" Base abstract class for Parser """
	
	def __init__( self ) -> None:
		
		""" Construct method of class Parser """
		
		raise NotImplementedError( f"Class {type( self ).__qualname__} is not implemented" )
	
	@abstract
	def parser( self, response:Union[MutableMapping[Str,Any],MutableSequence[MutableMapping[Str,Any]]], thread:Union[Int,Str]=0 ) -> Union[Result,Tuple[Cursor,Params,Result]]:
		
		"""
		The graphql response parser
		
		Parameters:
			response (MutableMapping[Str,Any]|MutableSequence[MutableMapping[Str,Any]]):
				Normalized request response content
			thread (Int|Str):
				Current thread position number
		
		Returns:
			results (Result|Tuple[Cursor,Params,Result]):
				Return result graphql parsed
		"""
	
	...
