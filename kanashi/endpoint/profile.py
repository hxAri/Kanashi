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

from kanashi.error import Error
from kanashi.object import Object
from kanashi.request import RequestError, RequestRequired
from kanashi.utils import File, JSON, String


#[kanashi.endpoint.ProfileError]
class ProfileError( Error ):
	pass
	

#[kanashi.endpoint.ProfileSuccess]
class ProfileSuccess( Object ):
	pass
	

#[kanashi.endpoint.ProfileMethods]
class ProfileMethods:
	
	#[ProfileMethods:Template]
	"""
	#[ProfileMethods.]
	def ( self ):
		pass
	"""
	
	#[ProfileMethods.block()]
	def block( self ):
		return self.app.block.block( self )
	
	#[ProfileMethods.favorite()]
	def favorite( self ):
		return self.app.favorite.favorite( self )
	
	#[ProfileMethods.follow()]
	def follow( self ):
		return self.app.follow.follow( self )
	
	#[ProfileMethods.report()]
	def report( self ):
		pass
	
	#[ProfileMethods.restrict()]
	def restrict( self ):
		pass
	
	#[ProfileMethods.saveProfilePicture( String name, Bool hd )]
	def saveProfilePicture( self, name:str=None, hd:bool=False ) -> ProfileSuccess:
		if name == None:
			name = self.username
		if name == "\\r":
			name = String.random( 16 )
		path = self.app.settings.path.image
		self.request.download( self.profilePictureHD if hd else self.profilePicture, saved := f"{path}/{name}.jpg" )
		return ProfileSuccess({
			"name": name,
			"path": path,
			"saved": saved
		})
	

