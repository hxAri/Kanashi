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

from time import sleep

from kanashi.endpoint.auth import AuthError
from kanashi.endpoint.profile import Profile
from kanashi.endpoint.user import UserError, UserNotFoundError
from kanashi.error import Error
from kanashi.object import Object
from kanashi.request import RequestError, RequestRequired
from kanashi.utils import File


#[kanashi.endpoint.FollowError]
class FollowError( Error ):
	pass
	

#[kanashi.endpoint.FollowSuccess]
class FollowSuccess( Object ):
	pass
	

#[kanashi.endpoint.Follow]
class Follow( RequestRequired ):
	
	#[Follow.throws( Profile user )]
	def throws( self, user: Profile ) -> None:
		if user.isMySelf:
			raise FollowError( "Unable to follow or unfollow for yourself" )
		if user.blockedByViewer:
			raise FollowError( "Unable to follow or unfollwo blocked account" )
	
	#[ProfileMethods.follow( Profile user )]
	def follow( self, user: Profile ) -> FollowSuccess:
		self.throws( user )
		self.session.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( user.username )
		})
		data = {
			"container_module": "\x70\x72\x6f\x66\x69\x6c\x65",
			"nav_chain": "\x50\x6f\x6c\x61\x72\x69\x73\x50\x72\x6f\x66\x69\x6c\x65\x52\x6f\x6f\x74\x3a\x70\x72\x6f\x66\x69\x6c\x65\x50\x61\x67\x65\x3a\x31\x3a\x76\x69\x61\x5f\x63\x6f\x6c\x64\x5f\x73\x74\x61\x72\x74",
			"user_id": user.id
		}
		if user.followedByViewer:
			target = f"https://www.instagram.com/api/v1/friendships/destroy/{user.id}/"
			action = "Unfollow"
		elif user.requestedByViewer:
			target = f"https://www.instagram.com/api/v1/friendships/destroy/{user.id}/"
			action = "Cancel request follow"
		else:
			target = f"https://www.instagram.com/api/v1/friendships/create/{user.id}/"
			action = "Following"
		resp = self.request.post( target, data=data )
		match resp.status_code:
			case 200:
				follow = resp.json()
				if "friendship_status" in follow:
					follow = follow['friendship_status']
					user.user.requested_by_viewer = private = follow['is_private']
					user.user.followed_by_viewer = following = follow['following']
					user.user.is_private = requested = follow['outgoing_request']
					return FollowSuccess({
						"id": user.id,
						"private": private,
						"username": user.username,
						"following": following,
						"requested": requested,
					})
				else:
					raise FollowError( f"Something wrong when {action} the {user.username}" )
			case 401:
				raise AuthError( f"Failed to {action}, because the credential is invalid, status 401", throw=self )
			case 404:
				raise UserNotFoundError( f"Target /{user.username}/ user not found" )
			case _:
				raise UserError( f"An error occurred while {action} the user [{resp.status_code}]" )
		pass
	
	#[Follow.getFollowersById( Int id )]
	def getFollowersById( self, id: int ):
		pass
	
	#[Follow.getFollowersByUsername( String username )]
	def getFollowersByUsername( self, username: str ):
		pass
	
	#[Follow.getFollowingById( Int id )]
	def getFollowingById( self, id: int ):
		pass
	
	#[Follow.getFollowingByUsername( String username )]
	def getFollowingByUsername( self, username: str ):
		pass
	
	#[Follow.nextCursorScroll( )]
	def nextCursorScroll( self ):
		pass
	