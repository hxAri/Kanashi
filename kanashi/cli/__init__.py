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

from re import findall

from kanashi.config import Config, ConfigError
from kanashi.error import Alert, Error, Throwable
from kanashi.endpoint import (
	AuthError, 
	Block, 
	BlockError, 
	BlockSuccess, 
	FavoriteError, 
	FavoriteSuccess, 
	FollowError, 
	FollowSuccess, 
	Profile, 
	ProfileError, 
	ProfileSuccess, 
	ReportError,
	ReportSuccess, 
	RestrictError, 
	RestrictSuccess, 
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

#[kanashi.cli.Cli]
class Cli( Kanashi, Util ):
	
	#[Cli()]
	def __init__( self ) -> None:
		
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
			"Kanashī v{}".format( self.settings.version ),
			"",
			"Author {}".format( self.settings.authors[0].name ),
			"Github {}".format( self.settings.source ),
			"Issues {}".format( self.settings.issues ),
			""
		]
	
	#[Cli.configRead()]
	def configRead( self ) -> None:
		try:
			self.thread( "Reading configuration file", self.config.read )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave, other=lambda: self.close( e, "Operation cannot be continued" ) )
		pass
	
	#[Cli.configSave()]
	def configSave( self ) -> None:
		try:
			self.thread( "Saving configuration file", self.config.save )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if self.settings.len() == 0:
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Cli.info()]
	def info( self ) -> None:
		self.output( self, self.parent.info )
		self.previous( self.main, ">>>" )
	
	#[Cli.main()]
	def main( self ) -> None:
		
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
				"Kanashī v{}".format( self.settings.version ),
				"Logged in as {}".format( self.active.username ),
				"",
				"Author {}".format( self.settings.authors[0].name ),
				"Github {}".format( self.settings.source ),
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
	
	#[Profile.profileBlock( Profile user, Int level )]
	def profileBlock( self, user:Profile, level:int=None ) -> None:
		next = 0
		action = "Unblock"
		if user.blockedByViewer == False and level == None:
			action = "Blocking"
			self.output( self, [ "",
				"They won't be able to message you or find",
				"your profile, posts or story on Instagram.",
				"They won't be notifed that you blocked them.",
				"", [
					f"Block {user.username} and other accounts",
					f"Block {user.username} and report",
					f"Block {user.username} only",
					f"Cancel"
				]
			])
			next = self.input( "Block", number=True, default=[ idx +1 for idx in range( 4 ) ] )
			match next:
				case 1:
					level = Block.BLOCK_MULTILEVEL
				case 2:
					level = Block.BLOCK_REPORT
				case 3:
					level = Block.BLOCK_ONLY
				case 4:
					self.profileOptions( user )
					return
		else:
			self.output( self, [ "",
				"Unblock {user.username}",
				"They will now be able to see your posts and follow you on Instagram. Instagram won't let them know you unblocked them."
			])
		try:
			block = self.thread( f"{action} account {user.username}", lambda: self.block.block( user, level=level ) )
			self.output( self, f"Successfully {action} {user.username}" )
			if level == Block.BLOCK_REPORT:
				next = self.input( "Next report [Y/n]", default=[ "Y", "y", "N", "n" ] )
				if next.upper() == "Y":
					self.profileReport( user )
				else:
					self.profileOptions( user )
			else:
				self.previous( lambda: self.profileOptions( user ), ">>>" )
		except Error as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				if self.settings.signin.active == self.active.username:
					self.settings.signin.active = False
				keep = self.input( "Keep login [Y/n]", default=[ "Y", "y", "N", "n" ] )
				if keep.upper() == "Y":
					self.profileOptions( user )
				else:
					self.settings.signin.switch.unset( self.active.username )
					self.active = None
					self.configSave()
					self.previous( self.main, ">>>" )
			elif isinstance( e, RequestError ):
				self.tryAgain(
					next=lambda: self.profileBlock( user ),
					other=lambda: self.profileOptions( user )
				)
			else:
				self.previous( lambda: self.profileOptions( user ), ">>>" )
		pass
	
	#[Profile.profileFollow( Profile user, Bool agree )]
	def profileFollow( self, user:Profile, agree:bool=False ) -> None:
		try:
			action = "Follow"
			if user.followedByViewer or user.requestedByViewer:
				action = "Unfollow"
				if user.requestedByViewer:
					action = "Cancel request follow"
				if agree == False:
					output = f"Are you sure will unfollow {user.username}"
					if user.isPrivateAccount:
						output = [ "",
							output,
							"If you change your mind, you'll have to",
							f"request to follow {user.username} again"
						]
					self.output( self, output )
					next = self.input( f"Unfollow {user.username} [Y/n]", default=[ "Y", "y", "N", "n" ] )
					if next.upper() == "N":
						self.profileOptions( user )
						return
					agree = True
			follow = self.thread( f"{action} {user.username}", lambda: self.follow.follow( user ) )
			if follow.following:
				output = f"Successfully following {user.username}"
			elif follow.requested:
				output = [ "",
					f"Successfully following {user.username}",
					f"But waiting to be approved from {user.username}"
				]
			else:
				output = f"Successfully unfollow {user.username}"
			self.output( self, output )
			self.previous( lambda: self.profileOptions( user ), ">>>" )
		except Error as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				if self.settings.signin.active == self.active.username:
					self.settings.signin.active = False
				keep = self.input( "Keep login [Y/n]", default=[ "Y", "y", "N", "n" ] )
				if keep.upper() == "Y":
					self.profileOptions( user )
				else:
					self.settings.signin.switch.unset( self.active.username )
					self.active = None
					self.configSave()
					self.previous( self.main, ">>>" )
			elif isinstance( e, RequestError ):
				self.tryAgain(
					next=lambda: self.profileFollow( user, agree ),
					other=lambda: self.profileOptions( user )
				)
			else:
				self.previous( lambda: self.profileOptions( user ), ">>>" )
		pass
	
	#[Profile.profileFavorite( Profile user )]
	def profileFavorite( self, user:Profile ) -> None:
		pass
	
	#[Profile.profileReport( Profile user, Dict data, Bool asked )]
	def profileReport( self, user:Profile, data:dict=None, asked:bool=True ) -> None:
		self.output( self, [ "",
			"This feature might take a long time to",
			"develop or even just make it, it is very",
			"likely that this feature will be removed",
			"from Kanashī"
		])
		self.previous( self.profileOptions, ">>>", user )
	
	#[Profile.profileRestrict()]
	def profileRestrict( self, user:Profile ) -> None:
		pass
	
	#[Profile.profileOptions( Profile user )]
	def profileOptions( self, user:Profile ) -> None:
		follow = "Follow"
		if user.followedByViewer:
			follow = "Unfollow"
		elif user.requestedByViewer:
			follow = "Cancel Request Follow"
		block = "Unblock" if user.blockedByViewer else "Block"
		restrict = "Unrestrict" if user.restrictedByViewer else "Restrict"
		favorite = "Make"
		opts = {
			"user.block": "{} User".format( block ),
			"user.follow": "{} User".format( follow ),
			"user.restrict": "{} User".format( restrict ),
			"user.report": "Report User",
			"user.favorite": "{} Favorite".format( favorite ),
			"user.profile-edges": "Edges",
			"save.profile-json": "Save Profile as Json",
			"save.profile-picture": "Save Profile Picture",
			"save.profile-picture-hd": "Save Profile Picture HD",
			"back": f"Back Previous",
			"main": f"Back Main"
		}
		self.output( self, [ *user.outputs, [ val for val in opts.values() ] ] )
		keys = [ key for key in opts.keys() ]
		next = self.input( None, number=True, default=[ 1+ i for i in range( len( opts ) ) ] )
		match keys[( next -1 )]:
			case "user.block":
				self.profileBlock( user )
			case "user.follow":
				self.profileFollow( user )
			case "user.report":
				self.profileReport( user )
			case "user.favorite":
				self.profileFavorite( user )
			case "user.restrict":
				self.profileRestrict( user )
			case "user.profile-edge":
				self.profileEdge( user )
			case "save.profile-json":
				self.saveProfile( user )
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
		pass
	
	#[Request.resetRequestRecords()]
	def resetRequestRecords( self ) -> None:
		try:
			self.thread( "Clear request records", self.request.reset )
			self.output( self, "The request log has been cleaned up" )
			self.previous( self.main, ">>>" )
		except RequestError as e:
			self.emit( e )
			self.tryAgain( next=self.resetRequestRecords, other=self.main )
		pass
	
	#[Save.saveProfilePicture( Object user, String name, Bool hd, Function | Method prev )]
	def saveProfilePicture( self, user:Profile, name:str=None, hd:bool=False, prev=None ) -> None:
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
			save = self.thread( f"Downloading profile picture {user.username}", lambda: user.saveProfilePicture( name, hd ) )
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
		pass
	
	#[SignIn.signInSaveInfo( SignInSuccess signin, String username, Bool default, Bool asked )]
	def signInSaveInfo( self, signin:SignInSuccess, username:str=None, default:bool=False, asked:bool=False ) -> None:
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
				"Kanashī provides a feature to save",
				"more than one login, do you want the",
				"current login to be used as the default",
				"for future use"
			])
			self.tryAgain(**{
				"label": "Save as default login [Y/n]",
				"other": lambda: self.signInSaveInfo( signin, username, False, True ),
				"next": lambda: self.signInSaveInfo( signin, username, True, True )
			})
		pass
	
	#[SignIn.signInWithPassword( String username, String password, String csrftoken, Bool agreement )]
	def signInWithPassword( self, username:str=None, password:str=None, csrftoken:str=None, agreement:bool=False ) -> None:
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
							"To use this tool again at a later time, Kanashī",
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
	
	#[SignIn.signInWithRemember( String cookies, String uagent )
	def signInWithRemember( self, cookies:str=None, uagent:str=None ) -> None:
		if cookies == None:
			self.output( self, [ "",
				"If you are afraid that your account will be",
				"suspended from Instagram because logging in",
				"from a third party is a fairly safe way",
				"because you don't need to enter your",
				"credentials, just paste your Instagram",
				"login cookie.",
				"",
				"A raw cookie will usually looks like this",
				"csrftoken=*****; ds_user_id=*****, ....",
				"",
				"If you are an Android user, please use Kiwi",
				"Browser to get your Instagram login cookies",
				"Please login as usual, after successfully",
				"logging in please open the [Deloper Tools]",
				"menu and select [Console] then run the",
				"JavaScript code below to copy your",
				"Instagram login cookie",
				"",
				"navigator.\x1b[33mclipboard\x1b[0m.\x1b[33mwriteText\x1b[0m(document.\x1b[33mcookie\x1b[0m)"
			])
			cookies = self.input( "cookies" )
		if uagent == None:
			uagent = self.input( "User-Agent", default=self.settings.browser.default )
		try:
			signin = self.thread( "Trying to SignIn with cookie", lambda: self.signin.remember( cookies, uagent ) )
			if isinstance( signin, SignInSuccess ):
				outputs = [
					"",
					"You have successfully logged in as {}".format( signin.username ),
					"To use this tool again at a later time, Kanashī",
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
					"next.save": "Next Save data",
					"next.save-doc": [
						"Save login information for future use"
					]
				}
				self.output( self, [ *outputs, [ value for value in options.values() ] ] )
				opts = self.rmdoc( options )
				next = self.input( None, number=True, default=[ 1+ idx for idx in range( len( opts ) ) ] )
				if opts[( next -1 )] == "next.save":
					self.signInSaveInfo( signin, signin.username )
				else:
					self.app.active = signin
					self.app.afterLogin()
					self.main()
			else:
				print( type( signin ).__name__ )
		except Error as e:
			self.emit( e )
			if isinstance( e, RequestError ):
				self.tryAgain( "Re-login [Y/n]", next=self.signInWithRemember, other=self.main )
			else:
				self.previous( self.main, ">>>" )
		pass
	
	#[SignIn.signInWithSwitch( Bool asked )]
	def signInWithSwitch( self, asked:bool=False ) -> None:
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
			if self.settings.signin.switch.len():
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
			else:
				self.output( self, "No account saved" )
				self.previous( self.main, ">>>" )
		pass
	
	#[SignIn.signInVerify2FA( SigIn2FARequired info, Int method, Int code )]
	def signInVerify2FA( self, info:SignIn2FARequired, method:int=1, code:int=None ) -> None:
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
			verify = self.thread( "Perform code verification", lambda: self.signin.verify2FA( info, method, code ) )
			print( verify )
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
	
	#[Request.submitNewRequest( String method, String url, **kwargs )]
	def submitNewRequest( self, method:str, url:str, **kwargs ) -> None:
		try:
			return self.thread( f"Request {method}: {url}", self.request.request, method=method, url=url, **kwargs )
		except RequestError as e:
			self.emit( e )
			return self.tryAgain( next=self.submitNewRequest, other=lambda:False, method=method, url=url, **kwargs )
		pass
	
	#[User.userCookieString()]
	def userCookieString( self ) -> None:
		cookies = Cookie.string( self.session.cookies )
		self.output( self, [ "", "This is a list of set login cookies", "", cookies ])
		self.previous( self.main, ">>>" )
	
	#[User.userGet()]
	def userGet( self ) -> None:
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
		pass
	
	#[User.userGetById( Int id )]
	def userGetById( self, id:int=None ) -> None:
		if id == None:
			self.output( self, "Enter the ID of the user you want to fetch" )
			id = self.input( "userid", number=True, default=self.active.id )
		try:
			user = self.thread( f"Retrieve user info by id {id}", lambda: self.user.getById( id ) )
			user.prev = self.userGet
			self.profileOptions( user )
		except Error as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				if self.settings.signin.active == self.active.username:
					self.settings.signin.active = False
				keep = self.input( "Keep login [Y/n]", default=[ "Y", "y", "N", "n" ] )
				if keep.upper() == "Y":
					self.userGetById()
				else:
					self.settings.signin.switch.unset( self.active.username )
					self.active = None
					self.configSave()
					self.previous( self.main, ">>>" )
			elif isinstance( e, UserError ):
				self.tryAgain( next=self.userGetById, other=self.userGet )
			elif isinstance( e, RequestError ):
				self.tryAgain( next=self.userGetById, other=self.userGet, id=id )
			else:
				self.previous( self.userGet, ">>>" )
		pass
	
	#[User.userGeyByUsername( String username )]
	def userGetByUsername( self, username:str=None ) -> None:
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
				find = findall( r"^r\:([^\n]+)$", username )
				try:
					username = find[0]
					user = self.user.recent.get( username )
					user.prev = self.userGetByUsername
					self.profileOptions( user )
					return
				except IndexError:
					pass
			except( AttributeError, KeyError, IndexError ):
				pass
		try:
			user = self.thread( f"Retrieve user info {username}", lambda: self.user.getByUsername( username ) )
			user.prev = self.userGetByUsername
			self.profileOptions( user )
		except Error as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				if self.settings.signin.active == self.active.username:
					self.settings.signin.active = False
				keep = self.input( "Keep login [Y/n]", default=[ "Y", "y", "n", "n" ] )
				if keep.upper() == "Y":
					self.userGetByUsername()
				else:
					self.settings.signin.switch.unset( self.active.username )
					self.active = None
					self.configSave()
					self.previous( self.main, ">>>" )
			elif isinstance( e, UserError ):
				self.tryAgain( next=self.userGetByUsername, other=self.userGet )
			elif isinstance( e, RequestError ):
				self.tryAgain( next=self.userGetByUsername, other=self.userGet, username=username )
			else:
				self.previous( self.userGet, ">>>" )
		pass
	