#[kanashi.endpoint.ProfileProperties]
class ProfileProperties:
	
	#[ProfileProperties:Template]
	"""
	#[ProfileProperties.]
	@property
	def ( self ):
		return( self.user. )
	"""
	
	#[ProfileProperties.biography]
	@property
	def biography( self ):
		return( self.user.biography )
	
	#[ProfileProperties.biographyEntities]
	@property
	def biographyEntities( self ):
		return( self.user.biography_with_entities.entities )
	
	#[ProfileProperties.biographyFormat]
	@property
	def biographyFormat( self ):
		return( self.user.biography_with_entities.raw_text.replace( "\n", "\x0a\x20\x20\x20\x20" ) )
	
	#[ProfileProperties.biographyRawText]
	@property
	def biographyRawText( self ):
		return( self.user.biography_with_entities.raw_text )
	
	#[ProfileProperties.blockedByViewer]
	@property
	def blockedByViewer( self ):
		return( self.user.blocked_by_viewer )
	
	#[ProfileProperties.categoryName]
	@property
	def categoryName( self ):
		return( self.user.category_name )
	
	#[ProfileProperties.countEdgeFelixVideoTimeline]
	@property
	def countEdgeFelixVideoTimeline( self ):
		return( self.user.edge_felix_video_timeline.count )
	
	#[ProfileProperties.countEdgeFollow]
	@property
	def countEdgeFollow( self ):
		return( self.user.edge_follow.count )
	
	#[ProfileProperties.countEdgeFollowedBy]
	@property
	def countEdgeFollowedBy( self ):
		return( self.user.edge_followed_by.count )
	
	#[ProfileProperties.countEdgeMediaCollections]
	@property
	def countEdgeMediaCollections( self ):
		return( self.user.edge_media_collections.count )
	
	#[ProfileProperties.countEdgeMutualFollowedBy]
	@property
	def countEdgeMutualFollowedBy( self ):
		return( self.user.edge_mutual_followed_by.count )
	
	#[ProfileProperties.countEdgeOwnerToTimelineMedia]
	@property
	def countEdgeOwnerToTimelineMedia( self ):
		return( self.user.edge_owner_to_timeline_media.count )
	
	#[ProfileProperties.countEdgeSavedMedia]
	@property
	def countEdgeSavedMedia( self ):
		return( self.user.edge_saved_media.count )
	
	#[ProfileProperties.edgeFelixVideoTimeline]
	@property
	def edgeFelixVideoTimeline( self ):
		return( self.user.edge_felix_video_timeline.edges )
	
	#[ProfileProperties.edgeFollow]
	@property
	def edgeFollow( self ):
		return( self.user.edge_follow.edges )
	
	#[ProfileProperties.edgeFollowedBy]
	@property
	def edgeFollowedBy( self ):
		return( self.user.edge_followed_by.edges )
	
	#[ProfileProperties.edgeMediaCollections]
	@property
	def edgeMediaCollections( self ):
		return( self.user.edge_media_collections.edges )
	
	#[ProfileProperties.edgeMutualFollowedBy]
	@property
	def edgeMutualFollowedBy( self ):
		return( self.user.edge_mutual_followed_by.edges )
	
	#[ProfileProperties.edgeOwnerToTimelineMedia]
	@property
	def edgeOwnerToTimelineMedia( self ):
		return( self.user.edge_owner_to_timeline_media.edges )
	
	#[ProfileProperties.edgeSavedMedia]
	@property
	def edgeSavedMedia( self ):
		return( self.user.edge_saved_media.edges )
	
	#[ProfileProperties.followedByViewer]
	@property
	def followedByViewer( self ) -> bool:
		return( self.user.followed_by_viewer )
	
	#[ProfileProperties.followsViewer]
	@property
	def followsViewer( self ) -> bool:
		return( self.user.follows_viewer )
	
	#[ProfileProperties.fullName]
	@property
	def fullName( self ) -> str:
		return( self.user.full_name )
	
	#[ProfileProperties.fullNameFormat]
	@property
	def fullNameFormat( self ) -> str:
		name = []
		if self.user.full_name != "":
			name.append( self.user.full_name )
		else:
			pass
		name.append( f"({self.user.username})" )
		if self.user.is_verified:
			name.append( "√" )
		return( "\x20".join( name ) )
	
	#[ProfileProperties.hasBlockedViewer]
	@property
	def hasBlockedViewer( self ) -> bool:
		return( self.user.has_blocked_viewer )
	
	#[ProfileProperties.id]
	@property
	def id( self ) -> int:
		return( self.user.id )
	
	#[ProfileProperties.isBusinessAccount]
	@property
	def isBusinessAccount( self ) -> bool:
		return( self.user.is_business_account )
		
	"""
	#[ProfileProperties.fetchIsById]
	@property
	def isFetchById( self ):
		return( self.fetch == Profile.FETCH_ID )
	
	#[ProfileProperties.fetchIsByUsername]
	@property
	def isFetchByUsername( self ):
		return( self.fetch == Profile.FETCH_USERNAME )
	"""
	
	#[ProfileProperties.isJoinedRecently]
	@property
	def isJoinedRecently( self ) -> bool:
		return( self.user.is_joined_recently )
	
	#[ProfileProperties.isMySelf]
	@property
	def isMySelf( self )-> bool:
		return( self.user.id == self.app.active.id )
	
	#[ProfileProperties.isNotMySelf]
	@property
	def isNotMySelf( self ) -> bool:
		return( self.user.id != self.app.active.id )
	
	#[ProfileProperties.isPrivateAccount]
	@property
	def isPrivateAccount( self ) -> bool:
		return( self.user.is_private )
	
	#[ProfileProperties.isProfessionalAccount]
	@property
	def isProfessionalAccount( self ) -> bool:
		return( self.user.is_professional_account )
	
	#[ProfileProperties.isVerified]
	@property
	def isVerified( self ) -> bool:
		return( self.user.is_verified )
	
	#[ProfileProperties.profilePicture]
	@property
	def profilePicture( self ) -> str:
		return( self.user.profile_pic_url )
	
	#[ProfileProperties.profilePictureHD]
	@property
	def profilePictureHD( self ) -> str:
		return( self.user.profile_pic_url_hd )
	
	#[ProfileProperties.pronouns]
	@property
	def pronouns( self ) -> list:
		return( self.user.pronouns )
	
	#[ProfileProperties.pronounsFormat]
	@property
	def pronounsFormat( self ) -> str:
		return( "/".join( self.pronouns ) )
	
	#[ProfileProperties.requestedByViewer]
	@property
	def requestedByViewer( self ) -> bool:
		return( self.user.requested_by_viewer )
	
	#[ProfileProperties.]
	@property
	def restrictedByViewer( self ) -> bool:
		return( self.user.restricted_by_viewer )
	
	#[ProfileProperties.username]
	@property
	def username( self ) -> str:
		return( self.user.username )
	

