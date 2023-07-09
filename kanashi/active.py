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


#[kanashi.active.Active]
class Active:
	
	#[Active( Dict user )]: None
	def __init__( self, user ):
		
		"""
		Construct method of class Active.
		
		:params Dict user
			User active data
		
		:return None
		:raises TypeError
			When the user data is invalid
		:raises ValueError
			When the user is invalid value
		"""
		
		if isinstance( user, dict ):
			if  "id" in user and \
				"fullname" in user and \
				"username" in user and \
				"password" in user and \
				"session" in user and \
				"browser" in user['session'] and \
				"cookies" in user['session'] and \
				"headers" in user['session'] and \
				"csrftoken" in user['session'] and \
				"sessionid" in user['session']:
				
				# Initialize Attributes.
				self.__parent__ = Object
				self.__parent__.__init__( self, user )
			else:
				raise TypeError( "Invalid user data" )
		else:
			raise ValueError( "Invalid user parameter, value must be type dict, {} passed".format( type( user ).__name__ ) )
		pass
	