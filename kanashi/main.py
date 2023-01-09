#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashi Copyright (c) 2022 - Ari Setiawan <ari160824@gmail.com>
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
# Kanashi is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from kanashi.cli import *
from kanashi.config import BaseConfig, Config
from kanashi.context import Context
from kanashi.endpoint import *
from kanashi.error import Alert, Error, Throwable
from kanashi.download import BaseDownload, Download, DownloadError
from kanashi.kanashi import Kanashi
from kanashi.object import Object
from kanashi.request import BaseRequest, Request, RequestError, RequestRequired
from kanashi.signin import BaseSignIn, SignIn, SignInError, SignInCheckpoint, SignIn2FARequired, SignIn2FAInvalidCode
from kanashi.utils import *

# Classes that start with the word Base,
# for example BaseSignIn are not used with the Main class,
# but classes like SignIn or without the Base prefix are
# used because it supports interaction with the User.

#[kanashi.Main]
class Main( Kanashi, Util ):
	
	#[Main()]
	def __init__( self ):
		
		# Default user active.
		self.active = None
		
		# Mapping attributes required before the user login.
		for attr in [ Config, Request,SignIn ]:
			name = attr.__name__
			name = name.lower()
			self.set( name, attr( self ) )
		
		# Check if there are active users.
		if user := self.config.signin.active:
			try:
				self.active = self.config.signin.switch.get( user )
				self.session.headers.update( self.active.headers.request.dict() )
				self.session.headers.update( self.active.headers.response.dict() )
				for attr in [ Block, Download, Favorite, Follow, Restrict, User ]:
					name = attr.__name__
					name = name.lower()
					name = name.replace( "base", "" )
					try:
						if not isinstance( self.get( name ), attr ):
							raise ValueError( f"The value of the {name} attribute must be {attr.__name__}, {type( self.get( name ) ).__name__} set" )
					except( AttributeError, ValueError ):
						self.set( name, attr( self ) )
			except( AttributeError, KeyError ) as e:
				self.close( e )
		
		# Copy parent class.
		self.parent = super()
		
		# Call parent constructor.
		self.parent.__init__( self )
		
	#[Main.info()]
	def info( self ):
		self.output( activity, parent.info, line=False )
		self.previous( self.main, "<<<" )
		
	#[Main.main()]
	def main( self ):
		if self.active:
			self.outputs = [
				"",
				"Kanashi v{}".format( self.config.setting.version ),
				"Logged in as {}".format( self.active.signin.username ),
				"",
				"Author {}".format( self.config.authors[0].name ),
				"Github {}".format( self.config.setting.source ),
				"Issues {}".format( self.config.setting.issues ),
				""
			]
			menu = {
				"get.user": "Get User Info",
				"get.user-doc": [
					"Get user by Id, Url, or Username"
				],
				"get.post": "Get Post Info",
				"get.post-doc": [
					"Get post by Id or Url"
				],
				"get.reel": "Get Reel Info",
				"get.reel-doc": [
					"Get reel by Id or Url"
				],
				"extract": "Extract",
				"extract-doc": [
					"Extract data like, timeline, reels, etc"
				],
				"search": "Search",
				"search-doc": [
					"Looks for something like users, hashtags"
				],
				"profile": "Profile",
				"profile-doc": [
					"Your account profile"
				],
				"switch": "Switch Account",
				"switch-doc": [
					"If you save the previous login info"
				],
				"logout": "Logout",
				"logout-doc": [
					"Remove your account from the device",
					"This requires you to login again when",
					"you want to use this tool again",
				],
				"support": "Support Project",
				"support-doc": [
					"Give spirit to the developer, no matter",
					"how many donations given will still",
					"be accepted"
				],
				"update": "Update Tool",
				"update-doc": [
					"Update the current version to the",
					"latest version, from real source"
				],
				"clear": "Clear Response",
				"clear-doc": [
					"Delete the entire request record"
				],
				"info": "Info",
				"info-doc": [
					"e.g Authors, Version, License, etc"
				],
				"exit": "Exit",
				"exit-doc": [
					"Close the program"
				]
			}
			
			keys = self.rmdoc( menu )
			vals = [ val for val in menu.values() ]
			
			self.output( activity, [ *self.outputs, vals ] )
			next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( keys ) ) ] )
			match keys[( next -1 )]:
				case "get.user":
					self.user.main()
				case "profile":
					self.user.getByUsername( self.active.signin.username )
				case "switch":
					self.signin.switch()
				case "support":
					self.support()
				case "update":
					self.update()
				case "clear":
					self.request.reset()
				case "info":
					self.info()
				case "exit":
					self.exit( activity, "Finish" )
				case _:
					print( next )
		else:
			self.welcome()
		
	#[Main.support()]
	def support( self ):
		self.open( self.config.setting.donate )
		self.main()
		
	#[Main.update()]
	def update( self ):
		self.previous( self.main, "<<<" )
		
	#[Main.welcome()]
	def welcome( self ):
		self.outputs = [
			"",
			"Kanashi v{}".format( self.config.setting.version ),
			"",
			"Author {}".format( self.config.authors[0].name ),
			"Github {}".format( self.config.setting.source ),
			"Issues {}".format( self.config.setting.issues ),
			""
		]
		menu = {
			"password": "SignIn Password",
			"password-doc": [
				"SignIn with username and password"
			],
			"session": "SignIn Session",
			"session-doc": [
				"Use login cookies from your browser"
			],
			"switch": "Switch Account",
			"switch-doc": [
				"If you save the previous login info"
			],
			"support": "Support Project",
			"support-doc": [
				"Give spirit to the developer, no matter",
				"how many donations given will still",
				"be accepted"
			],
			"update": "Update Tool",
			"update-doc": [
				"Update the current version to the",
				"latest version, from real source"
			],
			"clear": "Clear Response",
			"clear-doc": [
				"Delete the entire request record"
			],
			"info": "Info",
			"info-doc": [
				"e.g Authors, Version, License, etc"
			],
			"exit": "Exit",
			"exit-doc": [
				"Close the program"
			]
		}
		keys = self.rmdoc( menu )
		vals = [ val for val in menu.values() ]
		self.output( activity, [ *self.outputs, vals ] )
		next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( keys ) ) ] )
		match keys[( next -1 )]:
			case "password":
				self.signin.password()
			case "session":
				self.signin.remember()
			case "switch":
				self.signin.switch()
			case "support":
				self.support()
			case "update":
				self.update()
			case "clear":
				self.request.reset()
			case "info":
				self.info()
			case "exit":
				self.exit( activity, "Finish" )
		pass
	

if __name__ == "__main__":
	main = Main()
	main.main()
	