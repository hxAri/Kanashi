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


from typing import final

from kanashi import object as module
from kanashi.utility import typeof


#[kanashi.readonly.Readonly]
class Readonly:
	
	"""
	Class representation for handling the readonly property.
	This means the class will not or should not override any values it has set.
	But if the attribute has not been set then the attribute will be allowed to be set.
	"""
	
	#[Readonly.__setattr__( String name, Any value )]: None
	@final
	def __setattr__( self, name, value ) -> None:
		if isinstance( self, module.Object ):
			module.Object.__setattr__( self, name, value )
		else:
			excepts = []
			if "excepts" in self.__dict__:
				if isinstance( self.__dict__['excepts'], list ):
					for keyword in self.__dict__['excepts']:
						if keyword in excepts: continue
						if not isinstance( keyword, str ):
							excepts = []; break
						else:
							excepts.append( keyword )
			if name == "excepts":
				if isinstance( value, list ):
					allows = True
					for keyword in value:
						if keyword in excepts: continue
						if not isinstance( keyword, str ):
							allows = False; break
					if allows:
						self.__dict__['excepts'] = [ *excepts, *value ]
						return
			if name in self.__dict__:
				if name not in excepts:
					raise TypeError( f"Cannot override attribute \"{name}\", cannot override attribute that has been set in a class that extends the Readonly class" )
			self.__dict__[name] = value
		pass

	#[Readonly.__setitem__( String key, Any value )]: None
	@final
	def __setitem__( self, key, value ) -> None:
		if isinstance( self, module.Object ):
			module.Object.__setitem__( self, key, value )
		else:
			raise TypeError( "\"{}\" object does not support item assignment".format( typeof( self ) ) )
