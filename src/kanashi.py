#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
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

from builtins import str as Str
from click import (
	argument as Argument, 
	group, Group, 
	option as Option, 
	pass_context as Instance
)
from click.core import Context
from json import dumps as JsonEncoder
from subprocess import run as SubprocessRun
from sys import argv
from traceback import format_exception
from typing import final, MutableSequence, Self

from kanashi.client import Client, create as ClientBuilder
from kanashi.command import *
from kanashi.common import puts, typeof
from kanashi.constant import BasePath, BaseVenv
from kanashi.logger import *
from kanashi.manager import Manager


__all__ = [
	"Cli"
]


@final
@group
class Cli: """ Kanashi Command Line Interface """

@final
class Command:
	
	""" Kanashi Command Containers """
	
	logger = Logger( __name__ )
	
	@Cli.command( help="Instagram profile info" )
	@Option( "--username", help="Instagram account username" )
	@Instance
	def profile( context:Context, username:Str ) -> None:
		client:Client = context.obj['client']
		profile = client.profile( username, navigate=True )
		profile = profile['user']
		puts( JsonEncoder( profile ) )
	
	@Cli.command( help="Testing the program" )
	@Argument( "testing", required=False, type=Str )
	@Instance
	def testing( context:Context, testing:Str, **kwargs ) -> None:
		client:Client = context.obj['client']
		if testing is not None:
			puts( f"Executing program src/tests/{testing}.py" )
			execution = SubprocessRun( f"{BaseVenv}/bin/python {BasePath}/src/tests/{testing}.py", shell=True, capture_output=True )
			if execution.stderr is not None and execution.stderr:
				puts( f"Stderr {execution.stderr.decode()}" )
			if execution.stdout is not None and execution.stdout:
				puts( f"Stdout {execution.stdout.decode()}" )
			if execution.returncode == 0:
				puts( "Execution program is success" )
			else:
				puts( "Execution program is failed" )
				puts( f"Execution program has return code {execution.returncode}", close=execution.returncode )
		try:
			result = None
			puts( JsonEncoder( result, indent=4 ) )
		except BaseException as e:
			puts( "\x3a\x20".join([ typeof( e ), "\x0a".join( format_exception( e ) ) ]) )
		...
	
	...

@final
class Kanashi:
	
	""" Kanashi Main Program """
	
	client:Client
	""" Client Instance """
	
	commands:MutableSequence[Group]
	""" Registered commands """
	
	logger:Logger[Self]
	""" Logger Instance """
	
	manager:Manager
	""" Account Manager """
	
	def __init__( self ) -> None:
		
		""" Construct method of class Main """
		
		disabled = "--logging-store-disabled"
		enabled = "--logging-store-enabled"
		verbose = "--verbose"
		if verbose in argv:
			del argv[argv.index( verbose )]
			threshold( Level.VERBOSE )
		else:
			threshold( Level.DISABLE )
		if disabled in argv:
			del argv[argv.index( disabled )]
			disableStoreLog()
		elif enabled in argv:
			del argv[argv.index( enabled )]
			enableStoreLog()
		
		self.commands = [
			Account,
			Media,
			Story
		]
		self.logger = Logger( self )
	
	def main( self ) -> None:
		
		""" Main Program execution """
		
		self.logger.info( "Starting application with argv: {}", argv[1:] )
		self.manager = Manager()
		self.manager.onload()
		account = self.manager.configs['session'] \
			if self.manager.configs['session'] \
			else self.manager.anonymous
		
		self.client = ClientBuilder( \
			self.manager.account( account )
		)
		
		for command in self.commands:
			self.logger.info( "Registering command: {}[{}]", typeof( command ), command.name )
			Cli.add_command( command )
		
		self.logger.info( "Instantiate command line interface: {}", typeof( Cli ) )
		status = 0
		try:
			Cli( obj={ "client": self.client, "manager": self.manager })
		except Exception as e:
			status = e.code if hasattr( e, "code" ) else 1
			puts( "\x3a\x20".join([ typeof( e ), "\x0a".join( format_exception( e ) ) ]) )
		except SystemExit as e:
			status = e.code
		finally:
			self.logger.info( "Program terminated with status: {}", status )
			puts( close=status )
		...
	
	...


if __name__ == "__main__":
	kanashi = Kanashi()
	kanashi.main()

