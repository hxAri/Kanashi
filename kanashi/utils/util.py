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

import sys

from getpass import getpass
from os import system
from re import findall
from time import sleep

from kanashi.error import Error
from kanashi.utils.thread import Thread

# Application Banner
# Please don't change or override this
banner = "\x1b[1;38;5;32m\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x20\x20\x20\x3b\x3b\x20\x20\x1b[1;38;5;32m\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x20\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x20\x20\x20\x20\x3b\x20\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x20\x20\x20\x20\x3b\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x20\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x20\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x3b\x3b\x20\x20\x20\x3b\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x3b\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x1b[0m"

#[kanashi.utils.Util]
class Util:
	
	#[Util.clear()]
	def clear( self ):
		system( "clear" )
		
	#[Util.close()]
	def close( self, *args, **kwargs ):
		self.output( *args, **kwargs )
		sys.exit()
		
	#[Util.exit()]
	def exit( self, *args, **kwargs ):
		self.close( *args, **kwargs )
		
	#[Util.emit( BaseException|Error|List error )]
	def emit( self, error ):
		self.clear()
		name = type( self ).__name__
		strings = f"{name}\x2e\x65\x72\x72\x6f\x72\x0a"
		if isinstance( error, Error ):
			message = error.message
			code = error.code
			prev = error.prev
			if isinstance( prev, BaseException ):
				prevName = type( prev ).__name__
				prevMessage = str( prev )
				try:
					prevLine = prev.__traceback__.tb_lineno
				except AttributeError:
					prevLine = ""
				prev = f"\x20\x20{name}\x2e\x70\x72\x65\x76\x20{prevName}\x20{prevLine}\x0a"
				prev += f"\x20\x20\x20\x20{prevMessage}\x0a"
			else:
				prev = f""
			try:
				line = error.__traceback__.tb_lineno
			except AttributeError:
				line = "\x70\x61\x73\x73\x65\x64"
			error = type( error ).__name__
			strings += prev
			strings += f"\x20\x20{name}\x2e\x72\x61\x69\x73\x65\x20{error}\x20{code}\x0a"
			strings += f"\x20\x20{name}\x2e\x72\x61\x69\x73\x65\x20{error}\x20{line}\x0a"
			strings += f"\x20\x20\x20\x20{message}\x0a"
		else:
			if type( error ).__name__ == "list":
				try:
					message = [ str( error[0] ), error[1] ]
				except IndexError:
					message = str( error[0] )
				try:
					lineno = error[0].__traceback__.tb_lineno
				except AttributeError:
					lineno = "\x0a"
				error = type( error[0] ).__name__
			else:
				message = str( error )
				try:
					lineno = error.__traceback__.tb_lineno
				except AttributeError:
					lineno = "\x0a"
				error = type( error ).__name__
			strings = f"{name}\x2e\x65\x72\x72\x6f\x72\x0a "
			strings += f"\x20\x20{name}\x2e\x72\x61\x69\x73\x65\x20{error}\x20{lineno}\x0a"
			if type( message ).__name__ == "list":
				for i in range( len( message ) ):
					strings += f"\x20\x20\x20\x20{message[i]}\x0a"
			else:
				strings += f"\x20\x20\x20\x20{message}\x0a"
		for subject in findall( r"(\[Errno\s\d+\]\s*)", strings ):
			strings = strings.replace( subject, "" )
		print( "\x0a\x7b\x7d\x0a\x0a\x0a\x7b\x7d".format( banner, strings ) )
		
	#[Util.getpass( String label )]
	def getpass( self, label, ignore=True ):
		if label == None or label == "":
			place = "\x7b\x7d\x2e\x67\x65\x74\x70\x61\x73\x73\x3a\x20".format( type( self ).__name__ )
		else:
			place = "\x7b\x7d\x3a\x20".format( label )
		try:
			value = getpass( place )
			if value == "":
				value = self.getpass( label, ignore )
			return( value )
		except EOFError as e:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		except KeyboardInterrupt as e:
			if ignore == False:
				self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
			return( self.getpass( label, default, ignore ) )
		
	#[Util.input( String label )]
	def input( self, label, default=None, number=False, ignore=True ):
		if label == None or label == "":
			place = "\x7b\x7d\x2e\x69\x6e\x70\x75\x74\x3a\x20".format( type( self ).__name__ )
		else:
			place = "\x7b\x7d\x3a\x20".format( label )
		try:
			if number:
				value = int( input( place ) )
			else:
				value = input( place )
			if value == "":
				if default != None:
					value = default if type( default ).__name__ != "list" else default[0]
				else:
					value = self.input( label, default, number, ignore )
			if type( default ).__name__ == "list":
				try:
					default.index( value )
				except ValueError:
					value = self.input( label, default, number, ignore )
			return( value )
		except ValueError as e:
			return( self.input( label, default, number, ignore ) )
		except EOFError as e:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		except KeyboardInterrupt as e:
			if ignore == False:
				self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
			return( self.input( label, default, number, ignore ) )
		
	#[Util.open( String target )]
	def open( self, target ):
		system( "xdg-open {}".format( target ) )
		
	#[Util.output( Object refer, Dict|List|String message, Bool line )]
	def output( self, refer, message, line=False ):
		self.clear()
		base = refer
		try:
			refer = refer.__name__
		except AttributeError:
			named = type( refer ).__name__
			match named:
				case "str" | "int" | "float" | "complex" | "list" | "tuple" | "range" | "dict" | "set" | "frozenset" | "bool" | "bytes" | "bytearray" | "memoryview" | "NoneType":
					pass
				case _:
					refer = named
		named = type( self ).__name__
		strings = f"{named}\x2e\x6f\x75\x74\x70\x75\x74\x0a"
		if isinstance( refer, BaseException ):
			strings += f"\x20\x20{named}\x2e{refer}\x2e{base.__traceback__.tb__lineno}\x0a"
			strings += f"\x20\x20{named}\x2e{refer}\x2e{__name__}\x0a"
		else:
			strings += f"\x20\x20{named}\x2e{refer}\x0a"
		strings += self.println( message, 4, line )
		print( "\x0a\x7b\x7d\x0a\x0a\x0a\x7b\x7d".format( banner, strings ) )
		
	#[Util.println( Dict|List|String message, Int indent, Bool line )]
	def println( self, message, indent=4, line=False ):
		space = "\x20" * indent
		stack = ""
		match type( message ).__name__:
			case "dict":
				for i in message:
					match type( message[i] ).__name__:
						case "dict":
							try:
								stack += self.println(*[
									message[i]['message'],
									indent +4 if message[i]['line'] else indent,
									False if message[i]['line'] else True
								])
							except KeyError:
								stack += self.println(*[
									message[i],
									indent +4 if line else indent,
									False if line else True
								])
						case "list":
							stack += self.println(*[
								message[i],
								indent +4 if line else indent,
								False if line else True
							])
						case _:
							if line:
								stack += "\x7b\x30\x7d\x5b\x7b\x31\x7d\x5d\x20\x7b\x32\x7d\x0a".format( space, i, message[i] )
							else:
								stack += "\x7b\x30\x7d\x7b\x31\x7d\x0a ".format( space, message[i] )
			case "list":
				u = 0
				for i in range( len( message ) ):
					match type( message[i] ).__name__:
						case "dict":
							try:
								stack += self.println(*[
									message[i]['message'],
									indent +4 if message[i]['line'] else indent,
									False if message[i]['line'] else True
								])
							except KeyError:
								stack += self.println(*[
									message[i],
									indent +4 if line else indent,
									False if line else True
								])
							u += 1
						case "list":
							stack += self.println(*[
								message[i],
								indent +4 if line else indent,
								False if line else True
							])
							u += 1
						case _:
							if line:
								stack += "\x7b\x30\x7d\x5b\x7b\x31\x7d\x5d\x20\x7b\x32\x7d\x0a".format( space, i +1 -u, message[i] )
							else:
								stack += "\x7b\x30\x7d\x7b\x31\x7d\x0a".format( space, message[i] )
			case _:
				stack = "\x7b\x30\x7d\x7b\x31\x7d\x0a".format( space, message )
		return( stack )
		
	#[Util.thread( String strings, Function Object, *args, **kwargs )]
	def thread( self, strings, target, *args, **kwargs ):
		self.clear()
		print( "\x0a\x7b\x7d\x0a\x0a\x0a".format( banner ) )
		try:
			task = Thread( target=target, args=args, kwargs=kwargs )
			named = type( self ).__name__
			strings = "\x7b\x30\x7d\x7b\x31\x7d".format( "\x20" *4, strings )
			sys.stdout.write( "\x7b\x31\x7d\x2e\x74\x68\x72\x65\x61\x64\x0a\x7b\x30\x7d\x7b\x31\x7d\x2e\x61\x6c\x69\x76\x65\x0a".format( "\x20" *2, named ) )
			for e in strings:
				sys.stdout.write( e )
				sys.stdout.flush()
				if e != "\x20":
					#sleep( 00000.1 )
					pass
			task.start()
			while task.is_alive():
				for i in "\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x20":
					print( "\x0d\x7b\x7d\x20\x7b\x7d".format( strings, i ), end="" )
					sleep( 00000.1 )
			print( "\x0d\x0a" )
			self.clear()
		except EOFError as e:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		except KeyboardInterrupt:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		return( task.getReturn() )
	