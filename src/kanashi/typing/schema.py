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


@final
class Schema:

	""" Instagram Graphql Schema """

	def __init__( self, api:str, doc:int ):

		"""
		Construct method of class Schema

		:params Str api
			Facebook API request friendly name
		:params Int doc
			Facebook query doc
		:params List<Str> labels
			List of allowed label
		:params List<Str> typenames
			List of allowed type name

		:return None
		"""

		self.__api__ = api
		self.__doc__ = doc

	def __str__( self ) -> str: return f"{self.api}:{self.doc}:"

	@property
	def api( self ) -> str: return self.__api__

	@property
	def doc( self ) -> int: return self.__doc__

	...

