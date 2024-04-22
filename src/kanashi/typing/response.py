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

from builtins import bool as Bool, bytes as Bytes, int as Int, str as Str
from json import loads as JsonDecoder
from re import IGNORECASE
from re import match
from typing import Any, final, MutableMapping, MutableSequence, Union

from kanashi.typing.readonly import Readonly


@final
class Response( Readonly ):
	
	""" HTTP Request Typing Implementation """
	
	def __init__( self, url:Str, raw:Str, type:Str, status:Int, payload:Any, content:Bytes, cookies:MutableMapping[Str,Any], headers:MutableMapping[Str,Any], charset:Str, encoding:Str ) -> None:
		
		"""
		Construct method of class Response
		
		:params Str url
		:params Str raw
		:params Str type
		:params Int status
		:params Any payload
		:params Bytes content
		:params MutableMapping<Str,Any> cookies
		:params MutableMapping<Str,Any> headers
		:params Str charset
		:params Str encoding
		
		return None
		"""
		
		self.url:Str = url
		""" HTTP Request URL """
		
		self.raw:Str = raw
		""" HTTP Response content raw """
		
		self.type:Str = type
		""" HTTP Response content type """
		
		self.status:Int = status
		""" HTTP Response status code """
		
		self.payload:Any = payload
		""" HTTP Request payload """
		
		self.content:Bytes = content
		""" HTTP Response content raw (Bytes) """
		
		self.cookies:MutableMapping[Str,Any] = cookies
		""" HTTP Response cookies """
		
		self.headers:MutableMapping[Str,Any] = headers
		""" HTTP Response headers """
		
		self.charset:Str = charset
		""" HTTP Response content character-set """
		
		self.encoding:Str = encoding
		""" HTTP Response content encoding """
	
	def __repr__( self ) -> Str:
		return f"<Response url=\"{self.url}\" type={self.type} status={self.status} charset={self.charset} encoding={self.encoding} />"
	
	@property
	def isApplicationJson( self ) -> Bool:
		return match( "^(?:application/json)$", self.type if self.type is not None else "", IGNORECASE )
	
	@property
	def json( self ) -> Union[MutableMapping[Str,Any],MutableSequence[Any]]:
		if self.content and self.isApplicationJson is True:
			return JsonDecoder( self.content )
		return None
	
	...
