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

from kanashi.config import Config
from kanashi.error import AuthError, BlockError, FavoriteError, FollowError, ReportError, RestrictError, UserError, UserNotFoundError
from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.request import RequestRequired
from kanashi.utility import File, String


#[kanashi.profile.ProfilePriperties]
class ProfileProperties:
	
	@property
	def bestie( self ):
		return self.isBestie
	
	@property
	def biography( self ):
		return self.profile.biography
	
	@property
	def biographyFormat( self ):
		return "\x20\x20{}".format( self.biographyRawText.replace( "\n", "\x0a\x20\x20\x20\x20\x20\x20" ) )
	
	@property
	def biographyEntities( self ):
		return self.profile.biography_with_entities.entities
	
	@property
	def biographyEntityUsers( self ):
		users = []
		entities = self.biographyEntities
		for entity in entities:
			if  user := entity.user:
				users.append( user.username )
		return users
	
	@property
	def biographyEntityUsersFormat( self ):
		return "-\x20@{}".format( "\x0a\x20\x20\x20\x20-\x20@".join( self.biographyEntityUsers ) )
	
	@property
	def biographyEntityHashtags( self ):
		hashtags = []
		entities = self.biographyEntities
		for entity in entities:
			if  hashtag := entity.hashtag:
				hashtags.append( hashtag.name )
		return hashtags
	
	@property
	def biographyEntityHashtagsFormat( self ):
		return "-\x20#{}".format( "\x0a\x20\x20\x20\x20-\x20#".join( self.biographyEntityHashtags ) )
	
	@property
	def biographyRawText( self ):
		if  self.profile.biography_with_entities.raw_text == None:
			self.profile.biography_with_entities.raw_text = ""
		return self.profile.biography_with_entities.raw_text
	
	@property
	def blockedByViewer( self ):
		return self.profile.blocked_by_viewer
	
	@property
	def categoryName( self ):
		return self.profile.category_name
	
	@property
	def countEdgeFelixVideoTimeline( self ):
		return self.profile.edge_felix_video_timeline.count
	
	@property
	def countEdgeFollow( self ):
		return self.profile.edge_follow.count
	
	@property
	def countEdgeFollowedBy( self ):
		return self.profile.edge_followed_by.count
	
	@property
	def countEdgeMediaCollections( self ):
		return self.profile.edge_mutual_followed_by.count
	
	@property
	def countEdgeMutualFollowedBy( self ):
		return self.profile.edge_mutual_followed_by.count
	
	@property
	def countEdgeOwnerToTimelineMedia( self ):
		return self.profile.edge_owner_to_timeline_media.count
	
	@property
	def countEdgeSavedMedia( self ):
		return self.profile.edge_saved_media.count
	
	@property
	def edgeFelixVideoTimeline( self ):
		return self.profile.edge_felix_video_timeline.edges
	
	@property
	def edgeFollow( self ):
		return self.profile.edge_follow.edges
	
	@property
	def edgeFollowedBy( self ):
		return self.profile.edge_followed_by.edges
	
	@property
	def edgeMediaCollections( self ):
		return self.profile.edge_media_collections.edges
	
	@property
	def edgeMutualFollowedBy( self ):
		return self.profile.edge_mutual_followed_by.edges
	
	@property
	def edgeOwnerToTimelineMedia( self ):
		return self.profile.edge_owner_to_timeline_media.edges
	
	@property
	def edgeSavedMedia( self ):
		return self.profile.edge_saved_media.edges
	
	@property
	def followedByViewer( self ):
		return self.profile.followed_by_viewer
	
	@property
	def followsViewer( self ):
		return self.profile.follows_viewer
	
	@property
	def fullname( self ):
		return self.profile.full_name
	
	@property
	def fullnameFormat( self ):
		name = []
		if  self.fullname:
			name.append( self.fullname )
		else:
			pass
		name.append( f"({self.username})" )
		if  self.isVerified:
			name.append( "\x1b[1;36m√\x1b[0m" )
		return "\x20".join( name )
	
	@property
	def hasBlockedViewer( self ):
		return self.profile.has_blocked_viewer
	
	@property
	def id( self ):
		return self.profile.id
	
	@property
	def isBestie( self ):
		return self.profile.is_bestie
	
	@property
	def isBlockingReel( self ):
		return self.profile.is_blocking_reel
	
	@property
	def isBusinessAccount( self ):
		return self.profile.is_business_account
	
	@property
	def isEligibleToSubscribe( self ):
		return self.profile.is_eligible_to_subscribe
	
	@property
	def isEmbedsDisabled( self ):
		return self.profile.is_embeds_disabled
	
	@property
	def isFeedFavorite( self ):
		return self.profile.is_feed_favorite
	
	@property
	def isGuardianOfViewer( self ):
		return self.profile.is_guardian_of_viewer
	
	@property
	def isSupervisedByViewer( self ):
		return self.profile.is_supervised_by_viewer
	
	@property
	def isJoinedRecently( self ):
		return self.profile.is_joined_recently
	
	@property
	def isMutingNotes( self ):
		return self.profile.is_muting_profile
	
	@property
	def isMutingReel( self ):
		return self.profile.is_muting_reel
	
	@property
	def isMySelf( self ):
		return self.profile.id == self.viewer.id
	
	@property
	def isNotMySelf( self ):
		return self.profile.id != self.viewer.id
	
	@property
	def isPrivateAccount( self ):
		return self.profile.is_private
	
	@property
	def isProfessionalAccount( self ):
		return self.profile.is_professional_account
	
	@property
	def isSupervisedUser( self ):
		return self.profile.is_supervised_user
	
	@property
	def isVerified( self ):
		return self.profile.is_verified
	
	@property
	def muting( self ):
		return self.profile.muting
	
	@property
	def profilePicture( self ):
		return self.profile.rofile_pic_url
	
	@property
	def profilePictureHD( self ):
		if  self.profile.isset( "hd_profile_pic_url_info" ):
			return self.profile.hd_profile_pic_url_info.url
		elif  self.profile.isset( "hd_profile_pic_versions" ):
			return self.profile.hd_profile_pic_versions[-1].url
		return self.profile.profile_pic_url_hd
	
	@property
	def profilePictureHDResolution( self ):
		if  self.profile.isset( "hd_profile_pic_url_info" ):
			return "{}x{}".format(
				self.profile.hd_profile_pic_url_info.width,
				self.profile.hd_profile_pic_url_info.height
			)
		elif  self.profile.isset( "hd_profile_pic_versions" ):
			return "{}x{}".format(
				self.profile.hd_profile_pic_versions[-1].width,
				self.profile.hd_profile_pic_versions[-1].height
			)
		return "320x320"
	
	@property
	def pronouns( self ):
		return self.profile.pronouns
	
	@property
	def pronounsFormat( self ):
		if  self.pronouns:
			return "/".join( self.pronouns )
		return ""
	
	@property
	def requestedFollow( self ):
		return self.profile.incoming_request
	
	@property
	def requestedByViewer( self ):
		return self.profile.requested_by_viewer
	
	@property
	def restrictedByViewer( self ):
		return self.profile.restricted_by_viewer
	
	@property
	def subscribed( self ):
		return self.profile.subscribed
	
	@property
	def username( self ):
		return self.profile.username
	

