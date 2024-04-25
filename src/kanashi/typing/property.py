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
	def account( self ) -> Account:
		length = len( self.accounts )
		if self.active >= 1 and self.active <= length:
			return self.accounts[self.active-1]
		return None
	
	@property
	def accounts( self ) -> List[Account]:
		
		""" Return available accounts """
		
		if "accounts" in self:
			return self['accounts']
		return []
	
	...

@final
class Option( Mapping ):
	
	""" Option Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"name",
			"type",
			"value"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
		}
	
	@property
	def name( self ) -> Str:
		if "name" not in self:
			self['name'] = None
		return self['name']
	
	@property
	def type( self ) -> Str:
		if "type" not in self:
			self['type'] = None
		return self['type']
	
	@property
	def value( self ) -> Str:
		if "value" not in self:
			self['value'] = None
		return self['value']
	
	...

@final
class Settings( Mapping ):
	
	""" Setting Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"target",
			"options"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"options": Option
		}
	
	@property
	def target( self ) -> Str:
		
		""" Return the driver executable path """
		
		if "target" not in self:
			self['target'] = None
		return self['target']
	
	@property
	def options( self ) -> List[Option]:
		
		""" Return the driver options """
		
		if "options" not in self:
			self['options'] = []
		return self['options']
	
	...

@final
class Driver( Mapping ):
	
	""" Driver Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"chrome",
			"firefox"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"chrome": Settings,
			"firefox": Settings
		}
	
	@property
	def chrome( self ) -> Settings:
		
		""" Return the chrome driver configurations """
		if "chrome" not in self:
			self['chrome'] = None
		return self['chrome']
	
	@property
	def firefox( self ) -> Settings:
		
		""" Return the firefox driver configurations """
		if "firefox" not in self:
			self['firefox'] = None
		return self['firefox']
	
	...

@final
class Browser( Mapping ):
	
	""" Browser Typing Implementation """
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		return [
			"driver",
			"drivers",
			"uagents"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"drivers": Driver
		}
	
	@property
	def driver( self ) -> Str:
		
		""" ... """
		
		if "driver" not in self:
			self['driver'] = None
		return self['driver']
	
	@property
	def drivers( self ) -> Driver:
		
		""" ... """
		
		if "drivers" not in self:
			self['drivers'] = None
		return self['drivers']
	
	@property
	def uagents( self ) -> List[Str]:
		
		""" ... """
		
		if "uagents" not in self:
			self['uagents'] = None
		return self['uagents']
	
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
			"browser",
			"kanashi"
		]
	
	@property
	def __mapping__( self ) -> MutableMapping[Key,Val]:
		return {
			"authorization": Authorization,
			"browser": Browser,
			"kanashi": Kanashi
		}
	
	@property
	def authorization( self ) -> Authorization:
		
		""" Return authorization property """
		
		if "authorization" not in self:
			self['authorization'] = Authorization()
		return self['authorization']
	
	@property
	def browser( self ) -> Browser:
		
		""" Return browsers property """
		
		if "browser" not in self:
			self['browser'] = Browser()
		return self['browser']
	
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
