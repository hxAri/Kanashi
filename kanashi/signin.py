#!/usr/bin/env python

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

from kanashi.error import Alert, Error
from kanashi.object import Object
from kanashi.request import RequestRequired
from kanashi.utils import activity, Cookie, JSON, JSONError, String, Util

#[kanashi.SignInError]
class SignInError( Error ):
	
	# Login Detected as Spam.
	# If Spam has detected please wait for 24 hours.
	SPAM_DETECTED = 85181
	
	# User Notfound.
	USER_NOTFOUND = 85283
	
	# Invalid Password
	USER_PASSWORD = 85392
	
#[kanashi.SignIn2FAInvalidCode]
class SignIn2FAInvalidCode( SignInError ):
	pass
	
#[kanashi.SignIn2FARequired]
class SignIn2FARequired( Object ):
	pass
	
#[kanashi.SignInCheckpoint]
class SignInCheckpoint( Object ):
	pass
	
#[kanashi.SignInSuccess]
class SignInSuccess( Object ):
	
	# If user login with password
	PASSWORD = 18262
	
	# If user login with csrftoken
	REMEMBER = 29158
	
#[kanashi.BaseSignIn]
class BaseSignIn( RequestRequired ):
		
	#[BaseSignIn.csrftoken()]
	def csrftoken( self ):
		self.err = None
		try:
			self.app.session.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/"
			})
			resp = self.app.request.get( "https://i.instagram.com/api/v1/si/fetch_headers", timeout=10 )
			if resp:
				return( dict( resp.cookies )['csrftoken'] )
			if self.app.request.err:
				self.err = self.app.request.err
		except KeyError:
			self.err = Error( "Csrftoken prelogin is not available" )
		return( False )
		
	#[BaseSignIn.password( String username, String password )]
	def password( self, username, password, csrftoken ):
		self.app.session.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/",
			"X-CSRFToken": csrftoken
		})
		resp = self.app.request.post( "https://www.instagram.com/accounts/login/ajax/", allow_redirects=True, data={
			"username": username,
			"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password ),
			"queryParams": {},
			"optIntoOneTap": "false"
		})
		if resp != False:
			json = resp.json()
			if "two_factor_required" in json:
				return( SignIn2FARequired( json['two_factor_info'] ) )
			if "checkpoint_url" in json:
				return( SignInCheckpoint( json ) )
			elif "spam" in json:
				return( SignInError( "Oops! Looks like you are considered SPAM!", SignInError.SPAM_DETECTED ) )
			elif "user" in json:
				if json['user']:
					if "authenticated" in json and json['authenticated']:
						return( SignInSuccess({
							"id": json['userId'],
							"browser": self.session.headers['User-Agent'],
							"cookies": {
								**dict( self.session.cookies ),
								**dict( resp.cookies )
							},
							"content": json['user'],
							"headers": {
								"request": dict( self.session.headers )
							},
							"method": SignInSuccess.PASSWORD,
							"signin": {
								"username": username,
								"password": "hex[b64]\"{}\"".format( String.encode( password ) )
							}
						}))
					else:
						return( SignInError( "Incorrect password, or may have been changed", SignInError.USER_PASSWORD ) )
				else:
					return( SignInError( "User not found, or may be missing", SignInError.USER_NOTFOUND ) )
			if "status" in json and "message" in json:
				return( SignInError( json['message'] ) )
			else:
				return( SignInError( "An error occurred while signing in" ) )
		if self.app.request.err:
			self.err = self.app.request.err
		return( False )
		
	#[BaseSignIn.remember( String username, String csrftoken, String sessionid, String datr, String dpr, String ds_user_id, String ig_did, String mid, String rur, String shbid, String shbts, String uagent )]
	def remember( self, username, csrftoken, sessionid, datr, dpr, ds_user_id, ig_did, mid, rur, shbid, shbts, uagent ):
		pass
		
	#[BaseSignIn.save( SignInSuccess success, String username )]
	def save( self, succes, username ):
		self.app.active = success
		match success.method:
			case SignInSuccess.PASSWORD:
				self.app.setting.signin.switch.set({ username: success })
			case SignInSuccess.REMEMBER:
				self.app.setting.signin.switch.set({
					username: {
						# Xxxx
					}
				})
			case _:
				pass
		self.app.config.save()
		
	#[BaseSignIn.switch()]
	def switch( self ):
		raise SignInError( "The switch utility is not available for the BaseSigIn class because well, it is something that requires interaction" )
		
	#[BaseSignIn.verify( SignIn2FARequired info, Int method )]
	def verify( self, info, method, code ):
		try:
			self.app.session.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/accounts/login/two_factor?next=%2F"
			})
			resp = self.app.request.post( "https://www.instagram.com/accounts/login/ajax/two_factor/", allow_redirects=True, timeout=10, data={
				"identifier": info.two_factor_identifier,
				"trust_signal": "true",
				"username": info.username,
				"verificationCode": code,
				"verification_method": method,
				"queryParams": {
					"next":"/"
				}
			})
			if resp != False:
				print( resp )
				print( JSON.encode( resp.json() ) )
			if self.app.request.err:
				self.err = self.app.request.err
		except AttributeError as e:
			self.err = e
		return( False )
	

