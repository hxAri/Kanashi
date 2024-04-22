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

from builtins import bool as Bool, int as Int, str as Str
from typing import Any, final, MutableMapping, Union
from urllib.parse import unquote

from kanashi.typing.readonly import Readonly


@final
class Account( Readonly ):
	
	""" Account Typing Implementation """
	
	def __init__( self, cookies:Union[MutableMapping[Str,Any],Str], headers:MutableMapping[Str,Str], payload:MutableMapping[Str,Any], username:Str, password:Str ) -> None:
		
		"""
		Construct method of class Account
		
		:params MutableMapping<Str,Any>|Str cookies
			Account Request Cookies
		:params Mapping<Str,Str> headers
			Account Request Headers
		:params Mapping<Str,Any> payload
			Account Graphql Payload
		:params Str username
			Account Username
		:params Str password
			Account Password
		
		:return None
		"""
		
		if isinstance( cookies, Str ):
			explode = cookies.split( "\x3b\x20" )
			cookies = {}
			for part in explode:
				parts = part.split( "\x3d" )
				cookies[parts[0]] = unquote( parts[1] )
		
		self.cookies:Union[MutableMapping[Str,Any],Str] = cookies
		""" Account Request Cookies """
		
		self.headers:MutableMapping[Str,Str] = headers
		""" Account Request Headers """
		
		self.payload:MutableMapping[Str,Any] = payload
		""" Account Graphql Payload """
		
		self.username:Str = username
		""" Account Username """
		
		self.password:Str = password
		""" Account Password """
	
	@property
	def anonimous( self ) -> Bool:
		
		""" Return whether if account is anonimous """
		
		return self.username is None and self.password is None
	
	@property
	def authenticated( self ) -> Bool:
		
		""" Return whether if account is authenticated """
		
		if self.anonimous is False:
			if self.cookies is not None and self.cookies and \
			   self.headers is not None and self.headers and \
			   self.payload is not None and self.payload:
				for keyset in [ "rur", "sessionid", "shbid", "shbts" ]:
					if keyset not in self.cookies or not self.cookies[keyset]:
						continue
					return False
				for keyset in [ "av", "lsd" ]:
					if keyset not in self.payload or not self.payload[keyset]:
						continue
					return False
				return True
			...
		return False
	
	...
