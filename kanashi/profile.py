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

from kanashi.error import AuthError, BlockError, FavoriteError, FollowError, ReportError, RestrictError, UserError, UserNotFoundError
from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.request import RequestRequired
from kanashi.utility import File


#[kanashi.profile.ProfilePriperties]
class ProfileProperties:
	
	@property
	def besties( self ):
		return self.isBesties
	
	@property
	def biography( self ):
		return self.avoider( "biography" )
	
	@property
	def biographyFormat( self ):
		if  entity := self.avoider( "biography_with_entities" ):
			return entity.raw_text.replace( "\n", "\x0a\x20\x20\x20\x20" )
	
	@property
	def biographyEntities( self ):
		return self.avoider( "biography_with_entities", Object({ "entities": [] }) )
	
	@property
	def biographyEntitiesUser( self ):
		users = []
		if  entities := self.biographyEntities.entities:
			for entity in entities:
				if user := entity.user:
					users.append( user.username )
		return users
	
	@property
	def biographyEntitiesUserFormat( self ):
		if  users := self.biographyEntitiesUser:
			return "-\x20@".format( "\x0a\x20\x20\x20\x20-\x20@".join( users ) )
	
	@property
	def biographyEntitiesHashtag( self ):
		hashtags = []
		if  entities := self.biographyEntities.entities:
			for entity in entities:
				if hashtag := entity.hashtag:
					hashtags.append( hashtag.name )
		return hashtags
	
	@property
	def biographyEntitiesHashtagFormat( self ):
		if  hashtags := self.biographyEntitiesHashtag:
			return "-\x20#{}".format( "\x0a\x20\x20\x20\x20-\x20#".join( hashtags ) )
	
	@property
	def biographyRawText( self ):
		if  entity := self.avoider( "biography_with_entities" ):
			return entity.raw_text
	
	@property
	def blockedByViewer( self ):
		return self.avoider( "blocked_by_viewer" )
	
	@property
	def categoryName( self ):
		return self.avoider( "category_name" )
	
	@property
	def countEdgeFelixVideoTimeline( self ):
		if  edge := self.avoider( "edge_felix_video_timeline", 0 ):
			return edge.count
	
	@property
	def countEdgeFollow( self ):
		if  edge := self.avoider( "edge_follow", 0 ):
			return edge.count
	
	@property
	def countEdgeFollowedBy( self ):
		if  edge := self.avoider( "edge_followed_by", 0 ):
			return edge.count
	
	@property
	def countEdgeMediaCollections( self ):
		if  edge := self.avoider( "edge_mutual_followed_by", 0 ):
			return edge.count
	
	@property
	def countEdgeMutualFollowedBy( self ):
		if  edge := self.avoider( "edge_mutual_followed_by", 0 ):
			return edge.count
	
	@property
	def countEdgeOwnerToTimelineMedia( self ):
		if  edge := self.avoider( "edge_owner_to_timeline_media", 0 ):
			return edge.count
	
	@property
	def countEdgeSavedMedia( self ):
		if  edge := self.avoider( "edge_saved_media", 0 ):
			return edge.count
	
	@property
	def edgeFelixVideoTimeline( self ):
		if  edge := self.avoider( "edge_felix_video_timeline" ):
			return edge.edges
		return []
	
	@property
	def edgeFollow( self ):
		if  edge := self.avoider( "edge_follow" ):
			return edge.edges
		return []
	
	@property
	def edgeFollowedBy( self ):
		if  edge := self.avoider( "edge_followed_by" ):
			return edge.edges
		return []
	
	@property
	def edgeMediaCollections( self ):
		if  edge := self.avoider( "edge_media_collections" ):
			return edge.edges
		return []
	
	@property
	def edgeMutualFollowedBy( self ):
		if  edge := self.avoider( "edge_mutual_followed_by" ):
			return edge.edges
		return []
	
	@property
	def edgeOwnerToTimelineMedia( self ):
		if  edge := self.avoider( "edge_owner_to_timeline_media" ):
			return edge.edges
		return []
	
	@property
	def edgeSavedMedia( self ):
		if  edge := self.avoider( "edge_saved_media" ):
			return edge.edges
		return []
	
	@property
	def followedByViewer( self ):
		return self.avoider( "followed_by_viewer" )
	
	@property
	def followsViewer( self ):
		return self.avoider( "follows_viewer" )
	
	@property
	def fullname( self ):
		return self.avoider( "full_name" )
	
	@property
	def fullnameFormat( self ):
		name = []
		if  self.fullname:
			name.append( self.fullname )
		else:
			pass
		name.append( f"({self.username})" )
		if  self.isVerified:
			name.append( "√" )
		return "\x20".join( name )
	
	@property
	def hasBlockedViewer( self ):
		return self.avoider( "has_blocked_viewer" )
	
	@property
	def id( self ):
		return self.avoider( "id" )
	
	@property
	def isBesties( self ):
		return self.avoider( "is_besties" )
	
	@property
	def isBlockingReel( self ):
		return self.avoider( "is_blocking_reel" )
	
	@property
	def isBusinessAccount( self ):
		return self.avoider( "is_business_account" )
	
	@property
	def isEligibleToSubscribe( self ):
		return self.avoider( "is_eligible_to_subscribe" )
	
	@property
	def isEmbedsDisabled( self ):
		return self.avoider( "is_embeds_disabled" )
	
	@property
	def isFeedFavorite( self ):
		return self.avoider( "is_feed_favorite" )
	
	@property
	def isGuardianOfViewer( self ):
		return self.avoider( "is_guardian_of_viewer" )
	
	@property
	def isSupervisedByViewer( self ):
		return self.avoider( "is_supervised_by_viewer" )
	
	@property
	def isJoinedRecently( self ):
		return self.avoider( "is_joined_recently" )
	
	@property
	def isMutingNotes( self ):
		return self.avoider( "is_muting_profile" )
	
	@property
	def isMutingReel( self ):
		return self.avoider( "is_muting_reel" )
	
	@property
	def isMySelf( self ):
		return self.profile.id == self.viewer.id
	
	@property
	def isNotMySelf( self ):
		return self.profile.id != self.viewer.id
	
	@property
	def isPrivateAccount( self ):
		return self.avoider( "is_private" )
	
	@property
	def isProfessionalAccount( self ):
		return self.avoider( "is_professional_account" )
	
	@property
	def isSupervisedUser( self ):
		return self.avoider( "is_supervised_user" )
	
	@property
	def isVerified( self ):
		return self.avoider( "is_verified" )
	
	@property
	def muting( self ):
		return self.avoider( "muting" )
	
	@property
	def profilePicture( self ):
		return self.avoider( "rofile_pic_url" )
	
	@property
	def profilePictureHD( self ):
		return self.avoider( "profile_pic_url_hd" )
	
	@property
	def pronouns( self ):
		return self.avoider( "pronouns" )
	
	@property
	def pronounsFormat( self ):
		if  self.pronouns:
			return "/".join( self.pronouns )
		return ""
	
	@property
	def requestedByViewer( self ):
		return self.avoider( "requested_by_viewer" )
	
	@property
	def restrictedByViewer( self ):
		return self.avoider( "restricted_by_viewer" )
	
	@property
	def subscribed( self ):
		return self.avoider( "subscribed" )
	
	@property
	def username( self ):
		return self.avoider( "username" )
	

