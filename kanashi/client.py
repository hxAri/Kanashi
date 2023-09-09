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

from datetime import datetime
from random import randint
from re import findall, match
from time import sleep

from kanashi.decorator import logged
from kanashi.error import *
from kanashi.explore import Explore
from kanashi.inbox import Inbox
from kanashi.object import Object
from kanashi.profile import Profile
from kanashi.request import Request, RequestRequired
from kanashi.utility import Cookie, droper, JSON, String, typedef, typeof
	

#[kanashi.client.Client]
class Client( RequestRequired ):
	
	# Response dropkeys.
	Drops = Object({
		"direct": [],
		"friendship": {
			"show": [
				"blocking",
				"followed_by",
				"following",
				"incoming_request",
				"is_bestie",
				"is_blocking_reel",
				"is_eligible_to_subscribe",
				"is_feed_favorite",
				"is_guardian_of_viewer",
				"is_muting_notes",
				"is_muting_reel",
				"is_private",
				"is_restricted",
				"is_supervised_by_viewer",
				"muting",
				"outgoing_request",
				"subscribed"
			],
			"many": []
		},
		"inbox": [
			"counts",
			"last_checked",
			"priority_stories",
			"new_stories",
			"old_stories",
			"continuation_token",
			"subscription",
			"is_last_page",
			"partition"
		],
		"profile": {
			"api": {
				"graphql": "user"
			},
			"web": "user"
		}
	})
	
	# Instagram Graphql Query.
	Graphql = Object({
		"query": {
			"media": {
				"profile": {
					"hash": None,
					"id": None
				}
			},
			"profile": {
				"hash": "d4d88dc1500312af6f937f7b804c68c3"
			}
		}
	})
	
	#[Client( Request request, Mixed **kwargs )]: None
	def __init__( self, request=None, **kwargs ):
		
		"""
		Construct method of class Client
		
		:params Request request
			Instance of class Request
		:params Mixed **kwargs
			Client options
		
		:return None
		"""
		
		if  not isinstance( request, Request ):
			request = Request()
		
		# Instances of class from Request
		self.request = request
		
		# Instagram user info for signin.
		self.id = kwargs.pop( "id", None )
		self.username = kwargs.pop( "username", None )
		self.password = kwargs.pop( "password", None )
	
	#[Client.approve( Int id, Bool approve )]: Object
	@logged
	def approve( self, id, approve=None ):
		
		"""
		Approve or ignore request follow from user.
		
		:params Int id
			User id to be approve or ignore
		:params Bool approve
			Approve action
		
		:return Object
			Representation approve or ignore user results
		:raises ValueError
			When the user id or approve parameter is invalid
		raises ClientError
			When something wrong, please to check the request response history
		"""
		
		if  self.isUserId( id ):
			id = int( id )
		if  typedef( id, int, False ):
			raise ValueError( "Invalid id parameter, value must be type int or id valid numeric string, {} passed".format( typeof( approve ) ) )
		if  typedef( approve, bool, False ):
			raise ValueError( "Invalid approve parameter, value must be type bool, {} passed".format( typeof( approve ) ) )
		
		action = "Approve request"
		target = "https://www.instagram.com/api/v1/web/friendships/{}/approve/"
		if  not approve:
			action = "Ignore request"
			target = "https://www.instagram.com/api/v1/web/friendships/{}/ignore/"
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/",
			"Content-Type": "application/x-www-form-urlencoded"
		})
		
		# Trying to approve/ ignore request follow.
		request = self.request.post( target.format( id ), data={} )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				return Object({
					"id": id,
					"approve": approve,
					"ignoring": True if approve is False else False
				})
			else:
				raise ClientError( response['message'] if "message" in response and response['message'] else f"There was an error when {action} follow" )
		else:
			raise ClientError( f"An error occurred while {action} follow [{status}]" )
	
	def attempt( self, fullname, usermail, username, password ):
		
		# Update request headers.
		self.headers.update( **{
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		self.request.post( "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", data={
			"email": usermail,
			"enc_password": self.encpasw( password ),
			"first_name": fullname,
			"username": username,
			"opt_into_one_tap": False
		})
	
	#[Client.authenticated]: Bool
	@property
	def authenticated( self ):
		
		"""
		Return if user is authenticated.

		:return Bool
		"""
		
		if  isinstance( self.id, str ):
			if  not self.isUserId( self.id ):
				return False
			self.id = int( self.id )
		if  not isinstance( self.id, int ):
			return False
		if  "X-CSRFToken" not in self.headers:
			return False
		if  "csrftoken" not in self.cookies:
			return False
		else:
			if  self.cookies['csrftoken'] != self.headers['X-CSRFToken']:
				return False
		if  "ds_user_id" not in self.cookies:
			return False
		else:
			if  int( self.cookies['ds_user_id'] ) != int( self.id ):
				return False
		return True
	
	#[Client.csrftoken]: String
	@property
	def csrftoken( self ):
		
		"""
		Return csrftoken prelogin.
		
		:return String
			Csrftoken prelogin
		:raises CsrftokenError
			When csrftoken is not available
		"""
		
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		try:
			return self.request.get( "https://i.instagram.com/api/v1/si/fetch_headers" ).cookies['csrftoken']
		except KeyError as e:
			raise CsrftokenError( "Csrftoken prelogin is not available" )
		pass
	
	#[Client.direct()]: Object
	@logged
	def direct( self ):
		pass
	
	#[Client.encpasw( String password )]: String
	def encpasw( self, password ):
		return "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password )
	
	#[Client.explore( Int maxId, Bool includeFixedDestinations, Bool isNonpersonalizedExplore, Bool isPrefetch, Bool omitCoverMedia )]: Object
	@logged
	def explore( self, maxId=0, includeFixedDestinations=True, isNonpersonalizedExplore=False, isPrefetch=False, omitCoverMedia=False ):
		
		"""
		Get contents Instagram explore

		:params Int maxId
		:params Bool includeFixedDestinations
		:params Bool isNonpersonalizedExplore
		:params Bool isPrefetch
		:params Bool omitCoverMedia

		:return Explore
		:raises ClientError
			When something wrong, please to check the request response history
		"""

		# Update request headers.
		self.headers.update( **{
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/explore/"
		})

		# Trying to get contents from instagram explore.
		request = self.request.get( "https://www.instagram.com/api/v1/discover/web/explore_grid/", params={
			"include_fixed_destinations": includeFixedDestinations,
			"is_nonpersonalized_explore": isNonpersonalizedExplore,
			"is_prefetch": isPrefetch,
			"max_id": maxId,
			"module": "explore_popular",
			"omit_cover_media": omitCoverMedia
		})
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				return Explore(
					request=self.request,
					explore=response,
					# methods={}
				)
			else:
				raise ClientError( response['message'] if "message" in response and response['message'] else "There was an error when getting contents from instagram explore" )
		else:
			raise ClientError( f"An error occurred while fetching contents from instagram explore [{status}]" )
	
	#[Client.friendship( Int id )]: Object
	@logged
	def friendship( self, id ):
		
		"""
		Get user friendship info.
		
		:params Int id
			User id
		
		return Object
			Representation of friendship results
		"""
		
		self.sleep()
		
		# Update request headers.
		self.headers.update( **{
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		
		# Trying to restrieve user friendship.
		request = self.request.get( f"https://www.instagram.com/api/v1/friendships/show/{id}" )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				return Object( droper( response, Client.Drops.friendship.show ) )
			else:
				raise FriendshipError( response['message'] if "message" in response and response['message'] else "There was an error when getting friendship info" )
		else:
			raise FriendshipError( f"An error occurred while fetching the friendship [{status}]" )
	
	#[Client.friendshipShowMay( String username, List<Int> ids, Mixed **kwargs )]: Object
	@logged
	def friendshipShowMany( self, username, ids=[], **kwargs ):
		
		"""
		Friendship Show Many information of user based id from followers or following list.
		
		:params String username
			Username as referrer, which means the ID
			provided must match the follower or following
			with the given username
		:params List<Int> ids
			List id from follower or following list,
			not recommended for more than 32 id
		:params Mixed **kwargs
			:kwargs Bool followers
				If id from followers
			:kwargs Bool following
				If id from following
		
		:return Object
			Representation of request results.
		:raises ValueError
			When the user id is empty
			When the user id is invalid
			When the ids parameter is invalid
			When the user id more than 32 ids
		:raises ClientError
			When something wrong, please to check the request response history
		"""
		
		if  typedef( ids, list, False ):
			raise ValueError( "Invalid ids parameter, value must be type list<int>, {} passed".format( typeof( ids ) ) )
		else:
			if  len( ids ) <= 0:
				raise ValueError( "User ids can't be empty" )
			if  len( ids ) > 32:
				raise ValueError( "User ids must be less than 32 ids" )
			for i, id in enumerate( ids ):
				if  not self.isUserId( id ):
					raise ValueError( "Invalid user id in list of ids, user id must be int|numeric string, {} passed on ids[{}]".format( typeof( id ), i ) )
				ids[i] = int( id )
			
			# Default source path is followers.
			source = "followers"
			if  kwargs.pop( "following", False ):
				source = "following"
			
			# Update request headers.
			self.headers.update({
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/{}/{}/".format( username, source )
			})
			
			# Trying to get more data.
			request = self.request.post( "https://www.instagram.com/api/v1/friendships/show_many/", data={ "user_ids": ids } )
			status = request.status_code
			if status == 200:
				response = request.json()
				print( request )
			else:
				raise FriendshipError( f"An error occurred while fetching the friendship information of users [{status}]" )
	
	#[Client.graphql( Mixed **kwargs )]: Object
	@logged
	def graphql( self, **kwargs ):
		
		"""
		Get data from graphql query.
		"""
	
	#[Client.inbox()]: Inbox
	@logged
	def inbox( self ):
		
		"""
		Get news inbox notifications.
		
		:return Object
			Representation of inbox results
		:raises ClientError
			When something wrong, please to check the request response history
		"""
		
		# Update request headers.
		self.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		
		# Trying to get news inbox notifications.
		request = self.request.post( "https://www.instagram.com/api/v1/news/inbox/", data={} )
		status = request.status_code
		if status == 200:
			response = request.json()
			if "status" in response and response['status'] == "ok":
				return Inbox( self.request, droper( response, Client.Drops.inbox ) )
			else:
				raise ClientError( response['message'] if "message" in response and response['message'] else "There was an error when getting news inbox" )
		else:
			raise ClientError( f"An error occurred while fetching the news inbox notifications [{status}]" )
	
	#[Client.isUserId( String id )]: Bool
	def isUserId( self, id ):
		
		"""
		Return if string is valid id numeric string.
		
		:params String id
		
		:return Bool
		"""
		
		return bool( match( r"^[1-9]{1}[0-9]{9,10}$", str( id ) ) )
	
	#[Client.logout()]: Object
	@logged
	def logout( self ):
		
		"""
		Logout instagram account.
		
		:return Object
			Representation of logout results
		"""
		
		pass
	
	#[Client.media()]: Media|MediaCollection
	@logged
	def media( self ):
		pass
	
	#[Client.mediaById( Int id )]: Media
	@logged
	def mediaById( self, id ):
		if  not isinstance( id, int ):
			if  match( r"^\d+$", f"{id}" ) is None:
				raise ValueError( "Invalid id prameter, value must be type int or valid numeric" )
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/explore/"
		})
		
		# Trying to get media by id.
		request = self.request.get( f"https://www.instagram.com/api/v1/media/{id}/info/" )
		print( request )
	
	#[Client.pending()]: List<Object>
	@logged
	def pending( self ):
		
		"""
		Get pending request follow from users.
		
		:return List
			List object of pending request follow
		:raises ClientError
			When something wrong e.g data user doest not
			available or error on request json responses
		"""
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		
		# Trying to get request follow pending.
		request = self.request.get( "https://www.instagram.com/api/v1/friendships/pending/" )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "users" in response:
				users = []
				for user in response['users']:
					users.append( Object({ **user, "id": user['pk'] }) )
				return users
			else:
				raise ClientError( response['message'] if "message" in response and response['message'] else "There was an error when getting request follow pending" )
		else:
			raise ClientError( f"An error occurred while fetching the request pending [{status}]" )
	
	#[Client.profile( Int id, String url, String username )]: Profile
	@logged
	def profile( self, id=None, url=None, username=None ):
		
		"""
		Return user profile information by id|url|username
		
		:params Int id
			Get profile info by id
		:params String url
			Get profile info by url string
		:params String username
			Get profile info by username
		
		:return Profile
			Information about the user profile
		:raises TypeError
			When the id is invalid numeric string
			When the url is invalid url string
		:raises UserError
			When the user data does not available
			When there are unexpected error found
		:raises UserNotFoundError
			When the user not found
		:raises ValueError
			When the id|url|username is empty
		"""
		
		if  not isinstance( id, int ) and \
			not isinstance( id, str ) and \
			not isinstance( url, str ) and \
			not isinstance( username, str ):
			raise ValueError( "id|url|username required" )
		
		if  isinstance( id, str ):
			if  not self.isUserId:
				raise TypeError( "Invalid id value, id must be int or valid numeric string" )
			id = int( id )
			username = None
		if  isinstance( id, int ):
			profile = self.profileById( id )
			profile = {
				**profile,
				**self.profileByUsername( profile['username'] )
			}
		if  isinstance( url, str ):
			if  valid := match( r"^https?\:/{2}(?:www\.)instagram\.com\/(?P<username>[a-zA-Z0-9_\.]{1,30})\/{0,1}(?:\?[^\n]+)?$", url ):
				username = valid.group( "username" )
			else:
				raise TypeError( "Invalid url parameter, value must be valid profle url string" )
		if  isinstance( username, str ):
			profile = self.profileByUsername( username )
			profile = {
				**profile,
				**self.profileById( profile['id'] )
			}
		if  self.id != profile['id']:
			friendship = self.friendship( profile['id'] )
			friendship.dict()
		else:
			friendship = {}
		return Profile(
			request=self.request,
			methods={
				"approve": self.approve,
				"authenticated": lambda: self.authenticated,
				"friendship": self.friendship,
				"friendshipShowMany": self.friendshipShowMany,
				"graphql": self.graphql,
				"media": self.media
			},
			profile={
				**profile,
				**friendship
			},
			viewer=Object({
				"id": self.id,
				"username": self.username
			})
		)
	
	#[Client.profileById( Int id )]: Dict
	@logged
	def profileById( self, id ):
		
		"""
		Get user info by id.
		
		:params Int id
			User id profile
		
		:return Dict
			Profile info
		:raises UserError
			When the user data does not available
			When there are unexpected error found
		:raises UserNotFoundError
			When the user not found
		"""
		
		self.sleep()
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		
		# Trying to retrieve user info.
		request = self.request.get( f"https://i.instagram.com/api/v1/users/{id}/info/?profile_picture=true" )
		status = request.status_code
		match status:
			case 200:
				response = request.json()
				if  "user" in response and response['user'] and \
					"username" in response['user'] and response['user']['username']:
					return response['user']
				else:
					raise UserError( f"Target \"{id}\" user found but user data not available" )
			case 404:
				raise UserNotFoundError( f"Target \"{id}\" user not found" )
			case _:
				raise UserError( f"An error occurred while fetching the user [{status}]" )
	
	#[Client.profileByUsername( String username )]: Dict
	@logged
	def profileByUsername( self, username ):
		
		"""
		Get user info by username.
		
		:params String username
			Username profile
		
		:return Dict
			Profile info
		:raises UserError
			When the user data does not available
			When there are unexpected error found
		:raises UserNotFoundError
			When the user not found
		"""
		
		self.sleep()
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{username}/"
		})
		
		# Trying to retrieve user info.
		request = self.request.get( f"https://www.instagram.com/{username}?__a=1&__d=dis" )
		status = request.status_code
		match status:
			case 200:
				response = request.json()
				profile = None
				if  "graphql" in response:
					return response['graphql']['user']
				else:
					raise UserError( f"Target \"{username}\" user found but user data not available" )
			case 404:
				raise UserNotFoundError( f"Target \"{username}\" user not found" )
			case _:
				raise UserError( f"An error occurred while fetching the user [{status}]" )
	
	#[Client.signin( String username, String password, String csrftoken, Object|String|Dict cookies, String browser )]: Object
	def signin( self, username, password, csrftoken=None, cookies=None, browser=None ):
		
		"""
		Client login with username and password or remember with cookie.
		
		:params String username
			Username, Email Address or Phone number
		:params String password
			Your instagram password
		:params String csrftoken
			Csrftoken prelogin
		:params Object|String|Dict cookies
			Log in using the login information on the computer
		:params String browser
			if you log in using cookies, try to provide your browser's User Agent
		
		:return Object
			Representation of login results
		:raises PasswordError
			When the username is found but the password is invalid
		:raises SignInError
			When an error occurs while logging in
		:raises SpamError
			When you try to login too many times
		:raises UserNotFoundError
			When the username is not found
		:raises ValueError
			When the cookies invalid value
		"""
		
		result = Object({
			"checkpoint": None,
			"two_factor": None,
			"remember": False,
			"success": False,
			"verify": False,
			"signin": {
				"id": None,
				"fullname": None,
				"username": username,
				"password": password,
				"csrftoken": csrftoken,
				"sessionid": None
			},
			"result": None
		})
		
		if  cookies != None:
			if  isinstance( cookies, Object ):
				cookies = cookies.dict()
			if  isinstance( cookies, str ):
				cookies = Cookie.simple( cookies )
			if  isinstance( cookies, dict ):
				try:
					id = cookies['ds_user_id']
					csrftoken = cookies['csrftoken']
					sessionid = cookies['sessionid']
				except KeyError as e:
					raise SignInError( "Invalid cookie, there is no \"{}\" in the cookie".format( str( e ) ), prev=e )
				for i, cookie in enumerate( cookies ):
					Cookie.set( self.cookies, cookie, cookies[cookie], domain=".instagram.com", path="/" )
			else:
				raise ValueError( "Invalid cookie, value must be Dict|Str|Object, {} passed".format( type( cookies ).__name__ ) )
			
			# Update request headers.
			self.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/",
				"X-CSRFToken": csrftoken
			})
			
			# Trying to check if cookies is valid.
			request = self.request.get( f"https://i.instagram.com/api/v1/users/{id}/info/" )
			cookies = dict( request.cookies )
			status = request.status_code
			if  status == 200:
				response = request.json()
				if  "ds_user_id" in cookies or \
					"sessionid" in cookies or \
					"csrftoken" in cookies:
					if  "user" in response:
						if  isinstance( response['user'], dict ):
							if  "username" in response['user']:
								username = response['user']['username']
							if  "full_name" in response['user']:
								result.set({ "signin": { "fullname": response['user']['full_name'] } })
					result.set({
						"remember": True,
						"success": True,
						"signin": {
							"id": id,
							"username": username,
							"csrftoken": csrftoken,
							"sessionid": sessionid
						}
					})
				else:
					raise SignInError( response['message'] if "message" in response and response['message'] else "There was an error remembering the user" )
			else:
				raise SignInError( "Cookies are invalid or have expired" )
		else:
			if  not isinstance( username, str ):
				if  not isinstance( self.username, str ):
					raise SignInError( "Username can't be empty" )
				username = self.username
			if  not isinstance( password, str ):
				if  not isinstance( self.password, str ):
					raise SignInError( "Password can't be empty" )
			if  not isinstance( csrftoken, str ):
				try:
					csrftoken = self.headers['X-CSRFToken']
				except( AttributeError, KeyError ):
					csrftoken = self.csrftoken
			
			# Update request headers.
			self.headers.update({
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/accounts/login/",
				"X-CSRFToken": csrftoken
			})
			
			# Trying to log in.
			signin = self.request.post( "https://www.instagram.com/accounts/login/ajax/", allow_redirects=True, data={
				"username": username,
				"enc_password": self.encpasw( password ),
				"queryParams": {},
				"optIntoOneTap": "false"
			})
			
			# Get response json from login.
			response = signin.json()
			
			if  "checkpoint_url" in response:
				result.set({ "checkpoint": response })
			elif "two_factor_required" in response:
				result.set({
					"two_factor": {
						"cookies": signin.cookies,
						"headers": signin.headers,
						"info": response['two_factor_info']
					}
				})
			elif "user" in response:
				if  response['user']:
					if  "authenticated" in response and response['authenticated']:
						try:
							result.set({
								"success": True,
								"signin": {
									"id": response['userId'],
									"csrftoken": signin.cookies['csrftoken'],
									"sessionid": signin.cookies['sessionid']
								}
							})
						except KeyError as e:
							raise SignInError( "Invalid json user info", prev=e )
					else:
						raise PasswordError( f"Incorrect password for user \"{username}\", or may have been changed" )
				else:
					raise UserNotFoundError( f"User \"{username}\" not found, or may be missing" )
			elif "spam" in response:
				raise SpamError( "Oops! Looks like you are considered Spam!" )
			elif "status" in response and "message" in response:
				raise SignInError( response['message'] )
			else:
				raise SignInError( "An error occurred while signing in" )
		
		# If the user has actually successfully logged in.
		if  result.success:
			if  not isinstance( browser, str ):
				browser = self.headers['User-Agent']
			
			# Encode password if is available.
			password = "hex[b64]\"{}\"".format( String.encode( password ) ) if password else None
			result.set({
				"signin": {
					"id": result.signin.id,
					"username": result.signin.username
				},
				"result": {
					"id": result.signin.id,
					"fullname": result.signin.fullname,
					"username": result.signin.username if result.signin.username else username,
					"password": password,
					"session": {
						"browser": browser,
						"cookies": {
							**dict( self.cookies ),
							**dict( self.request.response.cookies )
						},
						"headers": {
							**dict( self.headers ),
							**{
								"X-CSRFToken": self.request.response.cookies['csrftoken'],
								"Cookie": Cookie.string( self.cookies )
							}
						},
						"csrftoken": result.signin.csrftoken,
						"sessionid": result.signin.sessionid
					}
				}
			})
			
		return result
	
	#[Client.sleep( Int delay )]: None
	def sleep( self, delay=1.6 ):
		
		"""
		Delay for avoid SPAM or Block from request.
		
		:params Int delay
			Time to sleep, delay must be >=1.4s
		
		:return None
		:raises ValueError
			When delay is less than one or equal one
		"""
		
		if  delay >= 1.4:
			sleep( delay )
		else:
			raise ValueError( "Delay must be greater or equals >=1.4s" )
	
	#[Client.verify()]: Object
	def verify( self ):
		pass
	