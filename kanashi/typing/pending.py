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


#[kanashi.typing.pending.Pending]
@final
class Pending( Readonly, User ):

	#[Pending.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"account_badges",
			"fbid_v2",
			"full_name",
			"has_anonymous_profile_picture",
			"id",
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
	

#[kanashi.typing.pending.Pendings]
@final
class Pendings( Typing ):

	#[Pendings.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"big_list",
            "friend_requests",
            "global_blacklist_sample",
            "next_max_id",
            "page_size",
			"sections",
            {
				"suggested_users": [
                	"suggestions"
				]
            },
            "users"
		]
	
	#[Pendings.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"users": Pending
		}
	
	#[Pendings.__nested__]: Bool
	@property
	def __nested__( self ) -> bool: return False

	#[Pendings.bigList]: Bool
	@property
	def bigList( self ) -> bool: return self['big_list']

	#[Pendings.friendRequests]: List<Object>
	@property
	def friendRequests( self ) -> list[Object]: return self['friend_requests']

	#[Pendings.globalBlacklistSample]: Any
	@property
	def globalBlacklistSample( self ) -> any: return self['global_blacklist_sample']

	#[Pendings.nextMaxId]: Str
	@property
	def nextMaxId( self ) -> str: return self['next_max_id']

	#[Pendings.pageSize]: Int
	@property
	def pageSize( self ) -> int: return self['page_size']

	#[Pendings.sections]: Any
	@property
	def sections( self ) -> any: return self['sections']

	#[Pendings.suggestions]: List<User>
	@property
	def suggestions( self ) -> list[User]: return self['suggestions']

	#[Pendings.users]: List<Pending>
	@property
	def users( self ) -> list[Pending]: return self['users']
	
