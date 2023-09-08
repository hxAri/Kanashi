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


from kanashi.collection import Collection
from kanashi.object import Object
from kanashi.request import RequestRequired
from kanashi.utility import typedef


#[kanashi.explore.ExploreItem]
class Explore( Collection, RequestRequired ):

	# Comment
	# Like
	# Media
	# Profile
	
	#[Explore( Request request, Object explore )]: None
	def __init__( self, request, explore ):

		"""
		Construct method of class Explore
		
		:params Request request
			Request context
		:params Object explore
			Result of explore request

		:return None
		"""

		self.__explore__ = explore
		self.__request__ = request
		self.__parent__ = super()
		self.__parent__.__init__( 
			items=explore.sectional_items, 
			value=ExploreSectionalItem, 
			request=request 
		)
	
	#[Explore.autoLoadMoreEnabled]: Bool
	@property
	def autoLoadMoreEnabled( self ):
		return self.__explore__.auto_load_more_enabled

	#[Explore.clusters]: Object
	@property
	def clusters( self ):
		return self.__explore__.clusters
	
	#[Explore.maxId]: Int
	@property
	def maxId( self ):
		return self.__explore__.max_id
	
	#[Explore.moreAvailable]: Bool
	@property
	def moreAvailable( self ):
		return self.__explore__.more_available
	
	#[Explore.nextMaxId]: Int
	@property
	def nextMaxId( self ):
		return self.__explore__.next_max_id
	
	#[Explore.rankedTimeInSeconds]: Int
	@property
	def rankedTimeInSeconds( self ):
		return self.__explore__.ranked_time_in_seconds
	
	#[Explore.rankToken]: Str
	@property
	def rankToken( self ):
		return self.__explore__.rank_token
	
	#[Explore.sessionPagingToken]: Str
	@property
	def sessionPagingToken( self ):
		return self.__explore__.session_paging_token
	

#[kanashi.explore.ExploreSectionalItem]
class ExploreSectionalItem( RequestRequired ):
	
	#[ExploreItem( Object context, Request request )]: None
	def __init__( self, context, request ):
		
		"""
		Construct method of class ExploreSectionalItem
		
		:params Object context
			Explore sectional items
		:params Request request
			Request context

		:return None
		"""
		
		self.__context__ = context
		self.__parent__ = super()
		self.__parent__.__init__( request )
	
	#[ExploreItem.exploreItemInfo]: Object
	@property
	def exploreItemInfo( self ):
		return self.__context__.explore_item_info
	
	#[ExploreItem.feedType]: Str
	@property
	def feedType( self ):
		return self.__context__.feed_type
	
	#[ExploreItem.layoutContent]: Object
	@property
	def layoutContent( self ):
		return Object({
			"one_by_two_item": self.layoutContentOneByTwoItem,
			"fill_items": self.layoutContentFillItems
		})
	
	#[ExploreItem.layoutContentOneByTwoItem]: ExploreClip
	@property
	def layoutContentOneByTwoItem( self ):
		return ExploreClip( clip=self.__context__.layout_content.one_by_two_item.clips, request=self.request )
	
	#[ExploreItem.layoutContentOneByTwoItemClips]: ExploreClipItem
	@property
	def layoutContentOneByTwoItemClips( self ):
		return Collection( value=ExploreClipItem, items=self.__context__.layout_content.one_by_two_item.clips.items, request=self.request )
	
	#[ExploreItem.layoutContentFillItems]: Collection<ExploreFillItem>
	@property
	def layoutContentFillItems( self ):
		return Collection( value=ExploreFillItem, items=self.__context__.layout_content.fill_items, request=self.request )
	
	#[ExploreItem.layoutType]: Str
	@property
	def layoutType( self ):
		return self.__context__.layoutType


#[kanashi.explore.ExploreClip]
class ExploreClip( RequestRequired ):
	
	#[ExploreClip( Object clip, Request request )]
	def __init__( self, clip, request ):

		"""
		Construct method of class ExploreClip
		
		:params Object context
			Explore clip info
		:params Request request
			Request context

		:return None
		"""

		self.__parent__ = super()
		self.__parent__.__init__( request )


#[kanashi.explore.ExploreClipItem]
class ExploreClipItem( RequestRequired ):
	
	#[ExploreClipItem( Object item, Request request )]
	def __init__( self, item, request ):

		"""
		Construct method of class ExploreClipItem
		
		:params Object item
			Explore object of clip item
		:params Request request
			Request context

		:return None
		"""

		self.__parent__ = super()
		self.__parent__.__init__( request )


#[kanashi.explore.ExploreFillItem]
class ExploreFillItem( RequestRequired ):
	
	#[ExploreFillItem( Object item, Request request )]
	def __init__( self, item, request ):

		"""
		Construct method of class ExploreFillItem
		
		:params Object item
			Explore object of fill item
		:params Request request
			Request context

		:return None
		"""

		self.__parent__ = super()
		self.__parent__.__init__( request )
	
