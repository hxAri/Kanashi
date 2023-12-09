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
from yutiriti.object import Object
from yutiriti.readonly import Readonly
from yutiriti.typing import Typing

from kanashi.typing.user import User


#[kanashi.typing.follow.Follow]
@final
class Follow:

	""" Follow Identity """

	#[kanashi.typing.follow.Follow$.Type]
	@final
	class Type( Readonly ):

		""" Follow Type """

		#[Type( Int type )]: None
		def __init__( self, type:int ) -> None:

			"""
			Construct method of class Type.

			:params Int type

			:return None
			"""

			match type:
				case 78323: name = "Follow"
				case 78263: name = "Unfollow"
				case 79763: name = "Unrequest"
				case _:
					raise ValueError( "Unknown follow type" )
			
			self.__name__ = name
			self.__type__ = type
		
		#[Type.name]: Str
		@property
		def name( self ) -> str: return self.__name__

		#[Type.value]: Int
		@property
		def value( self ) -> int: return self.__type__
	
	FOLLOW = Type( 78323 )
	UNFOLLOW = Type( 78263 )
	UNREQUEST = Type( 79763 )

#[kanashi.typing.follow.Follower]
class Follower( Typing, User ):

	#[Follower.__items__]: List<Dict|List|Object|Str>
	@final
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"account_badges",
			"fbid_v2",
			"full_name",
			"has_anonymous_profile_picture",
			"is_possible_bad_actor",
			"is_possible_scammer",
			"is_private",
			"is_verified",
			"latest_reel_media",
			"pk",
			"pk_id",
			"profile_pic_id",
			"profile_pic_url",
			"strong_id__",
			"third_party_downloads_enabled",
			"username"
		]
	

#[kanashi.typing.follow.Followers<Follower>]
class Followers( Typing ):

	#[Followers.__items__]: List<Dict|List|Object|Str>
	@final
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"big_list",
			"has_more",
			"next_max_id",
			"page_size",
			"should_limit_list_of_followers",
			"show_spam_follow_request_tab",
			"use_clickable_see_more",
			"users"
		]
	
	#[Followers.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"users": Follower
		}
	

#[kanashi.typing.follow.Following]
@final
class Following( Follower ): ...
	

#[kanashi.typing.follow.Followings<Following>]
@final
class Followings( Followers ):

	#[Followings.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"users": Following
		}
	

