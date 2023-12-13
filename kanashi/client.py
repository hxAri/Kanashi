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
from typing import final
from yutiriti.error import AuthError
from yutiriti.object import Object
from yutiriti.readonly import Readonly
from yutiriti.cookie import Cookie
from yutiriti.common import droper, typeof
from yutiriti.request import Cookies, Headers, Request, RequestRequired
from yutiriti.string import String

from kanashi.common import encpaswd, isUserId
from kanashi.config import Config
from kanashi.decorator import avoidForMySelf, logged
from kanashi.error import *
from kanashi.pattern import Pattern
from kanashi.typing import (
	AccessManager, 
	AccessManagerApps, 
	AccessManagerOAuth, 
	Active, 
	Checkpoint, 
	Direct, 
	Explore, 
	ExploreClip, 
	ExploreClipItem, 
	ExploreClipMedia, 
	ExploreFillItem, 
	ExploreFillMedia, 
	ExploreLayout, 
	ExploreSection, 
	Follow, 
	Follower, 
	Followers, 
	Following, 
	Followings, 
	Friendship, 
	FriendshipStatuses, 
	Inbox, 
	Logout, 
	Media, 
	Notification, 
	NotificationSMS, 
	NotificationPush, 
	Pending, 
	Pendings, 
	Privacy, 
	Profile, 
	SavedCollectionList, 
	SavedPosts, 
	Settings, 
	SignIn, 
	Story, 
	StoryFeed, 
	StoryFeedTray, 
	StoryFeedTrayReel, 
	StoryFeedTrayReels, 
	StoryHighlight, 
	StoryHighlights, 
	StoryHighlightReels, 
	StoryItem, 
	StoryProfile, 
	StoryProfileEdge, 
	StoryReel, 
	TwoFactor, 
	TwoFactorInfo, 
	User
)


