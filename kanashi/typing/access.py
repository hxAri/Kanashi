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
from yutiriti.typing import Typing

from kanashi.typing.active import Active
from kanashi.typing.checkpoint import Checkpoint
from kanashi.typing.two_factor import TwoFactor


#[kanashi.typing.access.AccessManager<AccessManagerApps, AccessManagerOAuth>]
@final
class AccessManager( Typing ):

	#[AccessManager.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"apps",
			"oauth"
		]
	
	#[AccessManager.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"apps": AccessManagerApps,
			"oauth": AccessManagerOAuth
		}
	

#[kanashi.typing.access.AccessManagerApps]
@final
class AccessManagerApps( Typing ):

	#[AccessManagerApps.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"authorizations"
		]
	
	#[AccessManagerApps.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
		}
	

#[kanashi.typing.access.AccessManagerOAuth]
@final
class AccessManagerOAuth( Typing ):

	#[AccessManagerOAuth.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"pending_apps",
			"accepted_apps"
		]
	
	#[AccessManagerOAuth.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
		}
	
