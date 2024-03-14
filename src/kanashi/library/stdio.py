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

from getpass import getpass
from os import name as OSName, system
from re import IGNORECASE
from re import Pattern, search as Search
from typing import Any, Callable, Dict, List, Union

from kanashi.common import colorize, typeof
from kanashi.library.storage import Storage
from kanashi.typing.builtins import Bool, Int, Str
from kanashi.typing.throwable import Throwable


def arrange( buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], indent:Int=4, line:Bool=False ) -> Str:
	
	"""
	Builder to arrange the ouput template

	:params Dict<Str,Any>|List<Dict<Str,Any>>|Str buffers
		The output buffers
	:params Int indent
		The output indentation
	:params Bool line
		Allow current buffer with line

	:return Str
	"""
	
	outputs = []
	spaces = "\x20" * indent
	if isinstance( buffers, dict ):
		for keyset in buffers:
			values = buffers[keyset]
			if isinstance( values, ( set, tuple ) ):
				values = list( values )
			if isinstance( values, dict ):
				if "message" in values:
					outputs.append( arrange( values['message'], indent +4 if "line" in values and values['line'] else indent, "line" in values and not values['line'] ) )
				else:
					outputs.append( arrange( values, indent +4 if line else indent, not line ) )
			elif isinstance( values, list ):
				outputs.append( arrange( values, indent +4 if line else indent, not line ) )
			else:
				message = values if isinstance( values, str ) else repr( values )
				outputs.extend( list( "\x7b\x30\x7d\x7b\x31\x7d\x29\x20\x1b[1;38;5;252m\x7b\x32\x7d\x1b[0m".format( spaces, keyset, part ) if line is True else "\x7b\x30\x7d\x7b\x31\x7d".format( spaces, part ) for part in message.split( "\x0a" ) ) )
			...
		...
	elif isinstance( buffers, list ):
		index = 0
		length = len( buffers )
		for i in range( length ):
			values = buffers[i]
			if isinstance( values, ( set, tuple ) ):
				values = list( values )
			if isinstance( values, dict ):
				if "message" in values:
					outputs.append( arrange( values['message'], indent +4 if "line" in values and values['line'] else indent, "line" in values and not values['line'] ) )
				else:
					outputs.append( arrange( values, indent +4 if line else indent, not line ) )
				index += 1
			elif isinstance( values, list ):
				outputs.append( arrange( values, indent +4 if line else indent, not line ) )
				index += 1
			else:
				message = values if isinstance( values, str ) else repr( values )
				for part in message.split( "\x0a" ):
					if line is True:
						post = i +1 - index
						leng = len( str( length ) )
						leng = leng +1 if leng == 1 else leng
						outputs.append( f"\x7b\x30\x7d\x7b\x31\x3a\x30\x3e{leng}\x7d\x29\x20\x1b[1;38;5;252m\x7b\x32\x7d\x1b[0m".format( spaces, post, part ) )
					else:
						outputs.append( "\x7b\x30\x7d\x7b\x31\x7d".format( spaces, part ) )
				...
			...
		...
	else:
		message = buffers if isinstance( buffers, str ) else repr( buffers )
		outputs.extend( list( "\x7b\x30\x7d\x7b\x31\x7d".format( spaces, part ) for part in message.split( "\x0a" ) ) )
	return "\x0a".join( outputs )

def stderr( context:Any, thrown:BaseException, buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], line:Bool=False, close:Bool=False ) -> None:
	if close is True:
		exit( context.errno if hasattr( context, "errno" ) else 1 )
	if isinstance( thrown, Throwable ):
		...
	else:
		...
	prints = arrange( buffers, line=line )

def stdin( context:Any=None, prompt:Str=None, default:Union[Int,List[Union[Int,Str]],Str]=None, filters:Union[Callable|List[Union[Callable,Pattern]],Pattern]=None, separator:Str="\x2e", number:Bool=False, password:Bool=False, ignore:Bool=True ) -> Int|None|Str:
	if not isinstance( prompt, str ):
		if prompt is not None:
			defined = type( prompt )
			typedef = typeof( prompt )
			qualname = prompt.__qualname__ if hasattr( prompt, "__qualname__" ) else None
			if typedef in [ "function", "method", "method-wrapper" ]:
				define = context if isinstance( context, type ) else type( context )
				if define is prompt.__class__:
					context = define.__name__
					prompt = qualname
				elif qualname == context.__qualname__ or hasattr( prompt, "__self__" ) and context is prompt.__self__.__class__:
					qualparts = qualname.split( "\x2e" )
					context = qualparts[0]
					prompt = "\x2e".join( qualparts[1:] )
				else:
					prompt = prompt.__qualname__
					separator = "$"
			elif defined is context or prompt is context:
				context = typedef
				prompt = "in"
			else:
				prompt = typedef
		else:
			prompt = "in"
	if not isinstance( context, str ):
		if context is not None:
			typedef = typeof( context )
			if typedef in [ "function", "method", "method-wrapper" ]:
				context = context.__name__
			else:
				context = typedef
		else:
			context = "System"
	display = colorize( "".join([ context, separator, prompt ]) )
	display+= "\x20"
	try:
		values = getpass( display ) if password is True else input( display )
		if not values:
			if default is None:
				return stdin( context, prompt, default, filters, separator, number, password, ignore )
			if isinstance( default, list ):
				return stdin( context, prompt, default, filters, separator, number, password, ignore ) if not default else default[0]
			return default
		elif filters is not None:
			filters = filters if isinstance( filters, list ) else [filters]
			for i, filter in enumerate( filters ):
				if isinstance( filter, Pattern ):
					if filter.match( values ) is not None:
						break
				elif callable( filter ) is True:
					if filter( values ) is True:
						break
				else:
					raise TypeError( "Invalid input \"filters\", filters must be Callable|List<Callable|Pattern>|Pattern, {}:{} passed".format( i, typeof( filter ) ) )
			return values if number is False else int( values )
		elif isinstance( default, list ):
			if number is True:
				values = int( values )
			if values not in default:
				return stdin( context, prompt, default, filters, separator, number, password, ignore )
			return values
		return values
	except EOFError as e:
		stderr( context, e, "Force close", close=True )
	except KeyboardInterrupt as e:
		if ignore is False:
			stderr( context, e, "Force close", close=True )
		print( "\r" )
		return stdin( context, prompt, default, filters, separator, number, password, ignore )
	except ValueError as e:
		return stdin( context, prompt, default, filters, separator, number, password, ignore )
	return None

def stdout( context:Any, buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], clear=False, line:Bool=False ) -> None:
	if clear is True:
		system( "cls" if OSName in [ "nt", "windows" ] else "clear" )
	print( arrange( buffers, line=line ) )


filename = "62616e6e65722e6878"
if Storage.f( filename ):
	contents = Storage.cat( filename )
	banner = ""
	chunks = len( contents )
	chunkSize = 2
	for i in range( 0, chunks, chunkSize ):
		banner += bytes.fromhex( contents[i:i+chunkSize] ).decode( "ASCII" )
else:
	banner = ""
