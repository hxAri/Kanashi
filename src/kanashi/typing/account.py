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

from builtins import bool as Bool, str as Str
from typing import Any, final, Literal, MutableMapping, Union
from urllib.parse import unquote

from kanashi.typing.map import Map
from kanashi.typing.readonly import Readonly


@final
class Account( Readonly ):
	
	""" Account Typing Implementation """
	
	def __init__( self, username:Str, password:Str, cookies:Union[MutableMapping[Str,Any],Str]=None, headers:MutableMapping[Str,Str]=None, graphql:MutableMapping[Union[Literal['headers'],Literal['payload']],MutableMapping[Str,Any]]=None, proxies:MutableMapping[Str,Str]=None, profile:MutableMapping[Str,Any]=None ) -> None:
		
		"""
		Construct method of class Account
		
		:params Str username
			Account Username
		:params Str password
			Account Password
		:params MutableMapping<Str,Any>|Str cookies
			Account Request Cookies
		:params Mapping<Str,Str> headers
			Account Request Headers
		:params MutableMapping<Literal<headers|payload>,MutableMapping<Str,Any>> graphql
			Account Request Graphql
		:params MutableMapping<Str,Str> proxies
			Account Request Proxies
		:params MutableMapping<Str,Any> profile
			Account Profile info
		
		:return None
		"""
		
		if isinstance( cookies, Str ):
			explode = cookies.split( "\x3b\x20" )
			cookies = {}
			for part in explode:
				parts = part.split( "\x3d" )
				cookies[parts[0]] = unquote( parts[1] )
		
		self.cookies:MutableMapping[Str,Any] = cookies if cookies is not None else {}
		""" Account Request Cookies """
		
		self.headers:MutableMapping[Str,Str] = headers if headers is not None else {}
		""" Account Request Headers """
		
		self.graphql:MutableMapping[Union[Literal['headers'],Literal['payload']],MutableMapping[Str,Any]] = graphql if graphql is not None else { "headers": {}, "payload": {} }
		""" Account Request Graphql """
		
		self.proxies:MutableMapping[Str,Str] = proxies
		""" Account Request Proxies """
		
		self.username:Str = username
		""" Account Username """
		
		self.password:Str = password
		""" Account Password """
		
		self.profile:Map[Str,Any] = Map( profile if profile is not None else {} )
		""" Account Profile Info """
	
	@property
	def anonymous( self ) -> Bool:
		
		""" Return whether if account is anonymous """
		
		return self.username is None and self.password is None
	
	@property
	def authenticated( self ) -> Bool:
		
		""" Return whether if account is authenticated """
		
		if self.anonymous is False:
			if self.cookies is not None and self.cookies and \
			   self.headers is not None and self.headers and \
			   self.graphql is not None and self.graphql and \
			   self.graphql['payload'] is not None and \
			   self.graphql['payload']:
				for keyset in [ "mid", "rur", "datr", "sessionid", "shbid", "shbts", "ig_did" ]:
					if keyset not in self.cookies or not self.cookies[keyset]:
						return False
				for keyset in [ "av", "lsd" ]:
					if keyset not in self.graphql['payload'] or not self.graphql['payload'][keyset]:
						return False
				return True
			return False
		return True
	
	...

@final
class Checkpoint( Readonly ):
	
	...
	
@final
class Verification( Readonly ):
	
	...
