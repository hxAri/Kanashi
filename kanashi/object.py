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

from kanashi.utils.json import JSON
from kanashi.utils.json import JSONError

#[kanashi.Object]
class Object:
	
	#[Object( Dictionary data, Object parent )]
	def __init__( self, data, parent=None ):
		self.__parent__ = parent
		self.__method__ = {}
		self.__data__ = {}
		
		# Inject data.
		self.set( data )
		
	#[Object.__repr__()]
	def __repr__( self ):
		return( self.json() )
		
	#[Object.__str__()]
	def __str__( self ):
		return( self.json() )
		
	#[Object.dict()]
	def dict( self ):
		data = {}
		copy = self.__data__
		for key in copy.keys():
			if isinstance( copy[key], Object ):
				data[key] = copy[key].dict()
			elif isinstance( copy[key], list ):
				data[key] = []
				for item in copy[key]:
					if isinstance( item, Object ):
						data[key].append( item.dict() )
					else:
						data[key].append( item )
			else:
				data[key] = copy[key]
		return( data )
		
	#[Object.dump()]
	def dump( self ):
		return( "{}".format( self.dict() ) )
		
	#[Object.json()]
	def json( self ):
		return( JSON.encode( self.dict() ) )
		
	#[Object.idxs()]
	def idxs( self ):
		return([ idx for idx in range( len( self.__data__ ) ) ])
		
	#[Object.keys()]
	def keys( self ):
		return( list( self.__data__.keys() ) )
		
	#[Object.get()]
	def get( self, key ):
		return( self.__dict__[key] )
		
	#[Object.len()]
	def len( self ):
		return( len( self.__data__ ) )
		
	#[Object.__set( Dictionary data )]
	def set( self, data ):
		match type( data ).__name__:
			case "dict":
				for key in data.keys():
					self.__data__[key] = data[key]
					match type( data[key] ).__name__:
						case "dict":
							self.__dict__[key] = Object( data[key] )
						case "list":
							self.__dict__[key] = []
							for item in data[key]:
								if type( item ).__name__ == "dict":
									self.__dict__[key].append( Object( item ) )
								else:
									self.__dict__[key].append( item )
						case _:
							self.__dict__[key] = data[key]
			case "str":
				try:
					self.set( JSON.decode( data ) )
				except JSONError as e:
					raise ValueError( "Invalid JSON String data parameter." )
			case _:
				raise ValueError( "Parameter data must be type Dictionary or JSON Strings, {} given".format( type( data ).__name__ ) )
		self.ref()
		
	#[Object.__ref()]
	def ref( self ) -> None:
		if self.__parent__ != None:
			for i, v in enumerate( self.__dict__ ):
				self.__parent__.__dict__[v] = self.__dict__[v]
	