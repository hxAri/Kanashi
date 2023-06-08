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

from datetime import datetime
from random import randint
from re import findall, match
from time import sleep

from kanashi.endpoint.auth import AuthError
from kanashi.error import Error
from kanashi.object import Object
from kanashi.request import RequestError, RequestRequired
from kanashi.utils import Cookie, JSON, JSONError, String

#[kanashi.endpoint.SignIn]
class SignIn( RequestRequired ):
	
	#[SignIn.csrftoken()]
	@property
	def csrftoken( self ):
		self.app.session.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})
		try:
			return self.request.get( "https://i.instagram.com/api/v1/si/fetch_headers", timeout=10 ).cookies['csrftoken']
		except RequestError as e:
			raise e
		except KeyError as e:
			raise SignInCsrftokenError( "Csrftoken prelogin is not available" )
		
	#[SignIn.password( String username, String password, String csrftoken )]
	def password( self, username, password, csrftoken=None ):
		if csrftoken == None:
			try:
				csrftoken = self.session.headers['X-CSRFToken']
			except KeyError:
				csrftoken = self.csrftoken
		self.session.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/accounts/login/",
			"X-CSRFToken": csrftoken
		})
		try:
			data = {
				"username": username,
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password ),
				"queryParams": {},
				"optIntoOneTap": "false"
			}
			resp = self.request.post( "https://www.instagram.com/accounts/login/ajax/", allow_redirects=True, data=data )
			json = resp.json()
			if "two_factor_required" in json:
				return SignIn2FARequired({
					**json['two_factor_info'],
					**{
						"cookies": resp.cookies,
						"headers": resp.headers
					}
				})
			if "checkpoint_url" in json:
				return SignInCheckpoint( json )
			elif "spam" in json:
				raise SignInSpamError( "Oops! Looks like you are considered SPAM!" )
			elif "user" in json:
				if json['user']:
					if "authenticated" in json and json['authenticated']:
						self.session.headers.update({
							"Origin": "https://www.instagram.com",
							"Referer": "https://www.instagram.com/"
						})
						try:
							user = self.request.get( f"https://i.instagram.com/api/v1/users/{json['userId']}/info/" )
							match user.status_code:
								case 200:
									user = user.json()
									user = user['user']
								case 401:
									raise AuthError( f"Failed to get user info, because the credential is invalid, status {user.status_code}", throw=self )
								case _:
									raise SignInError( f"Something wrong when get user info, status {user.status_code}" )
						except KeyError as e:
							raise SigInError( "Invalid json user info", prev=e )
						return SignInSuccess({
							"id": json['userId'],
							"username": user['username'],
							"browser": self.session.headers['User-Agent'],
							"cookies": {
								**dict( self.session.cookies ),
								**dict( resp.cookies )
							},
							"content": json['user'],
							"headers": {
								"request": {
									**dict( self.session.headers ),
									**{
										"X-CSRFToken": resp.cookies['csrftoken'],
										"Cookie": Cookie.string( self.session.cookies )
									}
								},
								"response": {
									"Cookie": Cookie.string( resp.cookies ),
									"Set-Cookie": resp.headers['Set-Cookie']
								}
							},
							"method": 18262,
							"signin": {
								"username": username,
								"password": "hex[b64]\"{}\"".format( String.encode( password ) )
							}
						})
					else:
						raise SignInPasswordError( "Incorrect password, or may have been changed" )
				else:
					raise SignInUserNotFoundError( "User not found, or may be missing" )
			elif "status" in json and "message" in json:
				raise SignInError( json['message'] )
			else:
				raise SignInError( "An error occurred while signing in" )
		except RequestError as e:
			raise e
		
	#[SignIn.remember( String cookies, String uagent )]
	def remember( self, cookies, uagent=None ):
		if type( cookies ).__name__ == "str":
			cookies = Cookie.simple( cookies )
		for cookie in cookies:
			self.session.cookies.set(
				cookie,
				cookies[cookie],
				domain=".instagram.com",
				path="/"
			)
		try:
			dsuserid = cookies['ds_user_id']
			csrftoken = cookies['csrftoken']
		except KeyError as e:
			if str( e ) == "csrftoken":
				message = "No Csrftoken in cookie"
			else:
				message = "Ds User Id not found in cookie"
			raise SignInCsrftokenError( message, prev=e )
		if uagent == None:
			uagent = self.app.settings.browser.default
		try:
			signin = self.request.get( f"https://i.instagram.com/api/v1/users/{dsuserid}/info/" )
			match signin.status_code:
				case 200:
					user = signin.json()
					user = user['user']
				case 401:
					raise AuthError( f"Failed to get user info, because the credential is invalid, status {signin.status_code}", throw=self )
				case _:
					raise SignInError( f"Something wrong when get user info, status {signin.status_code}" )
			return SignInSuccess({
				"id": dsuserid,
				"username": user['username'],
				"browser": self.session.headers['User-Agent'],
				"cookies": {
					**dict( self.session.cookies ),
					**dict( signin.cookies )
				},
				"content": user,
				"headers": {
					"request": {
						**dict( self.session.headers ),
						**{
							"X-CSRFToken": signin.cookies['csrftoken'],
							"Cookie": Cookie.string( self.session.cookies )
						}
					},
					"response": {
						"Cookie": Cookie.string( signin.cookies ),
						"Set-Cookie": signin.headers['Set-Cookie']
					}
				},
				"method": 29158,
				"signin": {
					"username": user['username'],
					"password": None
				}
			})
		except RequestError as e:
			raise e
		
	#[SignIn.save( SignInSuccess signin, String username, Bool default )]
	def save( self, signin, username=None, default=True ):
		if isinstance( signin, SignInSuccess ):
			if username == None:
				username = signin.username
			if signin.method == SignInSuccess.PASSWORD:
				if signin.signin.password != None:
					transform = match( r"^hex\[b64\]\"((\\x([a-fA-F0-9]{2})){4,})\"$", signin.signin.password )
					if transform == None:
						signin.signin.password = "hex[b64]\"{}\"".format( String.encode( signin.signin.password ) )
			else:
				pass
			self.app.active = signin
			self.app.settings.signin.set({ "active": username if default else False })
			self.app.settings.signin.switch.set({
				username: signin
			})
			self.app.afterLogin()
			try:
				self.app.config.save()
			except ConfigError as e:
				raise SignInError( "Failed save account", prev=e )
		else:
			raise SignInError( f"Value of parameter signin must be type SignInSuccess, {type( signin ).__name__} passed", prev=ValueError( "Invalid argument value passed" ) )
		
	#[SignIn.switch()]
	def switch( self ):
		pass
		
	#[SignIn.verify2FA( SignIn2FARequired info, Int method )]
	def verify2FA( self, info, method, code ):
		length = len( f"{code}" )
		if method == 1 or method == 2:
			if length == 8 and method == 2 or length == 6 and method == 1:
				try:
					cookies = info.headers['Cookie']
				except KeyError:
					cookies = Cookie.string( info.cookies )
				self.session.headers.update({
					"Cookie": cookies,
					"Origin": "https://www.instagram.com",
					"Referer": "https://www.instagram.com/accounts/login/two_factor?next=/"
				})
				try:
					data = {
						"identifier": info.two_factor_identifier,
						"trust_signal": True,
						"username": info.username,
						"verificationCode": code,
						"verification_method": method,
						"queryParams": "{ \"next\": \"/\" }"
					}
					#https://i.instagram.com/api/v1/accounts/two_factor_login/
					resp = self.app.request.post( "https://www.instagram.com/accounts/login/ajax/two_factor/", allow_redirects=True, timeout=10, data=data )
					match resp.status_code:
						case 200:
							print( "Success verify!" )
						case _:
							if resp.status_code >= 500:
								raise SignIn2FAError( f"There is an internal error on the server, status {resp.status_code}" )
							else:
								raise SignIn2FAError( f"An error occurred while verifying two-factor authentication, status {resp.status_code}" )
					pass
				except RequestError as e:
					raise e
				except AttributeError as e:
					raise SignIn2FAError( "Invalid two factor info", prev=e )
			else:
				raise SignIn2FAError( "The length of the verification code does not match" )
		else:
			raise SignIn2FAError( "Invalid two factor verification method" )
	

#[kanashi.endpoint.SignInCheckpoint]
class SignInCheckpoint( Object ):
	pass
	

#[kanashi.endpoint.SignInError]
class SignInError( Error ):
	pass
	

#[kanashi.endpoint.SignIn2FaError]
class SignIn2FAError( SignInError ):
	pass
	

#[kanashi.endpoint.SignInCsrftokenError]
class SignInCsrftokenError( SignInError ):
	pass
	

#[kanashi.endpoint.SignInPasswordError]
class SignInPasswordError( SignInError ):
	pass
	

#[kanashi.endpoint.SignInSpamError]
class SignInSpamError( SignInError ):
	pass
	

#[kanashi.endpoint.SignInUserNotFoundError]
class SignInUserNotFoundError( SignInError ):
	pass
	

#[kanashi.endpoint.SignInSuccess]
class SignInSuccess( Object ):
	
	# User SignIn with Password.
	PASSWORD = 18262
	
	# User SignIn with Cookies.
	REMEMBER = 29158
	

#[kanashi.endpoint.SignIn2FARequired]
class SignIn2FARequired( Object ):
	pass
	

#[kanashi.endpoint.SignIn2FARequired]
class SignIn2FASuccess( SignInSuccess ):
	pass
	