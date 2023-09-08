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

from kanashi.object import Object
from kanashi.utility import typedef, typeof

#[kanashi.collection.Collection]
class Collection:
	
	#[Collection( List|Dict|Object<Mixed> items, Mixed value, Mixed **kwargs )]
	def __init__( self, items, value, **kwargs ):

		"""
		Construct method of class Collection

		:params List|Dict|Object<Mixed> items
			Collection items
		:params Mixed value
			Collection value type
		:params Mixed **kwargs

		:return None
		:raises ValueError
			When the items is invalid value
		"""

		self.__kwargs__ = kwargs
		self.__items__ = []
		self.__index__ = 0
		self.__type__ = value
		if  typedef( items, dict ) or \
			typedef( items, list ) or \
			typedef( items, Object ):
			for item in items:
				self.__items__.append(
					value( item, **self.__kwargs__ )
				)
		else:
			raise ValueError( "Invalid value prameter, value must be type Dict|List|Object<{}>, {} passed".format( typeof( value ), typeof( items ) ) )
	
	#[Collection.__iter__()]: Collection
	def __iter__( self ):
		return self
	
	#[Collection.__next__()]: Mixed
	def __next__( self ):

		# Get current index iteration.
		index = self.__index__
		
		# Get object length.
		length = self.length
		try:
			if  index < length:
				self.__index__ += 1
				return self.__items__[index]
		except IndexError:
			pass
		raise StopIteration
	
	#[Collection.__getitem__( Int index )]: Mixed
	def __getitem__( self, index ):
		if  index in self.__items__:
			return self.__items__[index]
		raise IndexError( "\"{}\" collection has no index \"{}\"".format( typeof( self ), index ) ) 
	
	#[Collection.__setitem__( Int index, Mixed value )]: None
	def __setitem__( self, index, value ):
		if typedef( value, self.__type__, False ):
			raise ValueError( "Invalid value prameter, value must be {} int, {} passed".format( typeof( self.__type__ ), typeof( value ) ) )
		self.__items__[index] = value
	
	#[Collection.rewind()]: None
	def rewind( self ):
		self.__index__ = 0
	
	#[Collection.seek( Int index )]: None
	def seek( self, index ):
		if  index < 0:
			raise IndexError()
		if  index > self.length:
			raise IndexError()
	
	#[Collection.length]: Int
	@property
	def length( self ):
		return len( self.__items__ )
	