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


from json import (
	dumps,
	JSONDecodeError as JSONError, 
	loads, 
)
from typing import Any

from kanashi.utility.common import typedef


#[kanashi.utility.json.JSON]
class JSON:
	
	#[Json.decode( String string, Mixed *args, Mixed **kwargs )]
	@staticmethod
	def decode( string, *args, **kwargs ):
		return( loads( string, *args, **kwargs ) )
		
	#[Json.encode( Mixed values, Mixed *args, Mixed **kwargs )]
	@staticmethod
	def encode( values, *args, **kwargs ):
		if typedef( values, "Object" ):
			return values.json()
		kwargs['indent'] = kwargs.pop( "indent", 4 )
		return( dumps( values, *args, **kwargs ) )
		
	#[Json.isSerializable( Mixed values )]
	@staticmethod
	def isSerializable( values ):
		
		"""
		Return if value is serializable.
		
		:params Mixed values
		
		:return Bool
		"""
		
		try:
			JSON.encode( values )
		except OverflowError:
			return( False )
		except TypeError:
			return( False )
		return( True )
	
