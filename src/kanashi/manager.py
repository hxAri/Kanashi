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

from builtins import bool as Bool, int as Int, str as Str
from json import dumps as JsonEncoder, loads as JsonDecoder
from os import makedirs as mkdir
from os.path import isdir, isfile
from typing import (
	final, 
	Iterable, 
	Literal, 
	MutableMapping, 
	MutableSequence, 
	Optional, 
	Union
)

from kanashi.client import create as ClientBuilder
from kanashi.constant import HomePath, SelfPath
from kanashi.logger import Logger
from kanashi.typing import Account


__all__ = [
	"Manager"
]


@final
class Manager:
	
	"""
	Kanashi Account Manager
	
	This is just for manage account, this is not 
	requirement program except main program
	
	Examples:
	>>> manager = Manager()
	>>> account = manager.account( "guests" )
	>>> print( account.mapping )
	>>> manager.account( "guests", account )
	>>> manager.configs['session'] = manager.encoder( "guests" )
	>>> manager.update()
	"""
	
	anonymous:Str
	""" Guest or Anonymous previlege """
	
	configs:MutableMapping[Literal[ "accounts", "session" ],Union[MutableSequence[Str],Str]]
	""" Account Configuration """
	
	encoding:Str
	""" File Content Encoding """
	
	logger:Logger
	""" Logger Instance """
	
	pathname:MutableMapping[Literal[ "account", "basepath", "configs" ],Str]
	""" Application Pathnames """
	
	def __init__( self ) -> None:
		
		""" Construct method of class Manager """
		
		self.logger = Logger( self )
		self.anonymous = "\x36\x37\x37\x35\x36\x35\x37\x33\x37\x34"
		self.encoding = "UTF-8"
		self.pathname = dict(
			basepath=f"{HomePath}/.{SelfPath}",
			account=f"{HomePath}/.{SelfPath}/f978X8xiCEI9k40w",
			configs=f"{HomePath}/.{SelfPath}/0fNSpdrGDHu2E7cV"
		)
		if not isdir( self.pathname['basepath'] ):
			mkdir( self.pathname['basepath'] )
		if not isdir( self.pathname['account'] ):
			mkdir( self.pathname['account'] )
		self.configs = { "accounts": [], "session": None }
	
	def account( self, username:Str ) -> Account:
		
		"""
		Load account by username
		
		Parameters:
			username (Str):
				Account username
		
		Returns:
			Account:
				Account typing instance
		
		Raises:
			TypeError:
				Raises when account not found
		"""
		
		self.logger.info( "Trying to load account: {}", username )
		keyset = self.encoder( username )
		account = None
		filename = f"{self.pathname['account']}/{keyset}"
		if not self.exists( username ):
			raise TypeError( f"No such account username={username}" )
		with open( filename, "r", encoding=self.encoding ) as fopen:
			account = Account( **JsonDecoder( fopen.read() ) )
			fopen.close()
		return account
	
	def accounts( self ) -> Iterable[Account]:
		
		""" Iterate all accounts """
		
		self.logger.info( "Trying iterating all accounts" )
		for account in self.configs['accounts']:
			yield self.account( self.decoder( account ) )
		...
	
	def append( self, account:Account, indicate:Optional[Str]=None ) -> None:
		
		"""
		Append or add new account
		
		Parameters:
			account (Account):
				Account typing instance
			indicate (Optional[Str]):
				Indicate account username for keyset identity
		"""
		
		indicate = account.auth.username \
			if not account.anonymous \
			else indicate \
			if indicate is not None and indicate \
			else self.anonymous
		self.logger.info( "Registering account into manager: {}", indicate )
		keyset = self.encoder( indicate )
		filename = f"{self.pathname['account']}/{keyset}"
		with open( filename, "w", encoding=self.encoding ) as fopen:
			fopen.write( JsonEncoder( account.mapping, indent=4 ) )
			fopen.close()
		if keyset not in self.configs['accounts']:
			self.configs['accounts'] = sorted([ *self.configs['accounts'], keyset ])
			self.update()
		...
	
	def decoder( self, keyset:Str ) -> Str: return bytes.fromhex( keyset ).decode( self.encoding )
	
	def encoder( self, keyset:Str ) -> Str: return keyset.encode( self.encoding ).hex()
	
	def exists( self, username:Str ) -> Bool:
		
		"""
		Return if account username exists
		
		Parameters:
			username (Str):
				Account username
		
		Returns:
			Bool:
				Return true whether account exists
		"""
		
		keyset = self.encoder( username )
		return keyset in self.configs['accounts'] and isfile( f"{self.pathname['account']}/{keyset}" )
	
	@property
	def length( self ) -> Int: return len( self.configs['accounts'] )
	
	def onload( self ) -> None:
		
		""" Load saved configurations """
		
		if isfile( self.pathname['configs'] ):
			self.logger.info( "Loading configurations" )
			with open( self.pathname['configs'], "r", encoding=self.encoding ) as fopen:
				self.configs = JsonDecoder( fopen.read() )
				fopen.close()
			...
		else:
			self.logger.info( "Configuration not found: {}", self.pathname['configs'] )
		if not self.exists( self.anonymous ):
			self.logger.info( "Anonymous account does not exists: {}", self.anonymous )
			self.append( ClientBuilder().account, self.anonymous )
		account = self.configs['session']
		
		if not self.configs['session'] or \
		   not self.exists( self.configs['session'] ):
			self.configs['session'] = self.anonymous
		self.logger.info( "Set \"{}\" as default account session", account )
		self.update()
	
	def switch( self, username:Str ) -> None:
		
		""" Switch default account """
		
		self.logger.info( "Trying switch account into: {}", username )
		if not self.exists( username ):
			raise TypeError( f"No such account username={username}" )
		self.configs['session'] = username
		self.update()
	
	def update( self ) -> None:
		
		""" Save current configuration """
		
		for i, account in enumerate([ *self.configs['accounts'] ]):
			if not isfile( f"{self.pathname['account']}/{account}" ):
				self.logger.info( "Account with session \"{}\" deleted", account )
				del self.configs['accounts'][i]
			...
		self.logger.info( "Saving configurations" )
		with open( self.pathname['configs'], "w", encoding=self.encoding ) as fopen:
			fopen.write( JsonEncoder( self.configs, indent=4 ) )
			fopen.close()
		...
	
	...
