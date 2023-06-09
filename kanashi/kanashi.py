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

from os import system

from kanashi.config import Config, ConfigError
from kanashi.context import Context
from kanashi.endpoint import Block, Favorite, Follow, Report, Restrict, SignIn, User
from kanashi.request import Request
from kanashi.update import Update

#[kanashi.Kanashi]
class Kanashi( Context ):
	
	#[Kanashi( Object app )]
	def __init__( self, app=None ):
		
		# ...
		app = app if app != None else self
		
		# Call parent constructor.
		super().__init__( app )
		
		# Set class attributes required before login.
		self.beforeLogin()
		
		# Check if attribute active is set.
		try:
			if app.active == None:
				pass
		except AttributeError:
			app.active = None
		
		# Check if the user has not logged in.
		if app.active == None:
			if app.settings.signin.active != False:
				
				# Set class attribute required after user login.
				# Always call this method after successfully login.
				self.afterLogin()
		pass
	
	#[Kanashi.afterLogin()]
	def afterLogin( self ):
		
		# Get previously logged in users.
		user = self.app.settings.signin.active
		
		# Check if user has previois login.
		if self.active == None:
			if user != False:
				self.__afterLoginSetActive( user )
				self.__afterLoginSetAttr()
		else:
			self.__afterLoginSetAttr()
	
	#[Kanashi.__afterLoginSetActive( String user )]
	def __afterLoginSetActive( self, user ):
		try:
			if self.active == None:
				self.app.active = self.app.settings.signin.switch.get( user )
				self.app.session.headers.update( self.app.active.headers.response.dict() )
				self.app.session.headers.update( self.app.active.headers.request.dict() )
			for cookie in self.app.active.cookies.dict():
				self.app.session.cookies.set(
					cookie,
					self.app.active.cookies.get( cookie ),
					domain=".instagram.com",
					path="/"
				)
		except( AttributeError, KeyError ) as e:
			self.app.active = None
			self.app.settings.signin.set({ "active": False })
			try:
				self.app.config.save()
			except ConfigError as e:
				self.emit( e )
				exit()
			self.close( e, "Something wrong" )
		pass
	
	#[Kanashi.__afterLoginSetAttr()]
	def __afterLoginSetAttr( self ):
		
		# Mapping attributes required after the user login.
		for attr in [ Block, Favorite, Follow, Report, Restrict, User ]:
			name = attr.__name__
			name = name.lower()
			name = name.replace( "", "" )
			try:
				if not isinstance( self.app.get( name ), attr ):
					raise ValueError( f"The value of the {name} attribute must be {attr.__name__}, {type( self.app.get( name ) ).__name__} set" )
			except( AttributeError, ValueError ):
				self.app.set( name, attr( self.app ) )
		pass
	
	#[Kanashi.beforeLogin()]
	def beforeLogin( self ):
		
		# Mapping attributes required before the user login.
		for attr in [ Config, Request, SignIn, Update ]:
			name = attr.__name__
			name = name.lower()
			name = name.replace( "", "" )
			try:
				if not isinstance( self.app.get( name ), attr ):
					raise ValueError( f"The value of the {name} attribute must be {attr.__name__}, {type( self.app.get( name ) ).__name__} set" )
			except( AttributeError, IndexError, KeyError, ValueError ):
				self.app.set( name, attr( self.app ) )
			if name == "config":
				self.config.read()
		pass
	
	#[Kanashi.authors]
	@property
	def authors( self ): return( self.settings.authors )
	
	#[Kanashi.license]
	@property
	def license( self ): return( self.settings.license )
	
	#[Kanashi.version]
	@property
	def version( self ): return( self.settings.version )
	
	#[Kanashi.info]
	@property
	def info( self ): return([])
	
	#[Kanashi.supportProject()]
	def supportProject( self ):
		system( f"xdg-open {self.settings.donate}" )
		
	