#[kanashi.profile.Profile]
class Profile( ProfileProperties, Readonly, RequestRequired ):
	
	#[Profile.ATTRIBUTES]
	ATTRIBUTES = [
	]
	
	#[Profile( Object viewer, Request request, Dict profile, Mixed **kwargs )]: None
	def __init__( self, viewer, request, profile, **kwargs ):
		
		"""
		Construct method of class Profile.
		
		:params Object viewer
			Object represent user active
		:params Request request
			Object instance of request
		:params Dict profile
			User profile
		
		:return None
		"""
		
		# Viewer login information.
		self.viewer = viewer
		
		# Save profile user info.
		self.profile = Object( profile )
		
		# Instance of class Parent.
		self.__parent__ = super()
		self.__parent__.__init__( request )
		
		# Inherited methods from clients if available.
		self.__methods__ = kwargs.pop( "methods", {} )
	
	#[Profile.__getitem__( String key )]: Mixed
	def __getitem__( self, key ):
		return self.profile[key]
	
	#[Profile.__setitem__( String key, Mixed value )]: Mixed
	def __setitem__( self, key, value ):
		return self.profile.set({ key: value })
	
	#[Profile.prints]: List
	@property
	def prints( self ):
		
		"""
		Don't call this when you get profile info with id.
		This is only usage for Main class from kanashi.main.Main
		"""
		
		# General information to be displayed.
		# The empty string will be used for the new line.
		prints = [
			"",
			"id",
			"username",
			"fullname",
			"",
			"pronouns",
			"",
			"category",
			"",
			"account",
			"",
			"website",
			"",
			"biography",
			"",
			"follow",
			"",
			"block",
			"",
			"restrict",
			"muting",
			"",
			"bestie",
			"favorite",
			"",
			"edges",
			""
		]
		
		for i in range( len( prints ), 0, -1 ):
			idx = i -1
			val = prints[idx]
			match val:
				case "id":
					prints[idx] = f"ID|PK {self.id}"
				case "fullname":
					prints[idx] = f"Fullname \x1b[1;37m{self.fullname}\x1b[0m"
				case "username":
					prints[idx] = f"Username \x1b[1;38;5;189m{self.username}\x1b[0m"
					if  self.isVerified:
						prints[idx] += "\x20\x1b[1;36m√\x1b[0m"
				case "pronouns":
					prints[idx] = "\x0a\x20\x20\x20\x20\x20\x20..\x20".join([ "- Pronouns", self.pronounsFormat if self.pronounsFormat else "None" ])
				case "category":
					if  self.isProfessionalAccount:
						prints[idx] = "\x0a\x20\x20\x20\x20\x20\x20..\x20".join([ "- Category", self.categoryName if self.categoryName else "None" ])
					else:
						prints[idx] = "\x0a\x20\x20\x20\x20\x20\x20..\x20".join([ "- Category", "Not a Professional Account" ])
				case "account":
					account = []
					if  self.isPrivateAccount:
						account.append( "Private" )
					else:
						account.append( "Public" )
						if  self.isBusinessAccount:
							account.append( "Business" )
						if  self.isProfessionalAccount:
							account.append( "\x20Professional" )
					prints[idx] = "\x0a\x20\x20\x20\x20\x20\x20..\x20".join([ "- Account", "/".join( account ) ])
				case "website":
					prints[idx] = [ "- Website" ]
					if  self['bio_links']:
						if  "title" in self['bio_links'][0]:
							prints[idx].append( "Title {}".format( self['bio_links']['title'] ) )
						prints[idx].append( self['bio_links'][0]['link_type'].capitalize() )
						prints[idx].append( "\x1b[1;38;5;81m{}\x1b[0m".format( self['bio_links'][0]['url'] ) )
					else:
						prints[idx].append( "None" )
					prints[idx] = "\x0a\x20\x20\x20\x20\x20\x20..\x20".join( prints[idx] )
				case "biography":
					if  self.biography:
						prints[idx] = "\x0a\x20\x20\x20\x20".join([
							"----------------------------------------",
							"- Biography",
							"----------------------------------------",
							"{}".format( self.biographyFormat ),
							"----------------------------------------",
							"- Biography Entities",
							"----------------------------------------",
							"- Biography Entitity Users",
							"----------------------------------------",
							"{}".format( self.biographyEntityUsersFormat if self.biographyEntityUsers else "- None" ),
							"----------------------------------------",
							"- Biography Entitity Hashtags",
							"----------------------------------------",
							"{}".format( self.biographyEntityHashtagsFormat if self.biographyEntityHashtags else "- None" ),
							"----------------------------------------"
						])
					else:
						del prints[idx]
				case "block":
					if  self.isMySelf:
						prints[idx] = "- Block is not available for own profile"
					else:
						block = []
						if  self.hasBlockedViewer:
							block.append( "- This user has blocked your account" )
						else:
							block.append( "- This user did not block your account" )
						if  self.blockedByViewer:
							block.append( "- You have blocked this user" )
						else:
							block.append( "- You did not block this user" )
						prints[idx] = "\x0a\x20\x20\x20\x20".join( block )
				case "muting":
					if  self.isNotMySelf:
						if  self.muting:
							prints[idx] = "- You have mute this user"
						else:
							prints[idx] = "- You did not mute this user"
					else:
						prints[idx] = "- Mute is not available for own profile"
				case "restrict":
					if  self.isNotMySelf:
						if  self.restrictedByViewer:
							prints[idx] = "- You have restrict this user"
						else:
							prints[idx] = "- You did not restrict this user"
					else:
						prints[idx] = "- Restrict is not available for own profile"
				case "bestie":
					if  self.isNotMySelf:
						if  self.isBestie:
							prints[idx] = "- This user is your bestie"
						else:
							prints[idx] = "- This user is not your bestie"
					else:
						prints[idx] = "- Bestie is not available for own profile"
				case "favorite":
					if  self.isNotMySelf:
						if  self.isFeedFavorite:
							prints[idx] = "- This user feed is your favourite"
						else:
							prints[idx] = "- This user feed is not your favourite"
					else:
						prints[idx] = "- Favorite is not available for own profile"
				case "follow":
					if  self.isMySelf:
						prints[idx] = "- Follow is not available for own profile"
					else:
						follow = []
						if  self.followsViewer:
							follow.append( "- This user is following your account" )
						elif self.requestedFollow:
							follow.append( "- This user is requested follow your account" )
						else:
							follow.append( "- This user is not following your account" )
						if  self.followedByViewer:
							follow.append( "- You have followed this user" )
						elif self.requestedByViewer:
							follow.append( "- Your follow request has not been approved" )
						else:
							follow.append( "- You are not following this user" )
						prints[idx] = "\x0a\x20\x20\x20\x20".join( follow )
				case "edges":
					prints[idx] = "\x0a\x20\x20\x20\x20".join([
						"----------------------------------------",
						"┌───────┬───────┬────────┬─────────────┐",
						"│ Posts │ Felix │ Saveds │ Collections │",
						"├───────┼───────┼────────┼─────────────┤",
						"│ {} │ {} │ {} │ {} │",
						"└───────┴───────┴────────┴─────────────┘",
						"----------------------------------------",
						"┌─────────────┬─────────────┬──────────┐",
						"│  Followers  │  Following  │  Mutual  │",
						"├─────────────┼─────────────┼──────────┤",
						"│ {} │ {} │ {} │",
						"└─────────────┴─────────────┴──────────┘",
						"----------------------------------------"
					])
					prints[idx] = prints[idx].format(*[
						f"{self.countEdgeOwnerToTimelineMedia}".center( 5 ),
						f"{self.countEdgeFelixVideoTimeline}".center( 5 ),
						f"{self.countEdgeSavedMedia}".center( 6 ),
						f"{self.countEdgeMediaCollections}".center( 11 ),
						f"{self.countEdgeFollowedBy}".center( 11 ),
						f"{self.countEdgeFollow}".center( 11 ),
						f"{self.countEdgeMutualFollowedBy}".center( 8 ),
					])
				case _:
					pass
			pass
		return prints
	
	#[Profile.bestie()]: Object
	def bestie( self ):
		
		"""
		Make bestie or unbestie user.
		
		:return Object
			Bestie result representation
		:raises BestieError
			...
		"""
		
		if  self.isMySelf:
			raise BestieError( "Unable to set yourself as a bestie" )
		if  self.followedByViewer:
			self.headers.update({
				"Accept-Encoding": "gzip, deflate, br",
				"Content-Type": "application/json",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/{}/".format( self.username )
			})
			data = {
				"add": [],
				"remove": [],
				"source": "profile"
			}
			if  self.isBestie:
				action = "Remove Bestie"
				data['remove'].append( self.id )
			else:
				action = "Adding Bestie"
				data['add'].append( self.id )
			request = self.request.post( "https://www.instagram.com/api/v1/friendships/set_besties/", json=data )
			status = request.status_code
			if  status == 200:
				response = request.json()
				if  "friendship_statuses" in response:
					self.profile.is_bestie = False if self.isBestie else True
					return Object( response['friendship_statuses'] )
				else:
					raise BestieError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
			else:
				self.throws( action, status )
		else:
			raise BestieError( "Can't set user as bestie before following" )
	
	#[Profile.block()]: Object
	def block( self ):
		
		"""
		Block or unblock user.
		
		:return Object
			Block result representation
		:raises BlockError
			...
		"""
		
		if  self.isMySelf:
			raise BlockError( "Unable to block or unblock yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		if  self.blockedByViewer:
			target = "https://www.instagram.com/api/v1/web/friendships/{}/unblock/"
			action = "Unblock"
		else:
			target = "https://www.instagram.com/api/v1/web/friendships/{}/block/"
			action = "Blocking"
		request = self.request.post( target.format( self.id ) )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				self.profile.blocked_by_viewer = False if self.blockedByViewer else True
				return Object({
					"id": self.id,
					"username": self.username,
					"blocking": self.blockedByViewer
				})
			else:
				raise BlockError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
	
	#[Profile.confirm( Bool follow )]:
	def confirm( follow ):
		
		"""
		Confirm/ aprove or ignore request follow from user.
		"""
		
		if  not self.requestedFollow:
			raise ProfileError( "This user does not sent request to follow your account" )
		elif self.isMySelf:
			raise ProfileError( "Unable to aprove or ignore request follow for yourself" )
		else:
			pass
	
	#[Profile.export( String fname )]: None
	def export( self, fname=None ):
		
		"""
		Export profile info.
		
		:params String fname
			File name to save
			By default, Kanashī will save it in
			the ~/onsaved/exports/profile/ folder. To change
			it, please add a slash (/) before the filename,
			e.g /sdcard/path/filename without the file extension .json
		
		:return None
		:raise ProfileError
			When failed export profile info
		"""
		
		if  not isinstance( fname, str ):
			fname = self.username
		fdata = self.profile.json()
		if  fname[0] != "/":
			fname = Config.ONSAVED['export']['profile'].format( fname )
		else:
			fname = "{}.json".format( fname )
		try:
			File.write( fname, fdata )
		except Exception as e:
			raise ProfileError( "Failed to export profile info", prev=e )
	
	#[Profile.favorite()]: Object
	def favorite( self ):
		
		"""
		Make favorite or unfavorit user.
		
		:return Object
			Favorite result represent
		:raises FavoriteError
			...
		"""
		
		if  self.isMySelf:
			raise FavoriteError( "Unable to set yourself as a favourite" )
		if  self.followedByViewer:
			self.headers.update({
				"Accept-Encoding": "gzip, deflate, br",
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://www.instagram.com",
				"Referer": "https://www.instagram.com/{}/".format( self.username )
			})
			data = { "source": "profile" }
			if  self.isFeedFavorite:
				action = "Remove favorite"
				data['remove'] = [ self.id ]
			else:
				action = "Make favorite"
				data['add'] = [ self.id ]
			request = self.request.post( "https://www.instagram.com/api/v1/friendships/update_feed_favorites/", data=data )
			status = request.status_code
			if  status == 200:
				response = request.json()
				if  "status" in response and response['status'] == "ok":
					self.profile.is_feed_favorire = False if self.isFeedFavorite else True
					return Object({
						"id": self.id,
						"username": self.username,
						"favorite": self.isFeedFavorite
					})
				else:
					raise FavoriteError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
			else:
				self.throws( action, status )
		else:
			raise FavoriteError( "Can't set user as favorite before following" )
	
	#[Profile.follow()]: Object
	def follow( self ):
		
		"""
		Follow or follow user.
		
		:return Object
			Follow result represent
		:raises FollowError
			...
		"""
		
		if  self.isMySelf:
			raise FollowError( "Unable to follow or unfollow yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		data = {
			"container_module": "\x70\x72\x6f\x66\x69\x6c\x65",
			"nav_chain": "\x50\x6f\x6c\x61\x72\x69\x73\x50\x72\x6f\x66\x69\x6c\x65\x52\x6f\x6f\x74\x3a\x70\x72\x6f\x66\x69\x6c\x65\x50\x61\x67\x65\x3a\x31\x3a\x76\x69\x61\x5f\x63\x6f\x6c\x64\x5f\x73\x74\x61\x72\x74",
			"user_id": self.id
		}
		if  self.followedByViewer:
			target = f"https://www.instagram.com/api/v1/friendships/destroy/{self.id}/"
			action = "Unfollow"
		elif self.requestedByViewer:
			target = f"https://www.instagram.com/api/v1/friendships/destroy/{self.id}/"
			action = "Cancel request follow"
		else:
			target = f"https://www.instagram.com/api/v1/friendships/create/{self.id}/"
			action = "Following"
		request = self.request.post( target, data=data )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "friendship_status" in response:
				follow = response['friendship_status']
				self.profile.requested_by_viewer = follow['outgoing_request']
				self.profile.outgoing_request = follow['outgoing_request']
				self.profile.incoming_request = follow['incoming_request']
				self.profile.followed_by_viewer = follow['following']
				self.profile.is_private = follow['is_private']
				return Object({
					"id": self.id,
					"private": self.isPrivateAccount,
					"username": self.username,
					"following": self.followedByViewer,
					"requested": self.requestedByViewer
				})
			else:
				raise FollowError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
	
	#[Profile.remove()]: Object
	def remove( self ):
		
		"""
		Remove user from followers.
		"""
		
		if  not self.followsViewer:
			raise ProfileError( "This user does not following your account" )
		elif self.isMySelf:
			raise ProfileError( "Unable to remove yourself from follower" )
		else:
			pass
	
	#[Profile.report( Dict|Object options )]: Object
	def report( self, options ):
		
		"""
		Report user account.
		
		:return Object
			Report result represent
		:raises ReportError
			...
		"""
	
	#[Profile.restrict()]: Object
	def restrict( self ):
		
		"""
		Restrict or unrestrict user.
		
		:return Object
			Restrict result represent
		:raises RestrictError
			...
		"""
		
		if  self.isMySelf:
			raise RestrictError( "Unable to restrict or unrestrict yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		if  self.restrictedByViewer:
			action = "Restrict"
			target = "https://www.instagram.com/api/v1/web/restrict_action/restrict/"
		else:
			action = "Unrestrict"
			target = "https://www.instagram.com/api/v1/web/restrict_action/unrestrict/"
		data = { "target_user_id": self.id }
		request = self.request.post( target, data=data )
		status = request.status_code
		if  status == 200:
			response = request.json()
			if  "status" in response and response['status'] == "ok":
				self.profile.restricted_by_viewer = False if self.restrictedByViewer else True
				return Object({
					"id": self.id,
					"username": self.username,
					"restrict": self.restrictedByViewer
				})
			else:
				raise RestrictError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
		pass
	
	#[Profile.profilePictureSave( String name, Bool random )]: Object
	def profilePictureSave( self, name=None, random=False ):
		
		"""
		Download profile picture user.
		
		:return Object
			Download result represent
		"""
		
		if  not isinstance( name, str ):
			if  random:
				name = String.random( 32 )
				name += "-{}".format( self.profilePictureHDResolution )
			else:
				name = "{} ({}) {}".format( self.fullname, self.username, self.profilePictureHDResolution )
		if  name[0] != "/":
			fname = Config.ONSAVED['media']['profile'].format( name )
		else:
			fname = "{}.json".format( name )
		self.request.save( url := self.profilePictureHD, fname, fmode="wb" )
		return Object({
			"url": url,
			"fmode": "wb",
			"fname": name,
			"saved": fname
		})
	
	#[Profile.throws( String action, int status )]: None
	def throws( self, action, status ):
		
		"""
		Raises common errors in when request.
		
		:params String action
			Request action
		:params Int status
			Request response satus code
		
		:return None
		:raises AuthError
			...
		:raises UserNotFoundError
			...
		:raises UserError
			...
		"""
		
		match status:
			case 404:
				raise UserNotFoundError( f"Target \"{self.username}\" user not found" )
			case _:
				raise UserError( f"An error occurred while {action} the user [{status}]" )
	