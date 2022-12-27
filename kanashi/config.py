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

#[kanashi.BaseConfig]
class BaseConfig( Context ):
	
	#[BaseConfig.default]
	default = {
		"authors": [
			{
				"name": "Ari Setiawan",
				"nick": "hxAri",
				"email": "ari160824@gmail.com",
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
				"email": "okutairi0701@gmail.com",
				"github": "https://github.com/okutairi"
			},
		],
		"browser": {
			"default": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36",
			"private": "Instagram 64.0.0.14.96"
		},
		"license": {
			"name": "GNU General Public License v3",
			"link": "https://www.gnu.org/licenses"
		},
		"setting": {
			"donate": "https://paypal.me/hxAri",
			"source": "https://github.com/hxAri/Kanashi",
			"issues": "https://github.com/hxAri/Kanashi/issues",
			"update": "https://github.com/hxAri/Kanashi/archive/refs/tags/v{version}.zip",
			"version": "1.1.3"
		},
		"signin": {
			"active": None,
			"switch": {}
		}
	}
	
	#[BaseConfig( Object app )]
	def __init__( self, app ):
		self.fname = "settings.json"
		self.fattr = Object( {}, self )
		self.fdict = None
		
		# Allow other contexts to access.
		app.setting = self.fattr
		
		# Reading file configuration.
		self.read()
		
		# Call parent constructor.
		super().__init__( app )
		
	#[Config.read()]
	def read( self ):
		self.err = None
		try:
			self.fdict = File.json( self.fname )
			self.fattr.set( self.fdict )
		except FileNotFoundError as e:
			self.err = Error( "Configuration file not found", prev=e )
		except JSONError as e:
			self.err = Error( "Configuration file has corrupted", prev=e )
		return( self )
		
	#[Config.save()]
	def save( self ):
		self.err = None
		try:
			if self.fdict:
				data = self.fattr.dict()
			else:
				data = BaseConfig.default
				self.fdict = data
				self.fattr.set( data )
			File.write( self.fname, data )
		except BaseException as e:
			self.err = Error( "Failed save configuration", prev=e )
		return( self )
	

#[kanashi.Config]
class Config( BaseConfig, Util ):
	
	#[Config.read()]
	def read( self ):
		self.thread( "Reading file configuration", BaseConfig.read, self )
		if self.err:
			self.save()
		else:
			return( self )
		
	#[Config.save()]
	def save( self ):
		self.thread( "Saving file configuration", BaseConfig.save, self )
		if self.err:
			self.emit( self.err )
			if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				self.save()
		return( self )
	