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

from builtins import int as Int, str as Str
from typing import (
	Any, 
	final, 
	MutableMapping, 
	MutableSequence, 
	MutableSet, 
	Sequence, 
	Union
)


@final
class Represent:
	
	""" A base class for handle print representation of object """
	
	@staticmethod
	def normalize( string:Str ) -> Str:
		
		"""
		Normalize the string character
		
		:params Str string
		
		:return Str
		"""
		
		return string \
			.replace( "\"", "\\\"" ) \
			.replace( "\n", "\\n" ) \
			.replace( "\t", "\\t" )
	
	@staticmethod
	def wrapper( data:Union[MutableMapping[Any,Any],MutableSequence[Any]], indent:Int=4 ) -> Str:
		
		"""
		A wrapper method for handle generic object, e.g MutableMapping, MutableSequence, Map, etc
		
		:params MutableMapping<Key,Val>|MutableSequence<Any> data
		:params Int indent
		
		:return Str
		"""
		
		values = []
		spaces = "\x20" * indent
		if isinstance( data, MutableMapping ):
			keysets = list( data.keys() )
			for keyset in keysets:
				value = data[keyset]
				define = value if isinstance( value, type ) else type( value )
				typing = define.__name__
				if isinstance( value, ( MutableMapping, MutableSequence, MutableSet, tuple ) ):
					represent = Represent.convert( value, indent+4 )
					values.append( f"{keyset}: {represent}" )
				elif isinstance( value, Str ):
					values.append( f"{keyset}: {typing}(\"{Represent.normalize( value )}\")" )
				elif value is not None:
					values.append( f"{keyset}: {typing}({value})" )
				else:
					values.append( f"{keyset}: None" )
				...
			...
		elif isinstance( data, ( MutableSequence, MutableSet, Sequence ) ):
			index = 0
			for value in data:
				define = value if isinstance( value, type ) else type( value )
				typing = define.__name__
				if isinstance( value, ( MutableMapping, MutableSequence, MutableSet, tuple ) ):
					represent = Represent.convert( value, indent+4 )
					values.append( f"[{index}]: {represent}" )
				elif isinstance( value, Str ):
					values.append( f"[{index}]: {typing}(\"{Represent.normalize( value )}\")" )
				elif value is not None:
					values.append( f"[{index}]: {typing}({value})" )
				else: 
					values.append( f"[{index}]: None" )
				index += 1
		else:
			print( typing )
		return f",\n{spaces}".join( values )
	
	@staticmethod
	def convert( data:Any, indent:Int=4 ) -> Str:
		
		"""
		Convert Python objecct into string representation
		
		:params Any data
		:params Int indent
		
		:return Int
		"""
		
		define = data if isinstance( data, type ) else type( data )
		typing = define.__name__
		spaces = "\x20" * ( 0 if indent == 4 else indent -4 )
		if isinstance( data, ( MutableMapping, MutableSequence, MutableSet, tuple ) ):
			length = len( data )
			if isinstance( data, tuple ):
				opening, closing = ( "\x28", "\x29" )
			if isinstance( data, ( MutableMapping, MutableSet ) ):
				opening, closing = ( "\x7b", "\x7d" )
			if isinstance( data, MutableSequence ):
				opening, closing = ( "\x5b", "\x5d" )
			after = "\x20" * int( 0 if indent == 4 else indent -4 )
			before = "\x20" * indent
			if length >= 1:
				wrapped = Represent.wrapper( data, indent=indent )
				return f"{typing}{opening}\n{before}{wrapped}\n{after}{closing}"
			return f"{typing}{opening}\n{after}{closing}"
		return f"{typing}(\n{spaces})"
		
	...
