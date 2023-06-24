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

from datetime import datetime
from random import randint
from re import findall, match
from time import sleep

from kanashi.error import *
from kanashi.object import Object
from kanashi.profile import Profile
from kanashi.request import Request, RequestRequired
from kanashi.utility import Cookie, String


#[kanashi.client.Client]
class Client( RequestRequired ):
	
	# Instagram URL Targets
	URL = "https://www.instagram.com/{}"
	URL_API = "https://www.instagram.com/query/"
	URL_GRAPHQL = "https://www.instagram.com/graphql/query/"
	
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
		
		if not isinstance( request, Request ):
			request = Request()
		
		# Instances of class from Request
		self.request = request
		
		# Instagram user info for signin.
		self.id = kwargs.pop( "id", None )
		self.username = kwargs.pop( "username", None )
		self.password = kwargs.pop( "password", None )
	
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
	
	#[Client.friendship( Int id, String username )]: Object
	def friendship( self, id, username ):
		
		# Update request headers.
		self.headers.update( **{
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{username}/"
		})
		
		# Trying to restrieve user friendship.
		request = self.request.get( f"https://www.instagram.com/api/v1/friendships/show/{id}" )
		status = request.status_code
		match status:
			case 200:
				results = Object({})
				response = request.json()
				dropkeys = [
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
				]
				for key in dropkeys:
					if key in response:
						results[key] = response[key]
				return results
			case 401:
				raise AuthError( "Failed to get user info, because the credential is invalid, status 401", throw=self )
			case 404:
				raise UserNotFoundError( f"Target \"{username}\" user not found" )
			case _:
				raise UserError( f"An error occurred while fetching the user [{status}]" )
		
	
	#[Client.logout()]: Object
	def logout( self ):
		
		"""
		Logout instagram account.
		
		:return Object
			Representation of logout results
		"""
		
		pass
	
	#[Client.profile( String username, Int id, Bool cache, Bool friendship )]: Profile
	def profile( self, username=None, id=None, cache=False, friendship=False ):
		
		"""
		Return user profile information.
		
		:params String username
			Retrieve user profile by username
		:params Int id
			Retrieve user profile by user id
		:params Bool cache
			Retrieve users from the previous government
		:params Bool frindship
			Include retrieve user friendship
		
		:return Profile
			Information about the user profile
		:raises AuthError
			When an error occurs while fetching data
		:raises UserError
			When user profile is not available
		:raises UserNotFoundError
			When the username is not found
		:raises ValueError
			When username and id are empty
		"""
		
		# Retrieve user information using id
		if  isinstance( id, int ) or \
			isinstance( id, str ):
			
			# Update request headers.
			self.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/"
			})
			
			# Trying to retrieve user info.
			request = self.request.get( f"https://i.instagram.com/api/v1/users/{id}/info/" )
			status = request.status_code
			match status:
				case 200:
					profile = request.json()
					if  profile['user']['username'] != "":
						sleep( 1.6 )
						return self.profile( username=profile['user']['username'] )
					else:
						raise UserError( f"Target \"{id}\" user found but user data not available" )
				case 401:
					raise AuthError( "Failed to get user info, because the credential is invalid, status 401", throw=self )
				case 404:
					raise UserNotFoundError( f"Target \"{id}\" user not found" )
				case _:
					raise UserError( f"An error occurred while fetching the user [{status}]" )
			
		# Retrieve user information using username.
		elif isinstance( username, str ):
			
			# If cache is allowed.
			if cache:
				find = findall( r"^r\:([^\n]+)$", username )
				pass
			
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
						profile = response['graphql']['user']
					if  profile:
						if friendship:
							sleep( 1.2 )
							friendship = self.friendship( profile['id'], profile['username'] )
							profile = {
								**profile,
								**friendship.dict()
							}
						return Profile(
							request=self.request,
							profile=profile,
							viewer=Object({
								"id": self.id,
								"username": self.username
							})
						)
					else:
						raise UserError( f"Target \"{username}\" user found but user data not available" )
				case 401:
					raise AuthError( "Failed to get user info, because the credential is invalid, status 401", throw=self )
				case 404:
					raise UserNotFoundError( f"Target \"{username}\" user not found" )
				case _:
					raise UserError( f"An error occurred while fetching the user [{status}]" )
		else:
			raise ValueError( "Username or ID cannot be empty" )
		pass
	
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
			if  you log in using cookies, try to provide your browser's User Agent
		
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
				for i, cookie in enumerate( cookies ):
					Cookie.set( self.cookies, cookie, cookies[cookie], domain=".instagram.com", path="/" )
			else:
				raise ValueError( "Invalid cookie, value must be Dict|Str|Object, {} passed".format( type( cookies ).__name__ ) )
			try:
				id = cookies['ds_user_id']
				csrftoken = cookies['csrftoken']
				sessionid = cookies['sessionid']
			except KeyError as e:
				raise SignInError( "Invalid cookie, there is no \"{}\" in the cookie".format( str( e ) ), prev=e )
			
			# Update request headers.
			self.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/accounts/login/",
				"X-CSRFToken": result.signin.csrftoken
			})
			
			# Trying to check if cookies is valid.
			request = self.get( "https://www.instagram.com" )
			cookies = request.cookies.dict()
			status = request.status_code
			if  status != 200:
				if  "ds_user_id" not in cookies or \
					"sessionid" not in cookies or \
					"csrftoken" not in cookies:
					result.set({
						"remember": True,
						"success": True,
						"signin": {
							"id": id,
							"csrftoken": csrftoken,
							"sessionid": sessionid
						}
					})
				else:
					raise SignInError( "Cookies are invalid or have expired" )
			else:
				raise SignInError( "There was an error remembering the user" )
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
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password ),
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
						"dataset": response['two_factor_info']
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
							raise SigInError( "Invalid json user info", prev=e )
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
					"id": result.id,
					"username": result.username
				},
				"result": {
					"id": result.id,
					"fullname": result.fullname,
					"username": result.username,
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
	