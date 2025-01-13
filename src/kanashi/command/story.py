#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
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

from builtins import int as Int, str as Str
from click import Context, group, option as Option, pass_context as Initial
from typing import final

from kanashi.client import Client
from kanashi.common import puts
from kanashi.graphql.actions import (
	PolarisProfileStoryHighlightsTrayContentQuery
)


__all__ = [
	"Story"
]


@final
@group
class Story: """ Instagram story """

@Story.command( help="Instagram highlighted story tray" )
@Option( "--username", help="", required=True, type=Str )
@Initial
def highlight( context:Context, username:Str ) -> None:
	
	def formatter( id:Str, number:Int, owner:Str, title:Str ) -> Str:
		number = str( number )
		return "{number} {id} {owner} {title}".format(
			id=id[:28].ljust( 28 ),
			title=title[:30].ljust( 30 ),
			owner=owner[:30].ljust( 30 ),
			number=number[:2].ljust( 2 )
		)
	
	client:Client = context.obj['client']
	profile = client.profile( username, navigate=True )
	highlightsTray = client.graphql( PolarisProfileStoryHighlightsTrayContentQuery( profile['user']['id'] ) )
	puts( formatter( id="Id", title="Title", owner="Fullname", number="No", ), start="\n + " )
	for i, highlighted in enumerate( highlightsTray[2], 1 ):
		puts( formatter( id=highlighted['pk'], title=highlighted['title'], owner=profile['user']['full_name'], number=i ), start=" - " )
	...

