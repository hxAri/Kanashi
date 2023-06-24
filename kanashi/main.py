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

from random import choice

from kanashi.config import Config, ConfigError
from kanashi.error import *
from kanashi.kanashi import Kanashi
from kanashi.object import Object
from kanashi.profile import Profile
from kanashi.request import RequestRequired
from kanashi.utility import Utility


#[kanashi.runtime.main.Main]
class Main( Utility, RequestRequired ):
	
	#[Main()]: None
	def __init__( self ):
		
		# Instance of class Config.
		self.config = Config()
		self.configLoad()
		
		# Instance of class Kanashi.
		self.kanashi = Kanashi( config=self.config )
		
		# Represent user active.
		self.active = self.kanashi.active
		
		# Object represent configuration.
		self.settings = self.config.settings
		
		# Call constructor RequestRequired.
		self.parent = super()
		self.parent.__init__( self.kanashi.request )
	
	#[Main.about()]: None
	def about( self ):
		display = [ "helpers", "version", "license" ]
		displayLength = len( display )
		outputs = []
		for index, output in enumerate( display ):
			outputs.append( "{}".format( output.capitalize() ) )
			match output:
				case "helpers":
					authors = Config.AUTHORS
					for idx, author in enumerate( authors ):
						if  "name" in author:
							profile = []
							authors[idx] = []
							authors[idx].append( "{}".format( author['name'] ) )
							if  "section" in author:
								profile.append( "{}".format( author['section'] ) )
							if  "email" in author:
								profile.append( "Email {}".format( author['email'] ) )
							if  "github" in author:
								profile.append( "Github {}".format( author['github'] ) )
							authors[idx].append( profile )
					outputs = [
						*outputs,
						*authors
					]
				case "version":
					outputs.append( "Version Number v{}".format( Config.VERSION ) )
					outputs.append( "Version Release v{}".format( Config.VERSION_RELEASE ) )
				case "license":
					outputs.append( "{}".format( Config.LICENSE ) )
					outputs = [
						*outputs,
						*Config.LICENSE_DOC
					]
			if  index < displayLength -1:
				outputs.append( "\x20" )
			pass
		self.output( self, [ *self.outputs, *outputs ] )
		self.previous( self.main, ">>>" )
	
	#[Main.bestie( Profile profile, Bool ask )]: None
	def bestie( self, profile, ask=True ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile.isBestie and ask:
			self.output( self, f"You want to remove {profile.username} from your bestie?" )
			self.tryAgain( f"Keep remove {profile.username} as bestie [Y/n]", lambda: self.bestie( profile, ask=False ), lambda: self.profile( profile=profile ) )
		else:
			if  profile.isBestie:
				action = "Remove Bestie"
			else:
				action = "Adding Bestie"
			bestie = self.thread( f"Trying to {action}", lambda: profile.bestie() )
			try:
				print( bestie )
			except Exception as e:
				raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.bestie( profile, ask=ask ) } )
	
	#[Main.block( Profile profile, Bool ask )]: None
	def block( self, profile, ask=True ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile.blockedByViewer:
			action = "Unblock"
			output = [ "",
				f"Unblock {profile.username}",
				"",
				"They will now be able to see your posts and",
				"follow you on Instagram. Instagram won’t let",
				"them know you unblocked them."
			]
		else:
			action = "Blocking"
			output = [ "",
				"They won’t be able to message you or find",
				"your profile, posts or story on Instagram.",
				"They won’t be notifed that you blocked them."
			]
		if  ask == True:
			self.output( self, output )
			self.tryAgain( f"Ignore and next {action} [Y/n]", lambda: self.block( profile, ask=False ), lambda: self.profile( profile=profile ) )
		else:
			try:
				block = self.thread( f"Trying to {action.lower()} {profile.username}", lambda: profile.block() )
			except Exception as e:
				raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.block( profile, ask=ask ) } )
			self.output( self, "Successfully {} {}".format( action, profile.username ) )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Main.clean()]: None
	def clean( self ):
		self.thread( "Clear request records", self.request.clean )
		self.output( self, "The request log has been cleaned up" )
		self.previous( self.main, ">>>" )
	
	#[Main.configLoad()]: None
	def configLoad( self ):
		try:
			self.thread( "Reading configuration file", self.config.load )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if  not isinstance( self.config.settings, Object ):
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Main.configSave()]: None
	def configSave( self ):
		try:
			self.thread( "Saving configuration file", self.config.save )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if  not isinstance( self.config.settings, Object ):
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Main.explore()]: None
	def explore( self ):
		pass
	
	#[Main.favorite( Profile profile )]: None
	def favorite( self, profile ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if profile.isFeedFavorite:
			action = "Remove favorite"
		else:
			action = "Make favorite"
		favorite = self.thread( f"Trying to {action} {profile.username}", lambda: profile.favorite() )
		try:
			print( favorite )
		except Exception as e:
			raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.favorite( profile ) } )
	
	#[Main.follow( Profile profile, Bool ask )]: None
	def follow( self, profile, ask=True ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  ask and profile.followedByViewer or \
			ask and profile.requestedByViewer:
			output = "Are you sure will unfollow {}?".format( profile.username )
			if  profile.isPrivateAccount:
				output = [ "",
					output,
					"If you change your mind, you'll have to",
					"request to follow {} again".format( profile.username )
				]
			self.output( self, output )
			self.tryAgain( f"Unfollow {profile.username} [Y/n]", lambda: self.follow( profile, ask=False ), lambda: self.profile( profile=profile ) )
		else:
			action = "Follow"
			if  profile.followedByViewer:
				action = "Unfollow"
			elif profile.requestedByViewer:
				action = "Cancel request follow"
			try:
				follow = self.thread( f"{action} {profile.username}", lambda: profile.follow() )
			except Exception as e:
				raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.follow( profile, ask=ask ) } )
			if  follow.following == True:
				output = f"Successfully following {profile.username}"
			elif follow.requested == True:
				output = [ "",
					f"Successfully following {profile.username}",
					f"But waiting to be approved from {profile.username}"
				]
			else:
				output = f"Successfully unfollow {profile.username}"
			self.output( self, output )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Main.download()]: None
	def download( self ):
		pass
	
	#[Main.logout()]: None
	def logout( self ):
		pass
	
	#[Main.main()]: None
	def main( self ):
		
		"""
		return self.profile(
			profile=Profile(
				request=self.request,
				profile={
					**self.request.history[0]['content']['graphql']['user'],
					**self.request.history[1]['content']
				},
				viewer=Object({
					"id": self.active.id,
					"username": self.active.username
				})
			)
		)
		"""
		
		outputs = []
		options = []
		
		# Default main menu actions.
		actions = {
			"profile": {
				"signin": True,
				"action": self.profile,
				"output": "Visit Profile",
				"prints": [
					"Visit profile account"
				]
			},
			"search": {
				"signin": True,
				"action": self.search,
				"output": "Search Anything",
				"prints": [
					"Search posts, users, hashtags and more"
				]
			},
			"explore": {
				"signin": True,
				"action": self.explore,
				"output": "Explore Media",
				"prints": [
					"Explore recommended media"
				]
			},
			"signin": {
				"signin": {
					"require": False,
					"include": False
				},
				"action": self.signin,
				"output": "SignIn Account",
				"prints": [
					"SignIn with password or cookies"
				]
			},
			"logout": {
				"signin": True,
				"action": self.logout,
				"output": "Logout Account",
				"prints": [
					"Logout Instagram account"
				]
			},
			"download": {
				"action": self.download,
				"output": "Download Media",
				"prints": [
					"Download Instagram media"
				]
			},
			"switch": {
				"action": self.switch,
				"output": "Switch Account",
				"prints": [
					"Switch to another saved accounts"
				]
			},
			"setting": {
				"action": self.setting,
				"output": "Kanashī Settings",
				"prints": [
					"Kanashī configuration settings"
				]
			},
			"support": {
				"action": self.support,
				"output": "Support Project",
				"prints": [
					"When this program is useful for you"
				]
			},
			"clean": {
				"action": self.clean,
				"output": "Clear Response",
				"prints": [
					"Clear the entire request record"
				]
			},
			"about": {
				"action": self.about,
				"output": "About Kanashī",
				"prints": [
					"e.g Authors, Version, License, etc"
				]
			},
			"exit": {
				"action": lambda: self.exit( self, "Finish" ),
				"output": "Exit",
				"prints": [
					"Close the program",
					"Always use CTRL+D for shortcut"
				]
			}
		}
		
		# Default println outputs.
		self.outputs = [
			"",
			"Kanashī v{}\x1b[0m".format( Config.VERSION ),
			"",
			"Author {}".format( Config.AUTHOR ),
			"Github \x1b[1m\x1b[4;37m{}\x1b[0m".format( Config.GITHUB ),
			"Issues \x1b[1m\x1b[4;37m{}\x1b[0m".format( Config.ISSUES ),
			""
		]
		
		if  self.kanashi.isActive:
			self.outputs = [
				*self.outputs[0:2],
				"Logged as \x1b[1;38;5;189m{}\x1b[0m".format( self.active.fullname if self.active.fullname else self.active.username ),
				*self.outputs[2:]
			]
		
		for index, option in enumerate( actions ):
			index += 1
			values = actions[option]
			append = False
			if  "signin" in values:
				if  isinstance( values['signin'], dict ):
					if  self.kanashi.isActive:
						if  values['signin']['require'] or \
							values['signin']['require'] == False and \
							values['signin']['include'] == True:
							append = True
					else:
						if  values['signin']['require'] == False:
							append = True
				else:
					if  self.kanashi.isActive and values['signin'] or \
						self.kanashi.isActive == False and values['signin'] == False:
						append = True
			else:
				append = True
			if  append:
				options.append( option )
				outputs.append( values['output'] )
				if  "prints" in values:
					outputs.append( values['prints'] )
		
		self.output( self, [ *self.outputs, outputs ] )
		option = self.input( None, number=True, default=[ idx +1 for idx in range( len( options ) ) ] )
		actions[options[( option -1 )]]['action']()
	
	#[Main.profile( String username, Profile profile )]: None
	def profile( self, username=None, profile=None ):
		if  not isinstance( username, str ) and \
			not isinstance( profile, Profile ):
			self.output( self, [ "",
				"This tool is not used for illegal purposes",
				"like, data theft and so on, please use it",
				"properly",
				"",
				"Enter the user profile username"
			])
			self.profile( self.input( "Username", default=self.active.username ) )
		else:
			if  not isinstance( profile, Profile ):
				try:
					profile = self.thread( f"Retrieve user info {username}", lambda: self.kanashi.client.profile( username=username, friendship=True ) )
				except Exception as e:
					self.emit( e )
					if  isinstance( e, AuthError ):
						pass
					if  isinstance( e, UserError ):
						self.tryAgain( next=self.profile, other=self.main )
					if  isinstance( e, RequestError ):
						self.tryAgain( next=self.profile, other=self.main, username=username )
					else:
						self.previous( self.main, ">>>" )
					return
				self.profile( profile=profile )
			else:
				options = []
				outputs = []
				actions = {
					"block": {
						"avoid": True,
						"action": lambda: self.block( profile ),
						"filter": profile.blockedByViewer,
						"prints": [
							"Block or unblok this user"
						],
						"output": [
							"Block User",
							"Unblock User"
						]
					},
					"bestie": {
						"avoid": True,
						"follow": True,
						"action": lambda: self.bestie( profile ),
						"filter": profile.isBestie,
						"prints": [
							"Make or remove this user as bestie"
						],
						"output": [
							"Make Bestie",
							"Remove Bestie"
						]
					},
					"favorite": {
						"avoid": True,
						"follow": True,
						"action": lambda: self.favorite( profile ),
						"filter": profile.isFeedFavorite,
						"prints": [
							"Make or remove this user from favorite"
						],
						"output": [
							"Make Favorite",
							"Remove Favorite"
						]
					},
					"follow": {
						"avoid": True,
						"action": lambda: self.follow( profile ),
						"prints": [
							"Follow, unfollow or cancel request follow"
						],
						"output": [
							"Follow User",
							"Unfollow User",
							"Unrequest User"
						]
					},
					"report": {
						"avoid": True,
						"action": lambda: self.report( profile ),
						"prints": [ "Report this user profile" ],
						"output": "Report User"
					},
					"muting": {
						"avoid": True,
						"action": lambda: self.muting( profile ),
						"filter": profile.muting,
						"prints": [ "Mute posts, stories, and notes" ],
						"output": "Mute User"
					},
					"restrict": {
						"avoid": True,
						"action": lambda: self.restrict( profile ),
						"filter": profile.restrictedByViewer,
						"prints": [ "Restrict or unrestrict this user" ],
						"output": [
							"Restrict User",
							"Unrestrict User"
						]
					},
					"follows": {
						"action": lambda: self.follows( profile ),
						"output": "Profile Follows",
						"prints": [
							"Gets user followers, following or mutuals"
						]
					},
					"suggest": {
						"action": lambda: self.suggest( profile=profile ),
						"output": "Profile Suggest",
						"prints": [
							"Gests suggested user profiles"
						]
					},
					"medias": {
						"action": lambda: self.medias( profile=profile ),
						"output": "Profile Media",
						"prints": [
							"Gets media posts, reels, saveds, etc"
						]
					},
					"export": {
						"action": lambda: self.export( profile=profile ),
						"output": "Export Profile",
						"prints": [
							"Save profile info as json file"
						],
					},
					"main": {
						"action": self.main,
						"output": "Back to Main"
					}
				}
				for i, option in enumerate( actions ):
					action = actions[option]
					if  "avoid" in action and action['avoid'] and profile.isMySelf or \
						 "follow" in action and action['follow'] and not profile.followedByViewer:
							continue
					if  "output" in action:
						output = action['output']
						if  isinstance( output, list ):
							if  option == "follow":
								if  profile.followedByViewer:
									output = output[1]
								elif profile.requestedByViewer:
									output = output[2]
								else:
									output = output[0]
							elif "filter" in action:
								output = output[1 if action['filter'] else 0]
							else:
								continue
						outputs.append( output )
					options.append( option )
					if  "prints" in action:
						outputs.append( action['prints'] )
				try:
					self.output( self, [ *profile.prints, outputs ] )
					option = self.input( "Select", number=True, default=[ idx +1 for idx in range( len( options ) ) ] )
					actions[options[( option -1 )]]['action']()
				except ProfileError as e:
					self.emit( e.prev )
					data = e.data
					if "action" in data and callable( data['action'] ):
						self.tryAgain( next=data['action'], other=lambda: self.profile( profile=profile ) )
					else:
						self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Main.report( Profile profile )]: None
	def report( self, profile ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		pass
	
	#[Main.restrict( Profile profile, Bool ask )]: None
	def restrict( self, profile, ask=True ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile.restrictedByViewer == False and ask == True:
			self.output( self, [
				"",
				"Are you having a problem with {}?".format( profile.fullname ),
				"",
				"Limit unwanted interactions without having to",
				"block or unfollow someone you know.",
				"",
				"You’ll control if others can see their new",
				"comments on your posts.",
				"",
				"Their chat will be moved to your",
				"Message Requests, so they won’t see",
				"when you’ve read it."
			])
			self.tryAgain( "Restrict account [Y/n]", lambda: self.restrict( profile, ask=False ), lambda: self.profile( profile=profile ) )
		else:
			if  profile.restrictedByViewer:
				action = "Unrestrict"
			else:
				action = "Restrict"
			try:
				restrict = self.thread( f"Trying to {action} {profile.username}", lambda: profile.restrict() )
			except Exception as e:
				raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.restrict( profile, ask=ask ) } )
			self.output( self, "Successfully {} {}".format( action, profile.username ) )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Main.search()]: None
	def search( self ):
		pass
	
	#[Main.setting()]: None
	def setting( self ):
		pass
	
	#[Main.signin( String username, String password, Dict|Object|String cookies, String browser, Bool ask, Int flag )]: None
	def signin( self, username=None, password=None, csrftoken=None, cookies=None, browser=None, ask=True, flag=0 ):
		if  flag == 0:
			self.output( self, [
				"",
				"Please select the signin method", [
					"SignIn Manually",
					"SignIn Remember",
					"Verify 2FA",
					"Cancel"
				]
			])
			self.signin( flag=self.input( "Method", number=True, default=[ 1, 2, 3, 4 ] ) )
		elif flag == 1:
			if  ask:
				self.output( self, [
					"",
					"\x1b[1;38;5;214mWarnings\x1b[0m",
					"Reconsider not using the main account to",
					"login here, because the Developer is not",
					"responsible for anything that happens",
					"to the account used"
				])
				self.tryAgain( "Ignore and next [Y/n]", next=self.signin, other=self.main, ask=True, flag=1 )
				return
			if  not isinstance( username, str ):
				self.output( self, [ "",
					"Username account required for login",
					"Please enter your account username"
				])
				username = self.input( "Username" )
			if  not isinstance( password, str ):
				self.output( self, [ "",
					"Password account required for login",
					"Please enter the password carefully"
				])
				password = self.getpass( "Password" )
			self.signin( username, password, cookies, csrftoken, browser, True, 5 )
		elif flag == 2:
			if  not isinstance( cookies, str ) or \
				not isinstance( browser, str ):
				self.output( self, [
					"",
					"If you are afraid that your account will be",
					"suspended from Instagram because logging in",
					"from a third party is a fairly safe way",
					"because you don’t need to enter your",
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
					"navigator.\x1b[1;33mclipboard\x1b[0m.\x1b[1;33mwriteText\x1b[0m(document.\x1b[1;33mcookie\x1b[0m)"
				])
			if  not isinstance( cookies, str ):
				cookies = self.input( "Cookies" )
			if  not isinstance( browser, str ):
				browser = self.input( "Browser", default=choice( self.settings.browser.default ) )
			self.signin( username, password, cookies, csrftoken, browser, True, 5 )
		elif flag == 3:
			request = self.request.previously( "5m" )
			if  len( request ) >= 1:
				for history in request:
					if  history['target'] == "https://www.instagram.com/accounts/login/ajax/" and \
						"two_factor_required" in history['content'] and \
						"two_factor_info" in history['content']:
						return
				outputs = [
					"There is no history of login requests",
					"that provide two-factor verification data responses"
				]
			else:
				outputs = "There is no request history"
			self.output( self, outputs )
			self.previous( self.signin, ">>>" )
		elif flag == 4:
			self.main()
		elif flag == 5:
			try:
				signin = self.thread( "Trying to SignIn your account", lambda: self.kanashi.signin( username, password, cookies, csrftoken, browser ) )
				if  signin.success:
					self.active = self.kanashi.active
					self.output( self, "Successfully logged in as \x1b[1;38;5;189m{}\x1b[0m".format( signin.signin.fullname if signin.signin.fullname else signin.signin.username ) )
					save = self.input( "Save login info [Y/n]", default=[ "Y", "y", "N", "n" ] )
					if save.upper() == "Y":
						self.configSave()
					self.main()
				elif signin.two_factor:
					print( f"TwoFactor: {signin.two_factor}" )
					
				elif signin.checkpoint:
					print( f"Checkpoint: {signin.checkpoint}" )
					self.previous( self.close, ">>>" )
				else:
					self.output( self, [
						"",
						"There was an error logging in",
						"This usually happens due to some unhandled",
						"things like, setting cookies and information",
						"after login"
					])
					self.previous( self.close, ">>>" )
			except Exception as e:
				self.emit( e )
				if  isinstance( e, UserError ) or \
					isinstance( e, RequestError ):
					params = {
						"next": self.signin,
						"other": self.main,
						"username": username,
						"password": password,
						"csrftoken": csrftoken,
						"cookies": cookies,
						"browser": browser,
						"flag": flag,
						"ask": False
					}
					if  isinstance( e, PasswordError ):
						del params['password']
					if  isinstance( e, UserNotFoundError ):
						del params['username']
						del params['password']
					if  isinstance( e, RequestError ) or \
						isinstance( e, PasswordError ) or \
						isinstance( e, UserNotFoundError ):
						self.tryAgain( **params )
						return
				if  isinstance( e, AuthError ):
					pass
				self.tryAgain( next=self.signin, other=self.main, ask=False, flag=flag )
		else:
			raise TypeError( "Unsupported login method" )
	
	#[Main.support()]: None
	def support( self ):
		pass
	
	#[Main.switch( Int|String select, Bool ask )]: None
	def switch( self, select=None, ask=True ):
		if  ask and self.kanashi.isActive:
			self.output( self, [ "",
				"You have logged in as {}".format( self.active.fullname ),
				"You can choose an account that has logged",
				"in before or log in to another account"
			])
			self.tryAgain( "Switch account [Y/n]", next=self.switch, other=self.signin, ask=False )
		elif self.settings.signin.switch.len() >= 1:
			users = self.settings.signin.switch.keys()
			if  not isinstance( select, int ) and \
				not isinstance( select, str ):
				self.output( self, [ "",
					"Please select an account by filling in the",
					"account number or username, fill in the",
					"back slash to return",
					"",
					users
				])
				select = self.input( None, default=[ "\\", *users, *[ str( i +1 ) for i in range( len( users ) ) ] ] )
			if  select != "\\":
				try:
					try:
						idx = int( select )
						user = users[( idx -1 )]
					except ValueError:
						user = select
					#self.kanashi.switch( self.settings.signin.switch[user] )
					self.thread( "Update login information", lambda: self.kanashi.switch( self.settings.signin.switch[user] ) )
					self.output( self, f"You are logged as \x1b[1;38;5;189m{self.kanashi.active.username}\x1b[0m" )
					self.active = self.kanashi.active
					self.previous( self.main, ">>>" )
				except Exception as e:
					if  isinstance( e, ConfigError ):
						self.active = self.kanashi.active
						self.output( self, "Something wrong when update config" )
						self.tryAgain( next=self.configSave, other=self.main )
					else:
						self.emit( e )
						if  isinstance( e, RequestError ):
							self.tryAgain( next=self.switch, other=self.main, select=select, ask=False )
						else:
							self.input( ">>>", default="" )
							if  isinstance( e, AuthError ):
								self.close( self )
							else:
								self.switch( ask=False )
			else:
				self.main()
		else:
			self.output( self, [
				"No account saved in this device",
				"Want to add a new account or login?"
			])
			self.tryAgain( "Add new account [Y/n]", next=self.signin, other=self.main )
	
	