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
##

from kanashi.error import Error
from kanashi.endpoint.auth import AuthError
from kanashi.endpoint.profile import Profile
from kanashi.endpoint.user import UserError, UserNotFoundError
from kanashi.object import Object
from kanashi.request import RequestRequired


#[kanashi.endpoint.BlockError]
class BlockError( Error ):
	pass
	

#[kanashi.endpoint.BlockSuccess]
class BlockSuccess( Object ):
	pass
	

#[kanashi.endpoint.Block]
class Block( RequestRequired ):
	
	# Block and other account.
	BLOCK_MULTILEVEL = 78828
	
	# Block and report.
	BLOCK_REPORT = 86272
	
	# Block only.
	BLOCK_ONLY = 99278
	
	#[Block.throws( Profile user )]
	def throws( self, user: Profile ) -> None:
		if user.isMySelf:
			raise BlockError( "Unable to block or unblock yourself" )
	
	#[Block.block( Profile user, int level )]
	def block( self, user: Profile, level: int=None ) -> BlockSuccess:
		self.throws( user )
		self.session.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{user.username}/"
		})
		if user.blockedByViewer:
			target = f"https://www.instagram.com/api/v1/web/friendships/{user.id}/unblock/"
			action = "Unblock"
		else:
			target = f"https://www.instagram.com/api/v1/web/friendships/{user.id}/block/"
			action = "Blocking"
		resp = self.request.post( target )
		match resp.status_code:
			case 200:
				block = resp.json()
				if "status" in block and block['status'] == "ok":
					user.user.blocked_by_viewer = False if user.blockedByViewer else True
					return BlockSuccess({
						"id": user.id,
						"username": user.username,
						"blocking": False if user.blockedByViewer else True
					})
				else:
					raise BlockError( f"Something wrong when {action} the {user.username}" )
			case 401:
				raise AuthError( f"Failed to {action}, because the credential is invalid, status 401", throw=self )
			case 404:
				raise UserNotFoundError( f"Target /{user.username}/ user not found" )
			case _:
				raise UserError( f"An error occurred while {action} the user [{resp.status_code}]" )
		pass
	