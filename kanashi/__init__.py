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

# Application Banner
# Please don't change or override this
banner = "\x1b[1;38;5;32m\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x20\x20\x20\x3b\x3b\x20\x20\x1b[1;38;5;32m\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x20\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x20\x20\x20\x20\x3b\x20\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x20\x20\x20\x20\x3b\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x20\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x20\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x3b\x3b\x20\x20\x20\x3b\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x3b\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x1b[0m"

from os import system

from kanashi.config import BaseConfig, Config
from kanashi.context import Context
from kanashi.error import Alert, Error
from kanashi.kanashi import Kanashi
from kanashi.object import Object
from kanashi.request import BaseRequest, Request, RequestError
from kanashi.signin import BaseSignIn, SignIn, SignInError, SignInCheckpoint, SignIn2FARequired, SignIn2FAInvalidCode
from kanashi.utils import *

#[kanashi.Main]
class Main( Kanashi, Util ):
	
	#[Main()]
	def __init__( self ):
		
		self.config = Config( self )
		self.request = Request( self )
		self.signin = SignIn( self )
		
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
			authors.append( "Name {1}\n{0}Email {2}\n{0}Github {3}\n{0}".format(*[
				"\x20" *8,
				author.name,
				author.email,
				author.github
			]))
		info[info.index( "Replace" )] = authors
		self.output( "activity", info, line=False )
		self.input( "Return to the main page", default="" )
		self.main()
		
	#[Main.main()]
	def main( self ):
		try:
			if self.active:
				print( self.active )
			else:
				self.welcome()
		except AttributeError:
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
		self.output( "activity", [
			"",
			"Welcome to Kanashi v{}".format( self.config.setting.version ),
			"",
			"Author {}".format( self.config.authors[0].name ),
			"Github {}".format( self.config.setting.source ),
			"Issues {}".format( self.config.setting.issues ),
			"",
			[
				"SignIn Password",
				[
					"SignIn with username and password"
				],
				"SignIn Csrftoken",
				[
					"Use login cookies from your browser"
				],
				"Switch Account",
				[
					"If you save the previous login info"
				],
				"Support Project",
				[
					"Give spirit to the developer, no matter",
					"how many donations given will still",
					"be accepted"
				],
				"Update Tool",
				[
					"Update the current version to the",
					"latest version, from source"
				],
				"Clear Response",
				[
					"Delete the entire request record"
				],
				"Info",
				[
					"e.g Authors, Version, License, etc"
				],
				"Exit",
				[
					"Close the program"
				]
			]
		])
		try:
			opts = {
				1: self.signin.password,
				2: self.signin.cookie,
				3: self.signin.switch,
				4: self.support,
				5: self.update,
				6: self.request.clear,
				7: self.info
			}
			next = opts[self.input( None, number=True, default=[ 1+ i for i in range( 8 ) ] )]
			next()
		except KeyError:
			self.close( "activity", "Finish" )
	

if __name__ == "__main__":
	main = Main()
	main.main()
	