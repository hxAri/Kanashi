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

from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.typing.user import User
from kanashi.utility import typeof


#[kanashi.typing.active.Active]
@final
class Active( Object, Readonly, User ):

	#[Active( Dict|Object user )]
	def __init__( self, user:dict|Object ) -> None:
		
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
		
		if isinstance( user, ( dict, Object ) ):
			if  "id" not in user and \
				"fullname" not in user and \
				"username" not in user and \
				"password" not in user and \
				"session" not in user and \
				"browser" not in user['session'] and \
				"cookies" not in user['session'] and \
				"headers" not in user['session'] and \
				"csrftoken" not in user['session'] and \
				"sessionid" not in user['session']:
				raise TypeError( "Invalid user data" )
			else:
				super().__init__({
					"id": int( user['id'] ),
					"fullname": user['fullname'],
					"username": user['username'],
					"password": user['password'],
					"session": {
						"browser": user['session']['browser'],
						"cookies": user['session']['cookies'],
						"headers": user['session']['headers'],
						"csrftoken": user['session']['csrftoken'],
						"sessionid": user['session']['sessionid']
					}
				})
		else:
			raise ValueError( "Invalid user parameter, value must be type dict|Object, {} passed".format( typeof( user ) ) )
