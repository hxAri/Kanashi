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

from re import findall

from kanashi.endpoint.auth import AuthError
from kanashi.endpoint.profile import Profile
from kanashi.error import Error
from kanashi.object import Object
from kanashi.request import RequestError, RequestRequired

#[kanashi.endpoint.User]
class User( RequestRequired ):
	
	#[User( Object app )]
	def __init__( self, app ):
		
		# Save every previously searched user.
		# Only users with usernames only.
		# This will save resources.
		self.recent = Object({})
		
		# Call parent constructor.
		super().__init__( app )
		
		# Mapping request history.
		for history in self.request.history:
			
			# Find username.
			find = findall( r"^https\:\/\/(i|www)\.instagram\.com\/(api\/v1\/users\/web_profile_info[\/]{0,1}\?username\=([a-zA-Z0-9._]+)|([a-zA-Z0-9._]+)[\/]{0,1}\?__a\=\d+(\&__d\=dis)*)$", history['target'] )
			try:
				find = find[0]
				match find[0]:
					case "i":
						user = find[2]
					case "www":
						user = find[3]
					case _:
						continue
				if "content" in history:
					if "graphql" in history['content']:
						content = {
							**history['content']['graphql']['user'],
							**{
								"seo_category_infos": history['content']['seo_category_infos']
							}
						}
					else:
						content = history['data']['user']
					self.recent.set({
						user: Profile(
							app=self.app,
							user=content,
							prev=self.main
						)
					})
			except( IndexError, KeyError ):
				continue
		pass
		
	#[User.getById( Int id )]
	def getById( self, id ):
		try:
			self.session.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/"
			})
			resp = self.request.get( f"https://i.instagram.com/api/v1/users/{id}/info/" )
		except RequestError as e:
			raise e
		match resp.status_code:
			case 200:
				user = resp.json()
				if user['user']['username'] != "":
					return self.getByUsername( user['user']['username'] )
				else:
					raise UserInfoError( f"Target /{id}/ user found but user data not available" )
			case 401:
				raise AuthError( "Failed to get user info, because the credential is invalid, status 401", throw=self )
			case 404:
				raise UserNotFoundError( f"Target /{id}/ user not found" )
			case _:
				raise UserError( f"An error occurred while fetching the user [{resp.status_code}]" )
		pass
		
	#[User.getByUsername( String username )]
	def getByUsername( self, username ):
		try:
			find = findall( r"^r\:([^\n]+)$", username )
			try:
				username = find[0]
			except IndexError:
				return self.recent.get( username )
		except( AttributeError, KeyError ):
			pass
		try:
			return self.recent.get( username )
		except( AttributeError, KeyError ):
			pass
		try:
			# f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}" ['data']['user']
			# f"https://www.instagram.com/{username}?__a=1&__d=dis" ['graphql']['user']
			self.session.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/explore/"
			})
			resp = self.request.get( f"https://www.instagram.com/{username}?__a=1&__d=dis" )
			match resp.status_code:
				case 200:
					data = resp.json()
					user = data['graphql']['user']
					if user != None:
						self.recent.set({
							username: Profile(
								app=self.app,
								user=user,
								prev=self.main
							)
						})
						return self.recent.get( username )
					else:
						raise UserInfoError( f"Target /{username}/ user found but user data not available" )
				case 401:
					raise AuthError( "Failed to get user info, because the credential is invalid, status 401", throw=self )
				case 404:
					raise UserNotFoundError( f"Target /{username}/ user not found" )
				case _:
					raise UserError( f"An error occurred while fetching the user [{resp.status_code}]" )
		except RequestError as e:
			raise e
	

#[kanashi.endpoint.UserError]
class UserError( Error ):
	pass
	

#[kanashi.endpoint.UserInfoError]
class UserInfoError( UserError ):
	pass
	

#[kanashi.endpoint.UserNotFoundError]
class UserNotFoundError( UserError ):
	pass
	