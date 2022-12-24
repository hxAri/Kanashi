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

from kanashi import banner
from kanashi.error import Error
from kanashi.utils.thread import Thread

#[kanashi.utils.Util]
class Util:
	
	#[Util.clear()]
	def clear( self ):
		system( "clear" )
		
	#[Util.close()]
	def close( self, *args, **kwargs ):
		self.output( *args, **kwargs )
		exit()
		
	#[Util.exit()]
	def exit( self, *args, **kwargs ):
		self.close( *args, **kwargs )
		
	#[Util.emit( BaseException|Error|List error )]
	def emit( self, error ):
		#self.clear()
		name = type( self ).__name__
		strings = f"{name}.error\n"
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
				prev = f"\x20\x20{name}.prev {prevName} {prevLine}\n"
				prev += f"\x20\x20\x20\x20{prevMessage}\n"
			else:
				prev = f""
			try:
				line = error.__traceback__.tb_lineno
			except AttributeError:
				line = "passed"
			error = type( error ).__name__
			strings += prev
			strings += f"\x20\x20{name}.raise {error} {code}\n"
			strings += f"\x20\x20{name}.raise {error} {line}\n"
			strings += f"\x20\x20\x20\x20{message}\n"
		else:
			if type( error ).__name__ == "list":
				try:
					message = [ str( error[0] ), error[1] ]
				except IndexError:
					message = str( error[0] )
				try:
					lineno = error[0].__traceback__.tb_lineno
				except AttributeError:
					lineno = "\n"
				error = type( error[0] ).__name__
			else:
				message = str( error )
				try:
					lineno = error.__traceback__.tb_lineno
				except AttributeError:
					lineno = "\n"
				error = type( error ).__name__
			strings = f"{name}.error\n"
			strings += f"\x20\x20{name}.raise {error} {lineno}\n"
			if type( message ).__name__ == "list":
				for i in range( len( message ) ):
					strings += f"\x20\x20\x20\x20{message[i]}\n"
			else:
				strings += f"\x20\x20\x20\x20{message}\n"
		for subject in findall( r"(\[Errno\s\d+\]\s*)", strings ):
			strings = strings.replace( subject, "" )
		print( "\x0a\x7b\x7d\x0a\x0a\x0a\x7b\x7d".format( banner, strings ) )
		
	#[Util.getpass( String label )]
	def getpass( self, label, ignore=True ):
		if label == None or label == "":
			place = "{}.getpass:\x20".format( type( self ).__name__ )
		else:
			place = "{}:\x20".format( label )
		try:
			value = getpass( place )
			if value == "":
				value = self.getpass( label, ignore )
			return( value )
		except EOFError as e:
			self.close( e, "Force close." )
		except KeyboardInterrupt as e:
			if ignore == False:
				self.close( e, "Force close." )
			return( self.getpass( label, default, ignore ) )
		
	#[Util.input( String label )]
	def input( self, label, default=None, number=False, ignore=True ):
		if label == None or label == "":
			place = "{}.input:\x20".format( type( self ).__name__ )
		else:
			place = "{}:\x20".format( label )
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
			self.close( e, "Force close." )
		except KeyboardInterrupt as e:
			if ignore == False:
				self.close( e, "Force close." )
			return( self.input( label, default, number, ignore ) )
		
	#[Util.open( String target )]
	def open( self, target ):
		system( "xdg-open {}".format( target ) )
		
	#[Util.output( Object refer, Dict|List|String message, Bool line )]
	def output( self, refer, message, line=False ):
		#self.clear()
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
		strings = f"{named}.output\n"
		if isinstance( refer, BaseException ):
			strings += f"\x20\x20{named}.{refer}.{base.__traceback__.tb__lineno}\n"
			strings += f"\x20\x20{named}.{refer}.{__name__}\n"
		else:
			strings += f"\x20\x20{named}.{refer}\n"
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
								stack += "{0}[{1}]\x20{2}\n".format( space, i, message[i] )
							else:
								stack += "{0}{1}\n".format( space, message[i] )
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
								stack += "{0}[{1}]\x20{2}\n".format( space, i +1 -u, message[i] )
							else:
								stack += "{0}{1}\n".format( space, message[i] )
			case _:
				stack = "{0}{1}\n".format( space, message )
		return( stack )
		
	#[Util.thread( String strings, Function Object, *args, **kwargs )]
	def thread( self, strings, target, *args, **kwargs ):
		#self.clear()
		print( "\x0a\x7b\x7d\x0a\x0a\x0a".format( banner ) )
		try:
			task = Thread( target=target, args=args, kwargs=kwargs )
			named = type( self ).__name__
			strings = "\x7b\x30\x7d\x7b\x31\x7d".format( "\x20" *4, strings )
			caption = "\x7b\x31\x7d\x2e\x74\x68\x72\x65\x61\x64\x0a\x7b\x30\x7d\x7b\x31\x7d\x2e\x74\x68\x72\x65\x61\x64\x20\x41\x6c\x69\x76\x65\x0a\x7b\x32\x7d".format( "\x20" *2, named, strings )
			for e in caption:
				sys.stdout.write( e )
				sys.stdout.flush()
				#sleep( 00000.1 )
			task.start()
			while task.is_alive():
				for i in "\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x20":
					print( "\r{}\x20{}".format( strings, i ), end="" )
					sleep( 00000.1 )
			print( "\r\x0a" )
			#self.clear()
		except EOFError as e:
			self.close( e, "Foce close." )
		except KeyboardInterrupt:
			self.close( e, "Foece close." )
		return( task.getReturn() )
	