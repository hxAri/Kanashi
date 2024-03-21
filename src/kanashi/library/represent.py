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

from typing import Any, final, List, MutableMapping, Union

from kanashi.common import typeof
from kanashi.typing.builtins import Int, Key, Str, Val


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
	def wrapper( data:Union[List[Val],MutableMapping[Key,Val]], indent:Int=4 ) -> Str:
		
		"""
		A wrapper method for handle generic object, e.g Dict, List, Map, etc
		
		:params Generic[Key]|MutableMapping[Key,Val] data
		:params Int indent
		
		:return Str
		"""
		
		values = []
		length = len( data )
		spaces = "\x20" * indent
		if isinstance( data, ( dict, MutableMapping ) ):
			define = "\"{}\""
			indexs = data.keys()
		else:
			define = "[{}]"
			indexs = list( idx for idx in range( length ) )
		for index in indexs:
			key = define.format( index )
			value = data[index]
			if isinstance( value, ( dict, MutableMapping ) ):
				if len( value ) >= 1:
					values.append( "{}: {}".format( key, Represent.convert( value, indent +4 ) ) )
				else:
					values.append( "{}: {}(\n{})".format( key, typeof( value ), spaces ) )
			elif isinstance( value, list ):
				length = len( value )
				lspace = indent + 4
				lspace = "\x20" * lspace
				if length >= 1:
					array = []
					for i in range( length ):
						if isinstance( value[i], ( dict, list, MutableMapping ) ):
							array.append( "[{}]: {}".format( i, Represent.convert( value[i], indent +8 ) ) )
						else:
							if isinstance( value[i], str ):
								value[i] = f"\"{Represent.normalize( value[i] )}\""
							array.append( "[{}]: {}({})".format( i, typeof( value[i] ), value[i] ) )
					values.append( "{0}: {1}[\n{2}{4}\n{3}]".format( key, typeof( value ), lspace, spaces, f",\n{lspace}".join( array ) ) )
				else:
					values.append( "{0}: {1}(\n{2})".format( key, typeof( value ), spaces ) )
			else:
				if isinstance( value, str ):
					value = f"\"{Represent.normalize( value )}\""
				values.append( "{}: {}({})".format( key, typeof( value ), value ) )
		return f",\n{spaces}".join( values )
	
	@staticmethod
	def convert( data:Any, indent:Int=4 ) -> Str:
		
		"""
		Convert Python objecct into string representation
		
		:params Any data
		:params Int indent
		
		:return Int
		"""
		
		if len( data ) >= 1:
			return "{}(\n{}{}\n{})".format( typeof( data ), "\x20" * indent, Represent.wrapper( data, indent=indent ), "\x20" * ( 0 if indent == 4 else indent -4 ) )
		return "{}(\n{})".format( typeof( data ), "\x20" * ( 0 if indent == 4 else indent -4 ) )

	...
