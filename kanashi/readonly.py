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


#[kanashi.readonly.Readonly]
class Readonly:
	
	"""
	Class representation for handling the readonly property.
	This means the class will not or should not override any values it has set.
	But if the attribute has not been set then the attribute will be allowed to be set.
	"""
	
	#[Readonly.__setitem__( String key, Mixed value )]: None
	def __setitem__( self, key, value ):
		
		"""
		Set class item.
		
		:params String key
			Item key name
		:params Mixed value
			Item values
		
		:return None
		:raises KeyError
			When the key or item has been previously set
		:raises TypeError
			When the object or class does not extends class kanashi.object.Object
		"""
		
		try:
			excepts = self.excepts
		except( AttributeError, KeyError ):
			excepts = []
		
		if isinstance( self, Object ):
			if self.isset( key ) and key not in excepts:
				raise KeyError( f"Cannot override key \"{key}\", cannot override key that has been set in a class that extends the Readonly class" )
			else:
				self.set({ key, value })
		else:
			if key not in excepts:
				raise TypeError( "\"{}\" object does not support item assignment".format( type( self ).__name__ ) )
	
	#[Readonly.__setattr__( String name, Mixed value )]: None
	def __setattr__( self, name, value ):
		
		"""
		Set class attribute.
		
		:params String name
			Attribute name
		:params Mixed value
			Attribute values
		
		:return None
		:raises AttributeError
			When the attribute has been previously set
		"""
		
		try:
			excepts = self.excepts
		except AttributeError:
			excepts = []
		
		if  name in self.__dict__:
			if  name not in excepts:
				raise AttributeError( f"Cannot override attribute \"{name}\", cannot override attribute that has been set in a class that extends the Readonly class" )
		
		# Allow set when the attribute does not set.
		self.__dict__[name] = value
	