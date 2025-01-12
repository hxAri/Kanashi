#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
# Follow, Unfollow, Media downloader, etc.
#
# Kanashi Copyright (c) 2024 - hxAri <hxari@proton.me>
# Kanashi Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

from builtins import bool as Bool, int as Int, str as Str
from click import Context, group, option as Option, pass_context as Initial
from click.types import Path
from hashlib import md5
from json import dumps as JsonEncoder, loads as JsonDecoder
from os import makedirs as mkdir
from os.path import isdir, isfile
from re import compile as Pattern, IGNORECASE, MULTILINE
from typing import Any, final, MutableMapping, MutableSequence, Tuple, TypeVar as Var, Union
from urllib.parse import urlparse as urlparser
from xml.sax import saxutils

from kanashi.client import Client
from kanashi.common import puts, typeof
from kanashi.constant import HomePath
from kanashi.futures import ThreadExecutor
from kanashi.graphql.actions import (
	PolarisPostActionLoadPostQueryQuery,
	PolarisProfilePageContentQuery,
	PolarisStoriesV3HighlightsPageQuery,
	PolarisStoriesV3ReelPageStandaloneQuery
)
from kanashi.logger import Logger
from kanashi.request import request


__all__ = [
	"Media"
]


_logger = Logger( __name__ )
""" Logger Instance """

_Pathname = Var( "_Pathname", bytes, str )
""" Media Pathname Type """

_PathnameDefault:Str = f"{HomePath}/kanashi"
""" Stored Media Pathname Default """

_Source = Var( "_Source", bytes, str )
""" Media Source Type """