#[kanashi.client.Client]
class Client( RequestRequired, Readonly ):
	
	""" A Kanashi Client class """
	
	# Default client browser user agent.
	BROWSER = "Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/535.42 (KHTML, like Gecko)  Chrome/112.0.5615.137 Mobile Safari/600.3"
	
	# Default header settings for requests.
	HEADERS = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "en-US,en;q=0.9",
		"Authority": "www.instagram.com",
		"Connection": "close",
		"Origin": "https://www.instagram.com",
		"Referer": "https://www.instagram.com/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"User-Agent": "Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/535.42 (KHTML, like Gecko)  Chrome/112.0.5615.137 Mobile Safari/600.3",
		"Viewport-Width": "980",
		"X-Asbd-Id": "198387",
		"X-IG-App-Id": "1217981644879628",
		"X-IG-WWW-Claim": "hmac.AR04Hjqeow3ipAWpAcl8Q5Dc7eMtKr3Ff08SxTMJosgMAh-z",
		"X-Instagram-Ajax": "1007625843",
		"X-Requested-With": "XMLHttpRequest"
	}

	#[Client( Active active, Config config, Request request )]
	def __init__( self, active:Active=None, config:Config=None, request:Request=None ) -> None:

		"""
		Construct method of class Client.

		:params Active active
			Authenticated client
		:params Config config
			Appication configuration
		:params Request request
			Instance of class Request
		
		:return None
		:raises TypeError
			Raise when the value of parameter
			active and request is invalid value type
		"""

		self.__except__:list[str] = [
			"__active__",
			"__caching__",
			"__cookies__",
			"__headers__",
			"__request__",
			"__session__"
		]
		if config is not None:
			if isinstance( config, str ):
				config = Config( config )
			elif not isinstance( config, Config ):
				raise TypeError( "Invalid \"config\" parameter, value must be type Config, {} passed".format( typeof( config ) ) )
		else:
			config = Config()
		if len( config.settings ) <= 0:
			config.load()
		if request is not None:
			if not isinstance( request, Request ):
				raise TypeError( "Invalid \"request\" parameter, value must be type Request, {} passed".format( typeof( request ) ) )
		else:
			request = Request()
		if active is not None:
			if not isinstance( active, Active ):
				raise TypeError( "Invalid \"active\" parameter, value must be type Active, {} passed".format( typeof( active ) ) )
		elif config.settings.signin.active in config.settings.signin.switch:
			active = Active( config.settings.signin.switch[config.settings.signin.active] )
		if isinstance( active, Active ):
			request.headers.update( active.session.headers.props() )
			request.headers.update({ "User-Agent": active.session.browser })
			cookies = active.session.cookies
			for cookie in cookies.keys():
				Cookie.set( request.cookies, cookie, cookies[cookie], domain=".instagram.com", path="/" )
		else:
			request.headers.update( Client.HEADERS )
			if config.settings.browser.default is not None:
				browser = config.settings.browser.default
			else:
				browser = choice( config.settings.browser.randoms )
			request.headers.update({ "User-Agent": browser })
		
		self.__active__:Active|None = active
		self.__config__:Config = config
		self.__setting__:Settings = config.settings
		self.__request__:Request = request
	
	#[Client.access()]: AccessManager<AccessManagerApps, AccessManagerOAuth>
	@logged
	def access( self ) -> AccessManager:

		"""
		Restore Application Manager Access and
		OAuth Authentication to your account.

		:return AccessManager<AccessManagerApps, AccessManagerOAuth>
		:raises ClientError
			When something wrong, please to check the request response history
		"""

		#[Client.access$.apps( Self@Client self )]: AccessManagerApps
		def apps( self ) -> dict:
			self.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/accounts/manage_access/"
			})
			request = self.request.get( "https://www.instagram.com/api/v1/accounts/manage_access/web_info/" )
			content = request.json()
			status = request.status
			if status == 200:
				return content
			raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching account access info [{status}]" )

		#[Client.access$.oauth( Self@Client self )]: AccessManagerOAuth
		def oauth( self ) -> dict:
			self.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/accounts/manage_access/"
			})
			request = self.request.get( "https://www.instagram.com/api/v1/oauth/platform_tester_invites/" )
			content = request.json()
			status = request.status
			if status == 200:
				return content
			raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching OAuth Platform Tester Invites [{status}]" )
		
		return AccessManager({
			"apps": apps( self ),
			"oauth": oauth( self )
		})
	
	#[Client.active]: Active
	@final
	@property
	def active( self ) -> Active|None: return self.__active__

	#[Client.activate( Active active, Request request )]: None
	@final
	def activate( self, active:Active, request:Request=None ) -> None:
		if not isinstance( active, Active ):
			raise TypeError( "Invalid \"active\" parameter, value must be type Active, {} passed".format( typeof( active ) ) )
		if request is not None:
			if not isinstance( request, Request ):
				raise TypeError( "Invalid \"request\" parameter, value must be type Request, {} passed".format( typeof( request ) ) )
		else:
			request = Request( headers=active.session.headers )
			for cookie in active.session.cookies.keys():
				Cookie.set( request.cookies, cookie, active.session.cookies[cookie], domain=".instagram.com", path="/" )
		self.__active__:Active|None = active
		self.__request__:Request = request
	
	#[Client.approve( Int|Str|User user, Bool approve )]: Friendship
	@avoidForMySelf
	def approve( self, user:int|str|User, approve:bool=True ) -> Friendship:
		
		"""
		Approve or ignore request follow from user.
		
		:parans Int|Str|User user
		:params Bool approve
			Approve action
		
		:return Friendship
			Approve or ignore result represent
		:raises ValueError
			When the approve parameter is invalid
		:raises FriendshipError
			When the user does not request follow your account
			When you will approve yourself
		:raises TypeError
			When the approve does not passed when new Profile instance crated
		"""

		if user is None:
			raise ValueError( "User can't be empty" )
		if isinstance( user, int ):
			id = user
		elif isinstance( user, str ):
			user = self.user( username=user, count=1 )
			id = user.id if "id" in user else user.pk
		elif isinstance( user, User ):
			if "incoming_request" in user:
				if not user.incoming_request:
					raise FriendshipError( "This user does not sent request to follow your account" )
			id = user.id if "id" in user else user.pk
		else:
			raise TypeError( "Invalid \"user\" parameter, value must be type Int|str|User, {} passed".format( typeof( user ) ) )
		
		if approve is None:
			raise ValueError( "Follow request consent cannot be empty" )
		if not isinstance( approve, bool ):
			raise TypeError( "Invalid \"approve\" parameter, value must be type Bool, {} passed".format( typeof( approve ) ) )
		
		action = "Approve request"
		target = f"https://www.instagram.com/api/v1/web/friendships/{id}/approve/"
		if not approve:
			action = "Ignore request"
			target = f"https://www.instagram.com/api/v1/web/friendships/{id}/ignore/"
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/",
			"Content-Type": "application/x-www-form-urlencoded"
		})

		# Trying to approve/ ignore request follow.
		request = self.request.post( target, data={} )
		content = request.json()
		status = request.status
		if status == 200:
			return Friendship({ "id": id, "approve": approve, "ignoring": not approve, **content })
		raise FriendshipError( content['message'] if "message" in content and content['message'] else f"There was an error when {action} follow" )
	
	#[Client.attemp()]: Any
	def attemp( self ) -> any:
		
		"""
		...
		"""
		
		...
	
	#[Client.authenticated]: bool
	@final
	@property
	def authenticated( self ) -> bool:

		"""
		Return if client is authenticated.

		:return Bool
			Return True if client is authenticated
			Return False otherwise
		"""

		if isinstance( self.active, Active ):
			if isinstance( self.active.id, str ):
				if not isUserId( self.active.id ):
					return False
			return \
				"ds_user_id" in self.cookies and self.active.id == int( self.cookies['ds_user_id'] ) and \
				"User-Agent" in self.headers and self.active.session.browser == self.headers['User-Agent'] and \
				"X-CSRFToken" in self.headers and \
				"csrftoken" in self.cookies and self.cookies['csrftoken'] == self.headers['X-CSRFToken']
		return False
	
	#[Client.bestie( Friendship|Int|Profile|User user, Str username, Bool bestie )]: Friendship
	@final
	@logged
	@avoidForMySelf
	def bestie( self, user:Friendship|int|Profile|User, username:str|None=None, bestie:bool=True ) -> Friendship:

		"""
		Make bestie or unbestie user.

		:params Int|Profile|User user
		:params Str username
			Username is only for `Referer` header for avoid error
		:params Bool bestie
			True set user as bestie
			False otherwise
		
		:return Friendship
		:raises BestieError
			When you trying to make yourself as bestie
			When you are not following the user
			When something wrong, please to check the request response history
		"""

		if user is None:
			raise ValueError( "User can't be empty" )
		if isinstance( user, ( Friendship, Profile, User ) ):
			if "id" in user: pk = user['id']
			elif "pk" in user: pk = user['pk']
			else:
				raise ValueError( "Object {} does not set Id or Primary Key".format( typeof( user ) ) )
			if "following" in user:
				if user['following'] is not True:
					raise BestieError( "Can't set user as bestie before following" )
			if "username" in user:
				username = user['username']
			user = pk
		if isinstance( user, int ):
			if self.active.id == user:
				raise BestieError( "Unable to set yourself as a bestie" )
		else:
			raise TypeError( "Invalid \"user\" parameter, value must be type Friendship|Int|Profile|User, {} passed".format( typeof( user ) ) )
		
		if username is None:
			raise ValueError( "Username can't be empty, this require for \"Referer\" header" )
		if not isinstance( username, str ):
			raise TypeError( "Invalid \"username\" parameter, value must be type Str, {} passed".format( typeof( username ) ) )
		if match( Pattern.USERNAME, username ) is None:
			raise ValueError( f"Invalid username value, username format must be \"{Pattern.USERNAME}\", \"{username}\" passed" )
		
		# Update request headers.
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/json",
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{username}/"
		})

		# Request payloads.
		payload = {
			"add": [],
			"remove": [],
			"source": "\x70\x72\x6f\x66\x69\x6c\x65"
		}

		if bestie is True:
			action = "Remove Bestie"
			payload['remove'].append( user )
		else:
			action = "Adding Bestie"
			payload['add'].append( user )
		
		request = self.request.post( "https://www.instagram.com/api/v1/friendships/set_besties/", json=payload )
		content = request.json()
		status = request.status
		if status == 200:
			return Friendship( content['friendship_statuses'][str( user )] )
		raise BestieError( f"An error occurred while {action} the user [{status}]" )
	
	#[Client.block( Friendship|Int|Profile|User user, Bool block )]: Friendship
	@final
	@logged
	@avoidForMySelf
	def block( self, user:Friendship|int|Profile|User, block:bool=True ) -> Friendship:
		
		"""
		:raises BlockError
			When something wrong e.g data user doest not available or error on request json responses
		"""
		
		...
	
	#[Client.config]: Config
	@final
	@property
	def config( self ) -> Config: return self.__config__
	
	#[Client.csrftoken]: List|Str
	@final
	@property
	def csrftoken( self ) -> list|str:

		"""
		Return active csrftoken or crsftoken prelogin.
		
		:return Str
			String of csrftoken value
			List of request object and csrftoken
		:raises CsrftokenError
			When csrftoken is not available
		"""

		if not self.authenticated:
			self.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/accounts/login/"
			})
			try:
				target = "https://i.instagram.com/api/v1/si/fetch_headers"
				return self.request.options( target ).cookies['csrftoken']
			except KeyError as e:
				raise CsrftokenError( "Csrftoken prelogin is not available", prev=e )
		return self.active.csrftoken
	
	#[Client.checkpoint( Str url, Request request, Cookies|Dict|Object|Str cookies, Dict|Headers headers, Int choices )]: Object
	@final
	def checkpoint( self, url:str, request:Request=None, cookies:Cookies|dict|Object|str=None, headers:dict|Headers|Object=None, choices:int=1 ) -> Object:

		"""
		Bypass Checkpoint URL.

		Ohhh! Sorry i did not expect this bro :v

		Note that this method may not necessarily work
		But it will be better if you try it

		:params Str url
			Checkpoint url
		:params Request request
			Request instance, Forward instance requests when
			you are hit by a checkpoint during login
		:params Cookies|Dict|Object|Str cookies
			For manual usage without Request instance
		:params Dict|Headers headers
			For manual usage without Request instance
		:params Int choices
			Your choices requests
		
		:return Object
		"""

		if url is None:
			raise ValueError( "Url can't be empty" )
		if not isinstance( url, str ):
			raise TypeError( "Invalid \"url\" parameter, value must be type Str, {} passed".format( typeof( url ) ) )
		else:
			search = match( r"^(?:\/challenge\/action\/(?P<challenge>[^\n]+))$", url )
			if search is not None:
				challenge = search.group( "challenge" )
			else:
				raise ValueError( "Invalid checkpoint challenge URL" )
		if request is None:
			if cookies is None:
				raise ValueError( "Cookie can't be empty" )
			if not isinstance( cookies, ( Cookies, dict, Object, str ) ):
				raise TypeError( "Invalid \"cookies\" parameter, value must be type Cookies|Dict|Object|Str, {} passed".format( typeof( cookies ) ) )
			if isinstance( cookies, str ):
				cookies = Cookie.simple( cookies )
			elif isinstance( cookies, Headers ):
				cookies = dict( cookies )
			if isinstance( cookies, ( dict, Object ) ):
				for require in [ "csrftoken" ]:
					if require not in cookies:
						raise SignInError( f"Invalid cookie, there is no \"{require}\" in the cookie" )
			if headers is None:
				raise ValueError( "Headers can't be empty" )
			if not isinstance( cookies, ( Cookies, dict, Object, str ) ):
				raise TypeError( "Invalid \"headers\" parameter, value must be type Dict|Headers|Object, {} passed".format( typeof( headers ) ) )
			if isinstance( headers, Headers ):
				headers = dict( headers )
			elif isinstance( headers, Object ):
				headers = headers.props()
			request = Request( cookies=cookies, headers=headers, timeout=self.settings.timeout )
		
		# Update request headers.
		request.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"X-Csrftoken": cookies['csrftoken'],
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/challenge/action/{challenge}"
		})
		return request.post( f"https://www.instagram.com/api/v1/challenge/web/action/{challenge}", data={ "choice": choices })

	@final
	@logged
	def dayShells( self ) -> any:

		""" https://www.instagram.com/api/v1/archive/reel/day_shells/?timezone_offset=25200 """

	#[Client.destruct( Bool default )]: None
	@final
	@logged
	def destruct( self, default:bool=False ) -> None:

		"""
		Destroy the current active login session.

		:params Bool default
			Also delete the login session data in the configuration
		
		:return None
		"""

		if default is True:
			if self.settings.signin.active == self.active.username:
				self.settings.signin.active = None
			if self.active.username in self.settings.signin.switch:
				self.settings.signin.switch.delt( self.active.username )
		self.__active__ = None
		self.__request__ = Request( headers=Client.HEADERS, timeout=self.settings.timeout )
	
	#[Client.direct( Bool persistentBadging, Str folder, Int limit, Int threadMessageLimit, Int|Str cursor )]: Direct
	@logged
	def direct( self, persistentBadging:bool=True, folder:str="", limit:int=5, threadMessageLimit:int=1, cursor:int|str=None ) -> Direct:

		"""
		Get direct message inbox.

		:params Int|Str cursor
			Next page request of direct message inbox

		:return Direct<DirectThread<User>>
		:raises ClientError
			When something wrong, please to check the request response history
		:raise TypeError
			When the parameter value is invalid value
		"""

		params = {
			"folder": folder,
			"limit": limit,
			"persistentBadging": str( persistentBadging ),
			"thread_message_limit": threadMessageLimit
		}
		if cursor is not None:
			if isinstance( cursor, ( int, str ) ):
				params = { "cursor": cursor, "persistentBadging": params['persistentBadging'] }
			else:
				raise TypeError( "Invalid \"cursor\" parameter, value must be type Int|Str, {} passed".format( typeof( next ) ) )

		# Update request headers.
		self.headers.update({
			"Origin": "https://www,.instagram.com",
			"Referer": "https://www.instagram.com/inbox/"
		})

		# Trying to get direct message inbox.
		request = self.request.get( "https://www.instagram.com/api/v1/direct_v2/inbox/", params=params )
		content = request.json()
		status = request.status
		if status == 200:
			return Direct( content )
		else:
			raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching direct message inbox [{status}]" )
	
	#[Client.direct()]: Direct
	@logged
	def directPresence( self, persistence:bool=None, cache:bool=False ) -> Object:
		return self.request.get( "https://www.instagram.com/api/v1/direct_v2/get_presence/" )
	
	#[Client.explore( Int maxId, Bool includeFixedDestinations, Bool isNonPersonalizedExplore, Bool isPrefetch, Bool omitCoverMedia )]: Explore
	@logged
	def explore( self, maxId:int=0, includeFixedDestinations:bool=True, isNonPersonalizedExplore:bool=False, isPrefetch:bool=False, omitCoverMedia:bool=False ) -> Explore:
		
		"""
		Get contents of Instagram explore

		:params Int maxId
		:params Bool includeFixedDestinations
		:params Bool isNonPersonalizedExplore
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
			"is_nonpersonalized_explore": isNonPersonalizedExplore,
			"is_prefetch": isPrefetch,
			"max_id": maxId,
			"module": "explore_popular",
			"omit_cover_media": omitCoverMedia
		})
		content = request.json()
		status = request.status
		if status == 200:
			return Explore( content )
		else:
			raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching contents from instagram explore [{status}]" )
	
	#[Client.favorite( Friendship|Int|Profile|User user, Bool favorite ): Friendship
	@final
	@logged
	@avoidForMySelf
	def favorite( self, user:Friendship|int|Profile|User, favorite:bool ) -> Friendship:
		
		"""
		:raises FavoriteError
			When something wrong e.g data user doest not available or error on request json responses
		"""
		
		...
	
	#[Client.follow( Friendship|Int|Profile|User user, Follow.Type follow )]: Friendship
	@final
	@logged
	@avoidForMySelf
	def follow( self, user:Friendship|int|Profile|User, follow:Follow.Type ) -> Friendship:

		"""
		Follow, Unfollow, or Cancel request follow.

		:params Friendship|Int|Profile|User user
		:params Follow.Type follow
		
		:return Friendship
		:raises FollowError
			When you trying to follow yourself, this is ambigue bro!
			When something wrong, please to check the request response history
		"""

		username = None

		if user is None:
			raise ValueError( "User can't be empty" )
		if isinstance( user, ( Friendship, Profile, User ) ):
			if "id" in user: pk = user['id']
			elif "pk" in user: pk = user['pk']
			else:
				raise ValueError( "Object {} does not set Id or Primary Key".format( typeof( user ) ) )
			if "username" in user:
				username = user['username']
			user = pk
		if isinstance( user, int ):
			if self.active.id == user:
				raise BestieError( "Unable to follow or unfollow yourself" )
		else:
			raise TypeError( "Invalid \"user\" parameter, value must be type Friendship|Int|Profile|User, {} passed".format( typeof( user ) ) )
		
		if username is not None:
			if not isinstance( username, str ):
				raise TypeError( "Invalid \"username\" parameter, value must be type Str, {} passed".format( typeof( username ) ) )
			if match( Pattern.USERNAME, username ) is None:
				raise ValueError( f"Invalid username value, username format must be \"{Pattern.USERNAME}\", \"{username}\" passed" )

		if follow is None:
			raise ValueError( "\"follow\" can't be empty" )
		match follow:
			case Follow.FOLLOW:
				action = "Following"
				target = f"https://www.instagram.com/api/v1/friendships/create/{user}/"
			case Follow.UNFOLLOW:
				action = "Unfollowing"
				target = f"https://www.instagram.com/api/v1/friendships/destroy/{user}/"
			case Follow.UNREQUEST:
				action = "Cancel request follow"
				target = f"https://www.instagram.com/api/v1/friendships/destroy/{user}/"
			case _:
				raise TypeError( "Invalid \"follow\" parameter, value must be type Follow$.Type, {} passed".format( follow ) )
		
		# Update request headers.
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{username}/" if username is not None else "https://www.instagram.com/"
		})

		# Request payload.
		payload = {
			"container_module": "\x70\x72\x6f\x66\x69\x6c\x65",
			"nav_chain": "\x50\x6f\x6c\x61\x72\x69\x73\x50\x72\x6f\x66\x69\x6c\x65\x52\x6f\x6f\x74\x3a\x70\x72\x6f\x66\x69\x6c\x65\x50\x61\x67\x65\x3a\x31\x3a\x76\x69\x61\x5f\x63\x6f\x6c\x64\x5f\x73\x74\x61\x72\x74",
			"user_id": user
		}

		# Trying to follow user.
		request = self.request.post( target, data=payload )
		content = request.json()
		status = request.status
		if status == 200:
			return Friendship( content['friendship_status'] )
		raise FollowError( f"An error occurred while {action} the user [{status}]" )
	
	#[Client.followers( Int|Str|User user, Int count, Int nextMaxId )]: Followers<Follower>
	@logged
	def followers( self, user:int|str|User, count:int=12, nextMaxId:int=None ) -> Followers:

		"""
		Fetch user followers lists.

		:params Int|Str|User user
		:params Int count
			Size of followers, the default is 12
		:params Int nextMaxId
			Next maximal id to get
		
		:return Followers<Follower>
		:raises FollowerError
			When something wrong, please to check the request response history
		:raises TypeError
			when the parameter value is invalid value type
		:raises ValueError
			When the user parameter is empty
			When the username is invalid
			Whne the maximal id is over than followers count or less than
		"""

		# Default URL Referer
		referer = "https://www.instagram.com/explore/"

		if user is None:
			raise ValueError( "User can't be empty" )
		if isinstance( user, int ): ...
		elif isinstance( user, str ):
			if match( Pattern.ID ) is None:
				if match( Pattern.USERNAME, user ) is None:
					raise ValueError( "Invalid username" )
				referer = f"https://www.instagram.com/{user}/followers/"
				user = self.user( username=user, count=1 )
				user = user.id if "id" in user else user.pk
		elif isinstance( user, User ):
			if "username" in user or user.id is None:
				referer = f"https://www.instagram.com/{user.username}/followers/"
			if "id" not in user:
				if "pk" not in user or "pk" or user.pk is None:
					raise ValueError( "The User object does not have a user primary key" )
				user = user.pk
			else:
				user = user.id
		else:
			raise TypeError( "Invalid \"user\" parameter, value must be type Int|Str|User, {} passed".format( typeof( user ) ) )

		if count <= 0:
			raise ValueError( "The maximum number of counts cannot be less than 0" )
		if count >= 100:
			raise ValueError( "The maximum number of counts cannot exceed 100" )

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": referer
		})

		# Request parameters.
		params = { "count": count }

		# If next maximal id is available.
		if nextMaxId is not None:
			if not isinstance( nextMaxId, ( int, str ) ):
				raise TypeError( "Invalid \"nextMaxId\" paramater, value must be type Int|Str, {} passed".format( typeof( nextMaxId ) ) )
			elif isinstance( nextMaxId, str ):
				if match( Pattern.ID, nextMaxId ) is None:
					raise ValueError( "Invalid next maximal id value" )
			params['max_id'] = nextMaxId

		# Trying to get user followers.
		request = self.request.get( f"https://www.instagram.com/api/v1/friendships/{user}/followers/", params=params )
		content = request.json()
		status = request.status
		if status == 200:
			return Followers( content )
		raise FollowerError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the user followers [{status}]" )
	
	#[Client.following( Int|Str|User user, Int count, Int nextMaxId )]: Followings<Following>
	@logged
	def following( self, user:int|str|User, count:int=12, nextMaxId:int=None ) -> Followings:

		"""
		Fetch user following lists.

		:params Int|Str|User user
		:params Int count
			Size of followers, the default is 12
		:params Int nextMaxId
			Next maximal id to get
		
		:return Followers<Follower>
		:raises FollowerError
			When something wrong, please to check the request response history
		:raises TypeError
			when the parameter value is invalid value type
		:raises ValueError
			When the user parameter is empty
			When the username is invalid
			Whne the maximal id is over than followers count or less than
		"""

		# Default URL Referer
		referer = "https://www.instagram.com/explore/"

		if user is None:
			raise ValueError( "User can't be empty" )
		if isinstance( user, int ): ...
		elif isinstance( user, str ):
			if match( Pattern.ID ) is None:
				if match( Pattern.USERNAME, user ) is None:
					raise ValueError( "Invalid username" )
				referer = f"https://www.instagram.com/{user}/following/"
				user = self.user( username=user, count=1 )
				user = user.id if "id" in user else user.pk
		elif isinstance( user, User ):
			if "username" in user or user.id is None:
				referer = f"https://www.instagram.com/{user.username}/following/"
			if "id" not in user:
				if "pk" not in user or "pk" or user.pk is None:
					raise ValueError( "The User object does not have a user primary key" )
				user = user.pk
			else:
				user = user.id
		else:
			raise TypeError( "Invalid \"user\" parameter, value must be type Int|Str|User, {} passed".format( typeof( user ) ) )

		if count <= 0:
			raise ValueError( "The maximum number of counts cannot be less than 0" )
		if count >= 100:
			raise ValueError( "The maximum number of counts cannot exceed 100" )

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": referer
		})

		# Request parameters.
		params = { "count": count }

		# If next maximal id is available.
		if nextMaxId is not None:
			if not isinstance( nextMaxId, ( int, str ) ):
				raise TypeError( "Invalid \"nextMaxId\" paramater, value must be type Int|Str, {} passed".format( typeof( nextMaxId ) ) )
			elif isinstance( nextMaxId, str ):
				if match( Pattern.ID, nextMaxId ) is None:
					raise ValueError( "Invalid next maximal id value" )
			params['max_id'] = nextMaxId

		# Trying to get user followings.
		request = self.request.get( f"https://www.instagram.com/api/v1/friendships/{user}/following/", params=params )
		content = request.json()
		status = request.status
		if status == 200:
			return Followings( content )
		raise FollowerError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the user following [{status}]" )
	
	#[Client.friendship( Int id )]: Friendship
	@logged
	def friendship( self, id:int ) -> Friendship:
		
		"""
		Get user friendship info.
		
		:params Int id
		
		:return Friendship
		:raises FriendshipError
			When something wrong, please to check the request response history
		:raises TypeError
			When the value of parameter is invalid value type
		:raises ValueError
			When the value of user id is empty
		"""
		
		# Update request headers.
		self.headers.update( **{
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})

		if id is None:
			raise ValueError( "Id can't be empty" )
		if not isinstance( id, int ):
			raise TypeError( "Invalid \"id\" parameter, value must be type Int, {} passed".format( typeof( id ) ) )
		
		# Trying to restrieve user friendship.
		request = self.request.get( f"https://www.instagram.com/api/v1/friendships/show/{id}" )
		content = request.json()
		status = request.status
		if status == 200:
			return Friendship( content )
		raise FriendshipError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the friendship [{status}]" )
	
	#[Client.friendshipShowMay( Str username, List<Int> ids, Mixed **kwargs )]: FriendshipStatuses
	@logged
	def friendshipShowMay( self, username:str, ids:list[int|str]=[], **kwargs ) -> FriendshipStatuses:
		
		"""
		Friendship Show Many information of user based id from followers or following list.
		
		:params Str username
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
		
		:return FriendshipStatuses
		:raises FriendshipError
			When something wrong, please to check the request response history
		:raises ValueError
			When the user id is empty
			When the user id is invalid
			When the ids parameter is invalid
			When the user id more than 32 ids
		"""
		
		if not isinstance( ids, list ):
			raise ValueError( "Invalid ids parameter, value must be type list<int>, {} passed".format( typeof( ids ) ) )
		if len( ids ) <= 0:
			raise ValueError( "User ids can't be empty" )
		if len( ids ) > 32:
			raise ValueError( "User ids must be less than 32 ids" )
		for i, id in enumerate( ids ):
			if not isUserId( id ):
				raise ValueError( "Invalid user id in list of ids, user id must be Int or Numeric String, {} passed on ids[{}]".format( typeof( id ), i ) )
			ids[i] = int( id )
		
		# Update request headers.
		self.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/{}/".format( username, "followers" if "followers" in kwargs else "following" )
		})
		
		# Trying to get more data.
		request = self.request.post( "https://www.instagram.com/api/v1/friendships/show_many/", data={ "user_ids": ids } )
		content = request.json()
		status = request.status
		if status == 200:
			statuses = {}
			for key, value in enumerate( content['friendship_statuses'] ):
				statuses[key] = Friendship( value )
			return FriendshipStatuses({
				"friendship_statuses": statuses
			})
		raise FriendshipError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the friendship information of users [{status}]" )
	
	@logged
	def graphql( self, binding:any=None, **kwargs ) -> any:

		"""
		"""

		# Default graphql URL.
		url = "https://www.instagram.com/graphql/query/"

		# Default request method.
		method = kwargs.pop( "method", "GET" )

		# Resolve binding value.
		binding = binding if callable( binding ) else lambda value: value

		# Trying sent graphql request.
		request = self.request.request( method=method, url=url, **kwargs )
		content = request.json()
		status = request.status
		if status == 200:
			return binding( content )
		raise ClientError( f"Something wrong when sent graphql request [{status}]" )
	
	#[Client.inbox( Str continuationToken )]: Inbox
	@logged
	def inbox( self, continuationToken:str=None ) -> Inbox:
		
		"""
		Get news inbox notifications.

		:params Str continuationToken
			Next page request of inbox notification
		
		:return Inbox
		:raises ClientError
			When something wrong, please to check the request response history
		:raises NotImplementedError
			When the feature is not or does not implemented in current future
		:raises TypeError
			when the parameter value is invalid value type
		"""
		
		# Update request headers.
		self.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})

		if continuationToken is not None:
			if not isinstance( continuationToken, str ):
				raise TypeError( "Invalid \"continuationToken\" parameter, value must be tyoe Str, {} passed".format( typeof( continuationToken ) ) )
			raise NotImplementedError( "Action for {}$.continuationToken does not implemented".format( self.inbox ) )
		
		# Trying to get news inbox notifications.
		request = self.request.post( "https://www.instagram.com/api/v1/news/inbox/", data={} )
		content = request.json()
		status = request.status
		if status == 200:
			return Inbox( content )
		raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the news inbox notifications [{status}]" )
	
	#[Client.logout()]
	@logged
	def logout( self ): ...

	#[Client.media()]
	@logged
	def media( self, target:int|str, flag:Media.Type|Story.Type ): ...

	#[Client.notification( Str channel )]: Notification
	@logged
	def notification( self, channel:str ) -> Notification:

		"""
		Get settings of notification channel.

		:params Str channel
		
		:return Notification
		:raises ClientError
			When something wrong, please to check the request response history
		:raises TypeError
			When the value of parameter is invalid value type
		:raises ValueError
			When the value of channel is empty
		"""

		if channel is None:
			raise ValueError( "Channel can't be empty" )
		elif not isinstance( channel, str ):
			raise TypeError( "Invalid \"channel\" parameter, value must be type Str, {} passed".format( typeof( channel ) ) )
		else:
			channel = channel.strip()
			match channel:
				case "email-sms" | "email_sms":
					referer = "emails/settings"
				case "push":
					referer = "push/web/settings"
				case _:
					raise ValueError( "Invalid channel notification type" )

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{referer}/"
		})

		# Trying to get notification setting.
		request = self.request.get( "https://www.instagram.com/api/v1/notifications/settings/", params={ "channels": channel } )
		content = request.json()
		status = request.status
		if status == 200:
			return NotificationPush( content ) if channel == "push" else NotificationSMS( content )
		raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching notification settings [{status}]" )

	#[Client.pending( Str nextMaxId )]: Pendings<Pending>
	@logged
	def pending( self, nextMaxId:str=None ) -> Pendings:
		
		"""
		Get pending request follow from users.

		:params Str nextMaxId
			Next page request of pending request follow
		
		:return Pendings<Pending>
		:raises ClientError
			When something wrong e.g data user doest not available or error on request json responses,
			When something wrong, please to check the request response history
		:raises TypeError
			When the parameter value is invalid value
		"""
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})

		if nextMaxId is not None:
			if not isinstance( nextMaxId, str ):
				raise NotImplementedError( "Action for {}$.nextMaxId does not implemented".format( self.pending ) )
		
		# Trying to get request follow pending.
		request = self.request.get( "https://www.instagram.com/api/v1/friendships/pending/" )
		content = request.json()
		status = request.status
		if status == 200:
			return Pendings({ **content, "users": [ { **user, "id": user['pk'] if "id" not in user else user['id'] } for user in content['users'] ] })
		raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the request pending [{status}]" )
	
	#[Client.privacy()]: Privacy
	@logged
	def privacy( self ) -> Privacy:

		"""
		Get settings of privacy.
		
		:return Privacy
		:raises ClientError
			When something wrong e.g data user doest not available or error on request json responses
		"""

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": choice([
				"https://www.instagram.com/accounts/what_you_see/",
				"https://www.instagram.com/accounts/who_can_see_your_content/",
				"https://www.instagram.com/accounts/how_others_can_interact_with_you/"
			])
		})
		
		# Trying to get privacy setting.
		request = self.request.get( "hhttps://www.instagram.com/api/v1/accounts/privacy_and_security/web_info/" )
		content = request.json()
		status = request.status
		if status == 200:
			return Privacy( content )
		raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching privacy settings [{status}]" )
	
	#[Client.profile( Int|Str username )]: Profile
	@logged
	def profile( self, username:int|str ) -> Profile:

		"""
		Get user profile info by username or user ids.

		:params Int|Str username
			Int for user id, and Str for username.
			But if Str is containts valid user id, it will convert to Int.
		
		:return Profile
		:raises TypeError
			When the parameter value is invalid value
		:raises UserError
			When the user data does not available
			When there are unexpected error found
		:raises UserNotFoundError
			When the user is not found
		:raises ValueError
			When the username is empty
		"""

		#[Client.profile$.getByUid( Request session, Int id )]: Dict
		def getByUid( session:Request, id:int ) -> dict:

			"""
			Get user info by id.
			
			:params Request session
				Authenticated request session
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

			# Update request headers.
			session.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/explore/"
			})
			
			# Trying to retrieve user info.
			request = session.get( f"https://i.instagram.com/api/v1/users/{id}/info/?profile_picture=true" )
			content = request.json()
			status = request.status
			if status == 200:
				if "user" in content and content['user']:
					if "username" in content['user'] and content['user']['username']:
						return content['user']
				raise UserError( f"Target \"{id}\" user found but user data is not available" )
			elif status == 404:
				raise UserNotFoundError( f"Target \"{id}\" user not found" )
			else:
				raise UserError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the user [{status}]" )
		
		#[Client.profile$.getByUname( Request session, Str username )]
		def getByUname( session:Request, username:str ) -> dict:

			"""
			Get user info by username.
			
			:params Request session
				Authenticated request session
			:params Str username
				Username profile
			
			:return Dict
				Profile info
			:raises UserError
				When the user data does not available
				When there are unexpected error found
			:raises UserNotFoundError
				When the user not found
			"""

			# Update request headers.
			session.headers.update({
				"Origin": "https://www.instagram.com",
				"Referer": f"https://www.instagram.com/{username}/"
			})
			
			# Trying to retrieve user info.
			request = session.get( f"https://www.instagram.com/{username}?__a=1&__d=dis" )
			content = request.json()
			status = request.status
			if status == 200:
				if "graphql" not in content:
					raise UserError( f"Target \"{username}\" user found but user data not available" )
				return content['graphql']['user']
			elif status == 404:
				raise UserNotFoundError( f"Target \"{username}\" user not found" )
			else:
				raise UserError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the user [{status}]" )

		if username is None:
			raise ValueError( "Username can't be empty" )
		elif not isinstance( username, ( int, str ) ):
			raise TypeError( "Invalid \"username\" parameter, value must be type Int|Str, {} passed".format( typeof( username ) ) )
		elif isinstance( username, int ):
			profile = getByUid( self.request, username )
		else:
			profile = getByUid( self.request, int( username ) ) \
				if isUserId( username ) \
				else getByUname( self.request, username )
		if "id" not in profile:
			profile['id'] = profile['pk']
		if "pk" not in profile:
			profile['pk'] = profile['id']
		
		if int( profile['id'] ) != int( self.active.id ):
			friendship = self.friendship( profile['id'] )
		
		viewer = { "viewer": droper( self.active, [ "id", "fullname", "username" ]) }
		friendship = { 
			"blocking": False,
			"followed_by": False,
			"following": False,
			"incoming_request": False,
			"is_bestie": False,
			"is_blocking_reel": False,
			"is_eligible_to_subscribe": False,
			"is_feed_favorite": False,
			"is_guardian_of_viewer": False,
			"is_muting_notes": False,
			"is_muting_reel": False,
			"is_private": False,
			"is_restricted": False,
			"is_supervised_by_viewer": False,
			"muting": False,
			"outgoing_request": False,
			"subscribed": False,
		}
		return Profile({
			**friendship,
			**profile,
			**viewer
		})

	#[Client.remember( Str browser, Cookies|Dict|Object|Str cookies, Dict|Headers|Object headers )]: SignIn
	def remember( self, browser:str, cookies:Cookies|dict|Object|str, headers:dict|Headers|Object ) -> SignIn:

		"""
		Remembering login credential.

		:params Str browser
		:params Str username
		:params Cookies|Dict|Object|Str cookies
		:params Dict|Headers|Object headers

		:return SignIn
		:raises AuthError|RequestAuthError
			When the login credentials, cookies or headers is invalid or expired
		:raises SignInError
			When an error occurs while logging in
		:raises TypeError
			When the parameter value is invalid value type
		:raises ValueError
			When the value is required or can't be empty
		"""

		# if username is None:
		# 	raise ValueError( "Username can't be empty" )
		# if not isinstance( username, str ):
		# 	raise TypeError( "Invalid \"username\" parameter, value type must be Str, {} passed".format( typeof( username) ) )
		if headers is None:
			headers = Client.HEADERS
		if not isinstance( headers, ( dict, Headers ) ):
			raise TypeError( "Invalid \"headers\" parameter, value must be type Dict|Headers, {} passed".format( typeof( headers ) ) )
		if isinstance( headers, Headers ):
			headers = dict( headers )
		if isinstance( headers, Object ):
			headers = headers.props()
		headers = {
			**Client.HEADERS,
			**headers
		}
		if browser is not None:
			if not isinstance( browser, str ):
				raise TypeError( "Invalid \"browser\" parameter, value must be type Str, {} passed".format( typeof( browser ) ) )
		else:
			if "User-Agent" not in self.headers:
				if self.settings.browser.default is not None:
					browser = self.settings.browser.default
				elif Client.BROWSER is not None:
					browser = Client.BROWSER
				else:
					browser = choice( self.settings.browser.randoms )
			else:
				browser = headers['User-Agent']
		if cookies is None:
			raise ValueError( "Cookies can't be empty" )
		if not isinstance( cookies, ( Cookies, dict, Object, str ) ):
			raise TypeError( "Invalid \"headers\" parameter, value must be type Cookies|Dict|Object|Str, {} passed".format( typeof( cookies ) ) )
		if isinstance( cookies, str ):
			cookies = Cookie.simple( cookies )
		if isinstance( cookies, Headers ):
			cookies = dict( cookies )
		if isinstance( cookies, ( dict, Object ) ):
			for require in [ "ds_user_id", "csrftoken", "sessionid" ]:
				if require not in cookies:
					raise SignInError( f"Invalid cookie, there is no \"{require}\" in the cookie" )

		session = Request( 
			timeout=self.settings.timeout,
			cookies=cookies, 
			headers={
				**headers,
				**{
					"Origin": "https://www.instagram.com",
					"Referer": "https://www.instagram.com/accounts/edit/",
					"User-Agent": browser,
					"X-CSRFToken": cookies['csrftoken']
				}
			}
		)

		try:
			request = session.get( f"https://www.instagram.com/api/v1/accounts/edit/web_form_data/" )
			content = request.json()
			status = request.status
			if status == 200:
				return SignIn({
					"authenticated": True,
					"user": {
						"id": request.cookies['ds_user_id'],
						"fullname": f"{content['form_data']['first_name']} {content['form_data']['last_name']}".strip(),
						"username": content['form_data']['username'],
						"usermail": content['form_data']['email'],
						"password": None,
						"csrftoken": cookies['csrftoken'],
						"sessionid": cookies['sessionid'],
						"session": {
							"browser": browser,
							"cookies": dict( session.cookies ),
							"headers": dict( session.headers )
						},
						"request": session
					}
				})
			elif status == 401:
				raise AuthError( "Failed to remember login credentials" )
			else:
				raise SignInError( content['message'] if "message" in content and content['message'] else "An error occured while checking user credential" )
		except AuthError as e:
			raise AuthError( "Failed to remember login credentials", prev=e )
	
	#[Client.remove( Friendship|Int|Profile|User, Bool remove ): Friendship
	@final
	@logged
	@avoidForMySelf
	def remove( self, user:Friendship|int|Profile|User, remove:bool ) -> Friendship:
		
		"""
		:raises FollowerError
			When something wrong e.g data user doest not available or error on request json responses
		"""
		
		...
	
	#[Client.restrict( Friendship|Int|Profile|User user, Bool restrict ): Friendship
	@final
	@logged
	@avoidForMySelf
	def restrict( self, user:Friendship|int|Profile|User, restrcit:bool ) -> Friendship:
		
		"""
		:raises RestrictError
			When something wrong e.g data user doest not available or error on request json responses
		"""
		
		...
	
	#[Client.savedCollectionList( List<Str> collectionTypes, Bool getCoverMediaLists, Int includePublicOnly, Str maxId )]: SavedCollectionList
	@final
	@logged
	def savedCollectionList( self, collectionTypes:list[str] = [ "ALL_MEDIA_AUTO_COLLECTION", "MEDIA", "AUDIO_AUTO_COLLECTION" ], getCoverMediaLists:bool=True, includePublicOnly:int=0, maxId:str="" ) -> SavedCollectionList:

		"""
		"""

		# Create request parameters.
		parameters = {
			"collection_types": collectionTypes,
			"get_cover_media_lists": getCoverMediaLists,
			"include_public_only": includePublicOnly,
			"max_id": maxId
		}

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{self.active.username}/saved/"
		})

		# Trying to get collection lists.
		request = self.request.get( "https://www.instagram.com/api/v1/collections/list/", params=parameters )
		content = request.json()
		status = request.status
		if status == 200:
			return SavedCollectionList( content )
		raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching collection list [{status}]" )
	
	#[Client.savedPosts()]: SavedPosts
	@final
	@logged
	def savedPosts( self ) -> SavedPosts:
		
		"""
		"""

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{self.active.username}/saved/all-posts/"
		})

		# Trying to get saved posts.
		request = self.request.get( "https://www.instagram.com/api/v1/feed/saved/posts/" )
		content = request.json()
		status = request.status
		if status == 200:
			return SavedPosts( content )
		raise ClientError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching saved posts [{status}]" )
	
	#[Client.saveEdit( Str biography, Str email, Str externalUrl, Str firstName, Str phoneNumber, Str username )]: Bool
	@final
	@logged
	def saveEdit( self, biography:str, email:str, externalUrl:str, firstName:str, phoneNumber:str, username:str ) -> bool:

		"""
		"""

		# Create request payload.
		payload = {
			"biography": biography,
			"chaining_enabled": "on",
			"email": email,
			"external_url": externalUrl,
			"first_name": firstName,
			"phone_number": phoneNumber,
			"username": username
		}

		# Update request headers.
		self.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/accounts/edit/"
		})

		# Trying to update gender.
		request = self.request.post( "https://www.instagram.com/api/v1/web/accounts/edit/", data=payload )
		content = request.json()
		status = request.status
		if status == 200:
			return True
		raise UserError( content['message'] if "message" in content and content['message'] else f"An error occurred while updating user info [{status}]" )
	
	#[Client.setGender( Int gender, Str custom )]: Bool
	@final
	@logged
	def setGender( self, gender:int, custom:str=None ) -> bool:
		
		"""
		Update or set account gender

		:params Int gender
		:params Str custom

		:return Bool
			True if success, otherwise if failed
		:raises TypeError
			When the parameter value is invalid value type
		:raises UserError
			When something wrong, please to check the request response history
		:raises ValueError
			When the gender is empty
		"""

		if gender is None:
			raise ValueError( "Gender can't be empty" )
		elif not isinstance( gender, int ):
			raise TypeError( "Invalid \"gender\" parameter, value must be type Int, {} passed".format( typeof( gender ) ) )
		
		# Creating request payload.
		payload = {
			"custom": custom,
			"gender": gender
		}

		# Update request headers.
		self.headers.update({
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/accounts/edit/"
		})

		# Trying to update gender.
		request = self.request.post( "https://www.instagram.com/api/v1/web/accounts/set_gender/", data=payload )
		content = request.json()
		status = request.status
		if status == 200:
			return True
		raise UserError( content['message'] if "message" in content and content['message'] else f"An error occurred while updating gender [{status}]" )
		

	#[Client.settings]: Setting
	@final
	@property
	def settings( self ) -> Settings: return self.__setting__

	#[Client.signin( Str browser, Str username, Str password )]: SignIn
	def signin( self, browser:str, username:str, password:str ) -> SignIn:
		
		"""
		Client login with username and password.

		:params Str browser
		:params Str username
		:params Str password

		:return SignIn
		:raises LockedError
			When the account is checpoint on login, but Instagram has lock the account
		:raises PasswordError
			When the username is found but the password is invalid
		:raises SignInError
			When an error occurs while logging in
		:raises SpamError
			When you try to login too many times
		:raises TypeError
			When the parameter value is invalid value type
		:raises UserNotFoundError
			When the username is not found, or the account or 
			IP Address has ben takedown by Instagram
		"""

		if browser is not None:
			if not isinstance( browser, str ):
				raise TypeError( "Invalid \"browser\" parameter, value must be type Str, {} passed".format( typeof( browser ) ) )
		else:
			if "User-Agent" not in self.headers:
				if self.settings.browser.default is not None:
					browser = self.settings.browser.default
				elif Client.BROWSER is not None:
					browser = Client.BROWSER
				else:
					browser = choice( self.settings.browser.randoms )
		
		# To avoid collisions according to csrftoken.
		request = Request( headers=Client.HEADERS, timeout=self.settings.timeout )

		# For avoid incompatible User-Agent with csrftoken.
		request.headers.update({ "User-Agent": browser })

		if self.authenticated:
			active = self.active
			self.__active__ = None
			session = self.request
			self.__request__ = request
			
			# Tring get csrftoken
			csrftoken = self.csrftoken

			# Backing up previous active session.
			self.__active__ = active
			self.__request__ = session
		else:
			csrftoken = self.csrftoken
		
		# Update request headers.
		request.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/",
			"User-Agent": browser,
			"X-CSRFToken": csrftoken,
			"Content-Type": "application/x-www-form-urlencoded",
		})

		# Trying to login instagram account.
		signin = request.post( "https://www.instagram.com/api/v1/web/accounts/login/ajax/", allow_redirects=True, data={
			"username": username,
			"enc_password": encpaswd( password ),
			"queryParams": {},
			"optIntoOneTap": "false"
		})
		content = signin.json()
		if "authenticated" in content:
			if content['authenticated'] is False:
				raise PasswordError( f"Incorrect password for user \"{username}\", or may have been changed" )
			id = signin.cookies['ds_user_id']
			password = "hex[b64]\"{}\"".format( String.encode( password ) )
			csrftoken = signin.cookies['csrftoken']
			sessionid = signin.cookies['sessionid']
			return SignIn({
				"authenticated": True,
				"user": {
					"id": id,
					"fullname": None,
					"username": username,
					"usermail": None,
					"password": password,
					"csrftoken": csrftoken,
					"sessionid": sessionid,
					"session": {
						"browser": browser,
						"cookies": dict( signin.cookies ),
						"headers": dict( request.headers )
					},
					"request": request
				}
			})
		elif "checkpoint_url" in content:
			if "lock" in content and content['lock'] is True:
				raise LockedError( "Your account has been checkpointed and locked by Instagram" )
			return SignIn({
				"authenticated": False, 
				"checkpoint": Checkpoint( content ),
				"request": request,
				"response": signin
			})
		elif "spam" in content:
			raise SpamError( "Oops! Looks like you are considered Spam! Please try again later" )
		elif "two_factor_required" in content:
			raise ClientError( "Two Factor Authentication required" )
		else:
			raise UserNotFoundError( f"User \"{username}\" not found, or may be missing" )

	#[Client.story( Int|List[Int|Str]|Story target, Story.Type flag )]: Story
	@logged
	def story( self, target:int|list[int|str]|Story, flag:Story.Type=None ) -> Story:

		"""
		Get story info or media.

		Retrieve Instagram stories based on URLs, This also includes
		the URL of the user's profile, shared stories and the like,
		the ID from the story and the user's id, and also the
		user's username.

		Please note, if you use username or id, this will not return the media
		story directly, but you will also have to resend the request, it is highly
		recommended to use user id instead of username.

		:params Int|List[Int|Str]|Story target
		:params Story.Type flag

		:return StoryFeedTrayReels<StoryFeedTrayReel:reels<StoryItem<User>[],User>,StoryFeedTrayReel:media<StoryItem<User>[],User>>|
				StoryHighlights<StoryHightlight:reels<StoryItem<User>[],User>,StoryHightlight:media<StoryItem<User>[],User>>|
				StoryProfile<Chaining[],StoryProfileEdge<User>[],StoryReel<User>>
		"""

		#[Cient.story$.getByProfile( Int id, Str username, Story.Type flag )]: StoryProfile<Chaining[],StoryProfileEdge<User>[],StoryReel<User>>
		def getByProfile( id:int=None, username:str=None, flag:Story.Type=Story.PROFILE ) -> StoryProfile:
			
			"""
			Get story info by username or id.

			Please note, if you use username or id, this will not return the media
			story directly, but you will also have to resend the request, it is highly
			recommended to use user id instead of username.

			:params Int id
			:params Str username

			:return StoryProfile<Chaining[],StoryProfileEdge<User>[],StoryReel<User>>
			"""

			headers = {
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/"
			}
			variables = {
				"query_hash": "d4d88dc1500312af6f937f7b804c68c3",
				"include_chaining": "false",
				"include_suggested_users": "false",
				"include_logged_out_extras": "false",
				"include_live_status": "false",
				"include_reel": "true",
				"include_highlight_reels": "true"
			}

			if flag == Story.HIGHLIGHT:
				variables['include_reel'] = "false"
			elif flag == Story.TIMELINE:
				variables['include_highlight_reels'] = "false"
			if id is None:
				profile = self.user( username=username, count=3 )
				headers['Referer'] = f"https://www.instagram.com/{username}/"
				variables['user_id'] = profile.id
			else:
				variables['user_id'] = id
			
			# Trying to get data from graphql.
			return self.graphql( binding=StoryProfile, headers=headers, params=variables )

			# if "reel" in graphql:
			# 	for key in [ "owner", "user" ]:
			# 		if key in graphql['reel']:
			# 			graphql['reel'][key] = User( graphql['reel'][key] )
			# 	graphql['reel'] = StoryReel( graphql['reel'] )
			# if "edge_highlight_reels" in graphql:
			# 	for i in range( len( graphql.edge_highlight_reels.edges ) ):
			# 		graphql.edge_highlight_reels.edges[i] = StoryProfileEdge( graphql.edge_highlight_reels.edges[i] )
			# 		if "owner" in graphql.edge_highlight_reels.edges[i]:
			# 			graphql.edge_highlight_reels.edges[i]['owner'] = User( graphql.edge_highlight_reels.edges[i]['owner'] )
			
			# return graphql

		if target is None:
			raise ValueError( "Story target id or url required" )
		elif isinstance( target, int ):
			if flag is None:
				raise StoryError( "Unknown story type" )
			elif not isinstance( flag, Story.Type ):
				raise TypeError( "Invalid \"flag\" parameter, value must be type Story.Type, {} passed".format( typeof( flag ) ) )
			if flag == Story.PROFILE:
				return getByProfile( id=target )
			return self.story( target=[target], flag=flag )
		elif isinstance( target, str ):
			capt = match( Pattern.STORY, target )
			if capt is not None:
				groups = capt.groupdict()
				if "profile" in groups and groups['profile'] is not None:
					return getByProfile( username=groups['profile'], flag=Story.PROFILE if flag is None else flag )
				elif "username" in groups and groups['username'] is not None:
					return getByProfile( username=groups['username'], flag=Story.PROFILE if flag is None else flag )
				elif "timeline" in groups and groups['timeline'] is not None:
					profile = getByProfile( username=groups['user'], flag=Story.TIMELINE )
					return self.story( target=[profile.reel.latest_reel_media], flag=Story.TIMELINE )
				elif "highlight" in groups and groups['highlight'] is not None:
					return self.story( target=[groups['highlight']], flag=Story.HIGHLIGHT )
				else:
					return self.story( target=[groups['id']], flag=flag )
			raise StoryError( "Invalid story ids, or url" )
		elif isinstance( target, list ):
			if flag is None:
				raise StoryError( "Unknown story type" )
			elif flag == Story.PROFILE:
				raise StoryError( "Unsupported for get story from multiple story" )
			elif not isinstance( flag, Story.Type ):
				raise TypeError( "Invalid \"flag\" parameter, value must be type Story.Type, {} passed".format( typeof( flag ) ) )
			for i in range( len( target ) ):
				ids = target[i]
				if flag == Story.HIGHLIGHT:
					if match( r"^highlight\:", str( ids ) ) is None:
						ids = f"highlight:{ids}"
				if match( r"^reel_ids\=", str( ids ) ) is None:
					target[i] = f"reel_ids={ids}"
		elif isinstance( target, StoryFeed ):
			return self.story( target=[ tray.id for tray in target.tray ], flag=Story.TIMELINE )
		elif isinstance( target, StoryFeedTray ):
			return self.story( target=[ target.id ], flag=Story.TIMELINE )
		elif isinstance( target, StoryProfile ):
			if flag == Story.PROFILE:
				return self.story( target=target.reel.id, flag=Story.PROFILE )
			return self.story( target=[ highlight.id for highlight in target.edge_highlight_reels.edges ], flag=Story.HIGHLIGHT )
		elif isinstance( target, StoryProfileEdge ):
			return self.story( target=target.id, flag=Story.HIGHLIGHT )
		elif isinstance( target, StoryReel ):
			return self.story( target=target.id, flag=Story.PROFILE )
		elif isinstance( target, StoryItem ):
			raise TypeError( "Objects are item values, you can't do this" )
		elif isinstance( target, ( StoryFeedTrayReel, StoryHighlight, StoryHighlights ) ):
			raise TypeError( "Unable to get story from {}, because the object contains a list of story items".format( typeof( target ) ) )
		else:
			raise TypeError( "Invalid \"target\" parameter, value must be type Story, {} passed".format( typeof( target ) ) )
		
		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})

		# "query_hash": "297c491471fff978fa2ab83c0673a618"
		# "reel_ids": "3220634093712374533"

		# Trying get story media.
		request = self.request.get( "https://www.instagram.com/api/v1/feed/reels_media/?{}".format( "\x26".join( target ) ) )
		content = request.json()
		status = request.status
		if status == 200:
			# wrapper = StoryFeedTrayReel if flag == Story.TIMELINE else StoryHighlight
			# results = StoryFeedTrayReels if flag == Story.TIMELINE else StoryHighlights
			# for key in list( content['reels'].keys() ):
			# 	for i in range( len( content['reels'][key]['items'] ) ):
			# 		content['reels'][key]['items'][i]['user'] = User( content['reels'][key]['items'][i]['user'] )
			# 		content['reels'][key]['items'][i] = StoryItem( content['reels'][key]['items'][i] )
			# 	content['reels'][key]['user'] = User( content['reels'][key]['user'] )
			# 	content['reels'][key] = wrapper( content['reels'][key] )
			# for i in range( len( content['reels_media'] ) ):
			# 	for u in range( len( content['reels_media'][i]['items'] ) ):
			# 		content['reels_media'][i]['items'][u]['user'] = User( content['reels_media'][i]['items'][u]['user'] )
			# 		content['reels_media'][i]['items'][u] = StoryItem( content['reels_media'][i]['items'][u] )
			# 	content['reels_media'][i]['user'] = User( content['reels_media'][i]['user'] )
			# 	content['reels_media'][i] = wrapper( content['reels_media'][i] )
			# return results( content )
			return StoryFeedTrayReels( content ) if flag == Story.TIMELINE else StoryHighlights( content )
		else:
			raise StoryError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching story media info [{status}]" )

	#[Client.stories( Bool isFollowingFeed )]: StoryFeed<StoryFeedTray>
	@logged
	def stories( self, isFollowingFeed:bool=False ) -> StoryFeed:

		"""
		Get feed stories.

		:params Bool isFollowingFeed
			Default is False

		:return StoryFeed
		:raises StoryError
			When something wrong, please to check the request response history
		"""

		# Update request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/"
		})

		# Trying to get feed story.
		request = self.request.get( "https://www.instagram.com/api/v1/feed/reels_tray", params={ "is_following_feed": f"{isFollowingFeed}".lower() } )
		content = request.json()
		status = request.status
		if status == 200:
			# content = StoryFeed( content )
			# for i in range( len( content.tray ) ):
			# 	content.tray[i] = StoryFeedTray( content.tray[i] )
			# 	for key in [ "owner", "user" ]:
			# 		if key in content.tray[i][key]:
			# 			content.tray[i][key] = User( content.tray[i][key] )
			return StoryFeed( content )
		else:
			raise StoryError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching feed story [{status}]" )

	#[Client.switch( Str username, Bool save )]: None
	def switch( self, username:str, save:bool=True ) -> None:
		
		"""
		Change current authenticated user.

		:params Str username
		:params Bool save
			Allow changes to be saved in the configuration file.
		
		:return None
		:raises TypeError
			When the parameter value is invalid value type
		:raises ValueError
			When the username is empty or user not found
		"""

		if username is None:
			raise ValueError( "Username can't be empty" )
		if not isinstance( username, str ):
			raise TypeError( "Invalid \"username\" parameter, value must be type Str, {} passed".format( typeof( username ) ) )
		if username not in self.settings.signin.switch:
			raise TypeError( "There is no saved account with username {}".format( username ) )
		self.settings.signin.default = username
		self.activate( Active( self.settings.signin.switch[username] ) )
		if save:
			self.config.save()
	
	#[Client.user( Str username )]: User
	@logged
	def user( self, username:str, count:int=3 ) -> User:

		"""
		Get simple user info.

		:params Str username
		:params Int count
			Default is 12

		:return User
		:raises TypeError
			When the parameter value is invalid value
		:raises UserError
			When the user data does not available
			When there are unexpected error found
		:raises UserNotFoundError
			When the user is not found
		:raises ValueError
			When the username is empty
		"""

		if username is None:
			raise ValueError( "Username can't be empty" )
		elif not isinstance( username, str ):
			raise TypeError( "Invalid \"username\" parameter, value must be type Str, {} passed".format( typeof( username ) ) )

		# Updating request headers.
		self.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": f"https://www.instagram.com/{username}/"
		})

		# Trying to get user info.
		request = self.request.get( f"https://www.instagram.com/api/v1/feed/user/{username}/username/", params={ "count": count } )
		content = request.json()
		status = request.status
		if status == 200:
			if "user" in content:
				return User({ **content, "id": content['user']['pk'] })
			raise UserNotFoundError( f"Target \"{username}\" user not found" )
		elif status == 404:
			raise UserNotFoundError( f"Target \"{username}\" user not found" )
		else:
			raise UserError( content['message'] if "message" in content and content['message'] else f"An error occurred while fetching the user [{status}]" )
	