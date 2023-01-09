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

from kanashi.config import Config, ConfigError
from kanashi.error import Alert, Error, Throwable
from kanashi.endpoint import (
	AuthError, 
	BlockError, 
	BlockSuccess, 
	FavoriteError, 
	FavoriteSuccess, 
	FollowError, 
	FollowSuccess, 
	RestrictError, 
	RestrictSuccess, 
	ProfileError, 
	SignInCheckpoint, 
	SignInError, 
	SignIn2FAError, 
	SignInCsrftokenError, 
	SignInPasswordError, 
	SignInSpamError, 
	SignInUserNotFoundError, 
	SignInSuccess, 
	SignIn2FARequired, 
	SignIn2FASuccess, 
	UserError, 
	UserInfoError, 
	UserNotFoundError
)
from kanashi.kanashi import Kanashi
from kanashi.object import Object
from kanashi.request import RequestError
from kanashi.update import UpdateError
from kanashi.utils import Activity, Cookie, File, Util

#[kanashi.cli.Follow]
class Follow:
	
	#[Follow.ondelete( Profile user )]
	def ondelete( self, user ):
		pass
		
	#[Follow.onfollow( Profile user, Hashtag hashtag )]
	def onfollow( self, user=None, hashtag=None ):
		pass
		
	#[Follow.unfollow( Profile user, Hashtag hashtag )]
	def unfollow( self, user=None, hashtag=None ):
		pass
	

#[kanashi.cli.Request]
class Request:
	
	#[Request.resetRequestRecords()]
	def resetRequestRecords( self ):
		try:
			self.thread( "Clear request records", self.request.reset )
			self.output( self, "The request log has been cleaned up" )
			self.previous( self.main, ">>>" )
		except RequestError as e:
			self.emit( e )
			self.tryAgain( next=self.resetRequestRecords, other=self.main )
		
	#[Request.submitNewRequest( String method, String url, **kwargs )]
	def submitNewRequest( self, method, url, **kwargs ):
		try:
			return self.thread( f"Request {method}: {url}", self.request.request, method=method, url=url, **kwargs )
		except RequestError as e:
			self.emit( e )
			return self.tryAgain( next=self.submitNewRequest, other=lambda:False, method=method, url=url, **kwargs )
	

#[kanashi.cli.Profile]
class Profile:
	
	#[Profile.profileOptions( Profile user )]
	def profileOptions( self, user=None ):
		opts = {
			"user.block": "{} User".format( "Unblock" if user.blockedByViewer else "Block" ),
			"user.follow": "{} User".format( "Unfollow" if user.followedByViewer else "Follow" ),
			"user.restrict": "{} User",
			"user.favorite": "{} Favorite",
			"save.profile-json": "Save Profile As Json",
			"save.profile-picture": "Save Profile Picture",
			"save.profile-picture-hd": "Save Profile Picture HD",
			"back": f"Back Previous ({user.prev.__name__})",
			"main": f"Back Main ({self.app.__class__.__name__})"
		}
		self.output( self, [ *user.outputs, [ val for val in opts.values() ] ] )
		keys = [ key for key in opts.keys() ]
		next = self.input( None, number=True, default=[ 1+ i for i in range( len( opts ) ) ] )
		match keys[( next -1 )]:
			case "user.block":
				pass
			case "user.follow":
				if user.followedByViewer:
					self.unfollow( user )
				else:
					self.onfollow( user )
			case "user.favorite":
				pass
			case "user.restrict":
				pass
			case "save.profile-json":
				pass
			case "save.profile-picture":
				self.saveProfilePicture( user, prev=self.profileOptions )
			case "save.profile-picture-hd":
				self.saveProfilePicture( user, hd=True, prev=self.profileOptions )
			case "back":
				user.prev()
			case "main":
				self.main()
			case _:
				# If feature is coming soon.
				pass
	

