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


#[kanashi.media.MediaCollection]
class MediaCollection:
	
	#[MediaCollection( Dict medias, Int type )]: None
	def __init__( self, medias, type ):
		
		"""
		Construct method of class MediaCollection.
		
		:params List medias
			Media list
		
		:return None
		:raises ValueError
			When invalid media parameter
		"""
		
		if not isinstance( medias, list ):
			raise ValueError( "Invalid media parameter, value must be type list, {} passed".format( type( media ).__name__ ) )
		self.__index__ = 0
		self.__media__ = []
		for media in medias:
			self.__media__.append( Media( media, type ) )
		pass
	
	#[MediaCollection.__iter__()]: MediaCollection
	def __iter__( self ):
		return self
	
	#[MediaCollection.__next__()]: Media
	def __next__( self ):
		pass
	
	#[MediaCollection.__getitem__( Int index )]: Media
	def __getitem__( self, index ):
		pass
	
	#[MediaCollection.__setitem__( Int index, Media media )]: None
	def __setitem__( self, index, media ):
		pass
	
	#[MediaCollection.rewind()]: None
	def rewind( self ):
		self.__index__ = 0
	
	#[MediaCollection.seek( Int index )]: None
	def seek( self, index ):
		if index < 0:
			raise IndexError()
		if index > self.length:
			raise IndexError()
	
	#[MediaCollection.length]: Int
	@property
	def length( self ):
		return len( self.__media__ )
	

#[kanashi.media.Media]
class Media:
	
	TYPE_COLLECTION = 3
	TYPE_EXPLORE = 8
	TYPE_HASHTAG = 5
	TYPE_IGTV = 1
	TYPE_LOCATION = 9
	TYPE_POST = 2
	TYPE_REEL = 6
	TYPE_SAVED = 7
	TYPE_STORY = 4
	TYPE_SUGGESTED_REEL = 10
	TYPE_SUGGESTED_TIMELINE = 11
	TYPE_TIMELINE = 12
	TYPE_URL = 13
	
	#[Media()]: None
	def __init__( self, media, type=None ):
		pass
	
