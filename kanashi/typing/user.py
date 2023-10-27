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
from kanashi.typing.typing import Typing


#[kanashi.typing.user.User]
class User( Typing ):

	"""
	To indentify if object is obtained user info
	"""

	#[User.__nested__]: Bool
	@property
	def __nested__( self ) -> bool: return False

	#[User.__items__]: Dict<Str, Str>|List<Str>
	@property
	def __items__( self ) -> dict[str:str]|list[str]:
		return [
			"full_name",
			"id",
			"is_private",
			"is_verified",
			"pk",
			"pk_id",
			"profile_grid_display_type",
			"profile_pic_id",
			"profile_pic_url",
			"username",
			{
				"data": {
					"user": [
						"id"
					]
				}
			},
			{
				"user": [
					"full_name",
					"id",
					"is_private",
					"is_verified",
					"pk",
					"pk_id",
					"profile_grid_display_type",
					"profile_pic_id",
					"profile_pic_url",
					"username"
				]
			}
		]

	#[User.id]: Int
	@final
	@property
	def id( self ) -> int:

		"""
		Return id of user.

		:return Int
		:raises NotImplementedError
			When the property is not implemented
		"""

		if isinstance( self, Object ):
			if "id" in self:
				return int( self.__dict__['__data__']['id'] )
		if "id" in self.__dict__:
			return self.__dict__['id']
		raise NotImplementedError( "Property {} is not initialize ot implemented".format( self.id ) )
	
	#[User.username]: Str
	@final
	@property
	def username( self ) -> str:

		"""
		Return username of user.

		:return Str
		:raises NotImplementedError
			When the property is not implemented
		"""

		if isinstance( self, Object ):
			if "username" in self:
				return self.__dict__['__data__']['username']
		if "username" in self.__dict__:
			return self.__dict__['username']
		raise NotImplementedError( "Property {} is not initialize ot implemented".format( self.username ) )
	
