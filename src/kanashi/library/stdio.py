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
from re import IGNORECASE
from re import Pattern, search as Search
from typing import Any, Callable, Dict, List, Union

from kanashi.common import colorize, typeof
from kanashi.typing.builtins import *


def stderr( context:BaseException, buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], line:Bool=False, close:Bool=False ) -> None:
	stdout( context, buffers, line=line )
	if close is True:
		exit( context.errno if hasattr( context, "errno" ) else 1 )
	...

def stdin( context:Any, label:Str=None, default:Union[Int,List[Union[Int,Str]],Str]=None, filters:Union[Callable|List[Union[Callable,Pattern]],Pattern]=None, number:Bool=False, password:Bool=False, ignore:Bool=True ) -> Int|None|Str:
	if not isinstance( label, Str ) or context is not None:
		if context is None:
			label = "Std<In>"
		elif isinstance( context, Str ):
			matched = Search( r"(?:\[Y\/n\])\s?$", context, IGNORECASE )
			if matched is None:
				label = "Std<In<{}>>".format( context )
			else:
				label = context
		else:
			define = typeof( context )
			if define in [ "function", "method", "method-wrapper" ]:
				label = "Std<In<{}>>".format( context.__qualname__\
					.replace( ".<locals>.", "<Nested>" ) \
					# .replace( ".", "$" )
				)
			else:
				label = "Std<In<{}>>".format( define.capitalize() )
		label = colorize( label )
		label+= "\x20"
	try:
		values = getpass( label ) if password is True else input( label )
		if not values:
			if default is None:
				return stdin( None, label, default, filters, number, password, ignore )
			if isinstance( default, list ):
				return stdin( None, label, default, filters, number, password, ignore ) if not default else default[0]
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
					raise TypeError( "Invalid input \"filters\", filters must be Callable|List<Callable,Pattern>|Pattern, {}:{} passed".format( typeof( i, filter ) ) )
			return values if number is False else int( values )
		elif isinstance( default, list ):
			if number is True:
				values = int( values )
			if values not in default:
				return stdin( None, label, default, filters, number, password, ignore )
			return values
		return values
	except EOFError as e:
		stderr( e, "Force close", close=True )
	except KeyboardInterrupt as e:
		if ignore is False:
			stderr( e, "Force close", close=True )
		print( "\r" )
		return stdin( None, label, default, filters, number, password, ignore )
	except ValueError as e:
		return stdin( None, label, default, filters, number, password, ignore )
	return None

def stdout( context:Any, buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], line:Bool=False ) -> None:
	...
