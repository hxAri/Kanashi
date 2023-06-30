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

from kanashi.client import Client
from kanashi.config import Config, ConfigError
from kanashi.error import *
from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.utility import Cookie


#[kanashi.kanashi.Kanashi]
class Kanashi( Readonly ):
	
	#[Kanashi( Object active, Client client, Config config )]: None
	def __init__( self, active=None, client=None, config=None ):
		
		# Resolve if Client active is not available.
		if  not isinstance( active, Object ):
			active = self.__create()
		
		# Resolve if Client instance is not available.
		if  not isinstance( client, Client ):
			client = Client()
		
		# Resolve if Config instance is not available.
		if  not isinstance( config, Config ):
			config = Config()
			try:
				config.load()
			except ConfigError:
				pass
		
		# Readonly exceptional.
		self.excepts = [
			"active",
			"cookies",
			"headers",
			"request",
			"session"
		]
		
		# Instance of class Client.
		self.client = client
		
		# Instances of class from Request
		self.cookies = client.cookies
		self.headers = client.headers
		self.request = client.request
		self.session = client.session
		
		# Instance of class Config.
		self.config = config
		
		# Represent user active.
		self.active = active
		
		# Represent configuration settings.
		self.settings = config.settings
		
		# Prepare initialize.
		self.__prepare()
	
	#[Kanashi.__create()]: Object
	def __create( self ):
		return Object({
			"id": 0,
			"session": {
				"browser": None,
				"cookies": {},
				"headers": {},
				"response": {
					"headers": {}
				},
				"csrftoken": None,
				"sessionid": None
			},
			"fullname": False,
			"username": None,
			"password": None
		})
	
	#[Kanashi.__prepare()]: None
	def __prepare( self ):
		
		if  self.settings.browser.default:
			self.headers.update({
				"User-Agent": self.settings.browser.default
			})
		
		# Check if there are no active users in the instance.
		if  self.isActive == False:
			
			# Check if there are active user saved.
			if  self.settings.signin.active and \
				self.settings.signin.switch.isset( self.settings.signin.active ):
				self.active.set( self.settings.signin.switch[self.settings.signin.active] )
				self.setupable()
		pass
	
	#[Kanashi.authenticated<kanashi.client.Client.authenticated>]: Bool
	@property
	def authenticated( self ):
		return self.client.authenticated
	
	#[Kanashi.isActive]: Bool
	@property
	def isActive( self ):
		
		"""
		Return if current user representation is active.
		
		:return Bool
			True if current representation is active
			False Otherwise
		"""
		
		if  self.active.id and \
			self.active.username and \
			self.active.fullname is not False and \
			self.active.session.csrftoken and \
			self.active.session.sessionid is not None and \
			self.active.session.cookies.len() and \
			self.active.session.headers.len() and \
			self.authenticated:
			return True
		return False
	
	#[Kanashi.logout<kanashi.client.Client.logout>]: Object
	def logout( self ):
		
		# Unset current active user.
		self.active = None
		self.active = self.__create()
		pass
	
	#[Kanashi.setupable()]: None
	def setupable( self ):
		try:
			self.headers.update( **self.active.session.headers.dict() )
			self.headers.update({ "User-Agent": self.active.session.browser })
			cookies = self.active.session.cookies.dict()
			for i, cookie in enumerate( cookies ):
				Cookie.set( self.cookies, cookie, cookies[cookie] )
			self.client.id = self.active.id
			self.client.username = self.active.username
			self.client.password = self.active.password
		except AttributeError:
			pass
		except IndexError:
			pass
		except KeyError:
			pass
	
	#[Kanashi.signin<kanashi.client.Client.signin>]: Object
	def signin( self, username, password, csrftoken=None, cookies=None, browser=None ):
		
		# Trying to login.
		signin = self.client.signin( username, password, csrftoken, cookies, browser )
		
		# If login successfull.
		if  signin.success:
			
			# Set account as default login.
			self.active.set( signin.result )
			self.settings.signin.active = signin.result.username if signin.result.username else signin.result.id
			self.settings.signin.switch[signin.result.username] = signin.result.copy()
			self.setupable()
		
		return signin
	
	#[Kanashi.switch( Object user )]: Object
	def switch( self, user ):
		
		"""
		Switch session user active.
		
		:params Object user
			Representation of user active
		
		:return Object
			Representtation of user active
		:raises ValueError
			When invalid value passed
		"""
		
		if  isinstance( user, Object ):
			try:
				
				# Trying to re-login.
				# This is to ensure that the login credentials have not expired.
				signin = self.signin( None, None, **{
					"browser": user.session.browser,
					"cookies": user.session.cookies,
					"csrftoken": user.session.csrftoken
				})
				self.config.save()
			except RequestAuthError as e:
				if  user.username == self.active.username:
					self.active = None
					self.active = self.__create()
				if  user.username == self.settings.signin.active:
					self.settings.signin.active = None
				self.settings.signin.switch.unset( user.username )
				self.config.save()
				raise AuthError( "The credentials provided are invalid or may be expired", prev=e )
		else:
			raise ValueError( "User must be object representation of user info" )
		
		return signin
	