#[kanashi.endpoint.Profile]
class Profile( ProfileMethods, ProfileProperties, RequestRequired ):
	
	"""
	# Fetch Mode by ID
	FETCH_ID = 75619
	
	# Fetch Mode by Username
	FETCH_USERNAME = 85862
	"""
	
	#[Profile( Object app, Dict user, Function | Method prev )]
	def __init__( self, app, user, prev=None ):
		
		# Save user info.
		self.user = Object( user )
		
		# Set previous callback.
		match type( prev ).__name__:
			case "function" | "method":
				self.prev = prev
			case _:
				try:
					self.prev = app.main
				except AttributeError:
					self.prev = self.main
		
		self.outputs = [ "", "id", "", "name", "pronouns", "category", "account", "biography", "", "block", "", "follow", "", "edges", "" ]
		for i in range( len( self.outputs ), 0, -1 ):
			idx = i -1
			val = self.outputs[idx]
			match val:
				case "id":
					self.outputs[idx] = f"ID ({self.id})"
				case "name":
					self.outputs[idx] = f"- {self.fullNameFormat}"
				case "pronouns":
					pronouns = self.pronounsFormat
					if pronouns != "":
						self.outputs[idx] = f"- Pronouns {pronouns}"
					else:
						del self.outputs[idx]
				case "category":
					if self.isProfessionalAccount:
						self.outputs[idx] = "- Category {}".format( self.categoryName )
					else:
						del self.outputs[idx]
				case "account":
					account = []
					if self.isPrivateAccount:
						account.append( "Private" )
					else:
						account.append( "Public" )
						if self.isBusinessAccount:
							account.append( "Business" )
						if self.isProfessionalAccount:
							account.append( "Professional" )
					self.outputs[idx] = "- Account Type {}".format( "/".join( account ) )
				case "biography":
					if self.biography != "":
						self.outputs[idx] = "\x0a\x20\x20\x20\x20".join([
							"",
							"----------------------------------------",
							"- Biography",
							"----------------------------------------",
							self.biographyFormat,
							"----------------------------------------",
						])
					else:
						del self.outputs[idx]
				case "block":
					if self.id == app.active.id:
						self.outputs[idx] = "- This is your account, you can't block self"
					else:
						block = []
						if self.hasBlockedViewer:
							block.append( "- This user has blocked your account" )
						else:
							block.append( "- This user did not block your account" )
						if self.blockedByViewer:
							block.append( "- You have blocked this user" )
						else:
							block.append( "- You did not block this user" )
						self.outputs[idx] = "\x0a\x20\x20\x20\x20".join( block )
				case "follow":
					if self.id == app.active.id:
						self.outputs[idx] = "- This is your account, you can't follow self"
					else:
						follow = []
						if self.followsViewer:
							follow.append( "- This user is following your account" )
						else:
							follow.append( "- This user is not following your account" )
						if self.followedByViewer:
							follow.append( "- You have followed this user" )
						elif self.requestedByViewer:
							follow.append( "- Your follow request has not been approved" )
						else:
							follow.append( "- You are not following this user" )
						self.outputs[idx] = "\x0a\x20\x20\x20\x20".join( follow )
				case "edges":
					self.outputs[idx] = "\x0a\x20\x20\x20\x20".join([
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
					self.outputs[idx] = self.outputs[idx].format(*[
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
			
		self.block = app.block
		self.follow = app.follow
		self.restrict = app.restrict
		self.favorite = app.favorite
		
		# Call parent constructor.
		super().__init__( app )
	