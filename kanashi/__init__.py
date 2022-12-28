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

from os import system

from kanashi.cli import *
from kanashi.config import BaseConfig, Config
from kanashi.context import Context
from kanashi.enpoint import *
from kanashi.error import Alert, Error
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
		
		self.active = None
		self.config = Config( self )
		self.request = Request( self )
		self.signin = SignIn( self )
		self.user = User( self )
		
		self.active = self.setting.signin.switch.get( self.setting.signin.active )
		self.session.headers.update( self.active.headers.request.dict() )
		self.session.headers.update( self.active.headers.response.dict() )
		
		# Call parent constructor.
		super().__init__( self )
		
	#[Main.info()]
	def info( self ):
		info = [
			"",
			"Authors",
			"",
			"Replace",
			"Kanashi Version {}".format( self.config.setting.version ),
			"",
			"All Kanashi source code is licensed under the",
			"GNU General Public License v3. Please see the",
			"original document for more details",
			"",
			"License Name {}".format( self.config.license.name ),
			"License Docs {}".format( self.config.license.link ),
			"",
			"Copyright (c) 2022 - Ari Setiawan",
			"",
			"Disclaimer",
			"",
			"Kanashi is not affiliated with or endorsed,",
			"endorsed at all by Instagram or any other party,",
			"if you use the main account to use this tool we as",
			"Coders and Developers are not responsible for anything",
			"that happens to that account, use it at your own risk,",
			"and this is Strictly not for SPAM."
		]
		authors = []
		for author in self.config.authors:
			authors.append( "Name {1} ({2})\n{0}Email {3}\n{0}Github {4}\n{0}".format(*[
				"\x20" *8,
				author.name,
				author.nick,
				author.email,
				author.github
			]))
		info[info.index( "Replace" )] = authors
		self.output( activity, info, line=False )
		self.input( "Return to the main page", default="" )
		self.main()
		
	#[Main.main()]
	def main( self ):
		if self.active:
			self.output( activity, [
				"",
				"Kanashi v{}".format( self.config.setting.version ),
				"Logged in as {}".format( self.active.signin.username ),
				"",
				"Author {}".format( self.config.authors[0].name ),
				"Github {}".format( self.config.setting.source ),
				"Issues {}".format( self.config.setting.issues ),
				"",
				lists := [
					"Get User Info", [
						"e.g Fullname, Username, Bio, etc\n"
					],
					"Get User Post", [
						"e.g Captions, Tags, Images/ Videos, etc\n"
					],
					"Get Post Image/ Video",
					"Get Post Info", [
						"e.g Author, Captions, Tags, Images, etc\n"
					],
					"Get Story Image/ Video",
					"Get Story Info", [
						"e.g Author, Images or Videos\n"
					],
					"Get Reels Video",
					"Get Reels Info", [
						"e.g Author, Captions, Tags, Images, etc\n"
					],
					"Fetch Timesline Posts\n",
					"Fetch Suggested Users\n",
					"Follow Account", [
						"Follow accounts based on target accounts",
						"Or just follow one account only\n"
					],
					"Unfollow Account", [
						"Unfollow all accounts",
						"Or just unfollow one account only\n",
					],
					"Logout", [
						"Remove your account from the device",
						"This requires you to login again when",
						"you want to use this tool again\n",
					],
					"Support Project", [
						"Give spirit to the developer, no matter",
						"how many donations given will still",
						"be accepted\n"
					],
					"Update Tool", [
						"Update the current version to the",
						"latest version, from real source\n"
					],
					"Clear Response", [
						"Delete the entire request record\n"
					],
					"Info", [
						"e.g Authors, Version, License, etc\n"
					],
					"Exit", [
						"Close the program"
					]
				]
			])
			match self.input( None, number=True, default=[ 1+ idx for idx in range( len( lists ) ) ] ):
				case 1:
					self.user.tools()
				case _:
					self.close( activity, "Finish without logout" )
		else:
			self.welcome()
		
	#[Main.support()]
	def support( self ):
		self.open( self.config.setting.donate )
		self.main()
		
	#[Main.update()]
	def update( self ):
		self.main()
		
	#[Main.welcome()]
	def welcome( self ):
		self.output( activity, [
			"",
			"Welcome to Kanashi v{}".format( self.config.setting.version ),
			"",
			"Author {}".format( self.config.authors[0].name ),
			"Github {}".format( self.config.setting.source ),
			"Issues {}".format( self.config.setting.issues ),
			"",
			lists := [
				"SignIn Password", [
					"SignIn with username and password\n"
				],
				"SignIn Session", [
					"Use login cookies from your browser\n"
				],
				"Switch Account", [
					"If you save the previous login info\n"
				],
				"Support Project", [
					"Give spirit to the developer, no matter",
					"how many donations given will still",
					"be accepted\n"
				],
				"Update Tool", [
					"Update the current version to the",
					"latest version, from real source\n"
				],
				"Clear Response", [
					"Delete the entire request record\n"
				],
				"Info", [
					"e.g Authors, Version, License, etc\n"
				],
				"Exit", [
					"Close the program"
				]
			]
		])
		opts = {
			1: self.signin.password,
			2: self.signin.remember,
			3: self.signin.switch,
			4: self.support,
			5: self.update,
			6: self.request.reset,
			7: self.info
		}
		try:
			next = opts[self.input( None, number=True, default=[ 1+ idx for idx in range( len( lists ) ) ] )]
			next()
		except KeyError as e:
			self.close( activity, "Finish" )
		pass
	

if __name__ == "__main__":
	main = Main()
	main.main()
	