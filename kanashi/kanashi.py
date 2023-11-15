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
from pytz import utc as UTC
from re import findall, match
from typing import final

from kanashi.client import Client
from kanashi.config import Config
from kanashi.error import *
from kanashi.object import Object
from kanashi.pattern import Pattern
from kanashi.readonly import Readonly
from kanashi.request import (
	Cookies, 
	Headers, 
	Request, 
	RequestRequired
)
from kanashi.typing import *
from kanashi.utility import *


#[kanashi.kanashi.Kanashi]
class Kanashi( RequestRequired, Readonly, Utility ):
	
	#[Kanashi()]: None
	@final
	def __init__( self ) -> None:
		
		"""
		Construct method of class Kanashi

		:return None
		"""
		
		self.__except__:list[str] = [
			"__active__",
			"__caching__",
			"__cookies__",
			"__headers__",
			"__outputs__",
			"__request__",
			"__session__"
		]
		
		self.__caching__:Object = Object({
			"explore": None,
			"message": None,
			"notices": None,
			"pending": None,
			"profile": {},
			"searchs": {}
		})
		
		self.__config__:Config = Config( Config.FILENAME )
		self.configLoad()
		
		# Initialize Request Instance.
		self.__request__:Request = Request( history=True, timeout=self.settings.timeout )
		
		# Initialize Client Instance.
		self.__client__:Client = Client( config=self.config, request=self.request )
	
	#[Kanashi.about()]: None
	@final
	def about( self ) -> None:
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
					outputs.append( "\x20".join([ Config.LICENSE, Config.LICENSE_URL ]) )
					outputs = [
						*outputs,
						*Config.LICENSE_DOC
					]
			if  index < displayLength -1:
				outputs.append( "\x20" )
			pass
		self.output( self.about, [ *self.__outputs__, *outputs ] )
		self.previous( self.main, ">>>" )
	
	#[Kanashi.action( Str label, Dict actions, List prints, Bool info )]: Callable
	@final
	def action( self, label:str=None, actions:dict={}, prints:list=[], info:bool=True ) -> callable:
		
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
					"include": bool
						Filter if option must Even though the user has logged in
				},
				"output": List|Str,
					When value is list, filter must be available
				"prints": List|Str
					Output descriptions, this is optional
					When the value is String, it will transform to list
			}
		}
		"""
		
		outputs = []
		options = []
		
		# Default println outputs.
		self.__outputs__ = [
			"\x20",
			"Kanashī v{}\x1b[0m".format( Config.VERSION ),
			"\x20",
			"Author \x1b[1;38;5;254m{}\x1b[0m".format( Config.AUTHOR ),
			"Github \x1b[1m\x1b[4;37m{}\x1b[0m".format( Config.GITHUB ),
			"Issues \x1b[1m\x1b[4;37m{}\x1b[0m".format( Config.ISSUES ),
			"\x20"
		]
		
		if not isinstance( prints, list ): prints = [prints]
		if self.authenticated:
			self.__outputs__ = [
				*self.__outputs__[0:2],
				"Logged as \x1b[1;38;5;189m{}\x1b[0m".format( self.active.fullname if self.active.fullname else self.active.username ),
				*self.__outputs__[2:]
			]
		
		for option in actions.keys():
			action = actions[option]
			
			if "action" not in action or \
				not callable( action['action'] ): continue
			if "allows" in action and not action['allows']: continue
			if "follow" in action and not action['follow']: continue
			if "signin" in action:
				if isinstance( action['signin'], ( dict, Object ) ):
					if self.authenticated:
						if action['signin']['require'] is False or \
						   action['signin']['require'] is True and \
						   action['signin']['include'] is False: continue
					else:
						if action['signin']['require'] is True: continue
				else:
					if not self.authenticated and action['signin'] or self.authenticated and not action['signin']:
						continue
			
			if not "output" in action:
				continue
			if isinstance( action['output'], list ):
				if "filter" in action:
					if isinstance( action['filter'], list ):
						for i in range( len( action['filter'] ) ):
							if action['filter'][i] is True:
								action['output'] = action['output'][i]
								break
						if isinstance( action['output'], list ):
							action['output'] = action['output'][0]
					else:
						action['output'] = action['output'][bool( action['filter'] )]
			elif "filter" in action:
				if not action['filter']:
					continue
			options.append( option )
			outputs.append( action['output'] )
			if "prints" in action:
				if not isinstance( action['prints'], list ):
					action['prints'] = [action['prints']]
				outputs.append( action['prints'] )
		
		self.output( self.action, [ *self.__outputs__, *prints, outputs ] if info else [ *prints, outputs ] )
		option = self.input( label, number=True, default=[ idx +1 for idx in range( len( options ) ) ] )
		
		return actions[options[option -1 ]]['action']
	
	#[Kanashi.active]: Active
	@final
	@property
	def active( self ) -> Active: return self.client.active
	
	#[Kanashi.approve( User user, Bool approve, Bool confirm, Callable callback )]: None
	@final
	@logged
	@avoidForMySelf
	def approve( self, user:User, approve:bool=None, confirm:bool=None, callback:callable=None ) -> None:
		callback = callback if callable( callback ) else self.main
		if user is None:
			raise ValueError( "Parameter \"user\" required" )
		if approve is None:
			self.output( self.approve, "Do you want to accept this follow request?" )
			approve = self.input( "Approve [Y/n]", default=[ ">>>", "Y", "y", "N", "n" ] ).upper()
			if approve != ">>>":
				self.approve( user=user, callback=callback, approve=approve == "Y" )
			else:
				self.main()
		else:
			if confirm is None:
				self.output( self.approve, "For next action please confirm" )
				self.tryAgain( "Confirm [Y/n]", next=lambda: self.approve( user=user, approve=approve, confirm=True, callback=callback ), otheer=callback )
			else:
				action = "Approving" if approve is True else "Ignoring"
				display = user if isinstance( user ) else f"@{user}" if isinstance( user, str ) else user.id if "id" in user else user.pk
				try:
					friendship = self.thread( "{} request follow from {}".format( action, display ), lambda: self.client.approve( user=user, approve=approve ) )
					profiles = self.__profile__
					if friendship.id in profiles:
						profiles[friendship.id].set( friendship )
				except RequestError as e:
					self.emit( e )
					self.tryAgain( next=lambda: self.approve( user=user, approve=approve, confirm=True, callback=callback ), otheer=callback )
					return
				self.output( self.approve, f"Successfully {action} follow requests from {display}" )
				self.previous( callback )
	
	#[Kanashi.authenticated]: Bool
	@final
	@property
	def authenticated( self ) -> bool: return self.client.authenticated
	
	#[Kanashi.bestie( Profile profile, Bool ask )]: None
	@final
	@logged
	def bestie( self, profile, ask=True ) -> None:
		raise NotImplementedError( "Method {} is not initialized or implemented".format( self.bestie ) )
	
	#[Kanashi.cached]: Object
	@final
	@property
	def cached( self ) -> Object: return self.__caching__
	
	#[Kanashi.checkpoint( Str url, Request request, Cookies|Dict|Object|Str cookies, Dict|Headers headers, Int choices )]: None
	@final
	def checkpoint( self, url:str=None, request:Request=None, cookies:Cookies|dict|Object|str=None, headers:dict|Headers|Object=None, choices:int=0 ) -> None:
		if url is None:
			self.output( self.checkpoint, "Please input the Checkpoint URL" )
			url = self.input( "Checkppoint-URL" )
		if request is None:
			if cookies is None:
				cookies = {}
				for require in [ "csrftoken" ]:
					cookies[require] = self.input( require.capitalize() )
				next = self.input( "Add more [Y/n]", default=[ "Y", "y", "N", "n" ] )
				while next.upper() == "Y":
					cookie = self.input( "Cookie-Name" )
					values = self.input( "Cookie-Value" )
					next = self.input( "Add more [Y/n]", default=[ "Y", "y", "N", "n" ] )
					cookies[cookie] = values
			if headers is None:
				self.output( self.remember, "Want to add some additional headers" )
				next = self.input( "Add additonal header [Y/n]", default=[ "Y", "y", "N", "n" ] )
				while next.upper() == "Y":
					if headers == None:
						headers = {}
					header = self.input( "Header-Name" )
					values = self.input( "Header-Value" )
					next = self.input( "Add more [Y/n]", default=[ "Y", "y", "N", "n" ] )
					headers[header] = values
		
		challenge = self.thread( "Getting info of Checkpoint URL", self.client.checkpoint( url=url, request=request, cookies=cookies, headers=headers ) )
		print( challenge )
	
	#[Kanashi.choicer()]: Callable
	@final
	def choicer( self ) -> callable: ...
	
	#[Kanashi.clean()]: None
	@final
	def clean( self ) -> None:
		self.thread( "Clear request records", self.request.clean )
		self.output( self.clean, "The request log has been cleaned up" )
		self.previous( self.main, ">>>" )
	
	#[Kanashi.client]: Client
	@final
	@property
	def client( self ) -> Client: return self.__client__
	
	#[Kanashi.config]: Config
	@final
	@property
	def config( self ) -> Config: return self.__config__
	
	#[Kanashi.configLoad()]: None
	@final
	def configLoad( self ) -> None:
		try:
			self.thread( "Reading configuration file", self.config.load )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( "Create new [Y/n]", next=self.configSave )
		if not isinstance( self.config.settings, Object ):
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Kanashi.configSave( Str message )]: None
	@final
	def configSave( self, message:str=None ) -> None:
		try:
			self.thread( "Saving configuration file", self.config.save )
			self.output( self.configSave, message if message is not None else "Changes saved successfully" )
		except ConfigError as e:
			self.emit( e )
			self.tryAgain( next=self.configSave )
		if not isinstance( self.config.settings, Object ):
			self.close( e, "Operation cannot be continued" )
		pass
	
	#[Kanashi.configuration( Int flag )]: None
	@final
	def configuration( self, flag:int=0 ) -> None:
		if not isinstance( flag, int ):
			raise ValueError()
		if flag == 0:
			action = self.action( actions={
				"lists": {
					"action": lambda: self.configuration( flag=1 ),
					"output": "List available User-Agent"
				},
				"browser": {
					"action": lambda: self.configuration( flag=2 ),
					"output": "Change default User-Agent",
					"prints": [
						"This will only change the main",
						"configuration, this will not affect",
						"the configuration of the logged in account"
					]
				},
				"timeout": {
					"action": lambda: self.configuration( flag=3 ),
					"output": "Update request timeout",
					"prints": "Change default request timeouts"
				},
				"randoms": {
					"action": lambda: self.configuration( flag=4 ),
					"output": "Add or remove browser lists"
				},
				"cancel": {
					"action": lambda: self.main(),
					"output": "Cancel",
					"prints": "Back to main"
				}
			})
			action()
		elif flag == 1:
			self.output( self.configuration, [ "", self.settings.browser.randoms ] )
			self.previous( self.configuration, ">>>" )
		elif flag == 2:
			self.output( self.configuration, "Please enter the User-Agent that you will use as default" )
			self.settings.browser.default = self.input( "User-Agent" )
			self.configSave( "Default User-Agent has updated" )
			self.previous( self.configuration, ">>>" )
		elif flag == 3:
			self.output( self.configuration, "Please enter the request timeouts" )
			self.settings.timeout = self.input( "Timeout", number=True, default=self.settings.timeout )
			self.request.timeout = self.settings.timeout
			self.configSave( "Default request timeouts has updated" )
			self.previous( self.configuration, ">>>" )
		elif flag == 4:
			self.output( self.configuration, [
				"\nPlease select action:\n", [
					"List of User-Agent", [
						"Display available User-Agent"
					],
					"Add User-Agent", [
						"Add new User-Agent into lists"
					],
					"Remove User-Agent", [
						"Remove User-Agent from lists"
					],
					"Cancel", [
						"Back to before"
					]
				]
			])
			select = self.input( "Action", number=True, default=[ 1, 2, 3 ] )
			match select:
				case 1 | 2:
					next = "Y"
					if select == 1:
						while next.upper() == "Y":
							browser = self.input( "New User-Agent" )
							self.settings.browser.randoms.append( browser )
							next = self.input( "Add more [Y/n]", default=[ "Y", "y", "N", "n" ] )
					else:
						while next.upper() == "Y":
							self.output( self.configuration, [ "\nAvailable User Agents", self.settings.browser.randoms ])
							remove = self.input( "Remove User-Agent", number=True, default=[ idx +1 for idx in range( len( self.settings.browser.randoms ) ) ] )
							remove-= 1
							try:
								del self.settings.browser.randoms[remove]
								next = self.input( "Delete more [Y/n]", default=[ "Y", "y", "N", "n" ] )
							except IndexError:
								pass
					self.configSave( "User-Agent has updated" )
					self.previous( self.configuration, ">>>" )
				case 3:
					self.configuration()
		elif flag == 4:
			self.main()
		else:
			self.configuration()
	
	#[Kanashi.cookie()]: None
	@final
	@logged
	def cookie( self ) -> None:
		cookies = [ "Your current login session cookies\n" ]
		for cookie in self.cookies.keys():
			cookies.append( "{}: \"{}\"".format( cookie, str( self.cookies[cookie] ).replace( "\"", "\\\"" ) ) )
		self.output( self.cookie, cookies )
		self.previous( self.main, ">>>" )
	
	#[Kanashi.destruct()]: None
	@final
	@logged
	def destruct( self, default:bool=False ) -> None:
		self.__client__.destruct( default=default )
		self.__request__ = self.client.request
		self.__caching__ = Object({
			"explore": None,
			"message": None,
			"notices": None,
			"pending": None,
			"profile": {},
			"searchs": {}
		})
	
	#[Kanashi.direct( Int flag )]: None
	@final
	@logged
	def direct( self, flag:int=0 ) -> None:
		if self.cached.message is None:
			try:
				self.cached.message = self.thread( "Getting direct message inbox", lambda: self.client.direct() )
			except RequestError as e:
				self.emit( e )
				self.tryAgain( next=self.direct, other=self.main )
				return
		if flag == 1:
			prints = []
			direct = self.cached.message
			for thread in direct.inbox.threads:
				online = datetime.fromtimestamp( int( thread.last_seen_at[thread.last_seen_at.keys()[0]].timestamp ) / 1000000 )
				prints.append( "{} \u00b7 {}".format( thread.thread_title, f"@{thread.users[0].username}" if thread.users[0].full_name else thread.users[0].pk ) )
				prints.append([ "Last seen at {}-{}-{} {}:{}".format(
					online.year, 
					online.month, 
					online.day, 
					online.hour, 
					online.minute
				)])
			self.output( self.direct, [ 
				"\nList of direct threads message inbox",
				"Please input >>> for back to before\n",
				prints
			])
			select = self.input( "Select", default=[ ">>>", *[ str( idx+1 ) for idx in range( len( direct.inbox.threads ) ) ] ] )
			if select != ">>>":
				thread = direct.inbox.threads[int( select ) -1]
				online = datetime.fromtimestamp( int( thread.last_seen_at[thread.last_seen_at.keys()[0]].timestamp ) / 1000000 )
				action = self.action(
					info=False,
					prints=[
						"\nInviter is @{}".format( thread.inviter.username ),
						"Thread direct message of {} \u00b7 {}".format( thread.thread_title, f"@{thread.users[0].username}" if thread.users[0].full_name else thread.users[0].pk ),
						"This user is possible scammer {}".format( thread.users[0].is_possible_bad_actor.is_possible_scammer ),
						"Last seen at {}-{}-{} {}:{}\n".format(
							online.year, 
							online.month, 
							online.day, 
							online.hour, 
							online.minute
						)
					],
					actions={
						"profile": {
							"signin": True,
							"action": lambda: self.profile( thread.users[0].username if thread.users[0].full_name else thread.users[0].pk ),
							"filter": len( thread.users[0].full_name ) >= 1,
							"output": "Visit Profile",
							"prints": "Visit profile user"
						},
						"cancel": {
							"action": lambda: self.direct( flag=1 ),
							"output": "Cancel"
						}
					}
				)
				action()
			else:
				self.direct()
		elif flag == 2:
			direct = self.cached.message
			try:
				resume = self.thread( "Getting direct message inbox", lambda: self.client.direct( cursor=direct.inbox.next_cursor.cursor_thread_v2_id ) )
				direct.pending_requests_total = resume.pending_requests_total
				direct.snapshot_at_ms = resume.snapshot_at_ms
				direct.inbox.set({
					"has_older": resume.inbox.has_older,
					"next_cursor": resume.inbox.next_cursor,
					"prev_cursor": resume.inbox.prev_cursor,
					"unseen_count": resume.inbox.unseen_count,
					"unseen_count_ts": resume.inbox.unseen_count_ts,
				})
				for thread in resume.inbox.threads:
					direct.inbox.threads.append( thread )
			except RequestError as e:
				self.emit( e )
				self.tryAgain( next=lambda: self.direct( flag=2 ), other=self.direct() )
				return
			self.direct()
		else:
			direct = self.cached.message
			action = self.action( 
				info=False,
				prints=[
					"\nTotal direct threads message inbox is {}".format( len( direct.inbox.threads ) ),
					"Total direct pending request message is {}\n".format( direct.pending_requests_total )
				],
				actions={
					"display": {
						"signin": True,
						"action": lambda: self.direct( flag=1 ),
						"filter": len( direct.inbox.threads ) >= 1,
						"output": "Display Direct",
						"prints": "Display all direct threads message inbox"
					},
					"resume": {
						"signin": True,
						"action": lambda: self.direct( flag=2 ),
						"filter": direct.inbox.next_cursor.cursor_thread_v2_id is not None,
						"output": "Resume Cursor",
						"prints": "Resume next page direct message"
					},
					"cancel": {
						"action": self.main,
						"output": "Cancel"
					}
				}
			)
			action()
	
	#[Kanashi.download( Str url, Str save, Callable callback )]: None
	@final
	@logged
	def download( self, url:str, save:str=None, callback:callable=None ) -> None:
		callback = callback if callable( callback ) else self.main
		raise NotImplementedError( "Method {} is not initialized or implemented".format( self.download ) )
	
	#[Kanashi.explore( int flag )]: None
	@final
	@logged
	def explore( self, flag:int=0 ) -> None:
		self.cached.explore = Explore( File.json( "requests/api/v1/discover/web/explore_grid/response 2023-10-29 23:07:32.419220.json" )['response']['content'] )
		explore = self.cached.explore
		try:
			if flag == 1:
				prints = []
				for section in explore.sectional_items:
					prints.append( Text.fromSnakeToTitle( section.layout_type ) )
					prints.append([
						f"Feed type is {section.feed_type}",
						f"Aspect ratio is {section.explore_item_info.aspect_ratio}",
						f"Number of columns {section.explore_item_info.num_columns}"
					])
				self.output( self.explore, [
					"\nList of sectional explore items",
					"Please input >>> for back to before\n",
					prints
				])
				select = self.input( "Section", default=[ ">>>", *[ str( idx+1 ) for idx in range( len( explore.sectional_items ) ) ] ] )
				if select != ">>>":
					section = explore.sectional_items[( int( select ) -1 )]
					layout = section.layout_content;
					self.output( self.explore, [
						"Please select the action:\n", [
							"Layout Clips", [
								"Display layout clip items"
							],
							"Layout Items", [
								"Display layout content fill items"
							],
							"Cancel", [
								"Back to previous"
							]
						]
					])
					select = self.input( "Layout", default=[ 1, 2, 3 ], number=True )
					if select == 1:
						self.media( media=layout.one_by_two_item.clips.items[0].media, callback=lambda: self.explore( flag=1 ) )
					elif select == 2:
						self.media( media=layout.fill_items, callback=lambda: self.explore( flag=1 ) )
					else:
						self.explore( flag=1 )
				else:
					self.explore()
					all
			elif flag == 2:
				self.output( self.explore, f"Session paging token: \"{explore.session_paging_token}\"" )
				self.previous( self.explore, ">>>" )
			elif flag == 3:
				self.cached.explore = self.thread( "Getting contents from exploration", lambda: self.client.explore() )
				self.explore()
			elif flag == 4:
				if explore.more_available is False:
					self.output( self.explore, "Next page is not available" )
					self.tryAgain( "Refresh page [Y/n]", lambda: self.explore( flag=3 ), self.explore )
				else:
					refresh = self.thread( "Resume getting contents from exploration", lambda: self.client.explore( maxId=explore.max_id ) )
					explore.auto_load_more_enabled = refresh.auto_load_more_enabled
					explore.clusters = refresh.clusters
					explore.more_available = refresh.more_available
					explore.next_max_id = refresh.next_max_id
					explore.max_id = refresh.max_id
					explore.session_paging_token = refresh.session_paging_token
					explore.rank_token = refresh.rank_token
					explore.ranked_time_in_seconds = refresh.ranked_time_in_seconds
					for item in refresh.sectional_items:
						explore.sectional_items.append( item )
					self.output( self.explore, "The explore items section has been updated" )
					self.previous( self.explore, ">>>" )
			else:
				if explore is not None:	
					action = self.action( 
						info=False, 
						prints=[
							"\nAutoload more contents is {}:{}".format( explore.next_max_id, "available" if explore.more_available else "unavailable" ),
							"Please select the action:\n",
						], 
						actions={
							"display": {
								"singin": True,
								"action": lambda: self.explore( flag=1 ),
								"output": "Display Explore",
								"prints": "Display all sectional items"
							},
							"pagging": {
								"signin": True,
								"action": lambda: self.explore( flag=2 ),
								"output": "Session Token",
								"prints": "Display session paging token"
							},
							"refresh": {
								"signin": True,
								"action": lambda: self.explore( flag=3 ),
								"output": "Refresh Page",
								"prints": "Refresh items of explore"
							},
							"resume": {
								"singin": True,
								"action": lambda: self.explore( flag=4 ),
								"filter": explore.more_available,
								"output": "Resume Page",
								"prints": "Resume next page request of explore"
							},
							"cancel": {
								"action": self.main,
								"output": "Cancel"
							}
						}
					)
					action()
				else:
					self.explore( flag=3 )
		except RequestError as e:
			self.emit( e )
			self.tryAgain( next=lambda: self.explore( flag=flag ), other=self.main )
	
	#[Kanashi.inbox( Int flag, Bool next )]: None
	@final
	@logged
	def inbox( self, flag:int=0, next:bool=False ) -> None:
		self.cached.notices = Inbox( File.json( "/home/be-arisetiawan/Documents/self/personal/coding/Python/Kanashi/requests/api/v1/news/inbox/response 2023-10-29 16:58:14.218894.json" )['response']['content'] )
		try:
			if self.cached.notices is None:
				self.cached.notices = self.thread( "Getting notification inbox", self.client.inbox )
			elif self.cached.notices.continuation_token is not None and next is True:
				notice = self.thread( "Resume getting notification inbox", lambda: self.client.inbox( continuationToken=self.cached.notices.continuation_token ) )
				for key in notice.keys():
					if key == "priority_stories" or \
					key == "new_stories" or \
					key == "old_stories":
						for item in notice[key]:
							self.cached.notices[key].append( item )
					else:
						if key in self.cached.notices.__items__:
							self.cached.notices[key] = notice[key]
		except RequestError as e:
			if not isinstance( e, AuthError ):
				self.emit( e )
				self.tryAgain( next=lambda: self.inbox( flag=flag, next=next ), other=self.main )
		inbox = self.cached.notices
		if flag == 1:
			prints = []
			if len( inbox.priority_stories ) >= 1:
				prints.append( "\x20" )
				prints.append([])
				for story in inbox.priority_stories:
					prints[1].append( story.args.text )
			else:
				prints.append( "No recent priority notification updates" )
			self.output( self.inbox, prints )
			self.previous( self.inbox, ">>>" )
		elif flag == 2:
			prints = []
			if len( inbox.new_stories ) >= 1:
				prints.append( "\x20" )
				prints.append([])
				for story in inbox.new_stories:
					prints[1].append( story.args.text )
			else:
				prints.append( "No recent notification updates" )
			self.output( self.inbox, prints )
			self.previous( self.inbox, ">>>" )
		elif flag == 3:
			prints = []
			if len( inbox.old_stories ) >= 1:
				prints.append( "\x20" )
				prints.append([])
				for story in inbox.old_stories:
					prints[1].append( story.args.text )
			else:
				prints.append( "No notifications" )
			self.output( self.inbox, prints )
			self.previous( self.inbox, ">>>" )
		else:
			prints = [
				"\nYour Instagram notifications",
				"Last checked notification is {}\n".format( datetime.fromtimestamp( inbox.last_checked, tz=UTC ) )
			]
			counts = inbox.counts
			for key in counts.keys():
				prints.append( "  [{}] => {}".format( counts[key], Text.fromSnakeToTitle( key ) ) )
			prints.append( "\nPlease select action" )
			action = self.action( info=False, prints=prints, actions={
				"top": {
					"action": lambda: self.inbox( flag=1 ),
					"output": "Priority Notification",
					"prints": "Display all priority notifications"
				},
				"new": {
					"action": lambda: self.inbox( flag=2 ),
					"output": "Updated Notification",
					"prints": "Display all updated notifications"
				},
				"old": {
					"action": lambda: self.inbox( flag=3 ),
					"output": "Old Notification",
					"prints": "Display all old notifications"
				},
				# "next": {
				# 	"filter": not inbox.is_last_page,
				# 	"action": lambda: self.inbox( next=True ),
				# 	"output": "Resume Page",
				# 	"prints": "Resume next page request of notifications"
				# },
				"main": {
					"action": self.main,
					"output": "Cancel"
				}
			})
			action()
		...
	
	#[Kanashi.logout()]: None
	@final
	@logged
	def logout( self ) -> None:
		raise NotImplementedError( "Method {} is not initialized or implemented".format( self.logout ) )
	
	#[Kanashi.main()]: None
	def main( self ) -> None:
		raise NotImplementedError( "Method {} is not initialized or implemented".format( self.main ) )
	
	#[Kanashi.media( List<Media>|Media|Profile|User media, Int|Str target, Callable callback, Media.Type|Media.Type ftype )]: None
	@final
	@logged
	def media( self, media:list[Media]|Media|Profile|User=None, target:int|str=None, ftype:Media.Type|Story.Type=None, callback:callable=None ) -> None:
		callback = callback if callable( callback ) else self.main
		if media is None:
			if target is None:
				self.output( self.media, "Please enter the media ID or URL" )
				while media is None:
					media = self.input( "Media" )
					capture = match( Pattern.MEDIA, media )
					if capture is not None:
						groups = capture.groupdict()
						if "id" in groups and groups['id']:
							self.output( self.media, [
								"\nLooks like you have entered your ID",
								"but Kanashi doesn't know what ID it is\n", [
									"Post", [
										"Primary key for Instagram posts"
									],
									"Reels", [
										"Primary key for Instagram reel video"
									],
									"Story Highlight", [
										"The primary key of the story is highlighted"
									],
									"Story Timeline", [
										"The primary key of the tray reel timeline story"
									],
									"User", [
										"Instagram user primary key profile"
									],
									"Cancel", [
										"Cahnge Id"
									]
								]
							])
							select = self.input( "Type", defaulty=[ 1, 2, 3, 4, 5, 6 ], number=True )
						else:
							...
						# Add Handle for check Id type
					else:
						media = None
				...
			try:
				media = self.thread( f"Getting media info from {media}", lambda: self.client.media( target=target, flag=ftype ) )
			except RequestError as e:
				self.emit( e )
				self.tryAgain( next=lambda: self.media( target=target, callback=callback ), other=callback )
		elif isinstance( media, list ):
			if len( media ) >= 1:
				if all( isinstance( item, Media ) for item in media ):
					item = media[0]
					if isinstance( item, ExploreFillItem ):
						self.media( media=[ item.media for item in media ], callback=callback )
					elif isinstance( item, ExploreFillMedia ):
						structs = []
						length = len( media )
						for i in range( length ):
							item = media[i]
							struct = { f"{i+1}:{item.pk}": f"Owner @{item.owner.username}" }
							struct['Algorithm'] = "\x1b[1;37m{}\x1b[0m".format( Text.fromSnakeToTitle( item.algorithm ) )
							struct['Comercial'] = "\x1b[1;37m{}\x1b[0m".format( Text.fromSnakeToTitle( item.commerciality_status ) )
							struct['Interface'] = "https://www.instagram.com/p/{}".format( item.code )
							if item.caption:
								if item.caption.text:
									struct['Created'] = datetime.fromtimestamp( item.caption.created_at, tz=UTC )
									struct['Caption'] = []
									struct['Entity'] = {
										"Hashtag": [ f"#{hashtag}" for hashtag in findall( Pattern.HASHTAG_MULTILINE, item.caption.text ) ],
										"Users": [ f"@{user}" for user in findall( Pattern.USERNAME_MULTILINE, item.caption.text ) ]
									}
									parts = item.caption.text.split( "\x0a" )
									for part in parts:
										if len( part ) <= 0:
											struct['Caption'].append( "\x20" ); continue
										for u in range( 0, len( part ), 90 ):
											struct['Caption'].append( part[u:u+90] )
									if i != ( length -1 ):
										struct['Caption'] = "\x0a\u2502\x20\x20\x20\u2502\x20\x20\x20{}".format( "\x20" *4 ).join( struct['Caption'] )
									else:
										struct['Caption'] = "\x0a\x20\x20\x20\x20\u2502\x20\x20\x20{}".format( "\x20" *4 ).join( struct['Caption'] )
							structs.append( struct )
						self.output( self.media, [
							"\nList of fill Instagram media explore",
							"Please input >>> for back to before\n",
							tree( structs )
						])
						select = self.input( "Media", default=[ ">>>", *[ str( idx+1 ) for idx in range( length ) ] ] )
						if select != ">>>":
							self.media( media=media[( int( select ) -1 )], callback=lambda: self.media( media=media, callback=callback ) )
						else:
							callback()
					elif isinstance( item, ExploreClipItem ):
						self.media( media=item.media, callback=callback )
					else:
						self.output( self.media, "Unhandled and unsupported media type of item {}".format( typeof( item ) ) )
						self.previous( callback, ">>>" )
				else:
					self.output( self.media, "Unhandled and unsupported item type {}".format( typeof( media ) ) )
					print( repr( media[0] ) )
					self.previous( callback, ">>>" )
			else:
				self.output( self.media, "No media available" )
				self.previous( callback, ">>>" )
		elif isinstance( media, Media ):
			if isinstance( media, ExploreClipMedia ):
				struct = {}
				self.output( self.media, [
					tree([ struct ])
				])
			elif isinstance( media, ExploreFillMedia ):
				struct = { f"{media.pk}": f"Owner @{media.owner.username}" }
				struct['Algorithm'] = "\x1b[1;37m{}\x1b[0m".format( Text.fromSnakeToTitle( media.algorithm ) )
				struct['Comercial'] = "\x1b[1;37m{}\x1b[0m".format( Text.fromSnakeToTitle( media.commerciality_status ) )
				struct['Interface'] = "https://www.instagram.com/p/{}".format( media.code )
				if media.caption:
					if media.caption.text:
						struct['Caption'] = []
						struct['Entity'] = {
							"Hashtag": [ f"#{hashtag}" for hashtag in findall( Pattern.HASHTAG_MULTILINE, media.caption.text ) ],
							"Users": [ f"@{user}" for user in findall( Pattern.USERNAME_MULTILINE, media.caption.text ) ]
						}
						parts = media.caption.text.split( "\x0a" )
						for part in parts:
							if len( part ) <= 0:
								struct['Caption'].append( "\x20" ); continue
							for u in range( 0, len( part ), 90 ):
								struct['Caption'].append( part[u:u+90] )
						struct['Caption'] = "\x0a\u2502\x20\x20\x20\x20\x20\x20".join( struct['Caption'] )
				action = self.action(
					info=False,
					prints=[
						"\nPost from {}".format( f"\x1b[1;38;5;189m{media.owner.full_name}\x1b[0m {ITP} @{media.owner.username}" if media.owner.full_name else f"@{media.owner.username}" ),
						"Created at {}\n".format( datetime.fromtimestamp( media.caption.created_at, tz=UTC ) ),
						tree( struct )
					],
					actions={
					}
				)
			else:
				self.output( self.media, "Unhandled and unsupported media type {}".format( typeof( media ) ) )
				self.previous( callback, ">>>" )
		elif isinstance( media, User ):
			if isinstance( media, Profile ):
				...
		else:
			raise TypeError( "Invalid \"media\" parameter, value must be type List<Media>|Media|Profile|User, {} passed".format( typeof( media ) ) )
	
	#[Kanashi.pending( Int flag, Bool next )]: None
	@final
	@logged
	def pending( self, flag:int=0, next:str=False ) -> None:
		try:
			if self.cached.pending is None:
				self.cached.pending = self.thread( "Getting pending follow request", self.client.pending )
			elif self.cached.pending.nextMaxId is not None and next is True:
				pending = self.thread( "Resume getting pending follow requests", lambda: self.client.pending( nextMaxId=self.cached.pending.nextMaxId ) )
				for key in pending.key():
					if key == "friend_requests":
						for friend in pending.friendRequests:
							self.cached.pending.friend_requests.append( friend )
					elif key == "suggestions":
						for suggest in pending.suggestions:
							for user in self.cached.pending.suggestions:
								if user.id == suggest.id:
									continue
							self.cached.pending.suggestions.append( suggest )
					elif key == "users":
						for user in pending.users:
							self.cached.pending.suggestions.append( user )
					elif key in self.cached.pending.__items__:
						self.cached.pending[key] = pending[key]
		except RequestError as e:
			self.emit( e )
			self.tryAgain( next=lambda: self.pending( flag=flag, next=next ), other=self.main )
			return
		pending = self.cached.pending
		if flag == 1:
			prints = []
			for user in pending.users:
				prints.append( f"{user.full_name} @{user.username}" if user.full_name else f"@{user.username}" )
				prints.append([
					f"ID {user.pk}"
				])
			self.output( self.story, [
				"\nAll requests following you are pending",
				"Please input >>> for back to before\n",
				prints
			])
			select = self.input( "Select", default=[ ">>>", *[ str( idx +1 ) for idx in range( len( pending.users ) ) ] ] )
			if select != ">>>":
				profile = pending.users[( int( select ) -1 )]
				select = self.input( "Approve [Y/]", default=[ ">>>", "Y", "y", "N", "n" ] ).upper()
				if select == ">>>":
					self.pending( flag=1 )
				self.approve( user=profile, approve= select == "Y" )
			else:
				self.pending()
		elif flag == 2:
			...
		elif flag == 3:
			...
		elif flag == 4:
			...
		elif flag == 5:
			...
		elif flag == 6:
			...
		else:
			prints = [ "" ]
			for countable in [ "friend_requests", "suggestions", "users" ]:
				prints[0] += "  [{}] => {}\n".format( len( self.cached.pending[countable] ), Text.fromSnakeToTitle( countable ) )
			prints.append( "Please select action" )
			action = self.action( info=False, prints=[ "Your Instagram pending request follow\n", *prints ], actions={
				"follow": {
					"signin": True,
					"action": lambda: self.pending( flag=1 ),
					"filter": len( self.cached.pending.users ) >= 1,
					"output": "Follow Requests",
					"prints": "Display all request follow from users"
				},
				"friend": {
					"signin": True,
					"action": lambda: self.pending( flag=2 ),
					"output": "Friend Requests",
					"prints": "I don't know what is this,..."
				},
				"suggest": {
					"signin": True,
					"action": lambda: self.pending( flag=3 ),
					"output": "Suggested Users",
					"prints": "Display all suggestion users if available"
				},
				"next": {
					"signin": True,
					"action": lambda: self.pending( next=True ),
					"filter": self.cached.pending.nextMaxId is not None,
					"output": "Fetch next page pending requests"
				},
				"main": {
					"action": self.main,
					"output": "Cancel"
				}
			})
			action()
	
	#[Kanashi.profile( Int|Str username, Profile profile )]: None
	@logged
	def profile( self, username:int|str=None, profile:Profile=None ) -> None:
		raise NotImplementedError( "Method {} is not initialized or implemented".format( self.profile ) )
	
	#[Kanashi.remember( Str browser, Cookies|Dict|Object|Str cookies, Dict|Headers|Object headers )]: SignIn
	@final
	def remember( self, browser:str=None, cookies:Cookies|dict|Object|str=None, headers:dict|Headers|Object=None ) -> None:
		if browser is None:
			self.output( self.remember, "Please input your Browser User-Agent" )
			browser = self.input( "Browser", default=self.settings.browser.default )
		elif not isinstance( browser, str ):
			raise TypeError( "Invalid \"browser\" parameter, value must be type Str, {} passed".format( typeof( browser ) ) )
		if cookies is None:
			self.output( self.remember, [
				"\nChoose the option that suits you:\n", [
					"Manual Cookies", [
						"If you want to add cookies one by one"
					],
					"Raw Cookies", [
						"If you use raw cookies from Instagram"
					]
				]
			])
			select = self.input( self.remember, default=[ 1, 2 ], number=True )
			if select == 1:
				next = "Y"
				cookies = {}
				while next.upper() == "Y":
					ckey = self.input( "Cookie-Name" )
					cval = self.input( "Cookie-Value" )
					next = self.input( "Add more [Y/n]", default=[ "Y", "y", "N", "n" ] )
					cookies[ckey] = cval
			else:
				cookies = self.input( "Cookie-Raw" )
		elif not isinstance( cookies, ( Cookies, dict, Object, str ) ):
			raise TypeError( "Invalid \"cookies\" parameter, value must be type Cookies|Dict|Object|Str, {} passed".format( typeof( cookies ) ) )
		if headers is None:
			self.output( self.remember, "Want to add some additional headers" )
			next = self.input( "Add additonal header [Y/n]", default=[ "Y", "y", "N", "n" ] )
			while next.upper() == "Y":
				if headers == None:
					headers = {}
				hkey = self.input( "Header-Name" )
				hval = self.input( "Header-Value" )
				next = self.input( "Add more [Y/n]", default=[ "Y", "y", "N", "n" ] )
				headers[hkey] = hval
		elif not isinstance( headers, ( dict, Headers, Object ) ):
			raise TypeError( "Invalid \"browser\" parameter, value must be type Dict|Headers|Object, {} passed".format( typeof( headers ) ) )
		try:
			signin = self.thread( "Validates login credential recall", lambda: self.client.remember( browser=browser, cookies=cookies, headers=headers ) )
		except Throwable as e:
			self.emit( e )
			if isinstance( e, AuthError ):
				self.previous( self.main, ">>>" )
			else:
				self.tryAgain( other=self.main, next=lambda: self.remember( browser=browser, cookies=cookies, headers=headers ) )
			return
		if signin.authenticated:
			self.output( self.remember, f"Credentials are still valid, success considering @{signin.user.username}" )
			self.client.activate( signin.user )
			self.__request__ = self.client.request
			save = self.input( "Save login credentials [Y/n]", default=[ "Y", "y", "N", "n" ] )
			if save.upper() == "Y":
				self.settings.signin.switch[signin.user.username] = signin.user
				default = self.input( "Set as default [Y/n]", default=[ "Y", "y", "N", "n" ] )
				if default.upper() == "Y":
					self.settings.signin.active = signin.user.username
				self.configSave( "Changes have been saved" )
			self.previous( self.main, ">>>" )
		else:
			self.tryAgain( next=self.remember, other=self.main )
	
	#[Kanashi.search()]: None
	@logged
	def search( self ) -> None:
		raise NotImplementedError( self.search )
	
	#[Kanashi.setting()]: None
	@logged
	def setting( self ): None
	
	#[Kanashi.settings]: Setting
	@final
	@property
	def settings( self ) -> Settings: return self.config.settings
	
	#[Kanashi.signin( Str browser, String username, String password, Bool ask )]: None
	@final
	def signin( self, browser:str=None, username:str=None, password:str=None, ask=True ) -> None:
		if ask is True:
			self.output( self.signin, "Never use your main account to log in" )
			self.tryAgain( "Next login [Y/n]", next=lambda: self.signin( ask=False ), other=self.main )
		else:
			if browser is None:
				self.output( self.signin, "Please input your Browser User-Agent" )
				browser = self.input( "Browser", default=self.settings.browser.default )
			elif not isinstance( browser, str ):
				raise TypeError( "Invalid \"browser\" parameter, value must be type Str, {} passed".format( typeof( browser ) ) )
			if username is None:
				self.output( self.signin, "Please input your Instagram Username" )
				username = self.input( "Username" )
			elif not isinstance( username, str ):
				raise TypeError( "Invalid \"username\" parameter, value must be type Str, {} passed".format( typeof( username ) ) )
			if password is None:
				self.output( self.signin, "Please input your Instagram Password" )
				password = self.getpass( "Password" )
			elif not isinstance( password, str ):
				raise TypeError( "Invalid \"password\" parameter, value must be type Str, {} passed".format( typeof( password ) ) )
			try:
				signin = self.thread( "Trying to signin your account", lambda: self.client.signin( browser=browser, username=username, password=password ) )
			except Throwable as e:
				self.emit( e )
				if isinstance( e, PasswordError ):
					next=lambda: self.signin( browser=browser, username=username, ask=False )
				else:
					next=lambda: self.signin( browser=browser, ask=False )
				self.tryAgain( next=next, other=self.main )
			if signin.authenticated:
				self.output( self.signin, f"Successfully logged in as {signin.user.username}" )
				self.client.activate( signin.user, signin.request )
				self.__request__ = self.client.request
				save = self.input( "Save login credentials [Y/n]", default=[ "Y", "y", "N", "n" ] )
				if save.upper() == "Y":
					self.settings.signin.switch[signin.user.username] = signin.user
					default = self.input( "Set as default [Y/n]", default=[ "Y", "y", "N", "n" ] )
					if default.upper() == "Y":
						self.settings.signin.active = signin.user.username
					self.configSave( "Changes have been saved" )
				self.previous( self.main, ">>>" )
			elif "checkpoint" in signin:
				self.output( self.signin, [
					"\nYour account has been checkpoint:\n", [
						"Bypass Checkpoint", [
							"Note that this method may not necessarily work",
							"But it will be better if you try it"
						],
						"Login to another account",
						"Back to main"
					]
				])
				select = self.input( "Checkpoint", number=True, default=[ 1, 2, 3 ] )
				if select == 1:
					self.checkpoint( url=signin.checkpoint.checkpoint_url, request=signin.request )
				elif select == 2:
					self.signin( ask=False )
				else:
					self.main()
			elif "two_factor" in signin:
				self.output( self.signin, "Two Factor Required" )
			else:
				self.output( self.signin, "OOPS! Something wrong :(" )
				self.tryAgain( next=lambda: self.signin( browser=browser, ask=False ), other=self.main )
	
	#[Kanashi.story( Story story, Int|Str target, Int flag, Str username, Dict callback )]: None
	@final
	@logged
	def story( self, story:Story=None, target:int|str=None, flag:int=None, username:str=None, callback:dict=None ) -> None:
		if not isinstance( callback, dict ):
			callback = {
				"action": lambda: self.story( story=story, flag=flag ),
				"output": "Cancel",
				"prints": "Back to before"
			}
		if story is None:
			try:
				if flag == 1:
					storyType = Story.TIMELINE
					if target is None:
						self.output( self.story, "Please input Story target or Url" )
						capture = None
						while capture is None:
							target = self.input( "Story" )
							capture = match( Pattern.STORY, target )
							if capture is not None:
								groups = capture.groupdict()
								for key in [ "profile", "username" ]:
									if key in groups and groups[key] is not None:
										select = self.input( "Highlight only [Y/n]", default=[ "Y", "y", "N", "n" ] )
										storyType = Story.HIGHLIGHT if select.upper() == "Y" else Story.PROFILE
								break
							...
						...
					story = self.thread( f"Getting story info from {target}", lambda: self.client.story( target=target, flag=storyType ) )
					self.story( story=story, callback=callback )
				elif flag == 2:
					self.output( self.story, [
						"Only get from following feed or not",
						"The default value is False"
					])
					followingFeed = self.input( "Following Feed [Y/n]", default=[ "Y", "y", "N", "n" ] )
					story = self.thread( "Getting timeline feed story", lambda: self.client.stories( isFollowingFeed=followingFeed.upper() == "Y" ) )
					self.story( story=story, callback=callback )
				elif flag == 3:
					if username is None:
						self.output( self.story, "Please input user username" )
						username = self.input( "Username" )
					story = self.thread( f"Getting highlight story of @{username}", lambda: self.client.story( target=username, flag=Story.HIGHLIGHT ) )
					self.story( story=story, callback=callback )
				elif flag == 4:
					self.main()
				else:
					action = self.action( info=False, actions={
						"info": {
							"signin": True,
							"action": lambda: self.story( flag=1, callback=callback ),
							"output": "Story Info",
							"prints": "Story info by story id or url"
						},
						"feed": {
							"signin": True,
							"action": lambda: self.story( flag=2, callback=callback ),
							"output": "Story Feed",
							"prints": "Fetch stories from timeline feed"
						},
						"user": {
							"signin": True,
							"action": lambda: self.story( flag=3, callback=callback ),
							"output": "Story User",
							"prints": "Fetch stories by username"
						},
						"main": {
							"action": self.main,
							"output": "Cancel",
							"prints": "Back to main"
						}
					})
					action()
			except RequestError as e:
				self.emit( e )
				self.tryAgain( next=lambda: self.story( flag=flag, callback=callback ), other=self.story )
				return
		elif isinstance( story, StoryFeed ):
			if flag == 1:
				raise NotImplementedError( "Action for {}$.displayBroadcast does not implemented".format( self.story ) )
			elif flag == 2:
				if len( story.tray ) >= 1:
					stories = []
					for tray in story.tray:
						stories.append( f"{tray.user.full_name} (@{tray.user.username})" if tray.user.full_name else f"@{tray.user.username}" )
						stories.append([
							"Story Id {}".format( tray.id ),
							"Story Len {}".format( tray.media_count ),
							"Story Seen {}".format( tray.seen >= tray.seen_ranked_position )
						])
					self.output( self.story, [
						"\nAll tray story from feed timeline",
						"Please input >>> for back to before\n",
						stories
					])
					select = self.input( "Select", default=[ ">>>", *[ str( idx +1 ) for idx in range( len( story.tray ) ) ] ] )
					if select != ">>>":
						self.story( story=story.tray[( int( select ) -1 )], callback={ **callback, "action": lambda: self.story( story=story, flag=2 ) } )
					else:
						callback['action']()
				else:
					self.output( self.story, "There are no stories from the timeline feed" )
					self.previous( lambda: self.story( story=story ) )
			elif flag == 3:
				callback['action']()
			else:
				action = self.action( 
					info=False, 
					prints=[ 
						"\nRanking Token \"{}\"".format( story.story_ranking_token ),
						"Please select action:\n"
					], 
					actions={
						"broadcast": {
							"action": lambda: self.story( story=story, flag=1, callback={ **callback, "action": lambda: self.story( story=story ) } ),
							"output": "Display Broadcast",
							"prints": "Timeline feed broadcast"
						},
						"trays": {
							"action": lambda: self.story( story=story, flag=2, callback={ **callback, "action": lambda: self.story( story=story ) } ),
							"output": "Display Tray",
							"prints": "Timeline feed stories"
						},
						"cancel": callback
					}
				)
				action()
		elif isinstance( story, StoryFeedTray ):
			if flag == 1: 
				...
			elif flag == 2: 
				...
			elif flag == 3: 
				...
			elif flag == 4: 
				...
			else:
				action = self.action( 
					info=False, 
					prints=[
						"\nThis story will expire on {}".format( datetime.fromtimestamp( story.expiring_at ) ),
						"A timeline feed story from @{}".format( story.user.username ),
						"The total number of media IDs {}".format( story.media_count ),
						"Please select action:\n"
					],
					actions={
						"ids": {
							"signin": True,
							"action": lambda: self.story( story=story, flag=1, callback={ **callback, "action": lambda: self.story( story=story ) } ),
							"output": "Media IDs",
							"prints": "Display all story media ids"
						},
						"urls": {
							"signin": True,
							"action": lambda: self.story( story=story, flag=2, callback={ **callback, "action": lambda: self.story( story=story ) } ),
							"output": "Media URLs",
							"prints": "Display all story media urls"
						},
						"fetch": {
							"signin": True,
							"action": lambda: self.story( story=story, flag=3, callback={ **callback, "action": lambda: self.story( story=story ) } ),
							"output": "Fetch Media",
							"prints": "Fetch all story media ids"
						},
						"cancel": callback
					}
				)
				action()
		elif isinstance( story, StoryFeedTrayReel ):
			print( self.colorize( repr( story ) ) )
		elif isinstance( story, StoryFeedTrayReels ):
			print( self.colorize( repr( story ) ) )
		elif isinstance( story, StoryHighlight ):
			print( self.colorize( repr( story ) ) )
		elif isinstance( story, StoryHighlights ):
			print( self.colorize( repr( story ) ) )
		elif isinstance( story, StoryItem ):
			print( self.colorize( repr( story ) ) )
		elif isinstance( story, StoryProfile ):
			print( self.colorize( repr( story ) ) )
		elif isinstance( story, StoryProfileEdge ):
			print( self.colorize( repr( story ) ) )
		else:
			raise TypeError( "Invalid \"story\" parameter, value must be type Story, {} passed".format( typeof( story ) ) )
		...
	
	#[Kanashi.support()]: None
	@final
	def support( self ) -> None:
		status = self.xdgopen( "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x70\x61\x79\x70\x61\x6c\x2e\x6d\x65\x2f\x68\x78\x41\x72\x69" )
		self.output( self.support, "Thank you very much for your support ^><" if status == 0 else "Something wrong when running xdg-open :(" )
		self.previous( self.main, ">>>" )
	
	#[Kanashi.switch( Int|Str select, Bool ask )]: None
	@final
	def switch( self, select:int|str=None, ask:bool=True ) -> None:
		if len( self.settings.signin.switch ) >= 1:
			outputs = [ 
				"\nPlease select the account you want to use.",
				"Please input >>> for back to cancel operation\n"
			]
			if self.authenticated:
				display = self.active.fullname \
					if self.active.fullname \
					else \
						f"@{self.active.username}"
				if ask is True:
					self.output( self.switch, [
						"\nYou are currently logged in as \x1b[1;38;5;189m{}\x1b[0m".format( display ),
						"Please press Y to continue changing account"
					])
					return self.tryAgain( "Next [Y/n]", next=lambda: self.switch( ask=False ), other=self.main )
				else:
					outputs = [ "\nYou are currently logged in as \x1b[1;38;5;189m{}\x1b[0m".format( display ), *outputs ]
			menu = []
			users = self.settings.signin.switch.keys()
			for key in users:
				menu.append( "{} (@{})".format(
					self.settings.signin.switch[key].fullname,
					self.settings.signin.switch[key].username
				))
			self.output( self.switch, [ *outputs, menu ] )
			select = self.input( "Switch", default=[ ">>>", *users, *[ str( i +1 ) for i in range( len( users ) ) ] ] )
			if select == ">>>":
				return self.main()
			elif match( r"^\d+$", select ):
				select = self.settings.signin.switch[users[ int( select ) -1 ]]
			else:
				select = self.settings.signin.switch[select]
			default = self.input( "Set as default [Y/n]", default=[ "Y", "y", "N", "n" ] )
			active = Active( select )
			if default.upper() == "Y":
				self.settings.signin.active = active.username
				self.configSave( "Changes have been saved" )
			self.client.activate( active )
			self.__request__ = self.client.request
			self.main()
		else:
			self.output( self.switch, "Oops! No account saved" )
			self.previous( self.main, ">>>" )
	