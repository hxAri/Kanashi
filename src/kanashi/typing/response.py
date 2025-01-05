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

from builtins import bool as Bool, bytes as Bytes, int as Int, str as Str
from json import loads as JsonDecoder
from re import IGNORECASE
from re import match
from requests.cookies import RequestsCookieJar
from requests.structures import CaseInsensitiveDict
from typing import Any, final, MutableMapping, MutableSequence, Union


__all__ = [
	"Response"
]


@final
class Response:
	
	""" HTTP Request Typing Implementation """
	
	url:Str
	""" HTTP Request URL """
	
	text:Str
	""" HTTP Response content raw """
	
	type:Str
	""" HTTP Response content type """
	
	status:Int
	""" HTTP Response status code """
	
	payload:Any
	""" HTTP Request payload """
	
	content:Bytes
	""" HTTP Response content raw (Bytes) """
	
	cookies:RequestsCookieJar
	""" HTTP Response cookies """
	
	headers:CaseInsensitiveDict
	""" HTTP Response headers """
	
	charset:Str
	""" HTTP Response content character-set """
	
	encoding:Str
	""" HTTP Response content encoding """
	
	def __init__( self, url:Str, text:Str, type:Str, status:Int, payload:Any, content:Bytes, cookies:RequestsCookieJar, headers:CaseInsensitiveDict, charset:Str, encoding:Str ) -> None:
		
		"""
		Construct method of class Response
		
		Parameters:
			url (Str):
				Request url
			text (Str):
				Request response text
			type (Str):
				Request response content type
			status (Int):
				Request response status code
			payload (Any):
				Request payload
			content (Bytes):
				Request response content byte
			cookies (RequestsCookieJar):
				Request response cookies
			headers (CaseInsensitiveDict):
				Request response headers
			charset (Str):
				Request response content character set
			encoding (Str):
				Request response content encoding
		"""
		
		self.url = url
		self.text = text
		self.type = type
		self.status = status
		self.payload = payload
		self.content = content
		self.cookies = cookies
		self.headers = headers
		self.charset = charset
		self.encoding = encoding
	
	def __repr__( self ) -> Str:
		return f"<Response url=\"{self.url}\" type={self.type} status={self.status} charset={self.charset} encoding={self.encoding} />"
	
	@property
	def isApplicationJson( self ) -> Bool:
		return match( "^(?:application/json)$", self.type if self.type is not None else "", IGNORECASE ) is not None
	
	@property
	def isJavaScript( self ) -> Bool:
		return match( "^(?:text/javascript)$", self.type if self.type is not None else "", IGNORECASE ) is not None
	
	@property
	def json( self ) -> Union[MutableMapping[Str,Any],MutableSequence[Any]]:
		if self.content and self.isApplicationJson is True:
			return JsonDecoder( self.content )
		return None
	
	...