def download( timeline:Union[MutableMapping[Str,Any],MutableSequence[Any]], pathname:Str, thread:Union[Int,Str]=None ) -> None:
	
	"""
	Media downloader
	
	Parameters:
		timeline (Union[MutableMapping[Str,Any],MutableSequence[Any]]):
			Timeline metadata info
		pathname (Str):
			Pathname of stored media
		thread (Int|Str):
			Current thread position number
	"""
	
	def parser( timeline:MutableMapping[Str,Any], pathname:Str, thread:Union[Int,Str] ) -> MutableSequence[Tuple[_Source,_Pathname]]:
		
		"""
		Timeline media parser
		
		Parameters:
			timeline (MutableMapping[Str,Any]):
				Timeline metadata info
			pathname (Str):
				Pathname of stored media
			thread (Int|Str):
				Current thread position number
		
		Returns:
			MutableSequence[Tuple[_Source,_Pathname]]:
				MutableSequence of tuple source media url and pathname stored media
		"""
		
		sources = []
		typename = "unknown"
		timelineId = timeline['id']
		if "type" in timeline and timeline['type']:
			typename = timeline['type']
		elif "__typename" in timeline and timeline['__typename']:
			typename = timeline['__typename']
		match typename:
			case "GraphHighlightReel" | "GraphReel":
				pathname+= f"/{timeline['owner']['username']}"
				for item in timeline['items']:
					match item['__typename']:
						case "GraphStoryImage":
							image = max( item['display_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
							sources.append( tuple([ image['src'], f"{pathname}/{typename}/GraphStoryImage/{timelineId}" ]) )
						case "GraphStoryVideo":
							video = max( item['video_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
							sources.append( tuple([ video['src'], f"{pathname}/{typename}/GraphStoryVideo/{timelineId}" ]) )
							thumbnail = max( item['display_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
							sources.append( tuple([ thumbnail['src'], f"{pathname}/{typename}/GraphStoryVideo/{timelineId}" ]) )
						case _:
							_logger.warning( "Unknown media {} typename: {}", typename, item['__typename'], thread=thread )
			case "GraphSidecar":
				match media['type']:
					case "GraphImage":
						sources.append( tuple([ media['image'], f"{pathname}/GraphSidecar/GraphImage/{timelineId}" ]) )
					case "GraphVideo":
						sources.append( tuple([ media['video'], f"{pathname}/GraphSidecar/GraphVideo/{timelineId}" ]) )
						sources.append( tuple([ media['thumbnail'], f"{pathname}/GraphSidecar/GraphVideo/{timelineId}" ]) )
					case _:
						_logger.warning( "Unknown media GraphSidecar typename: {}", media['type'], thread=thread )
			case "GraphImage":
				sources.append( tuple([ timeline['image'], f"{pathname}/GraphImage/{timelineId}" ]) )
			case "GraphVideo":
				sources.append( tuple([timeline['video'], f"{pathname}/GraphVideo/{timelineId}" ]) )
				sources.append( tuple([ timeline['thumbnail'], f"{pathname}/GraphVideo/{timelineId}" ]) )
			case "kanashi.client.Client.profile":
				if not pathname.endswith( timeline['username'] ):
					pathname+= f"/{timeline['username']}"
				sources.append( tuple([ timeline['profile_pic_url_hd'], f"{pathname}/profile" ]) )
			case "kanashi.graphql.actions.profile.PolarisProfilePageContentQuery":
				if not pathname.endswith( timeline['username'] ):
					pathname+= f"/{timeline['username']}"
				sources.append( tuple([ timeline['hd_profile_pic_url_info']['url'], f"{pathname}/profile" ]) )
			case "kanashi.client.Client.reels":
				if not pathname.endswith( timeline['owner']['username'] ):
					pathname+= f"/{timeline['owner']['username']}"
				match timeline['media_type']:
					case 1:
						image = max( timeline['image_versions2']['candidates'], key=lambda resource: ( resource['width'], resource['height'] ) )
						sources.append( tuple([ timeline['url'], f"{pathname}/{typename}/{timelineId}" ]) )
					case 2:
						video = None
						if "video_dash_manifest" in timeline and timeline['video_dash_manifest']:
							videoDashManifests = videoDashManifest( timeline['video_dash_manifest'] )
							video = max( videoDashManifests, key=lambda resource: ( resource['width'], resource['height'] if "height" in resource else 0 ) )
						elif "video_versions" in timeline and timeline['video_versions']:
							video = min( timeline['video_versions'], key=lambda resource: ( resource['type'] ) )
						sources.append( tuple([ video['url'], f"{pathname}/{typename}/{timelineId}" ]) )
						thumbnail = max( timeline['image_versions2']['candidates'], key=lambda resource: ( resource['width'], resource['height'] ) )
						sources.append( tuple([ thumbnail['url'], f"{pathname}/{typename}/{timelineId}" ]) )
					case _:
						_logger.warning( "Unknown media {} typename: {}", typename, timeline['media_type'], thread=thread )
			case "XDTGraphSidecar":
				for edge in timeline['edge_sidecar_to_children']['edges']:
					match edge['node']['__typename']:
						case "XDTGraphImage":
							media = max( edge['node']['display_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
							sources.append( tuple([ media['src'], f"{pathname}/XDTGraphSidecar/XDTGraphImage/{timelineId}" ]) )
						case "XDTGraphVideo":
							sources.append( tuple([ edge['node']['video_url'], f"{pathname}/XDTGraphSidecar/XDTGraphVideo/{timelineId}" ]) )
							thumbnail = max( edge['node']['display_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
							sources.append( tuple([ thumbnail['src'], f"{pathname}/XDTGraphSidecar/XDTGraphVideo/{timelineId}" ]) )
						case _:
							_logger.warning( "Unknown media XDTGraphSidecar typename: {}", edge['node']['__typename'], thread=thread )
					...
				...
			case "XDTGraphImage":
				media = max( timeline['display_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
				sources.append( tuple([ media['src'], f"{pathname}/XDTGraphImage/{timelineId}" ]) )
			case "XDTGraphVideo":
				sources.append( tuple([ timeline['video_url'], f"{pathname}/XDTGraphVideo/{timelineId}" ]) )
				thumbnail = max( timeline['display_resources'], key=lambda resource: ( resource['config_width'], resource['config_height'] ) )
				sources.append( tuple([ thumbnail['src'], f"{pathname}/XDTGraphVideo/{timelineId}" ]) )
			case "XDTReelDict":
				if not pathname.endswith( timeline['user']['username'] ):
					pathname+= f"/{timeline['user']['username']}"
				timelineId = timeline['id'].split( "\x3a" )[-1]
				for item in timeline['items']:
					match item['__typename']:
						case "XDTMediaDict":
							match item['media_type']:
								case 1:
									image = max( item['image_versions2']['candidates'], key=lambda resource: ( resource['width'], resource['height'] ) )
									sources.append( tuple([ image['url'], f"{pathname}/XDTReelDict/XDTMediaDict/{timelineId}" ]) )
								case 2:
									video = None
									if "video_dash_manifest" in item and item['video_dash_manifest']:
										videoDashManifests = videoDashManifest( item['video_dash_manifest'] )
										video = max( videoDashManifests, key=lambda resource: ( resource['width'], resource['height'] if "height" in resource else 0 ) )
									elif "video_versions" in item and item['video_versions']:
										video = min( item['video_versions'], key=lambda resource: ( resource['type'] ) )
									sources.append( tuple([ video['url'], f"{pathname}/XDTReelDict/XDTMediaDict/{timelineId}" ]) )
									thumbnail = max( item['image_versions2']['candidates'], key=lambda resource: ( resource['width'], resource['height'] ) )
									sources.append( tuple([ thumbnail['url'], f"{pathname}/XDTReelDict/XDTMediaDict/{timelineId}" ]) )
								case _:
									_logger.warning( "Unknown media XDTReelDict[XDTMediaDict] type: {}", item['media_type'], thread=thread )
						case _:
							_logger.warning( "Unknown media XDTReelDict typename: {}", item['__typename'], thread=thread )
			case "XDTMediaDict":
				if not pathname.endswith( timeline['user']['username'] ):
					pathname+= f"/{timeline['user']['username']}"
				timelineId = timeline['pk']
				match timeline['media_type']:
					case 1:
						image = max( timeline['image_versions2']['candidates'], key=lambda resource: ( resource['width'], resource['height'] ) )
						sources.append( tuple([ image['url'], f"{pathname}/XDTMediaDict/{timeline['user']['pk']}" ]) )
					case 2:
						video = None
						if "video_dash_manifest" in timeline and timeline['video_dash_manifest']:
							videoDashManifests = videoDashManifest( timeline['video_dash_manifest'] )
							video = max( videoDashManifests, key=lambda resource: ( resource['width'], resource['height'] if "height" in resource else 0 ) )
						elif "video_versions" in timeline and timeline['video_versions']:
							video = min( timeline['video_versions'], key=lambda resource: ( resource['type'] ) )
						sources.append( tuple([ video['url'], f"{pathname}/XDTMediaDict/{timeline['user']['pk']}" ]) )
						thumbnail = max( timeline['image_versions2']['candidates'], key=lambda resource: ( resource['width'], resource['height'] ) )
						sources.append( tuple([ thumbnail['url'], f"{pathname}/XDTMediaDict/{timeline['user']['pk']}" ]) )
					case _:
						_logger.warning( "Unknown media XDTMediaDict type: {}", timeline['media_type'], thread=thread )
			case _:
				_logger.warning( "Unknown media typename: {}", typename, thread=thread )
		return sources
	
	def videoDashManifest( contents:Str )-> MutableSequence[MutableMapping[Str,Union[Int,Str]]]:
		
		"""
		Parser for video dash manifest.
		
		Parameters:
			contents (Str):
				The contents dash manifest string
		
		Returns:
			MutableSequence[MutableMapping[Str,Union[Int,Str]]]:
				MutableSequence of video versions
		"""
		
		results = []
		positionEnd = 0
		positionStart = 0
		terminatorBegin = "<Representation"
		terminatorEnd = "</Representation>"
		terminatorBaseUrlBegin = "<BaseURL>"
		terminatorBaseUrlEnd = "</BaseURL>"
		try:
			while True:
				positionStart = contents.index( terminatorBegin, positionEnd )
				positionEnd = contents.index( terminatorEnd, positionStart )
				positionPropertyStart = positionStart
				positionPropertyStart+= len( terminatorBegin )
				positionPropertyEnd = contents.index( ">", positionPropertyStart )
				representPropertyRaw = contents[positionPropertyStart:positionPropertyEnd]
				representContentRaw = contents[positionPropertyEnd+1:positionEnd]
				positionBaseUrlContentStart = representContentRaw.index( terminatorBaseUrlBegin )
				positionBaseUrlContentStart+= len( terminatorBaseUrlBegin )
				positionBaseUrlContentEnd = representContentRaw.index( terminatorBaseUrlEnd, positionBaseUrlContentStart )
				properties = {}
				properties['url'] = saxutils.unescape( representContentRaw[positionBaseUrlContentStart:positionBaseUrlContentEnd] )
				searchs = {
					"id": str,
					"width": int,
					"height": int,
					"codecs": str,
					"mimeType": str
				}
				for item in searchs.items():
					keyset = item[0]
					pattern = Pattern( f"(?P<{keyset}>{keyset}\\=\"(?P<value>[^\"]*)\")", IGNORECASE|MULTILINE )
					matches = pattern.search( representPropertyRaw )
					if matches is not None:
						value = saxutils.unescape( matches.group( "value" ) )
						properties[keyset] = item[1]( value ) if callable( item[1] ) is True else value
						del value
					del pattern
				results.append( properties )
				del properties
		except ValueError: ...
		finally:
			...
		return results
	
	sources = []
	if isinstance( timeline, MutableMapping ):
		sources = parser( timeline, pathname, thread=thread )
	elif isinstance( timeline, MutableSequence ):
		for media in timeline:
			sources.extend( parser( media, f"{pathname}", thread=thread ) )
	for extend, target in enumerate( sources, 1 ):
		if thread is not None:
			if isinstance( thread, Int ) and thread >= 1:
				extend = f"T<{thread},E<{extend}>>"
			if isinstance( thread, Str ) and thread:
				extend = f"D<{thread},E<{extend}>>"
		source, pathname = target
		if not isdir( pathname ):
			_logger.info( "Create directory pathname: {}", pathname, thread=extend )
			mkdir( pathname )
		urlparsed = urlparser( source )
		pfilename = urlparsed.path.split( "\x2f" )[-1].split( "\x2e" )
		filenamen = md5( pfilename[0].encode() ).hexdigest()
		filenamed = f"{pathname}/{filenamen}.{pfilename[-1]}"
		if isfile( filenamed ):
			_logger.info( "File exists media: {}.{}", filenamen, pfilename[-1], thread=extend )
			continue
		_logger.info( "Downloading media: {}.{}", filenamen, pfilename[-1], thread=extend )
		response = request( "GET", source, stream=True )
		if not response.status in [ 200, 201 ]:
			_logger.warning( "Failed download media: {}.{}", filenamen, pfilename[-1], thread=extend )
			continue
		_logger.info( "Opening file media: {}.{}", filenamen, pfilename[-1], thread=extend )
		with open( filenamed, "wb" ) as fopen:
			_logger.info( "Writing content media: {}.{}", filenamen, pfilename[-1], thread=extend )
			fopen.write( response.content )
			fopen.close()
		_logger.info( "Successfully download media: {}.{}", filenamen, pfilename[-1], thread=extend )
	_logger.info( "Successfully download: {} media", len( sources ), thread=thread )


@final
@group
class Media: """ Instagram media """


@Media.command( help="Instagram profile picture media" )
@Option( "--user", help="Instagram profile id or username", required=True, type=Str )
@Option( "--pathname", help="Output the directory name to store the media", default=_PathnameDefault, type=Path( exists=False, dir_okay=True, writable=True ) )
@Initial
def profile( context:Context, pathname:Str, user:Str ) -> None:
	client:Client = context.obj['client']
	if user.isdigit():
		profile = client.graphql( PolarisProfilePageContentQuery( user ) )
		profile['__typename'] = typeof( PolarisProfilePageContentQuery )
	else:
		profile = client.profile( user )
		profile = profile['user']
		profile['__typename'] = typeof( client.profile )
	if not pathname.endswith( profile['username'] ):
		pathname+= f"/{profile['username']}"
	if not isdir( pathname ):
		_logger.info( "Create directory pathname: {}", pathname )
		mkdir( pathname )
	_logger.info( "Saving instagram metadata: {}/metadata-profile", pathname )
	with open( f"{pathname}/metadata-profile", "w" ) as fopen:
		fopen.write( JsonEncoder( profile, indent=4 ) )
		fopen.close()
	download( profile, pathname=pathname )
	puts( f"Successfully download profile picture {profile['username']}" )

@Media.command( help="Instagram profile picture media" )
@Option( "--user", help="Instagram profile user id", required=True, type=Str )
@Option( "--limit", help="Instagram profile reels item limit", required=False, type=Int )
@Option( "--pathname", help="Output the directory name to store the media", default=_PathnameDefault, type=Path( exists=False, dir_okay=True, writable=True ) )
@Initial
def reels( context:Context, limit:Int, user:Str, pathname:Str ) -> None:
	client:Client = context.obj['client']
	if not user.isdigit():
		puts( f"Invalid profile user id {user}", close=1 )
	iterator = client.reels( user, terminator=lambda item, position: limit != None and position >= limit )
	executor = ThreadExecutor(
		name="Instagram Profile Reels",
		callback=download,
		pathname=pathname,
		dataset=iterator,
		workers=20,
		timeout=4,
		delays=0,
		sleepy=0
	)
	for executed in executor:
		del executed
	puts( f"Successfully download profile reels" )

@Media.command( help="Instagram shortcode media" )
@Option( "--code", help="Instagram shortcode e.g url like /p/DER2KEDyajR", required=True, type=Str )
@Option( "--pathname", help="Output the directory name to store the media", default=_PathnameDefault, type=Path( exists=False, dir_okay=True, writable=True ) )
@Initial
def shortcode( context:Context, code:Str, pathname:Str ) -> None:
	client:Client = context.obj['client']
	urlparsed = urlparser( code )
	shortcode = urlparsed.path.split( "\x2f" )[-1]
	shortcodeMedia = client.graphql( PolarisPostActionLoadPostQueryQuery( shortcode ) )
	if not pathname.endswith( shortcodeMedia['owner']['username'] ):
		pathname+= f"/{shortcodeMedia['owner']['username']}"
	if not isdir( pathname ):
		_logger.info( "Create directory pathname: {}", pathname )
		mkdir( pathname )
	_logger.info( "Saving instagram metadata: {}/metadata-shortcode-{}", pathname, shortcode )
	with open( f"{pathname}/metadata-shortcode-{shortcode}", "w" ) as fopen:
		fopen.write( JsonEncoder( shortcodeMedia, indent=4 ) )
		fopen.close()
	download( shortcodeMedia, pathname=pathname )
	puts( "Successfully download media from shortcode" )

@Media.command( help="Instagram story media" )
@Option( "--id", help="Instagram story id highlighted or user id, commas separated", required=True, type=Str )
@Option( "--highlight", help="Tell the program if the id is a highlight id", is_flag=True )
@Option( "--pathname", help="Output the directory name to store the media", default=_PathnameDefault, type=Path( exists=False, dir_okay=True, writable=True ) )
@Initial
def story( context:Context, id:Str, highlight:Bool, pathname:Str ) -> None:
	ids = id.split( "\x2c" )
	length = len( ids )
	client:Client = context.obj['client']
	if not client.account.anonymous:
		polarisStories = []
		if highlight is True:
			highlightReelIds = list( f"highlight:{reelId}" if not reelId.startswith( "highlight" ) else reelId for reelId in ids )
			polarisStories = client.graphql( PolarisStoriesV3HighlightsPageQuery( 1, highlightReelIds ) )
		else:
			polarisStoriesReel = client.graphql( PolarisStoriesV3ReelPageStandaloneQuery( ids ) )
			for polarisStoryReel in polarisStoriesReel:
				for polarisStoryReelItem in polarisStoryReel['items']:
					polarisStoryReelItem['user'] = { **polarisStoryReel['user'] }
					polarisStories.append( polarisStoryReelItem )
		download( polarisStories, pathname )
	else:
		reelIds = ids if not highlight else []
		reelIds = list( int( reelId ) for reelId in reelIds )
		highlightReelIds = ids if highlight is True else []
		for i, reelId in enumerate( highlightReelIds ):
			if reelId.startswith( "\x68\x69\x67\x68\x6c\x69\x67\x68\x74\x3a" ):
				reelId = reelId.removeprefix( "\x68\x69\x67\x68\x6c\x69\x67\x68\x74\x3a" )
			highlightReelIds[i] = int( reelId )
		reelsMedia = client.story( reelIds=reelIds, highlightReelIds=highlightReelIds )
		download( reelsMedia, pathname )
	puts( f"Successfully download media from {length} story" )