#[kanashi.profile.Profile]
class Profile( ProfileProperties, Readonly, RequestRequired ):
	
	#[Profile( Object viewer, Request request, Dict profile )]: None
	def __init__( self, viewer, request, profile ):
		
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
		
		# Instance of parent class.
		self.parent = super()
		self.parent.__init__( request )
	
	#[ProfileProperties.__getitem__( String key )]: Mixed
	def __getitem__( self, key ):
		return self.avoider( key )
	
	#[Profile.prints]: List
	@property
	def prints( self ):
		
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
			"besties",
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
					prints[idx] = f"ID {self.id}"
				case "fullname":
					prints[idx] = f"Fullname \x1b[1;37m{self.fullname}\x1b[0m"
				case "username":
					prints[idx] = f"Username \x1b[4m\x1b[1;38;5;189m{self.username}\x1b[0m"
				case "pronouns":
					prints[idx] = "\x0a\x20\x20\x20\x20....".join([ "- Pronouns", self.pronounsFormat if self.pronounsFormat else "None" ])
				case "category":
					if  self.isProfessionalAccount:
						prints[idx] = "\x0a\x20\x20\x20\x20....".join([ "- Category", self.categoryName if self.categoryName else "None" ])
					else:
						del prints[idx]
				case "account":
					account = []
					if  self.isPrivateAccount:
						account.append( "Private" )
					else:
						account.append( "Public" )
						if  self.isBusinessAccount:
							account.append( "Business" )
						if  self.isProfessionalAccount:
							account.append( "Professional" )
					prints[idx] = "\x0a\x20\x20\x20\x20....".join([ "- Account", "/".join( account ) ])
				case "website":
					prints[idx] = [ "- Website" ]
					if self['bio_links']:
						if "title" in self['bio_links'][0]:
							prints[idx].append( "Title {}".format( self['bio_links']['title'] ) )
						prints[idx].append( self['bio_links'][0]['link_type'].capitalize() )
						prints[idx].append( "\x1b[1;38;5;81m{}\x1b[0m".format( self['bio_links'][0]['url'] ) )
					else:
						prints[idx].append( "None" )
					prints[idx] = "\x0a\x20\x20\x20\x20....".join( prints[idx] )
				case "biography":
					if  self.biography != "":
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
							"{}".format( self.biographyEntitiesUserFormat ),
							"----------------------------------------",
							"- Biography Entitity Hashtags",
							"----------------------------------------",
							"{}".format( self.biographyEntitiesHashtagFormat ),
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
				case "besties":
					if  self.isNotMySelf:
						if  self.isBesties:
							prints[idx] = "- This user is your besties"
						else:
							prints[idx] = "- This user is not your besties"
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
						"│ Posts │ Reels │ Saveds │ Collections │",
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
	
	#[Profile.avoider( String key, Mixed default )]: Mixed
	def avoider( self, key, default=None ):
		
		"""
		Drop profile info wthout raise KeyError
		
		:params String key
		:params Mixed default
		
		:return Mixed
		"""
		
		if  self.profile.isset( key ):
			return self.profile[key]
		return default
	
	#[Profile.besties()]: Object
	def besties( self ):
		
		"""
		Make besties or unbesties user.
		
		:return Object
			Besties result representation
		:raises BestiesError
			...
		"""
		
		if  self.isMySelf:
			raise BestiesError( "Unable to set yourself as a besties" )
		if self.followedByViewer:
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
			if self.isBesties:
				action = "Remove Besties"
				data['remove'].append( self.id )
			else:
				action = "Adding Besties"
				data['add'].append( self.id )
			request = self.request.post( "https://www.instagram.com/api/v1/friendships/set_besties/", json=data )
			status = request.status_code
			if status == 200:
				response = request.json()
				if "friendship_statuses" in response:
					self.profile.is_besties = False if self.isBesties else True
					return Object( response['friendship_statuses'] )
				else:
					raise BestiesError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
			else:
				self.throws( action, status )
		else:
			raise BestiesError( "Can't set user as besties before following" )
	
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
	
	#[Profile.export( String fname )]: None
	def export( self, fname=None ):
		if  not isinstance( fname, str ):
			fname = self.username
		fdata = self.profile.dict()
		pass
	
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
			if self.isFeedFavorite:
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
				self.profile.followed_by_viewer = follow['following']
				self.profile.is_private = follow['is_private']
				return Object({
					"id": self.id,
					"private": self.isPrivate,
					"username": self.username,
					"following": self.followedByViewer,
					"requested": self.requestedByViewer
				})
			else:
				raise FollowError( response['message'] if "message" in response and response['message'] else f"Something wrong when {action} the {self.username}" )
		else:
			self.throws( action, status )
	
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
		
		if self.isMySelf:
			raise RestrictError( "Unable to restrict or unrestrict yourself" )
		self.headers.update({
			"Accept-Encoding": "gzip, deflate, br",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/{}/".format( self.username )
		})
		if self.restrictedByViewer:
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
	
	#[Profile.profilePictureSave()]: Object
	def profilePictureSave( self ):
		
		"""
		Download profile picture user.
		
		:return Object
			Download result represent
		"""
		
		pass
	
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
			case 401:
				raise AuthError( f"Failed to {action}, because the credential is invalid, status 401" )
			case 404:
				raise UserNotFoundError( f"Target \"{self.username}\" user not found" )
			case _:
				raise UserError( f"An error occurred while {action} the user [{status}]" )
	