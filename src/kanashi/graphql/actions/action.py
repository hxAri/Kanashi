#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Facebook, e.g Login. Logout, Profile Info,
# Follow, Unfollow, Media downloader, etc.
#
# Kanashi Copyright (c) 2024 - hxAri <hxari@proton.me>
# Kanashi Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

from builtins import bool as Bool, str as Str
from typing import Any, Self, MutableMapping

from kanashi.graphql.parser import Parser
from kanashi.graphql.schema import Schema


__all__ = [
	"Action"
]


class Action( Parser ):
	
	""" Kanashi Graphql Action """
	
	authentication:Bool
	""" Indicate if action require authorization """
	
	pagination:Self
	""" Indicate if action support pagination query """
	
	query:Bool
	""" Indicate if action is graphql query not graphql api """
	
	schema:Schema
	""" Indicate the action schema """
	
	variables:MutableMapping[Str,Any]
	""" Indicate the action variables for payload """
	
	...

