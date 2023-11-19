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


from re import Pattern
from typing import final


@final
class Pattern:

	""" Instagram Pattern
	"""

	""" JSON Content Type """
	APPLICATION_JSON:Pattern = r"^application\/json(?:\;\s*charset\=[A-Z0-9\-]+(\;?\s*)?)?$"

	""" Hashtag Pattern """
	HASHTAG:Pattern = r"^(?P<hashtag>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)$"
	HASHTAG_MULTILINE:Pattern = r"\#(?P<hashtag>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)"

	""" HTML Content Type """
	HTML:Pattern = r"^text/html(?:\;\s*charset\=[A-Z0-9\-]+(\;?\s*)?)?$"

	""" ID Pattern """
	ID:Pattern = r"^(?P<id>\d+)$"

	""" Media Pattern """
	MEDIA:Pattern = r"^$"

	""" Profile Pattern
	
	:include ID
	:include Profile URL
	:include Username
	"""
	PROFILE:Pattern = r"^(?:(?:(?:https?://(?:www\.)?instagram\.com/)(?P<profile>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)/?)|(?P<username>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)|(?P<id>\d+))$"
	PROFILE_URL:Pattern = r"^(?:(?:https?://(?:www\.)?instagram\.com/)(?P<profile>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)/?)$"
	
	""" Story Pattern

	:include ID
	:include Highlight URL
	:include Profile URL
	:include Timeline URL
	:include Username
	"""
	STORY:Pattern = r"^(?:(?:(?:https?://(?:www\.)?instagram\.com/)(?:(?:(?:stories/)(?:(?:highlights/(?P<highlight>\d+))|(?P<user>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)/(?P<timeline>\d+)))|(?P<profile>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*))/?)|(?P<username>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)|(?P<id>\d+))$"
	STORY_URL:Pattern = r"^(?:(?:(?:https?://(?:www\.)?instagram\.com/)(?:(?:(?:stories/)(?:(?:highlights/(?P<highlight>\d+))|(?P<user>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)/(?P<timeline>\d+))))/?))$"

	""" Username Pattern """
	USERNAME:Pattern = r"^(?P<username>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)$"
	USERNAME_MULTILINE:Pattern = r"\@(?P<username>[a-zA-Z_](?:[a-zA-Z0-9_\.]*[a-zA-Z0-9_]?)*)"
