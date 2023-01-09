#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashi Copyright (c) 2022 - Ari Setiawan <ari160824@gmail.com>
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
# Kanashi is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from time import sleep

from kanashi.endpoint.auth import AuthError
from kanashi.endpoint.profile import Profile
from kanashi.error import Error
from kanashi.object import Object
from kanashi.request import RequestError, RequestRequired
from kanashi.utils import File

#[kanashi.endpoint.Follow]
class Follow( RequestRequired ):
	
	#[Follow.ondelete( Profile user )]
	def ondelete( self, user ):
		""" Delete followers """
		pass
		
	#[Follow.onfollow( Profile user, Hashtag hashtag )]
	def onfollow( self, user=None, hashtag=None ):
		""" Follow account or hashtag """
		try:
			if isinstance( user, Profile ):
				self.session.headers.update({ "Referer": f"https://www.instargram.com/{user.username}/" })
				if user.followedByViewer:
					action = "unfollow"
					url = f"https://www.instagram.com/api/v1/web/friendships/{user.id}/unfollow/"
				else:
					action = "follow"
					url = f"https://www.instagram.com/api/v1/web/friendships/{user.id}/follow/"
				resp = self.request.post( url )
				match resp.status_code:
					case 200:
						json = resp.json()
						if json['status'] == "ok":
							return FollowSuccess({ **json, **{ "action": action, "target": user } })
						else:
							raise FollowError( f"" )
					case 401:
						raise AuthError( f"" )
					case _:
						raise FollowError( f"" )
				pass
			# elif isinstance( hashtag, Hashtag ):
			#	self.session.headers.update({ "Referer": f"https://www.instagram.com/explore/tags/{hashtag.}" })
			#	pass
			else:
				raise FollowError( "The user or hashtag parameter is required, no arguments are passed" )
		except RequestError as e:
			raise e
		
	#[Follow.unfollow( Profile user, Hashtag hashtag )]
	def unfollow( self, user=None, hashtag=None ):
		""" Unfollow account of hashtag """
		try:
			if isinstance( user, Profile ):
				pass
			# elif isinstance( hashtag, Hashtag ):
			#	pass
			else:
				raise FollowError( "The user or hashtag parameter is required, no arguments are passed" )
		except RequestError as e:
			raise e
		
	#[Follow.getFollowersById( Int id )]
	def getFollowersById( self, id ):
		pass
		
	#[Follow.getFollowersByUsername( String username )]
	def getFollowersByUsername( self, username ):
		pass
		
	#[Follow.getFollowingById( Int id )]
	def getFollowingById( self, id ):
		pass
		
	#[Follow.getFollowingByUsername( String username )]
	def getFollowingByUsername( self, username ):
		pass
		
	#[Follow.]
	def nextCursorScroll( self ):
		pass
	

#[kanashi.endpoint.FollowError]
class FollowError( Error ):
	pass
	

#[kanashi.endpoint.FollowSuccess]
class FollowSuccess( Object ):
	pass
	