#[kanashi.cli.Save]
class Save:
	
	#[Save.saveProfilePicture( Object user, String name, Bool hd, Function | Method prev )]
	def saveProfilePicture( self, user, name=None, hd=False, prev=None ):
		if prev == None:
			prev = self.main
		if name == None:
			self.output( self, [
				"Enter a name for the profile photo",
				"Enter \x1b[1;37m\\r\x1b[0m to give it a random name"
			])
			name = self.input( f"Default ({user.username})", default=user.username )
		if prev.__name__ == self.profileOptions.__name__:
			prev = lambda: self.profileOptions( user )
		try:
			save = self.thread( f"Downloading profile picture /{user.username}/", lambda: user.saveProfilePicture( name, hd ) )
			self.output( self, [ "Profile picture saved", f"on{save.saved}" ])
			self.previous( prev, ">>>" )
		except Error as e:
			self.emit( e )
			self.tryAgain(
				next=self.saveProfilePicture,
				other=prev,
				prev=prev,
				user=user,
				name=name,
				hd=hd
			)
	

#[kanashi.cli.SignIn]
class SignIn:
	
	#[SignIn.signInSaveInfo( SignInSuccess signin, String username, Bool default, Bool asked )]
	def signInSaveInfo( self, signin, username=None, default=False, asked=False ):
		if asked:
			try:
				self.thread( "Saving your login info", lambda: self.signin.save( signin, username, default ) )
				self.output( self, "Login info has ben saved" )
				self.previous( self.main, ">>>" )
			except SignInError as e:
				self.emit( e )
				self.tryAgain(**{
					"next": lambda: self.signInSaveInfo( signin, username, default, True ),
					"other": lambda: self.main()
				})
		else:
			self.output( self, [
				"Kanashi provides a feature to save",
				"more than one login, do you want the",
				"current login to be used as the default",
				"for future use"
			])
			self.tryAgain(**{
				"label": "Save as default login [Y/n]",
				"other": lambda: self.signInSaveInfo( signin, username, False, True ),
				"next": lambda: self.signInSaveInfo( signin, username, True, True )
			})
		
	#[SignIn.signInWithPassword( String username, String password, String csrftoken, Bool agreement )]
	def signInWithPassword( self, username=None, password=None, csrftoken=None, agreement=False ):
		if agreement:
			if username == None:
				self.output( self, [ "",
					"Username account required for login",
					"Please enter your account username"
				])
				username = self.input( "username" )
			if password == None:
				self.output( self, [ "",
					"Password account required for login",
					"Please enter the password carefully"
				])
				password = self.getpass( "password" )
			try:
				signin = self.thread( "Trying to SignIn your account", lambda: self.signin.password( username, password, csrftoken ) )
				match type( signin ).__name__:
					case SignIn2FARequired.__name__:
						options = {
							"next.with-code-sent": "Verify with code sent",
							"next.with-code-sent-doc": [],
							"next.with-backup-code": "Verify with backup code",
							"next.with-backup-code-doc": [
								"Verify 2 factor verification with code backup",
								"Use these when you can't access your device"
							],
							"back": "Cancel",
							"back-doc": [
								"Cancel login back to main"
							]
						}
						outputs = [
							"",
							"Oops! It looks like your account has active",
							"two-factor security that needs to be verified",
							""
						]
						self.output( self, [ *outputs, [ value for value in options.values() ] ] )
						opts = self.rmdoc( options )
						next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( opts ) ) ] )
						match opts[( next -1 )]:
							case "next.with-code-sent" | "next.with-backup-code":
								self.signInVerify2FA( signin, next )
							case "back":
								self.main()
					case SignInCheckpoint.__name__:
						print( signin )
						print( self.request.response )
					case SignInSuccess.__name__:
						outputs = [
							"",
							"You have successfully logged in as {}".format( signin.username ),
							"To use this tool again at a later time, Kanashi",
							"provides a feature to save login info, you can",
							"also log out at any time",
							""
						]
						options = {
							"next.none": "Next Main",
							"next.none-doc": [
								"Next to main without save any data",
								"But every successful request will",
								"still be logged to response file"
							],
							"next.save-with-password": "Next Save with Password",
							"next.save-with-password-doc": [
								"This includes saving login data",
								"such as your username and password,",
								"reconsider not saving it because",
								"passwords are only transformed",
								"to Base64 strings!"
							],
							"next.save-without-password": "Next Save without Password",
							"next.save-without-password-doc": [
								"This is almost the same as the",
								"previous option but doesn't save",
								"the password at all"
							]
						}
						self.output( self, [ *outputs, [ value for value in options.values() ] ] )
						opts = self.rmdoc( options )
						next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( opts ) ) ] )
						match opts[( next -1 )]:
							case "next.none":
								self.app.active = signin
								self.app.afterLogin()
								self.main()
							case _:
								if opts[( next -1 )] == "next.save-without-password":
									signin.signin.password = None
								self.signInSaveInfo( signin, signin.username )
						pass
				pass
			except Error as e:
				self.emit( e )
				if isinstance( e, AuthError ):
					self.previous( self.main, ">>>" )
				elif isinstance( e, SignInError ):
					match type( e ).__name__:
						case SignInCsrftokenError.__name__:
							self.tryAgain( next=self.signInWithPassword, other=self.main, username=username, password=password, agreement=True )
						case SignInPasswordError.__name__:
							self.tryAgain( next=self.signInWithPassword, other=self.main, username=username, csrftoken=csrftoken, agreement=True )
						case SignInSpamError.__name__:
							self.previous( self.main, ">>>" )
						case _:
							self.tryAgain( next=self.signInWithPassword, other=self.main, csrftoken=csrftoken, agreement=True )
				elif isinstance( e, RequestError ):
					self.tryAgain( "Re-login [Y/n]", next=self.signInWithPassword, other=self.main, username=username, password=password, csrftoken=csrftoken, agreement=True )
				else:
					self.previous( self.main, ">>>" )
		else:
			self.output( self, [
				"",
				"Reconsider not using the main account to",
				"login here, because the Developer is not",
				"responsible for anything that happens",
				"to the account used"
			])
			self.tryAgain( "Next login [Y/n]", next=self.signInWithPassword, other=self.main, username=username, password=password, csrftoken=csrftoken, agreement=True )
		pass
		
	#[SignIn.signInWithSwitch( Bool asked )]
	def signInWithSwitch( self, asked=False ):
		if asked == False:
			if self.active != None:
				self.output( self, [ "",
					"You have logged in as {}".format( self.active.username ),
					"You can choose an account that has logged",
					"in before or log in to another account"
				])
				self.tryAgain( "Switch account [Y/n]", next=self.signInWithSwitch, other=self.signInWithPassword, asked=True )
			else:
				self.signInWithSwitch( True )
		else:
			users = self.settings.signin.switch.keys()
			self.output( self, [ "",
				"Please select an account by filling in the",
				"account number or username, fill in the",
				"back slash to return", "",
				users
			])
			user = self.input( None, default=[ "\\", *users, *[ str( i +1 ) for i in range( len( users ) ) ] ] )
			if user != "\\":
				try:
					idx = int( user )
					user = users[( idx -1 )]
				except ValueError:
					pass
				self.active = self.settings.signin.switch.get( user )
				self.app.session.headers.update( self.app.active.headers.request.dict() )
				self.app.session.headers.update( self.app.active.headers.response.dict() )
				self.afterLogin()
				self.main()
			else:
				self.main()
		pass
		
	#[SignIn.signInVerify2FA( SigIn2FARequired info, Int method, Int code )]
	def signInVerify2FA( self, info, method=1, code=None ):
		if code == None:
			message = []
			if method == 1:
				if info.sms_two_factor_on:
					message = [
						"Enter the verification code sent to",
						"your phone number, ********{}".format( info.obfuscated_phone_number )
					]
				elif info.totp_two_factor_on:
					message = "Enter the TOTP verification code"
				elif info.whatsapp_two_factor_on:
					message = [
						"Enter the verification code sent to",
						#"your WhatsApp number, ********{}".format( info.obfuscated_phone_number )
					]
			else:
				message = "Enter the verification backup code"
			self.output( self, message )
			code = self.input( "code", number=True )
		try:
			self.thread( "Perform code verification", lambda: self.signin.verify2FA( info, method, code ) )
		except Error as e:
			self.emit( e )
			if isinstance( e, SignInError ):
				match type( e ).__name__:
					case _:
						pass
			elif isinstance( e, RequestError ):
				self.tryAgain( "Re-verify [Y/n]", next=self.signInVerify2FA, other=self.main, info=info, method=method, code=code )
			else:
				self.previous( self.main, ">>>" )
		pass
	

