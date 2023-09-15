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

import re
import sys

from getpass import getpass
from os import system
from re import findall
from time import sleep

from kanashi.error import Error
from kanashi.utility import Thread
from kanashi.utility.common import typedef


# Application Banner
# Please don't change or override this
banner = "\x1b[1;38;5;32m\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x20\x20\x20\x3b\x3b\x20\x20\x1b[1;38;5;32m\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x20\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x20\x20\x20\x20\x3b\x20\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x20\x20\x20\x20\x3b\x3b\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x20\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;32m\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x1b[1;38;5;111m\x3b\x20\x3b\x3b\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x1b[1;38;5;32m\x3b\x3b\x3b\x3b\x20\x20\x20\x3b\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x3b\x20\x20\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x3b\x3b\x3b\x3b\x3b\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x3b\x3b\x3b\x20\x20\x20\x20\x20\x3b\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x1b[0m"


#[kanashi.utility.utility.Utility]
class Utility:
	
	#[Utility.clear()]
	def clear( self ):
		system( "clear" )
	
	#[Utility.close( Mixed *args, Mixed **kwargs )]
	def close( self, *args, **kwargs ):
		self.output( *args, **kwargs )
		sys.exit()
	
	#[Utility.colorize( String format, String base )]:
	def colorize( self, string, base=None ):
		result = ""
		strings = [ x for x in re.split( r"((?:\x1b|\033)\[[0-9\;]+m)", string ) if x != "" ]
		regexps = {
			"number": {
				"pattern": r"(?P<number>\b(?:\d+)\b)",
				"colorize": "\x1b[1;38;5;61m{}{}"
			},
			"define": {
				"handler": lambda match: re.sub( r"(\.|\-){1,}", lambda m: "\x1b[1;38;5;69m{}\x1b[1;38;5;111m".format( m.group() ), match.group( 0 ) ),
				"pattern": r"(?P<define>(?:@|\$)[a-zA-Z0-9_\-\.]+)",
				"colorize": "\x1b[1;38;5;111m{}{}"
			},
			"symbol": {
				"pattern": r"(?P<symbol>\\|\:|\*|-|\+|/|&|%|=|\;|,|\.|\?|\!|\||<|>|\~){1,}",
				"colorize": "\x1b[1;38;5;69m{}{}"
			},
			"bracket": {
				"pattern": r"(?P<bracket>\{|\}|\[|\]|\(|\)){1,}",
				"colorize": "\x1b[1;38;5;214m{}{}"
			},
			"boolean": {
				"pattern": r"(?P<boolean>\b(?:False|True|None)\b)",
				"colorize": "\x1b[1;38;5;199m{}{}"
			},
			"typedef": {
				"pattern": r"(?P<typedef>\b(?:int|float|str|list|tuple|dict|set|bool|range|AttributeError|BaseException|BaseExceptionGroup|GeneratorExit|KeyboardInterrupt|BufferError|EOFError|ExceptionGroup|ImportError|ModuleNotFoundError|LookupError|IndexError|KeyError|MemoryError|NameError|UnboundLocalError|OSError|BlockingIOError|ChildProcessError|ConnectionError|BrokenPipeError|ConnectionAbortedError|ConnectionRefusedError|ConnectionResetError|FileExistsError|FileNotFoundError|InterruptedError|IsADirectoryError|NotADirectoryError|PermissionError|ProcessLookupError|TimeoutError|ReferenceError|RuntimeError|NotImplementedError|RecursionError|StopAsyncIteration|StopIteration|SyntaxError|IndentationError|TabError|SystemError|TypeError|ValueError|UnicodeError|UnicodeDecodeError|UnicodeEncodeError|UnicodeTranslateError|Warning|BytesWarning|DeprecationWarning|EncodingWarning|FutureWarning|ImportWarning|PendingDeprecationWarning|ResourceWarning|RuntimeWarning|SyntaxWarning|UnicodeWarning|UserWarning)\b)",
				"colorize": "\x1b[1;38;5;213m{}{}"
			},
			"linked": {
				"handler": lambda match: re.sub( r"(\\|\:|\*|-|\+|/|&|%|=|\;|,|\.|\?|\!|\||<|>|\~){1,}", lambda m: "\x1b[1;38;5;69m{}\x1b[1;38;5;43m".format( m.group() ), match.group( 0 ) ),
				"pattern": r"(?P<linked>\bhttps?://[^\s]+)",
				"colorize": "\x1b[1;38;5;43m\x1b[4m{}{}"
			},
			"version": {
				"handler": lambda match: re.sub( r"([\d\.]+)", lambda m: "\x1b[1;38;5;190m{}\x1b[1;38;5;112m".format( m.group() ), match.group( 0 ) ),
				"pattern": r"(?P<version>\b[vV][\d\.]+\b)",
				"colorize": "\x1b[1;38;5;112m{}{}"
			},
			"kanashi": {
				"pattern": r"(?P<kanashi>\b(?:[kK]anash[i|ī])\b)",
				"colorize": "\x1b[1;38;5;111m{}{}"
			},
			"comment": {
				"pattern": r"(?P<comment>\#\S+)",
				"colorize": "\x1b[1;38;5;250m{}{}"
			},
			"string": {
				"handler": lambda match: re.sub( r"(?<!\\)(\\\"|\\\'|\\`|\\r|\\t|\\n|\\s)", lambda m: "\x1b[1;38;5;208m{}\x1b[1;38;5;220m".format( m.group() ), match.group( 0 ) ),
				"pattern": r"(?P<string>(?<!\\)(\".*?(?<!\\)\"|\'.*?(?<!\\)\'|`.*?(?<!\\)`))",
				"colorize": "\x1b[1;38;5;220m{}{}"
			}
		}
		if not isinstance( base, str ):
			base = "\x1b[0m"
		try:
			last = base
			escape = None
			pattern = "(?:{})".format( "|".join( regexp['pattern'] for regexp in regexps.values() ) )
			compile = re.compile( pattern, re.MULTILINE | re.S )
			skipable = []
			for idx, string in enumerate( strings ):
				if  idx in skipable:
					continue
				color = re.match( r"^(?:\x1b|\033)\[([^m]+)m$", string )
				if  color != None:
					index = idx +1
					escape = color.group( 0 )
					last = escape
					try:
						while( rescape := re.match( r"(?:\x1b|\033)\[([^m]+)m", strings[index] ) ) is not None:
							skipable.append( index )
							escape += rescape.group( 0 )
							last = rescape.group( 0 )
							index += 1
					except IndexError:
						break
					if  index +1 in skipable:
						index += 1
					skipable.append( index )
				else:
					escape = last
					index = idx
				string = strings[index]
				search = 0
				match = None
				while( match := compile.search( string, search ) ) is not None:
					if match.groupdict():
						groups = match.groupdict().keys()
						for group in groups:
							if  group in regexps and \
								isinstance( regexps[group], dict ) and \
								isinstance( match.group( group ), str ):
								colorize = regexps[group]['colorize']
								break
						chars = match.group( 0 )
						if  "rematch" in regexps[group] and typedef( regexps[group]['rematch'], dict ):
							pass
						if  "handler" in regexps[group] and callable( regexps[group]['handler'] ):
							result += escape
							result += string[search:match.end() - len( chars )]
							result += colorize.format( regexps[group]['handler']( match ), escape )
							search = match.end()
							continue
						result += escape
						result += string[search:match.end() - len( chars )]
						result += colorize.format( chars, escape )
						search = match.end()
					pass
				result += escape
				result += string[search:]
				#escape = None
		except Exception as e:
			print( e )
			print( e.__traceback__.tb_lineno )
		return result
	
	#[Utility.exit( Mixed *args, Mixed **kwargs )]
	def exit( self, *args, **kwargs ):
		self.close( *args, **kwargs )
	
	#[Utility.emit( BaseException|Error|List error )]
	def emit( self, error: BaseException ):
		self.clear()
		name = type( self ).__name__
		strings = f"{name}\x2e\x65\x72\x72\x6f\x72\x0a"
		if  isinstance( error, Error ):
			message = error.message
			code = error.code
			prev = error.prev
			if  isinstance( prev, BaseException ):
				prevName = type( prev ).__name__
				prevMessage = str( prev )
				try:
					prevFile = prev.__traceback__.tb_frame.f_code.co_filename
					prevLine = prev.__traceback__.tb_lineno
				except AttributeError:
					prevFile = None
					prevLine = None
				prev = ""
				if  prevFile and prevLine:
					prev += f"\x20\x20{name}\x2e\x70\x72\x65\x76\x20{prevName}\x0a"
					prev += f"\x20\x20\x20\x20{prevFile}\x20{prevLine}\x0a"
				prev += f"\x20\x20{name}\x2e\x70\x72\x65\x76\x20{prevName}\x0a"
				prev += f"\x20\x20\x20\x20{prevMessage}\x0a"
			else:
				prev = ""
			try:
				file = error.__traceback__.tb_frame.f_code.co_filename
				line = error.__traceback__.tb_lineno
			except AttributeError:
				file = "Initialize"
				line = "\x70\x61\x73\x73\x65\x64"
			error = type( error ).__name__
			strings += prev
			strings += f"\x20\x20{name}\x2e\x72\x61\x69\x73\x65\x20{error}\x20{code}\x0a"
			strings += f"\x20\x20{name}\x2e\x72\x61\x69\x73\x65\x20{error}\x0a"
			strings += f"\x20\x20\x20\x20{file}\x20{line}\x0a"
			strings += f"\x20\x20\x20\x20{message}\x0a"
		else:
			if  isinstance( error, list ):
				try:
					message = [ str( error[0] ), error[1] ]
				except IndexError:
					message = str( error[0] )
				try:
					filename = error[0].__traceback__.tb_frame.f_code.co_filename
					lineno = error[0].__traceback__.tb_lineno
				except AttributeError:
					filename = None
					lineno = None
				error = type( error[0] ).__name__
			else:
				message = str( error )
				try:
					filename = error.__traceback__.tb_frame.f_code.co_filename
					lineno = error.__traceback__.tb_lineno
				except AttributeError:
					filename = None
					lineno = None
				error = type( error ).__name__
			strings = f"{name}\x2e\x65\x72\x72\x6f\x72\x0a "
			strings += f"\x20\x20{name}\x2e\x72\x61\x69\x73\x65\x20{error}\x0a"
			if  filename and lineno:
				strings += f"\x20\x20\x20\x20{filename}\x20{lineno}\x0a"
			if  isinstance( message, list ):
				for i in range( len( message ) ):
					strings += f"\x20\x20\x20\x20{message[i]}\x0a"
			else:
				strings += f"\x20\x20\x20\x20{message}\x0a"
		for subject in findall( r"(\[Errno\s\d+\]\s*)", strings ):
			strings = strings.replace( subject, "" )
		print( "\x0a\x7b\x7d\x0a\x0a\x0a\x7b\x7d".format( banner, self.colorize( f"\x1b[0m{strings}" ) ) )
	
	#[Utility.getpass( String label )]
	def getpass( self, label, ignore=True ):
		if  label == None or label == "":
			place = "\x7b\x7d\x2e\x67\x65\x74\x70\x61\x73\x73\x3a\x20".format( type( self ).__name__ )
		else:
			place = "\x7b\x7d\x3a\x20".format( label )
		try:
			value = getpass( self.colorize( place ) )
			if  value == "":
				value = self.getpass( label, ignore )
			return value
		except EOFError as e:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		except KeyboardInterrupt as e:
			if  ignore == False:
				self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
			print( "\r" )
			return self.getpass( label, ignore )
	
	#[Utility.input( String label )]:
	def input( self, label, default=None, number=False, ignore=True ):
		if  label == None or label == "":
			place = "\x7b\x7d\x2e\x69\x6e\x70\x75\x74\x3a\x20".format( type( self ).__name__ )
		else:
			if  label != "<<<" and label != ">>>":
				place = "\x7b\x7d\x3a\x20".format( label )
			else:
				place = label
		try:
			if  number:
				value = int( float( input( self.colorize( place ) ) ) )
			else:
				value = input( self.colorize( place ) )
			if  value == "":
				if  default != None:
					value = default if type( default ).__name__ != "list" else default[0]
				else:
					value = self.input( label, default, number, ignore )
			if  type( default ).__name__ == "list":
				try:
					default.index( value )
				except ValueError:
					value = self.input( label, default, number, ignore )
			return value
		except ValueError as e:
			return self.input( label, default, number, ignore )
		except EOFError as e:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		except KeyboardInterrupt as e:
			if  ignore == False:
				self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
			print( "\r" )
			return self.input( label, default, number, ignore )
	
	#[Utility.open( String target )]:
	def open( self, target ):
		try:
			system( "xdg-open {}".format( target ) )
		except BaseException:
			pass
	
	#[Utility.output( Object refer, Dict|List|String message, Bool line )]:
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
		if  isinstance( refer, BaseException ):
			strings += f"\x20\x20{named}\x2e{refer}\x2e{base.__traceback__.tb__lineno}\x0a"
			strings += f"\x20\x20{named}\x2e{refer}\x2e{__name__}\x0a"
		else:
			strings += f"\x20\x20{named}\x2e{refer}\x0a"
		strings += self.println( message, 4, line )
		print( "\x0a\x7b\x7d\x0a\x0a\x0a\x7b\x7d".format( banner, self.colorize( f"\x1b[0m{strings}" ) ) )
	
	#[Utility.previous( Function | Method back, String label, *args, **kwargs )]
	def previous( self, back, label=None, *args, **kwargs ):
		match type( back ).__name__:
			case "function" | "method":
				if  label == None:
					try:
						label = f"Back ({back.__self__.__class__.__name__})"
					except AttributeError:
						label = f"Back ({back.__name__})"
				self.input( label, default="" )
				return back( *args, **kwargs )
			case _:
				raise ValueError( f"Argument back must be type Function|Method, {type( back ).__name__} given" )
	
	#[Utility.println( Dict|List|String message, Int indent, Bool line )]
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
							if  line:
								stack += "\x7b\x30\x7d\x7b\x31\x7d\x29\x20\x7b\x32\x7d\x0a".format( space, i, message[i] )
							else:
								stack += "\x7b\x30\x7d\x7b\x31\x7d\x0a ".format( space, message[i] )
			case "list":
				u = 0
				l = len( message )
				for i in range( l ):
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
							if  line:
								index = i +1 -u
								length = len( str( l ) )
								length = length +1 if length == 1 else length
								format = f"\x7b\x30\x7d\x7b\x31\x3a\x30\x3e{length}\x7d\x29\x20\x7b\x32\x7d\x0a"
								stack += format.format( space, index, message[i] )
							else:
								stack += "\x7b\x30\x7d\x7b\x31\x7d\x0a".format( space, message[i] )
			case _:
				stack = "\x7b\x30\x7d\x7b\x31\x7d\x0a".format( space, message )
		return stack
	
	#[Utility.rmdoc( Dict lists )]
	def rmdoc( self, lists ):
		stack = []
		for i in lists:
			match type( lists[i] ).__name__:
				case "dict" | "list" | "set" | "tuple":
					pass
				case _:
					stack.append( i )
		return stack
	
	#[Utility.thread( String strings, Function Object, *args, **kwargs )]
	def thread( self, strings, target, *args, **kwargs ):
		self.clear()
		print( "\x0a\x7b\x7d\x0a\x0a\x0a".format( banner ) )
		try:
			task = Thread( target=target, args=args, kwargs=kwargs )
			named = type( self ).__name__
			strings = "\x7b\x30\x7d\x7b\x31\x7d".format( "\x20" *4, strings )
			sys.stdout.write( self.colorize( "\x7b\x31\x7d\x2e\x74\x68\x72\x65\x61\x64\x0a\x7b\x30\x7d\x7b\x31\x7d\x2e\x61\x6c\x69\x76\x65\x0a".format( "\x20" *2, named ) ) )
			for e in strings:
				sys.stdout.write( e )
				sys.stdout.flush()
				if  e != "\x20":
					#sleep( 00000.1 )
					pass
			task.start()
			while task.is_alive():
				for i in "\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x5c\x7c\x2f\x2d\x20":
					print( "\x0d\x7b\x7d\x20\x1b[1;33m\x7b\x7d".format( self.colorize( strings ), i ), end="" )
					#sleep( 00000.1 )
			print( "\x0d\x0a" )
			#sleep( 00000.1 )
			self.clear()
		except EOFError as e:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		except KeyboardInterrupt:
			self.close( e, "\x46\x6f\x72\x63\x65\x20\x63\x6c\x6f\x73\x65" )
		error = task.getExcept()
		if  isinstance( error, BaseException ):
			raise error
		else:
			return task.getReturn()
	
	#[Utility.tryAgain( String label, Function | Method next, Function | Method other, String value, List defaultValue, *args, **kwargs )]:
	def tryAgain( self, label="Try again [Y/n]", next=None, other=None, value="Y", defaultValue=[ "Y", "y", "N", "n" ], *args, **kwargs ):
		if  self.input( label, default=defaultValue ).upper() == value:
			if  callable( next ):
				return next( *args, **kwargs )
			else:
				raise ValueError( "Argument next must be type Function|Method, {} passed".format( type( next ).__name__ ) )
		else:
			if  callable( other ):
				return other()
		pass
	