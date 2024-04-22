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

from builtins import int as Int, str as Str
from typing import Any, Dict, final, List, MutableMapping, MutableSequence, Union

from kanashi.typing.account import Account
from kanashi.typing.builtins import Key,Val
from kanashi.typing.map import Mapping
from kanashi.typing.readonly import Readonly


@final
class Author( Mapping, Readonly ):
	
	""" Author Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"name",
			"email",
			"github"
		]
	
	@property
	def name( self ) -> Str:
		
		""" The Author Name """
		
		return self['name'] if "name" in self else None
	
	@property
	def email( self ) -> Str:
		
		""" The Author Email Address """
		
		return self['email'] if "email" in self else None
	
	@property
	def github( self ) -> Str:
		
		""" The Author Github Username """
		
		return self['github'] if "github" in self else None
	
	...

@final
class Authorization( Mapping ):
	
	""" Authorization Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"active",
			"accounts"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"accounts": Account
		}
	
	@property
	def active( self ) -> Int:
		
		""" Return current account active position """
		
		if "active" in self:
			return self['active']
		return 0
	
	@property
	def accounts( self ) -> List[Account]:
		
		""" Return available accounts """
		
		if "accounts" in self:
			return self['accounts']
		return []
	
	...

@final
class Kanashi( Mapping ):
	
	""" Kanashi Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"author", 
			"description", 
			"environment", 
			"homepage", 
			"issues", 
			"repository", 
			"version" 
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"author": Author
		}
	
	@property
	def author( self ) -> Author:
		
		""" Return author information """
		
		if "author" not in self:
			self['author'] = Author()
		return self['author']
	
	@property
	def description( self ) -> Str:
		
		""" Return Kanashi description """
		
		return self['description'] if "description" in self else None
	
	@property
	def environment( self ) -> Str:
		
		""" Return current application environment """
		
		return self['environment'] if "environment" in self else None
	
	@property
	def homepage( self ) -> Str:
		
		""" Return Kanashi homepage url """
		
		return self['homepage'] if "homepage" in self else None
	
	@property
	def issues( self ) -> Str:
		
		""" Return kanashi issue url """
		
		return self['issues'] if "issues" in self else None
	
	@property
	def repository( self ) -> Str:
		
		""" Return kanashi repository url """
		
		return self['repository'] if "repository" in self else None
	
	@property
	def version( self ) -> Str:
		
		""" Return current kanashi version """
		
		return self['version'] if "version" in self else None
	
	...

@final
class Property( Mapping, Readonly ):
	
	""" Property Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"authorization",
			"browsers",
			"kanashi"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"authorization": Authorization,
			"kanashi": Kanashi
		}
	
	@property
	def authorization( self ) -> Authorization:
		
		""" Return authorization property """
		
		if "authorization" not in self:
			self['authorization'] = Authorization()
		return self['authorization']
	
	@property
	def browsers( self ) -> List[Str]:
		
		""" Return browsers User-Agent """
		
		if "browsers" not in self:
			self['browsers'] = []
		return self['browsers']
	
	@property
	def kanashi( self ) -> Kanashi:
		
		""" Return kanashi property info """
		
		if "kanashi" not in self:
			self['kanashi'] = Kanashi()
		return self['kanashi']
	
	@property
	def contents( self ) -> Dict[Str,Any]:
		
		""" Return kanashi properties as dictionary """
		
		browsers = Properties.browsers
		accounts = []
		for account in self.authorization.accounts:
			accounts.append({
				"cookies": account.cookies,
				"headers": account.headers,
				"payload": account.payload,
				"username": account.username,
				"password": account.password
			})
		active = Properties.authorization.active
		kanashi = {
			"author": {
				"name": Properties.kanashi.author.name,
				"email": Properties.kanashi.author.email,
				"github": Properties.kanashi.author.github
			},
			"description": Properties.kanashi.description,
			"environment": Properties.kanashi.environment,
			"homepage": Properties.kanashi.homepage,
			"issues": Properties.kanashi.issues,
			"repository": Properties.kanashi.repository,
			"version": Properties.kanashi.version
		}
		return {
			"authorization": {
				"active": active,
				"accounts": accounts
			},
			"browsers": browsers,
			"kanashi": kanashi
		}
	
	...


Properties:Property = Property()
""" Global Kanashi Configuration """
