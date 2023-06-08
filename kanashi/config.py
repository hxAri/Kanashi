#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashi Copyright (c) 2022 - Ari Setiawan <ari160824@gmail.com>
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
# Kanashi is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from kanashi.context import Context
from kanashi.error import Error
from kanashi.object import Object
from kanashi.utils import File, JSONError, Util

#[kanashi.Config]
class Config( Context ):
	
	#[Config.default]
	default = {
	    "authors": [
	        {
	            "name": "Ari Setiawan",
	            "nick": "hxAri",
	            "email": "hxari@proton.me",
	            "github": "https://github.com/hxAri"
	        },
	        {
	            "name": "Aisyah Diesliana",
	            "nick": "Lianary",
	            "email": None,
	            "github": "https://github.com/AisyahDiesliana"
	        },
	        {
	            "name": "Falsa Fadilah Nugraha",
	            "nick": "Valxxa",
	            "email": None,
	            "github": None
	        },
	        {
	            "name": "Okutairi",
	            "nick": "Okutairi",
	            "email": None,
	            "github": "https://github.com/okutairi"
	        }
	    ],
	    "browser": {
	        "default": "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
	        "private": "Instagram 274.0.0.26.90"
	    },
	    "license": {
	        "name": "GNU General Public License v3",
	        "link": "https://www.gnu.org/licenses"
	    },
	    "path": {
	        "collection": "onsaved/collections",
	        "comment": "onsaved/comments",
	        "follower": "onsaved/followers",
	        "following": "onsaved/following",
	        "image": "onsaved/images",
	        "like": "onsaved/likes",
	        "post": "onsaved/posts",
	        "profile": "onsaved/profiles",
	        "reel": "onsaved/reels",
	        "saved": "onsaved/saveds",
	        "story": "onsaved/story",
	        "video": "onsaved/videos",
	        "views": "onsaved/views"
	    },
	    "donate": "https://paypal.me/hxAri",
	    "source": "https://github.com/hxAri/Kanashi",
	    "issues": "https://github.com/hxAri/Kanashi/issues",
	    "update": "https://github.com/hxAri/Kanashi/archive/refs/tags/v{version}.zip",
	    "signin": {
	        "active": False,
	        "switch": {}
	    },
	    "version": "1.1.5"
	}
	
	#[Config( Object app )]
	def __init__( self, app ):
		
		self.fname = "settings.json"
		self.fattr = Object( {}, self )
		self.fdict = None
		
		# Allow other contexts to access.
		app.settings = self.fattr
		
		# Call parent constructor.
		super().__init__( app )
		
	#[Config.read()]
	def read( self ):
		try:
			self.fdict = File.json( self.fname )
			self.fattr.set( self.fdict )
			return( True )
		except FileNotFoundError as e:
			raise ConfigError( "Configuration file not found", throw=self, prev=e )
		except JSONError as e:
			raise ConfigError( "Configuration file has corrupted", throw=self, prev=e )
		return True
		
	#[Config.save()]
	def save( self ):
		try:
			if self.fdict != None:
				data = self.fattr.dict()
			else:
				data = Config.default
				self.fdict = data
				self.fattr.set( data )
			File.write( self.fname, data )
		except Exception as e:
			raise ConfigError( "Failed save configuration", throw=self, prev=e )
		return True
	

#[kanashi.ConfigError]
class ConfigError( Error ):
	pass
	