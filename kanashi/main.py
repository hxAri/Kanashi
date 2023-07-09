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

from random import choice
from re import match

from kanashi.client import logged
from kanashi.config import Config, ConfigError
from kanashi.error import *
from kanashi.kanashi import Kanashi
from kanashi.media import Media, MediaCollection
from kanashi.object import Object
from kanashi.profile import Profile
from kanashi.request import RequestRequired
from kanashi.utility import Utility, tree, typedef


#[kanashi.main.Actions]
class Actions:
	
	#[Actions()]: None
	def __init__( self ):
		
		# Instance of class Config.
		self.config = Config()
		self.configLoad()
		
		# Instance of class Kanashi.
		self.kanashi = Kanashi( config=self.config )
		
		# Instance of class Client.
		self.client = self.kanashi.client
		
		# Represent user active.
		self.active = self.kanashi.active
		
		# Object represent configuration.
		self.settings = self.config.settings
		
		# Visited profiles.
		self.profiles = {}
		
		# Call constructor RequestRequired.
		self.parent = super()
		self.parent.__init__( self.kanashi.request )
	
	#[Actions.about()]: None
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
		self.output( self.about, [ *self.outputs, *outputs ] )
		self.previous( self.main, ">>>" )
	
	#[Actions.action( String label, Dict actions, List prints, Bool info )]: Function|Method
	def action( self, label=None, actions={}, prints=[], info=True ):
		
		"""
		actions={
			"option": {
				"action": lambda: ...,
					Function|Method action
				"filter": bool,
					Filter if option is allowed
				"allows": bool,
					Filter if option is not allowed
				"signin": {
					"require": bool,
						Filter if option must be signin
					"inclufe": bool
						Filter if option must Even though the user has logged in
				},
				"output": List|String,
					When value is list, filter must be available
				"prints": List|String
					Output descriptions, this is optional
					When the value is String, it will transform to list
			}
		}
		"""
		
		outputs = []
		options = []
		
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
		
		if  not isinstance( prints, list ): prints = [prints]
		if  self.authenticated:
			self.outputs = [
				*self.outputs[0:2],
				"Logged as \x1b[1;38;5;189m{}\x1b[0m".format( self.active.fullname if self.active.fullname else self.active.username ),
				*self.outputs[2:]
			]
		
		for index, option in enumerate( actions ):
			action = actions[option]
			if  "action" not in action:
				continue
			else:
				if  not callable( action['action'] ): continue
			if  "allows" in action and not action['allows']: continue
			if  "follow" in action and not action['follow']: continue
			if  "signin" in action:
				if  isinstance( action['signin'], dict ):
					if  self.authenticated:
						if  action['signin']['require'] is False or \
							action['signin']['require'] is True and \
							action['signin']['include'] is False:
							continue
					else:
						if  action['signin']['require'] is True:
							continue
				else:
					if  self.authenticated and not action['signin'] or \
						not self.authenticated and not action['signin']:
						continue
			if  "output" in action:
				if  isinstance( action['output'], list ):
					if  "filter" in action:
						if  isinstance( action['filter'], list ):
							for i in range( len( action['filter'] ) ):
								if  action['filter'][i] is True:
									action['output'] = action['output'][i]
									break
							if  isinstance( action['output'], list ):
								action['output'] = action['output'][0]
						else:
							action['output'] = action['output'][bool( action['filter'] )]
				elif "filter" in action:
					if  not action['filter']:
						continue
			else:
				continue
			options.append( option )
			outputs.append( action['output'] )
			if  "prints" in action:
				if  not isinstance( action['prints'], list ):
					action['prints'] = [action['prints']]
				outputs.append( action['prints'] )
		
		if  info:
			params = [ *self.outputs, *prints, outputs ]
		else:
			params = [ *prints, outputs ]
		self.output( self.action, params )
		option = self.input( label, number=True, default=[ idx +1 for idx in range( len( options ) ) ] )
		return actions[options[option -1 ]]['action']
	
	#[Actions.approve( Object|Profile user, Bool approve )]: None
	@logged
	def approve( self, user, approve=None ):
		if  not isinstance( user, Object ) and \
			not isinstance( user, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Object|Profile, {} passed".format( type( user ).__name__ ) )
		if  typedef( approve, bool, False ):
			self.output( self.approve, "For next action please confirm" )
			approve = self.input( "Approve [Y/n]", default=[ True, "Y", "y", "N", "n", "\\" ] )
			match approve.upper():
				case "\\":
					if  typedef( user, Profile ):
						self.profile( profile=profile )
					else:
						self.main()
				case "N":
					self.approve( user=user, approve=False )
				case _:
					self.approve( user=user, approve=True )
		action = "Approve request"
		if  not approve:
			action = "Ignore request"
		request = self.client.approve( id=user.id, approve=approve )
		print( request )
	pass
	
	#[Actions.authenticated<kanashi.client.Client.authenticated>]: Bool
	@property
	def authenticated( self ):
		return self.kanashi.isActive
	
	#[Actions.bestie( Profile profile, Bool ask )]: None
	@logged
	def bestie( self, profile, ask=True ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile.isBestie and ask:
			self.output( self.bestie, f"You want to remove {profile.username} from your bestie?" )
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
	
	#[Actions.block( Profile profile, Bool ask )]: None
	@logged
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
			self.output( self.block, output )
			self.tryAgain( f"Ignore and next {action} [Y/n]", lambda: self.block( profile, ask=False ), lambda: self.profile( profile=profile ) )
		else:
			try:
				block = self.thread( f"Trying to {action.lower()} {profile.username}", lambda: profile.block() )
			except Exception as e:
				raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.block( profile, ask=ask ) } )
			self.output( self.block, "Successfully {} {}".format( action, profile.username ) )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Actions.clean()]: None
	def clean( self ):
		self.thread( "Clear request records", self.request.clean )
		self.output( self.clean, "The request log has been cleaned up" )
		self.previous( self.main, ">>>" )
	
	#[Actions.configLoad()]: None
	def configLoad( self ):
		try:
			self.thread( "Reading configuration file", self.config.load )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if  not isinstance( self.config.settings, Object ):
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Actions.configSave()]: None
	def configSave( self ):
		try:
			self.thread( "Saving configuration file", self.config.save )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if  not isinstance( self.config.settings, Object ):
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Actions.direct()]: None
	def direct( self ):
		self.client.direct()
	
	#[Actions.download( String url )]: None
	def download( self, url ):
		if  not isinstance( url, str ):
			raise ValueError( "Invalid url parameter, value must be type str, {} passed".format( type( url ).__name__ ) )
		pass
	
	#[Actions.explore()]: None
	@logged
	def explore( self ):
		pass
	
	#[Actions.export( Profile profile, String profilename, Media media, String medianame, Int mediatype )]: None
	def export( self, profile=None, profilename=None, media=None, medianame=None, mediatype=None ):
		if  not isinstance( profile, Profile ) and \
			not isinstance( media, Media ):
			raise TypeError( "No data needs to be saved" )
		try:
			if  isinstance( profile, Profile ):
				if  not isinstance( profilename, str ):
					self.output( self.export, [
						"",
						"By default, Kanashī will save it in",
						"the ~/onsaved/exports/profile/ folder.",
						"To change it, please add a slash before",
						"the filename and without the .json",
						"",
						"e.g /sdcard/path/filename"
					])
					profilename = self.input( label := "~/{}".format( Config.ONSAVED.export.profile.format( profile.username ) ), default=profile.username )
				self.thread( f"Exporting profile info {profile.username}", lambda: profile.export( profilename ) )
				self.output( self.export, "Exported into {}".format( profilename if profilename[0] == "/" else label ) )
				if  isinstance( media, Media ):
					self.tryAgain( "Next save media [Y/n]", next=self.export( media=media, medianame=medianame, mediatype=mediatype ), other=lambda: self.profile( profile=profile ) )
				else:
					self.previous( lambda: self.profile( profile=profile ), ">>>" )
			if  isinstance( media, Media ):
				pass
		except Exception as e:
			self.emit( e )
			self.tryAgain( **{
				"next": lambda: self.export( **{
					"media": media,
					"medianame": medianame,
					"mediatype": mediatype,
					"profile": profile,
					"profilename": profilename
				}),
				"other": self.close
			})
	
	#[Actions.favorite( Profile profile )]: None
	@logged
	def favorite( self, profile ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile.isFeedFavorite:
			action = "Remove favorite"
		else:
			action = "Make favorite"
		try:
			favorite = self.thread( f"Trying to {action} {profile.username}", lambda: profile.favorite() )
		except Exception as e:
			raise ProfileError( "Unexpected error", prev=e, data={ "action": lambda: self.favorite( profile ) } )
		self.output( self.favorite, "Successfully {} {}".format( action, profile.username ) )
		self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Actions.follow( Profile profile, Bool ask )]: None
	@logged
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
			self.output( self.follow, output )
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
			self.output( self.follow, output )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Actions.inbox( Object inbox, Int order )]: None
	@logged
	def inbox( self, inbox=None, order=None ):
		if inbox == None:
			try:
				return self.inbox( inbox=Object( self.request.history[-1]['response']['content'] ) )
				return self.inbox( inbox=self.client.inbox() )
			except RequestError as e:
				self.emit( e )
				self.tryAgain( next=self.inbox, other=self.main )
		else:
			print( inbox )
	
	#[Actions.logout()]: None
	@logged
	def logout( self ):
		pass
	
	#[Actions.main()]: None
	def main( self ):
		pass
	
	#[Actions.pending( List<Object> pending )]: None
	@logged
	def pending( self, pending=None ):
		if  not isinstance( pending, list ):
			try:
				pending = self.thread( "Trying to get pending request follow", lambda: self.client.pending() )
				for i, v in enumerate( pending ):
					pending[i] = Object( v )
			except Exception as e:
				self.emit( e )
				if  not isinstance( e, RequestAuthError ):
					self.tryAgain( next=self.pending, other=self.main )
					return
		users = []
		for user in pending:
			users.append( user.username )
		self.output( self.pending, [
			"",
			"Select a user for the action,",
			"type iteration index or username",
			"",
			[ "@{}".format( user ) for user in users ]
		])
		select = self.input( None, default=[ "\\", *users, *[ str( i +1 ) for i in range( len( users ) ) ] ] )
		if  select != "\\":
			try:
				idx = int( select )
				user = users[( idx -1 )]
			except ValueError:
				user = select
			for u in pending:
				if  u.username == user:
					user = u
					break
			if  not user.isset( "id" ):
				user.id = user.pk
			prints = [ "", "Please select action for @{}".format( user.username ), "" ]
			action = self.action( info=False, prints=prints, actions={
				"profile": {
					"action": lambda: self.profile( username=user.username ),
					"output": "Visit Profile",
					"prints": "Visit profile account"
				},
				"approve": {
					"action": lambda: self.approve( user=user, approve=True ),
					"output": "Approve Request",
					"prints": "Approve request follow"
				},
				"ignore": {
					"action": lambda: self.approve( user=user, approve=False ),
					"output": "Ignore Request",
					"prints": "Ignore request follow"
				},
				"cancel": {
					"action": self.main,
					"output": "Cancel"
				}
			})
			action()
		else:
			self.main()
	
	#[Main.picture( Profile profile, String fname, Bool random )]: None
	def picture( self, profile, fname=None, random=False ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile['has_anonymous_profile_picture']:
			self.output( self.picture, "User has no profile picture" )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
		if  not isinstance( fname, str ) or not random:
			self.output( self.picture, [
				"",
				"By default Kanashī will save the profile photo",
				"in the ~/onsaved/medias/profile/ folder to",
				"change it please prefix the slash before the",
				"file name and don’t give the file extension",
				"",
				"e.g /sdcard/path/fo/filename"
			])
			default = "{} ({}) {}".format( profile.fullname, profile.username, profile.profilePictureHDResolution )
			fname = self.input( label := "~/{}".format( Config.ONSAVED.media.profile.format( default ) ), default=default )
			save = self.thread( "Saving profile picture {}".format( profile.username ), lambda: profile.profilePictureSave() )
			self.output( self.picture, "Saved on {}".format( fname ) )
			self.previous( lambda: self.profile( profile=profile ) )
	
	#[Actions.profile( String username, Profile profile )]: None
	@logged
	def profile( self, username=None, profile=None ):
		pass
	
	#[Actions.remove( Profile profile )]: None
	@logged
	def remove( self, profile ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		pass
	
	#[Actions.report( Profile profile )]: None
	@logged
	def report( self, profile ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		pass
	
	#[Actions.restrict( Profile profile, Bool ask )]: None
	@logged
	def restrict( self, profile, ask=True ):
		if  not isinstance( profile, Profile ):
			raise ValueError( "Invalid profile parameter, value must be type Profile, {} passed".format( type( profile ).__name__ ) )
		if  profile.restrictedByViewer == False and ask == True:
			self.output( self.restrict, [
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
			self.output( self.restrict, "Successfully {} {}".format( action, profile.username ) )
			self.previous( lambda: self.profile( profile=profile ), ">>>" )
	
	#[Actions.search()]: None
	@logged
	def search( self ):
		pass
	
	#[Actions.setting()]: None
	def setting( self ):
		pass
	
	#[Actions.signin( String username, String password, Dict|Object|String cookies, String browser, Object|Dict two_factor, Object|Dict verify Bool ask, Int flag )]: None
	def signin( self, 
			username=None, 
			password=None, 
			csrftoken=None, 
			cookies=None, 
			browser=None, 
			two_factor=None, 
			verify=None, 
			ask=True, 
			flag=0 
		):
		if  flag == 0:
			self.output( self.signin, [
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
				self.output( self.signin, [
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
				self.output( self.signin, [ "",
					"Username account required for login",
					"Please enter your account username"
				])
				username = self.input( "Username" )
			if  not isinstance( password, str ):
				self.output( self.signin, [ "",
					"Password account required for login",
					"Please enter the password carefully"
				])
				password = self.getpass( "Password" )
			self.signin( username, password, cookies, csrftoken, browser, True, 5 )
		elif flag == 2:
			if  not isinstance( cookies, str ) or \
				not isinstance( browser, str ):
				self.output( self.signin, [
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
			if  typedef( two_factor, dict ) or \
				typedef( two_factor, Object ):
				if  "cookies" not in two_factor:
					pass
				if  "headers" not in two_factor:
					pass
				if  "info" not in two_factor:
					pass
			else:
				return self.signin( username=username, password=password, browser=browser, two_factor={}, verify=verify, flag=3 )
			if  typedef( verify, dict, False ) and \
				typedef( verify, Object, False ):
				return self.signin( username=username, password=password, browser=browser, two_factor=two_factor, verify={}, flag=3 )
			if  "method" not in verify:
				handle = lambda method: self.signin(
					username=username,
					password=password,
					browser=browser,
					two_factor=two_factor,
					verify={
						"method": method
					},
					flag=3
				)
				action = self.action( **{
					"info": False,
					"prints": [
						"",
						"This method may not necessarily work, but it's",
						"also a good idea if you try to verify this",
						"",
						"Also make sure you have set your User-Agent with",
						"your own browser, don't use random",
						""
					],
					"actions": {
						"sent": {
							"action": lambda: handle( 0 ),
							"output": "Verify with code sent"
						},
						"backup": {
							"action": lambda: handle( 1 ),
							"output": "Verify with backup code",
							"prints": [
								"Verify 2 factor verification with code backup",
								"Use these when you can't access your device"
							]
						},
						"cancel": {
							"action": lambda: self.close( self.signin, "Close" ),
							"output": "Cancel verify"
						}
					}
				})
				return action()
			if  "code" not in verify:
				pass
		elif flag == 4:
			self.main()
		elif flag == 5:
			try:
				signin = self.thread( "Trying to SignIn your account", lambda: self.kanashi.signin( username, password, cookies, csrftoken, browser ) )
				if  signin.success == True:
					output = [
						"",
						"You have successfully logged in as \x1b[1;38;5;189m{}\x1b[0m".format( signin.signin.fullname if signin.signin.fullname else signin.signin.username ),
						"To use this tool again at a later time, Kanashī",
						"provides a feature to save login info, you can",
						"also log out at any time"
					]
					if  signin.remember:
						output = [ "", "Your login information is still valid", *output ]
					self.active = self.kanashi.active
					self.output( self.signin, output )
					save = self.input( "Save login info [Y/n]", default=[ "Y", "y", "N", "n" ] )
					if  save.upper() == "Y":
						self.configSave()
					self.main()
				elif signin.two_factor:
					output = [
						"",
						"Oops! It looks like your account has active",
						"two-factor security that needs to be verified",
						""
					]
					self.output( self.signin, output )
					self.tryAgain( **{
						"label": "Vefify 2FA [Y/n]",
						"other": lambda: self.close( self.signin, "Close" ),
						"next": lambda: self.signin(
							username=username,
							password=password,
							browser=browser,
							two_factor=signin.wo_factor,
							flag=3
						)
					})
				elif signin.checkpoint:
					print( f"Checkpoint: {signin.checkpoint}" )
					self.previous( lambda: self.close( self.signin, "Force close" ), ">>>" )
				else:
					self.output( self.signin, [
						"",
						"There was an error logging in",
						"This usually happens due to some unhandled",
						"things like, setting cookies and information",
						"after login",
						"",
						"Please report this issue"
					])
					self.previous( lambda: self.close( self.signin, "Force close" ), ">>>" )
			except Exception as e:
				self.emit( e )
				if  isinstance( e, UserError ) or \
					isinstance( e, RequestError ) and not \
					isinstance( e, RequestAuthError ):
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
					if  isinstance( e, RequestError ) and not \
						isinstance( e, RequestAuthError ) or \
						isinstance( e, PasswordError ) or \
						isinstance( e, UserNotFoundError ):
						self.tryAgain( **params )
						return
				if  isinstance( e, AuthError ) or \
					isinstance( e, RequestAuthError ):
					pass
				self.tryAgain( next=self.signin, other=self.main, ask=False, flag=flag )
		else:
			raise TypeError( "Unsupported login method" )
	
	#[Actions.support()]: None
	def support( self ):
		pass
	
	#[Actions.switch( Int|String select, Bool ask )]: None
	def switch( self, select=None, ask=True ):
		if  ask and self.kanashi.isActive:
			self.output( self.switch, [ "",
				"You have logged in as {}".format( self.active.fullname ),
				"You can choose an account that has logged",
				"in before or log in to another account"
			])
			self.tryAgain( "Switch account [Y/n]", next=self.switch, other=self.signin, ask=False )
		elif self.settings.signin.switch.len() >= 1:
			users = self.settings.signin.switch.keys()
			if  not isinstance( select, int ) and \
				not isinstance( select, str ):
				self.output( self.switch, [ "",
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
					self.output( self.switch, f"You are logged as \x1b[1;38;5;189m{self.kanashi.active.username}\x1b[0m" )
					self.active = self.kanashi.active
					self.previous( self.main, ">>>" )
				except Exception as e:
					if  isinstance( e, ConfigError ):
						self.active = self.kanashi.active
						self.output( self.switch, "Something wrong when update config" )
						self.tryAgain( next=self.configSave, other=self.main )
					else:
						self.emit( e )
						if  isinstance( e, RequestError ) and not \
							isinstance( e, RequestAuthError ):
							self.tryAgain( next=self.switch, other=self.main, select=select, ask=False )
						else:
							self.input( ">>>", default="" )
							if  isinstance( e, AuthError ) or \
								isinstance( e, RequestAuthError ):
								self.close( self )
							else:
								self.switch( ask=False )
				pass
			else:
				self.main()
		else:
			self.output( self.switch, [
				"No account saved in this device",
				"Want to add a new account or login?"
			])
			self.tryAgain( "Add new account [Y/n]", next=self.signin, other=self.main )
	

#[kanashi.main.Main]
class Main( Actions, Utility, RequestRequired ):
	
	#[Main.main()]: None
	def main( self ):
		
		action = self.action( actions={
			"profile": {
				"signin": True,
				"action": self.profile,
				"output": "Visit Profile",
				"prints": "Visit profile account"
			},
			"search": {
				"signin": True,
				"action": self.search,
				"output": "Search Anything",
				"prints": "Search posts, users, hashtags and more"
			},
			"direct": {
				"signin": True,
				"action": self.direct,
				"output": "Direct Inbox",
				"prints": "Display direct inbox messages"
			},
			"inbox": {
				"signin": True,
				"action": self.inbox,
				"output": "News Inbox",
				"prints": "Display news inbox notifications"
			},
			"pending": {
				"signin": True,
				"action": self.pending,
				"output": "Follow Pending",
				"prints": "Approve or ignore follow requests"
			},
			"explore": {
				"signin": True,
				"action": self.explore,
				"output": "Explore Media",
				"prints": "Explore recommended media"
			},
			"signin": {
				"signin": {
					"require": False,
					"include": False
				},
				"action": self.signin,
				"output": "SignIn Account",
				"prints": "SignIn with password or cookies"
			},
			"logout": {
				"signin": True,
				"action": self.logout,
				"output": "Logout Account",
				"prints": "Logout Instagram account"
			},
			"download": {
				"signin": True,
				"action": self.download,
				"output": "Download Media",
				"prints": "Download Instagram media"
			},
			"switch": {
				"action": self.switch,
				"allows": self.settings.signin.switch.len() >= 2 and self.authenticated or self.settings.signin.switch.len() >= 1 and not self.authenticated,
				"output": "Switch Account",
				"prints": [
					"Switch to another saved accounts"
				]
			},
			"setting": {
				"action": self.setting,
				"output": "Kanashī Settings",
				"prints": "Kanashī configuration settings"
			},
			"support": {
				"action": self.support,
				"output": "Support Project",
				"prints": "When this program is useful for you"
			},
			"clean": {
				"action": self.clean,
				"output": "Clear Response",
				"prints": "Clear the entire request record"
			},
			"about": {
				"action": self.about,
				"output": "About Kanashī",
				"prints": "e.g Authors, Version, License, etc"
			},
			"exit": {
				"action": lambda: self.exit( self.main, "Finish" ),
				"output": "Exit",
				"prints": [
					"Close the program",
					"Always use CTRL+D for shortcut"
				]
			}
		})
		action()
	
	#[Main.profile( String username, Profile profile )]: None
	@logged
	def profile( self, username=None, profile=None ):
		if  not isinstance( username, str ) and \
			not isinstance( profile, Profile ):
			self.output( self.profile, [ "",
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
					username = username.lower()
					if not username in self.profiles:
						profile = self.thread( f"Retrieve user info {username}", lambda: self.kanashi.client.profile( username=username ) )
						self.profiles[username] = profile
					else:
						profile = self.profiles[username]
				except Exception as e:
					self.emit( e )
					if  isinstance( e, AuthError ) or \
						isinstance( e, RequestAuthError ):
						pass
					if  isinstance( e, UserError ):
						self.tryAgain( next=self.profile, other=self.main )
					if  isinstance( e, RequestError ) and not \
						isinstance( e, RequestAuthError ):
						self.tryAgain( next=self.profile, other=self.main, username=username )
					else:
						self.previous( self.main, ">>>" )
					return
				self.profile( profile=profile )
			else:
				action = self.action( prints=profile.prints, info=False, actions={
					"block": {
						"signin": True,
						"action": lambda: self.block( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": profile.blockedByViewer,
						"output": [
							"Block User",
							"Unblock User"
						],
						"prints": "Block or unblok this user"
					},
					"bestie": {
						"follow": True,
						"signin": True,
						"action": lambda: self.bestie( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": profile.isBestie,
						"output": [
							"Make Bestie",
							"Remove Bestie"
						],
						"prints": "Make or remove this user as bestie"
					},
					"confirm": {
						"signin": True,
						"action": lambda: self.confirm( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": profile.requestedFollow,
						"output": "Confirm Request",
						"prints": "Confirm or ignore request follow from user"
					},
					"favorite": {
						"follow": True,
						"signin": True,
						"action": lambda: self.favorite( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": profile.isFeedFavorite,
						"output": [
							"Make Favorite",
							"Remove Favorite"
						],
						"prints": "Make or remove this user from favorite"
					},
					"follow": {
						"signin": True,
						"action": lambda: self.follow( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": [
							not profile.followedByViewer and not profile.requestedByViewer,
							profile.followedByViewer,
							profile.requestedByViewer
						],
						"output": [
							"Follow User",
							"Unfollow User",
							"Unrequest User"
						],
						"prints": "Follow, unfollow or cancel request follow"
					},
					"remove": {
						"signin": True,
						"action": lambda: self.remove( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": profile.followsViewer,
						"output": "Remove Follower",
						"prints": "Remove this user from follower list"
					},
					"report": {
						"signin": True,
						"action": lambda: self.report( profile=profile ),
						"allows": profile.isNotMySelf,
						"output": "Report User",
						"prints": "Report this user profile"
					},
					"muting": {
						"follow": True,
						"action": lambda: self.muting( profile=profile ),
						"allows": profile.isNotMySelf,
						"output": "Mute User",
						"prints": "Mute posts and stories from this user"
					},
					"restrict": {
						"signin": True,
						"action": lambda: self.restrict( profile=profile ),
						"allows": profile.isNotMySelf,
						"filter": profile.restrictedByViewer,
						"output": [
							"Restrict User",
							"Unrestrict User"
						],
						"prints": "Restrict or unrestrict this user"
					},
					"follows": {
						"signin": True,
						"action": lambda: self.follows( profile=profile ),
						"filter": profile.isPrivateAccount and profile.followedByViewer or profile.isPrivateAccount is False or profile.isMySelf,
						"output": "Profile Follows",
						"prints": "Gets user followers and following"
					},
					"mutuals": {
						"signin": True,
						"action": lambda: self.mutuals( profile=profile ),
						"allows": profile.isNotMySelf,
						"output": "Profile Mutuals",
						"prints": "Get mutual users from this user"
					},
					"suggest": {
						"signin": True,
						"action": lambda: self.suggest( profile=profile ),
						"allows": profile.isNotMySelf,
						"output": "Profile Suggest",
						"prints": "Gests suggested user from this user"
					},
					"medias": {
						"signin": True,
						"action": lambda: self.medias( profile=profile ),
						"filter": profile.isPrivateAccount and profile.followedByViewer or profile.isPrivateAccount is False or profile.isMySelf,
						"output": "Profile Media",
						"prints": "Gets media posts, reels, saveds, etc"
					},
					"picture": {
						"signin": True,
						"action": lambda: self.picture( profile=profile ),
						"output": "Profile Picture",
						"prints": "Download profile picture"
					},
					"export": {
						"signin": True,
						"action": lambda: self.export( profile=profile ),
						"output": "Export Profile",
						"prints": "Save profile info as json file"
					},
					"main": {
						"action": self.main,
						"output": "Back to Main"
					}
				})
				try:
					action()
				except ProfileError as e:
					self.emit( e.prev )
			pass
		pass
	