#[kanashi.cli.User]
class User:
	
	#[User.userCookieString()]
	def userCookieString( self ):
		cookies = Cookie.string( self.session.cookies )
		self.output( self, [ "", "This is a list of set login cookies", "", cookies ])
		self.previous( self.main, ">>>" )
		
	#[User.userGet()]
	def userGet( self ):
		outputs = [
			"",
			"This tool is not used for illegal",
			"purposes like, data theft and so on,",
			"please use it properly",
			""
		]
		options = {
			"next.get-by-id": "Get user by Id",
			"next.get-by-username": "Get user by Username",
			"back": "Back to main"
		}
		self.output( self, [ *outputs, [ value for value in options.values() ] ] )
		opts = self.rmdoc( options )
		next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( opts ) ) ] )
		match opts[( next -1 )]:
			case "next.get-by-id":
				self.userGetById()
			case "next.get-by-username":
				self.userGetByUsername()
			case _:
				self.main()
		
	#[User.userGetById( Int id )]
	def userGetById( self, id=None ):
		if id == None:
			self.output( self, "Enter the ID of the user you want to fetch" )
			id = self.input( "userid", number=True, default=self.active.id )
		try:
			user = self.thread( f"Retrieve user info by id /{id}/", lambda: self.user.getById( id ) )
		except Error as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				if self.settings.signin.active == self.active.username:
					self.settings.signin.active = False
				self.settings.signin.switch.unset( self.active.username )
				self.config.save()
				self.previous( self.main, ">>>" )
			elif isinstance( e, UserError ):
				self.tryAgain( next=self.userGetByUsername, other=self.userGet )
			elif isinstance( e, RequestError ):
				self.tryAgain( next=self.userGetByUsername, other=self.userGet, username=username )
			else:
				self.previous( self.userGet, ">>>" )
			return
		user.prev = self.userGet
		self.profileOptions( user )
		
	#[User.userGeyByUsername( String username )]
	def userGetByUsername( self, username=None ):
		if username == None:
			if self.user.recent.len() > 0:
				self.output( self, [ "",
					"Below are the records of previous searches",
					"This is not logged in the configuration file",
					"However the Request class might write to file",
					"Enter a username starting with \x1b[1mr:\x1b[0m for a new",
					"result, example of writing like this \x1b[1mr:test\x1b[0m",
					"",
					self.user.recent.keys()
				])
			else:
				self.output( self, "Enter the username that you will fetch" )
			username = self.input( "username", default=self.active.username )
		try:
			user = self.thread( f"Retrieve user info /{username}/", lambda: self.user.getByUsername( username ) )
		except Error as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				if self.settings.signin.active == self.active.username:
					self.settings.signin.active = False
				self.settings.signin.switch.unset( self.active.username )
				self.config.save()
				self.previous( self.main, ">>>" )
			elif isinstance( e, UserError ):
				self.tryAgain( next=self.userGetByUsername, other=self.userGet )
			elif isinstance( e, RequestError ):
				self.tryAgain( next=self.userGetByUsername, other=self.userGet, username=username )
			else:
				self.previous( self.userGet, ">>>" )
			return
		user.prev = self.userGetByUsername
		self.profileOptions( user )
	

