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

from builtins import bool as Bool, int as Int, str as Str
from json import dumps as JsonEncoder
from re import match
from typing import Any, Dict, final, List, MutableMapping, MutableSequence, MutableSet, Self, Tuple, Union

from kanashi.common import droper, serializeable, typeof
from kanashi.library.represent import Represent
from kanashi.typing.builtins import Key, Val
from kanashi.typing.immutable import Immutable


class Map( MutableMapping[Key,Val] ):
	
	""" Map Typing Implementation """
	
	def __init__( self, collection:Union[Self,MutableMapping[Key,Val]]=None ) -> None:
		
		"""
		Construct method of class Map
		
		:params MutableMapping<Key, Value>|Map data
		
		:return None
		"""
		
		self.__dict__['__index__'] = 0
		self.__dict__['__values__'] = []
		self.__dict__['__keysets__'] = []
		if isinstance( self, Immutable ):
			self.__dict__['__excepts__'] = []
		self.update( collection if isinstance( collection, MutableMapping ) else {} )
	
	@final
	def __contains__( self, name:Key ) -> Bool:
		
		"""
		Return whether the map has attribute or item
		
		:params Key name
		
		:return Bool
		"""
		
		return name in self.__keysets__
	
	@final
	def __delattr__( self, key:Key ) -> None:
		
		"""
		Delete map attribute
		
		:params Key key
		
		:return None
		"""
		
		if key in self.__dict__:
			if key not in [ "__keysets__", "__index__", "__values__" ]:
				del self.__dict__[key]
		elif key in self.__dict__['__keysets__']:
			del self.__dict__['__keysets__'][key]
	
	@final
	def __delitem__( self, index:Key ) -> None:
		
		"""
		Delete map item
		
		:params Key index
		
		:return None
		"""
		
		if index in self.__dict__['__keysets__']:
			del self.__dict__['__keysets__'][index]
		elif index in self.__dict__:
			if index not in [ "__keysets__", "__index__", "__parent__" ]:
				del self.__dict__[index]
	
	@final
	def __getattr__( self, name:Key ) -> Val:
		
		"""
		Return map attribute value
		
		:params Key name
		
		:return Val
		"""
		
		if name in self.__dict__:
			return self.__dict__[name]
		if name in self.__dict__['__keysets__']:
			return self.__dict__['__values__'][self.__dict__['__keysets__'].index( name )]
		raise AttributeError( "\"{}\" Map object has no attribute \"{}\"".format( typeof( self ), name ) )
	
	@final
	def __getitem__( self, key:Key ) -> Val:
		
		"""
		Return map item value
		
		:params Key key
		
		:return Val
		"""
		
		if key in self.__dict__['__keysets__']:
			return self.__dict__['__values__'][self.__dict__['__keysets__'].index( key )]
		if key in self.__dict__:
			return self.__dict__[key]
		raise KeyError( "\"{}\" Map object has no item \"{}\"".format( typeof( self ), key ) )
	
	@final
	@property
	def __index__( self ) -> Int:
		
		""" Return number of index iteration """
		
		return self.__dict__['__index__']
	
	@final
	def __iter__( self ) -> Self:
		return self
	
	@final
	def __iterator__( self, values:Union[Self,MutableMapping[Key,Val],MutableSequence[Val],MutableSet[Val],Tuple[Val]] ) -> Union[Self,MutableMapping[Key,Val],MutableSequence[Val],MutableSet[Val],Tuple[Val]]:
		
		"""
		Map value iterator normalizer
		
		:params MutableMapping<Key,Val>|MutableSequence<Val>|MutableSet<Val>|Tuple<Val> values
		
		:return MutableMapping<Key,Val>|MutableSequence<Val>|MutableSet<Val>|Tuple<Val>
		"""
		
		if isinstance( values, Immutable ):
			return values
		if isinstance( values, MutableMapping ):
			keysets = list( values.keys() )
			for keyset in keysets:
				value = values[keyset]
				if not isinstance( value, ( MutableMapping, MutableSequence, MutableSet, tuple ) ):
					continue
				if isinstance( value, Map ):
					define = typeof( value )
					if not isinstance( value, Mapping ) and define not in [ "Map", "MapBuilder" ]:
						value = builder( self, value )
				elif isinstance( value, MutableMapping ):
					value = Map( value )
				else:
					value = self.__iterator__( value )
				values[keyset] = value
		if isinstance( values, ( MutableSequence, MutableSet, tuple ) ):
			typedef =  type( values )
			values = list( values )
			for i, value in enumerate( values ):
				if not isinstance( value, MutableMapping ):
					continue
				if isinstance( value, ( MutableMapping, MutableSequence, MutableSet, tuple ) ):
					if isinstance( value, Map ):
						define = typeof( value )
						if not isinstance( value, Mapping ) and define not in [ "Map", "MapBuilder" ]:
							value = builder( self, value )
					elif isinstance( value, MutableMapping ):
						value = Map( value )
					else:
						value = self.__iterator__( value )
				if isinstance( value, ( MutableSequence, MutableSet, tuple ) ):
					value = self.__iterator__( value )
				values[i] = value
			values = typedef( values )
		return values
	
	@final
	def __serialize__( self, *args:Any, **kwargs:Any ) -> Str:
		
		"""
		Return serialized of Map
		
		:params Any *args
		:params Any **kwargs
		
		:return Str
		"""
		
		def iterator( values:Union[Dict[Key,Val],List[Val]] ) -> Dict[Key,Val]:
			if isinstance( values, dict ):
				for keyset in values:
					value = values[keyset]
					if isinstance( value, ( dict, list ) ):
						values[keyset] = iterator( values[keyset] )
					elif not serializeable( value ):
						values[keyset] = str( value )
			elif isinstance( values, list ):
				for index, value in enumerate( values ):
					if isinstance( value, ( dict, list ) ):
						values[index] = iterator( value )
					elif not serializeable( value ):
						values[index] = str( value )
			return values
		return JsonEncoder( iterator( self.__props__() ), *args, **kwargs )
	
	@final
	def __len__( self ) -> Int:
		
		""" Return length of map """
		
		return len( self.__dict__['__keysets__'] )
	
	@final
	def __next__( self ) -> Tuple[Key,Val]:
		
		""" Return next iteration """
		
		index = self.__dict__['__index__']
		values = self.__dict__['__values__']
		keysets = self.__dict__['__keysets__']
		length = self.length
		try:
			if index < length:
				self.__index__ += 1
				keyset = keysets[index]
				value = values[index]
				return tuple( (keyset, value) )
		except IndexError:
			pass
		raise StopIteration
	
	@final
	def __props__( self ) -> Dict[Key,Val]:
		
		"""
		Return Dictionary of Map
		
		:return Dict<Key, Value>
		"""
		
		result = {}
		values = self.__dict__['__values__']
		for index, keyset in enumerate( self.__dict__['__keysets__'] ):
			if isinstance( values[index], Map ):
				result[keyset] = values[index].__props__()
			elif isinstance( values[index], list ):
				result[keyset] = []
				for item in values[index]:
					if isinstance( item, Map ):
						result[keyset].append( item.__props__() )
					else:
						result[keyset].append( item )
			else:
				result[keyset] = values[index]
		return result
	
	@final
	def __repr__( self ) -> Str:
		
		"""
		Return string representation of Map.
		
		:return Str
		"""
		
		return Represent.convert( self, indent=4 )
	
	@final
	def __set__( self, keyset:Key, values:Union[Self,MutableMapping[Key,Val],MutableSequence[Val],MutableSet[Val],Tuple[Val]] ) -> None:
		
		"""
		Map setter
		
		:params Key keyset
		:params MutableMapping<Key,Val>|MutableSequence<Val>|MutableSet<Val>|Tuple<Val> values
		
		:return None
		:raises TypeError
			When the keyset is set and Map is Immutable
		"""
		
		values = self.__iterator__( values )
		excepts = [ "__index__" ]
		if isinstance( self, Immutable ):
			excepts = [ *excepts, *self.__dict__['__excepts__'] ]
		else:
			excepts = [ *excepts, *self.__dict__['__keysets__'] ]
		for eliminate in [ "__excepts__", "__keysets__", "__values__" ]:
			if eliminate in excepts:
				del excepts[excepts.index( eliminate )]
			...
		if keyset in self.__dict__:
			if keyset == "__excepts__":
				if isinstance( values, list ):
					for value in values:
						if not isinstance( value, str ):
							if keyset in self.__dict__:
								raise TypeError( f"Cannot override attribute \"{keyset}\", cannot override attribute that has been set in a class that extends the Immutable class" )
							self.__dict__['__excepts__'] = excepts
							break
						self.__dict__['__excepts__'].append( value )
					...
				...
			if keyset not in excepts:
				raise TypeError( f"Cannot override attribute \"{keyset}\", cannot override attribute that has been set in a class that extends the Immutable class" )
			self.__dict__[keyset] = values
		elif keyset in self.__dict__['__keysets__']:
			if keyset not in excepts:
				raise TypeError( f"Cannot override item \"{keyset}\", cannot override item that has been set in a class that extends the Immutable class" )
			position = self.__dict__['__keysets__'].index( keyset )
			original = self.__dict__['__values__'][position]
			if values is not original:
				if isinstance( original, Map ) and isinstance( values, MutableMapping ):
					originalNamedType = typeof( original )
					differentNamedType = typeof( values )
					if originalNamedType not in [ "Map", "MapBuilder", differentNamedType ]:
						self.__dict__['__values__'][position] = values
					if isinstance( values, Map ):
						for generic in values:
							original[generic[0]] = generic[1]
						...
					else:
						for key in values:
							original[key] = values[key]
						...
					...
				elif isinstance( original, list ) and isinstance( values, list ):
					for item in values:
						if item not in original:
							original.append( item )
						...
					...
				else:
					self.__dict__['__values__'][position] = values
				...
			...
		else:
			self.__dict__['__keysets__'].append( keyset )
			self.__dict__['__values__'].append( values )
		...
	
	@final
	def __setattr__( self, name:Key, value:Val ) -> None:
		
		"""
		Map set or update attribute value by name
		
		:params Key name
		:params Val value
		
		:return None
		"""
		
		self.__set__( name, value )
	
	@final
	def __setitem__( self, key:Key, value:Val ) -> None:
		
		"""
		Map set or update item value by key
		
		:params Key key
		:params Val value
		
		:return None
		"""
		
		self.__set__( key, value )
	
	@final
	def __str__( self ) -> Str:
		
		""" Return serialized map """
		
		return self.__serialize__()
	
	@final
	def keys( self ) -> List[Key]:
		
		""" Return list of map keyset """
		
		return self.__dict__['__keysets__']
	
	@final
	@property
	def length( self ) -> Int:
		
		""" Return length of map """
		
		return self.__len__()
	
	def update( self, collection:Union[Self,MutableMapping[Key,Val]] ) -> None:
		
		"""
		Update the Map object
		
		:params MutableMapping<Key,Val> collection
		
		:return None
		:raises TypeError
			When the value of parameter is invalid value
		"""
		
		if not isinstance( collection, MutableMapping ):
			raise TypeError( "Invalid \"collection\" parameter, value must be type MutableMapping<Key,Val>, {} passed".format( typeof( collection ) ) )
		if isinstance( collection, Map ):
			for generic in collection:
				self.__set__( generic[0], generic[1] )
			...
		else:
			for keyset in collection:
				self.__set__( keyset, collection[keyset] )
			...
		...
	
	...