#[kanashi.SignIn]
class SignIn( BaseSignIn, Util ):
		
	#[SignIn.csrftoken()]
	def csrftoken( self ):
		csrftoken = BaseSignIn.csrftoken( self )
		if csrftoken:
			return( csrftoken )
		else:
			self.emit( self.err )
			if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				return( self.csrftoken() )
		return( False )
		
	#[SignIn.password( String username, String password )]
	def password( self, username=None, password=None, csrftoken=None ):
		self.output( activity, [
			"Please enter your username, phone number or email address",
			"and also your Instagram account password"
		])
		if csrftoken == None:
			csrftoken = self.csrftoken()
			sleep( 1 )
		if csrftoken:
			if username == None:
				username = self.input( "username" )
			if password == None:
				password = self.getpass( "password" )
			signin = BaseSignIn.password( self, username, password, csrftoken )
			if signin != False:
				match type( signin ).__name__:
					case SignInCheckpoint.__name__:
						self.output( activity, "Your account has been checkpoint" )
						if self.input( "Verify your account [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
							pass
						else:
							self.app.main()
					case SignIn2FARequired.__name__:
						self.output( activity, [
							"Two factor code required",
							"",
							[
								"Verify with code sent",
								"Verify with backup code",
								"Cancel"
							]
						])
						next = self.input( None, number=True, default=[ 1, 2, 3 ])
						if next != 3:
							self.verify( signin, next )
						else:
							self.app.main()
					case SignInSuccess.__name__:
						self.save( signin, username )
					case SignInError.__name__:
						self.emit( signin )
						match signin.code:
							case SignInError.SPAM_DETECTED:
								self.input( "Return to the main page", default="" )
								self.app.main()
							case SignInError.USER_NOTFOUND:
								if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
									self.password( csrftoken=csrftoken )
								else:
									self.app.main()
							case SignInError.USER_PASSWORD:
								if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
									self.password(
										username=username,
										csrftoken=csrftoken
									)
								else:
									self.app.main()
							case _:
								if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
									self.password()
								else:
									self.app.main()
					case _:
						self.output( activity, "Something wrong" )
						if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
							self.password( csrftoken=csrftoken )
						else:
							self.app.main()
			else:
				self.emit( self.err )
				if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
					self.password(
						username=username,
						password=password,
						csrftoken=csrftoken
					)
				else:
					self.app.main()
		else:
			self.app.main()
		
	#[SignIn.remember( String username, String csrftoken, String sessionid, String datr, String dpr, String ds_user_id, String ig_did, String mid, String rur, String shbid, String shbts, String uagent )]
	def remember( self, username=None, csrftoken=None, sessionid=None, datr=None, dpr=None, ds_user_id=None, ig_did=None, mid=None, rur=None, shbid=None, shbts=None, uagent=None ):
		cookies = {
			"csrftoken": csrftoken or self.input( "csrftoken" ),
			"sessionid": sessionid or self.input( "sessionid" ),
			"datr": datr or self.input( "datr" ),
			"dpr": dpr or self.input( "dpr" ),
			"ds_user_id": ds_user_id or self.input( "ds_user_id", number=True ),
			"ig_did": ig_did or self.input( "ig_did" ),
			"mid": mid or self.input( "mid" ),
			"rur": rur or self.input( "rur" ),
			"shbid": shbid or self.input( "shbid" ),
			"shbts": shbts or self.input( "shbts" )
		}
		if username == None:
			username = self.input( "username" )
		if uagent == None:
			if self.input( "Use default User-Agent [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "N":
				uagent = self.input( "User-Agent" )
			else:
				uagent = self.app.config.browser.default
		pass
		
	#[SignIn.save( SignInSuccess success, String username )]
	def save( self, success, username ):
		self.output( activity, "You have successfully logged into Instagram" )
		if self.input( "Save login info [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
			if match( r"^([a-zA-Z_\x80-\xff]([a-zA-Z0-9_\.\x80-\xff]{0,}[a-zA-Z0-9_\x80-\xff]{1})*)$", username ) == None:
				self.output( activity, [
					"Oops!It seems you did not log in using your username,",
					"please enter your username to use at a later time"
				])
				username = self.input( "username" )
			if self.input( "Save as default account [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				self.app.setting.signin.active = username
			BaseSignIn.save( success, username )
			self.main()
		else:
			self.app.main()
		
	#[SignIn.switch()]
	def switch( self ):
		user = self.app.setting.signin.active
		users = self.app.setting.signin.switch
		if user:
			self.output( activity, [
				"Previously you have logged in as {}".format( user ),
				"Cancel if this is not your account"
			])
			if self.input( "Next as {} [Y/n]".format( user ), default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				user = users.get( user )
			else:
				self.app.setting.signin.active = None
				self.switch()
				return
		else:
			self.output( activity, [
				"",
				"Select login as",
				"",
				users.keys()
			])
			user = users.keys()[ self.input( None, number=True, default=[ 1+ idx for idx in range( users.len() ) ] ) -1 ]
			user = users.get( user )
		self.output( activity, [
			"Re-login with password [Y]",
			"or keep using current login info [N]"
		])
		self.session.headers.update( user.headers.request.dict() )
		self.session.headers.update( user.headers.response.dict() )
		if self.input( "Next [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
			match user.method:
				case SignInSuccess.PASSWORD:
					self.output( activity, [
						"Records of previous logins and your",
						"passwords have been saved. Keep using",
						"the password you previously used [Y/n]"
					])
					if self.input( "Use the previous one [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
						find = findall( r"^hex\[b64\]\"((\\x([a-fA-F0-9]{2})){4,})\"$", user.signin.password )
						try:
							password = String.decode( find[0][0] )
						except IndexError:
							password = None
					else:
						password = None
					self.password(
						password=password,
						username=user.signin.username,
						csrftoken=user.cookies.csrftoken
					)
				case SignInSuccess.REMEMBER:
					self.password(
						username=user.signin.username,
						csrftoken=user.cookies.csrftoken
					)
				case _:
					pass
		else:
			self.app.active = user
			self.app.main()
		
	#[SignIn.verify( SignIn2FARequired info, Int method )]
	def verify( self, info, method, code=None ):
		if code == None:
			self.output( activity, "Enter the verification code" if method == 1 else "Enter the backup code" )
			code = self.input( "code", number=True )
		verify = BaseSignIn.verify( self, info, method, code )
		if verify != False:
			print( verify )
		else:
			self.emit( self.err )
			if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				self.verify(
					info=info,
					code=code,
					method=method
				)
			else:
				self.app.main()
	