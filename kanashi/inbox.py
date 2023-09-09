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

from random import randint

from kanashi.object import Object
from kanashi.request import Request, RequestRequired
from kanashi.utility import typedef, typeof

#[kanashi.inbox.InboxProperty]
class InboxProperty:

	@property
	def activityFeedDotBadge( self ):
		return self.__activityFeedDotBadge__
		
	@property
	def activityFeedDotBadgeOnly( self ):
		return self.__activityFeedDotBadgeOnly__
	
	@property
	def campaignNotification( self ):
		return self.__campaignNotification__

	@property
	def comments( self ):
		return self.__comments__
	
	@property
	def commentLikes( self ):
		return self.__commentLikes__
	
	@property
	def continuationToken( self ):
		return self.__inbox__.continuation_token

	@property
	def countActivityFeedDotBadge( self ):
		return self.__inbox__.counts.activity_feed_dot_badge

	@property
	def countActivityFeedDotBadgeOnly( self ):
		return self.__inbox__.counts.activity_feed_dot_badge_only

	@property
	def countCampaignNotification( self ):
		return self.__inbox__.counts.campaign_notification

	@property
	def countComments( self ):
		return self.__inbox__.counts.comments

	@property
	def countCommentLikes( self ):
		return self.__inbox__.counts.comment_likes

	@property
	def countFundraiser( self ):
		return self.__inbox__.counts.fundraiser

	@property
	def countLikes( self ):
		return self.__inbox__.counts.likes

	@property
	def countNewPosts( self ):
		return self.__inbox__.counts.new_posts

	@property
	def countPhotosOfYou( self ):
		return self.__inbox__.counts.photos_of_you

	@property
	def countPromotional( self ):
		return self.__inbox__.counts.promotional

	@property
	def countRelationships( self ):
		return self.__inbox__.counts.relationships
		
	@property
	def countRequests( self ):
		return self.__inbox__.counts.requests

	@property
	def countShoppingNotification( self ):
		return self.__inbox__.counts.shopping_notification
	
	@property
	def countUsertags( self ):
		return self.__inbox__.counts.user_tags

	@property
	def fundraiser( self ):
		return self.__fundraiser__
	
	@property
	def isLastPage( self ):
		return self.__inbox__.is_last_page
	
	@property
	def lastChecked( self ):
		return self.__inbox__.last_checked

	@property
	def likes( self ):
		return self.__likes__

	@property
	def newPosts( self ):
		return self.__newPosts__
	
	@property
	def newStories( self ):
		return self.__inbox__.new_stories

	@property
	def oldStories( self ):
		return self.__inbox__.old_stories
	
	@property
	def partition( self ):
		return self.__inbox__.partition
	
	@property
	def photosOfYou( self ):
		return self.__photosOfYou__

	@property
	def priorityStories( self ):
		return self.__inbox__.priority_stories

	@property
	def promotional( self ):
		return self.__promotional__
	
	@property
	def relationships( self ):
		return self.__relationships__

	@property
	def requests( self ):
		return self.__requests__

	@property
	def shoppingNotification( self ):
		return self.__shoppingNotification__

	@property
	def usertags( self ):
		return self.__usertags__

#[kanashi.inbox.Inbox]
class Inbox( RequestRequired ):

	# Generate random number for Inbox Flags Iterator.
	NEW_STORY = randint( 11111, 99999 )
	OLD_STORY = randint( 11111, 99999 )
	PRIORITY_STORY = randint( 11111, 99999 )

	Type = Object({
		"ActivityFeedDotBadge": {
			"common": 0,
			"story": 0
		},
		"ActivityFeedDotBadgeOnly": {
			"common": 0,
			"story": 0
		},
		"Comments": {
			"common": 0,
			"story": 0
		},
		"CommentLike": {
			"common": 1,
			"story": 13
		},
		"CampaignNotification": {
			"common": 0,
			"story": 0
		},
		"Fundraiser": {
			"common": 0,
			"story": 0
		},
		"Likes": {
			"common": 1,
			"story": 60
		},
		"NewPost": {
			"common": 0,
			"story": 0
		},
		"PhotosOfYou": {
			"common": 0,
			"story": 0
		},
		"Promotional": {
			"common": 0,
			"story": 0
		},
		"Relationship": {
			"common": 3,
			"story": 101
		},
		"Requests": {
			"common": 0,
			"story": 0
		},
		"ShoppingNotification": {
			"common": 0,
			"story": 0
		},
		"Usertags": {
			"common": 0,
			"story": 0
		}
	})
	
	#[Inbox.__init__( Request request, Dict|Object inbox, Mixed **kwargs )]: None
	def __init__( self, request, inbox, **kwargs ):
		if  typedef( request, Request, False ):
			raise ValueError( "Invalid request parameter, value must be type Request, {} given".format( typeof( request ) ) )
		if  typedef( inbox, dict, False ) and \
			typedef( inbox, Object, False ):
			raise ValueError( "Invalid inbox parameter, value must be type Dict|Object, {} given".format( typeof( inbox ) ) )
		
		# Instance of class Parent.
		self.__parent__ = super()
		self.__parent__.__init__( request )

		# Save user Inbox.
		self.__inbox__ = Object( inbox )

		# Inherited methods from clients if available.
		self.__methods__ = kwargs.pop( "methods", {} )

		# User inbox informations.
		self.__activityFeedDotBadge__ = Object({})
		self.__activityFeedDotBadgeOnly__ = Object({})
		self.__comments__ = Object({})
		self.__commentLikes__ = Object({})
		self.__campaignNotification__ = Object({})
		self.__fundraiser__ = Object({})
		self.__likes__ = Object({})
		self.__newPosts__ = Object({})
		self.__photosOfYou__ = Object({})
		self.__promotional__ = Object({})
		self.__relationships__ = Object({})
		self.__requests__ = Object({})
		self.__shoppingNotification__ = Object({})
		self.__usertags__ = Object({})

		# Filtering Inbox.
		self.__iterator( inbox.old_stories, Inbox.OLD_STORY )
		self.__iterator( inbox.new_stories, Inbox.NEW_STORY )
		self.__iterator( inbox.priority_stories, Inbox.PRIORITY_STORY )
	
	def __filter( self, items, flags=0 ):
		match flags:
			case Inbox.OLD_STORY:
				story = "__oldStory__"
			case Inbox.NEW_STORY:
				story = "__newStory__"
			case Inbox.PRIORITY_STORY:
				story = "__priorityStory__"
			case _:
				raise ValueError( "Invalid flags parameter" )
		for item in items:
			for type in Inbox.Type:
				if  item.type == type.type and \
					item.story_type == type.story:
					pass
			self.__dict__[story].set( item.pk, item )
	
