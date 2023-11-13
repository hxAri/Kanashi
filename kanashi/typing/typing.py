#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022 13:44
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


from re import match
from typing import final

from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.utility import droper, typeof


#[kanashi.typing.typing.Typing]
class Typing( Object ):

	"""
	The Typing class has almost the same way of working as the Object class
	from Kanashi, but Typing will only forward the items returned by the __items__
	method to its parent class, its Object from Kanashi, the aim is to avoid errors
	when checking response data and so on because, Kanashi treats dictionaries and also
	lists as objects will be very confusing considering that Instagram usually provides
	a fairly large response to be processed and, when the JSON response is passed to a
	class that extends the Typing class it will only take and also set the value that
	was returned by the previous __items__ method however, we can also set incompatible
	items from outside the class or inside except the instance.

	Apart from that, Typing also normalizes strings to int values ​​if the value only contains numbers.
	"""

	#[Typing( Dict|List|Object data, Object parent )]: None
	@final
	def __init__( self, data:dict|Object, parent:object=None ) -> None:
		if not isinstance( data, ( dict, Object ) ):
			raise TypeError( "Invalid \"data\" parameter, value must be type Dict|Object, {} passed".format( typeof( data ) ) )
		parent = super()
		parent.__init__(
			self.__resolver__(
				self.__mapper__( 
					self.__mapping__, 
					droper( 
						items=data, 
						search=self.__items__, 
						nested=self.__nested__ 
					) 
				)
			)
		)
	
	#[Typing.__items__]: Dict<Str, Str>|List<Str>
	@property
	def __items__( self ) -> dict[str:str]|list[str]:
		raise NotImplementedError( "Property {} is not initialize or implemented".format( self.__allows__ ) )
	
	#[Typing.__mapper__( Dict|Object properties, Any values )]: Any
	@final
	def __mapper__( self, properties:dict|Object, values:any ) -> any:
		if not isinstance( values, ( dict, list, Object ) ): return values 
		for key in list( properties.keys() ):
			if key in values:
				if isinstance( properties[key], type ):
					if isinstance( values[key], properties[key] ):
						continue
					elif isinstance( values[key], ( dict, Object ) ):
						values[key] = properties[key]( values[key] )
					elif isinstance( values[key], list ):
						for i in range( len( values[key] ) ):
							if isinstance( values[key][i], properties[key] ):
								continue
							values[key][i] = properties[key]( values[key][i] )
						...
					...
				elif isinstance( properties[key], ( dict, Object ) ):
					if isinstance( properties[key], type ):
						if isinstance( values[key], properties[key] ):
							continue
					if isinstance( values[key], ( dict, Object ) ):
						values[key] = self.__mapper__( properties[key], values[key] )
					elif isinstance( values[key], list ):
						for i in range( len( values[key] ) ):
							if isinstance( values[key][i], properties[key] ):
								continue
							if isinstance( values[key][i], ( dict, Object ) ):
								values[key][i] = self.__mapper__( properties[key], values[key][i] )
						...
			...
		return values
	
	#[Typing.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object: return {}
	
	#[Typing.__nested__]: Bool
	@property
	def __nested__( self ) -> bool: return True

	#[Typing.__resolver__( Any value )]: Any
	@final
	def __resolver__( self, value:any ) -> any:
		if isinstance( value, Readonly ):
			return value
		if isinstance( value, ( dict, list, Object ) ):
			if isinstance( value, dict ):
				indexs = list( value.keys() )
			elif isinstance( value, Object ):
				indexs = value.keys()
			else:
				indexs = [ idx for idx in range( len( value ) ) ]
			for i in range( len( indexs ) ):
				index = indexs[i]
				value[index] = self.__resolver__( value[index] )
		elif isinstance( value, str ):
			if match( r"^\d+$", value ):
				value = int( value )
		return value