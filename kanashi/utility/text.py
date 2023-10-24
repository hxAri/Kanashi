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


#[kanashi.utility.text.Text]
@final
class Text:

	#[Text.fromSnakeToCamel( Str string )]: Str
	@staticmethod
	def fromSnakeToCamel( string:str ) -> str:
		parts = string.split( "\x5f" )
		return "{}{}".format( parts[0], "".join( part.capitalize() for part in parts[1:] ) )

	#[Text.fromSnakeToTitle( Str string )]: Str
	@staticmethod
	def fromSnakeToTitle( string:str ) -> str: return "\x20".join([ part.capitalize() for part in string.split( "\x5f" ) ])
	