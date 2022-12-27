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
from time import sleep

from kanashi.context import Context
from kanashi.error import Alert, Error
from kanashi.object import Object
from kanashi.utils import JSON, JSONError, Util

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
	pass
	

#[kanashi.BaseSignIn]
class BaseSignIn( Context ):
	
	#[BaseSignIn( Object app )]
	def __init__( self, app ):
		
		# Copy Request and Session instance.
		self.request = app.request
		self.session = app.session
		
		# Call parent constructor.
		super().__init__( app )
		
	#[BaseSignIn.cookie( String csrftoken, String sessionid, String datr, String dpr, String ds_user_id, String ig_did, String mid, String rur, String shbid, String shbts, String uagent )]
	def cookie( self, csrftoken, sessionid, datr, dpr, ds_user_id, ig_did, mid, rur, shbid, shbts, uagent ):
		pass
	
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
							"cookies": dict( resp.cookies ),
							"profile": json['user']
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
	
	#[SignIn.cookie( String csrftoken, String sessionid, String datr, String dpr, String ds_user_id, String ig_did, String mid, String rur, String shbid, String shbts, String uagent )]
	def cookie( self, csrftoken=None, sessionid=None, datr=None, dpr=None, ds_user_id=None, ig_did=None, mid=None, rur=None, shbid=None, shbts=None, uagent=None ):
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
		if uagent == None:
			if self.input( "Use default User-Agent [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "N":
				uagent = self.input( "User-Agent" )
			else:
				uagent = self.app.config.browser.default
		pass
		
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
						self.output( "activity", "Your account has been checkpoint" )
						if self.input( "Verify your account [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
							pass
						else:
							self.app.main()
					case SignIn2FARequired.__name__:
						self.output( "activity", [
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
						print( "You Are Loged Into Instagram!" )
						print( signin )
					case SignInError.__name__:
						self.emit( signin )
						match SignInError.code:
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
						self.output( "activity", "Something wrong" )
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
		
	#[SignIn.switch()]
	def switch( self ):
		user = self.app.setting.signin.active
		users = self.app.setting.signin.switch
		try:
			if user:
				self.output( "activity", [
					"You have previously logged in as {}",
					"Next if this is you otherwise click n",
					"default=Y"
				])
				if self.input( f"Next as {user} [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
					user = users.get( user )
				else:
					user = None
					self.app.setting.signin.active = None
			if users.len() > 0:
				self.output( "activity", [] ) if user == None else None
				self.cookie(**{
					**user.cookies,
					**{
						"uagent": user.browser
					}
				})
			else:
				self.output( "activity", "There is no account to select" )
				self.input( "Return to the main page", default="" )
				self.app.main()
		except KeyError as e:
			self.emit( e )
			self.input( "Return to the main page", default="" )
			self.app.main()
		
	#[SignIn.verify( SignIn2FARequired info, Int method )]
	def verify( self, info, method, code=None ):
		if code == None:
			self.output( "verify", "Enter the verification code" if method == 1 else "Enter the backup code" )
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
	