#[kanashi.cli.Cli]
class Cli( Follow, Kanashi, Request, Profile, Save, SignIn, User, Util ):
	
	#[Cli()]
	def __init__( self ):
		
		# Default user active value.
		self.active = None
		
		# Create config class instance.
		self.config = Config( self )
		self.configRead()
		
		# Save parent class instance.
		self.parent = super()
		self.parent.__init__( self )
		
		# Default outputs.
		self.outputs = [
			"",
			"Kanashi v{}".format( self.settings.version ),
			"",
			"Author {}".format( self.settings.authors[0].name ),
			"Github {}".format( self.settings.github ),
			"Issues {}".format( self.settings.issues ),
			""
		]
		
	#[Cli.configRead()]
	def configRead( self ):
		try:
			self.thread( "Reading configuration file", self.config.read )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave, other=lambda: self.close( e, "Operation cannot be continued" ) )
		
	#[Cli.configSave()]
	def configSave( self ):
		try:
			self.thread( "Saving configuration file", self.config.save )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if self.settings.len() == 0:
			self.close( e, "Operation cannot be continued" )
		
	#[Cli.main()]
	def main( self ):
		
		# Default options before user login.
		options = {
			"password": "SignIn Password",
			"password-doc": [
				"SignIn with username and password"
			],
			"session": "SignIn Session",
				"session-doc": [
				"Use login cookies from your browser"
			],
			"switch": "Switch Account",
				"switch-doc": [
				"If you save the previous login info"
			],
			"support": "Support Project",
			"support-doc": [
				"Give spirit to the developer, no matter",
				"how many donations given will still",
				"be accepted"
			],
			"update": "Update Tool",
			"update-doc": [
				"Update the current version to the",
				"latest version, from real source"
			],
			"clear": "Clear Response",
			"clear-doc": [
				"Delete the entire request record"
			],
			"info": "Info",
			"info-doc": [
				"e.g Authors, Version, License, etc"
			],
			"exit": "Exit",
			"exit-doc": [
				"Close the program"
			]
		}
		
		# Check if user is login.
		if self.active != None:
			self.outputs = [
				"",
				"Kanashi v{}".format( self.settings.version ),
				"Logged in as {}".format( self.active.username ),
				"",
				"Author {}".format( self.settings.authors[0].name ),
				"Github {}".format( self.settings.github ),
				"Issues {}".format( self.settings.issues ),
				""
			]
			options = {
				"get.user": "Get User Info",
				"get.user-doc": [
					"Get user by Id, Url, or Username"
				],
				"get.post": "Get Post Info",
				"get.post-doc": [
					"Get post by Id or Url"
				],
				"get.reel": "Get Reel Info",
				"get.reel-doc": [
					"Get reel by Id or Url"
				],
				"cookies": "Cookies",
				"cookies-doc": [
					"Display my cookies"
				],
				"extract": "Extract",
				"extract-doc": [
					"Extract data like timeline, reels, etc"
				],
				"search": "Search",
				"search-doc": [
					"Looks for something like users, hashtags"
				],
				"profile": "Profile",
				"profile-doc": [
					"Your account profile"
				],
				"switch": "Switch Account",
				"switch-doc": [
					"If you save the previous login info"
				],
				"logout": "Logout",
				"logout-doc": [
					"Remove your account from the device",
					"This requires you to login again when",
					"you want to use this tool again",
				],
				"support": "Support Project",
				"support-doc": [
					"Give spirit to the developer, no matter",
					"how many donations given will still",
					"be accepted"
				],
				"update": "Update Tool",
				"update-doc": [
					"Update the current version to the",
					"latest version, from real source"
				],
				"clear": "Clear Response",
				"clear-doc": [
					"Delete the entire request record"
				],
				"info": "Info",
				"info-doc": [
					"e.g Authors, Version, License, etc"
				],
				"exit": "Exit",
				"exit-doc": [
					"Close the program"
				]
			}
		self.output( self, [ *self.outputs, [ value for value in options.values() ] ])
		opts = self.rmdoc( options )
		next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( opts ) ) ] )
		try:
			match opts[( next -1 )]:
				case "get.user":
					self.userGet()
				case "profile":
					self.userGetByUsername( self.active.username )
				case "cookies":
					self.userCookieString()
				case "password":
					self.signInWithPassword()
				case "session":
					self.signInWithRemember()
				case "switch":
					self.signInWithSwitch()
				case "support":
					self.supportProject()
				case "update":
					self.updateTool()
				case "clear":
					self.resetRequestRecords()
				case "info":
					self.info()
				case "exit":
					self.exit( self, "Finish" )
				case _:
					self.output( self, f"Options {opts[( next -1 )]} is coming soon" )
					self.previous( self.main, ">>>" )
			pass
		except AuthError as e:
			self.emit( e )
		pass
	