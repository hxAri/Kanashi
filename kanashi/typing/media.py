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
from yutiriti import Object, Readonly, Typing


#[kanashi.typing.media.Media]
class Media( Typing ):

	#[kanashi.typing.media.Media.Type]
	@final
	class Type( Readonly ):

		""" Media Type """

		#[Type( Int type )]: None
		def __init__( self, type:int ) -> None:

			"""
			Construct method of class Type.

			:params Int type

			:return None
			"""

			match type:
				case 26552: name = "Story Tray Reel"
				case 66545: name = "Story Profile"
				case 81656: name = "Story Highlight"
				case _:
					raise ValueError( "Unknown media type" )
			
			self.__name__ = name
			self.__type__ = type
		
		#[Type.name]: Str
		@property
		def name( self ) -> str: return self.__name__

		#[Type.value]: Int
		@property
		def value( self ) -> int: return self.__type__
	
	STORY_HIGHLIGHT = Type( 81656 )
	STORY_PROFILE = Type( 66545 )
	STORY_TRAY_REEL = Type( 26552 )