class Mapping( Map[Key,Val] ):

	""" Mapping Typing Implementation """
	
	@final
	def __init__( self, collection:Union[Self,MutableMapping[Key,Val]]=None ) -> None:
		
		"""
		Construct method of class Mapping
		
		:params MutableMapping<Key,Val> collection
		
		:return None
		"""
		
		super() \
			.__init__(
				self.__resolver__(
					self.__mapper__( 
						self.__mapping__, 
						droper( 
							items=collection if collection is not None else {}, 
							search=self.__items__, 
							nested=self.__nested__ 
						) 
					)
				)
			)
		...
	
	@property
	def __items__( self ) -> Union[MutableMapping[Key,Val],MutableSequence[Val]]:
		
		""" Return mapping schema """
		
		raise NotImplementedError( "Property __items__ is not initialize or implemented" )
	
	@final
	def __mapper__( self, properties:MutableMapping[Key,Val], values:Any ) -> Any:
		
		"""
		Mapper of Map
		
		:params MutableMapping<Key,Val> properties
		:params Any values
		
		:return Any
		"""
		
		if not isinstance( values, ( MutableMapping, MutableSequence ) ): return values 
		for key in properties:
			if key in values:
				if isinstance( properties[key], type ):
					if isinstance( values[key], properties[key] ):
						continue
					if isinstance( values[key], MutableMapping ):
						values[key] = properties[key]( values[key] )
					elif isinstance( values[key], MutableSequence ):
						for i in range( len( values[key] ) ):
							if isinstance( values[key][i], properties[key] ):
								continue
							if not isinstance( properties[key], Map ):
								values[key][i] = properties[key]( **values[key][i] )
							else:
								values[key][i] = properties[key]( values[key][i] )
				elif isinstance( properties[key], MutableMapping ):
					if isinstance( properties[key], type ):
						if isinstance( values[key], properties[key] ):
							continue
					if isinstance( values[key], MutableMapping ):
						values[key] = self.__mapper__( properties[key], values[key] )
					elif isinstance( values[key], MutableSequence ):
						for i in range( len( values[key] ) ):
							if isinstance( values[key][i], properties[key] ):
								continue
							if isinstance( values[key][i], MutableMapping ):
								values[key][i] = self.__mapper__( properties[key], values[key][i] )
							...
						...
					...
				...
			...
		return values
	
	@property
	def __mapping__( self ) -> MutableMapping:
		
		""" Return mapping schema """
		
		return {
		}
	
	@property
	def __nested__( self ) -> Bool:
		
		""" Return whether if the schema of map support nested """
		
		return True
	
	@final
	def __resolver__( self, value:Any ) -> Any:
		
		"""
		Mapping resolver
		
		:params Any value
		
		:return Any
		"""
		
		if isinstance( value, Immutable ):
			return value
		elif isinstance( value, MutableMapping ):
			if isinstance( value, Map ):
				for generic in value:
					value[generic[0]] = self.__resolver__( generic[1] )
			else:
				for keyset in value:
					value[keyset] = self.__resolver__( value[keyset] )
		elif isinstance( value, MutableSequence ):
			value = list( self.__resolver__( v ) for v in value )
		elif isinstance( value, str ) and match( r"^\d+$", value ) is not None:
			value = int( value )
		return value
	
	@final
	def update( self, collection:Union[Self,MutableMapping[Key,Val]] ) -> None:
		
		"""
		Update the Map object
		
		:params MutableMapping<Key,Val> collection
		
		:return None
		:raises TypeError
			When the value of parameter is invalid value
		"""
		
		super() \
		.update(
			self.__resolver__(
				self.__mapper__( 
					self.__mapping__, 
					droper( 
						items=collection, 
						search=self.__items__, 
						nested=self.__nested__ 
					) 
				)
			)
		)

def builder( parent:Map[Key,Val], collection:Union[Map[Key,Val],MutableMapping[Key,Val]] ) -> Map[Key,Val]:
	
	"""
	Map builder for child, 
	
	:params Map parent
	:params Dict<Key, Value> data
	
	:return Map
	"""
	
	if not isinstance( parent, Map ):
		raise TypeError()
	if not isinstance( parent, type ):
		parent = type( parent )
	
	@final
	class MapBuilder( parent ):
		
		"""
		Children Map builder for avoid unhandled argument 
		when create new Map for children value
		"""
		
		def __init__( self, collection:Union[Self,MutableMapping[Key,Val]] ) -> None:
			Map.__init__( self, collection )
		
		...
	
	return MapBuilder( collection )
