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

from builtins import bool as Bool, int as Int, str as Str
from datetime import datetime
from io import TextIOWrapper
from json import dumps as encoder
from mimetypes import guess_type as mimetype
from os import makedirs as mkdir, path
from sys import path as paths
from typing import Any, List, Union


BASEPARTS:List[Str] = paths[0].split( "\x2f" )
BASEPATH:Str = "\x2f".join( BASEPARTS[:BASEPARTS.index( "src" )] )
""" The Base Path of Kanashi Application """

BASEPARTS:List[Str] = paths[4].split( "\x2f" )
BASEVENV:Str = "\x2f".join( BASEPARTS[:BASEPARTS.index( "lib" )] )
""" The Base Path of Virtual Environment """

# Delete unused constant and variables.
del BASEPARTS
del paths


class Storage:
	
	""" Kanashi Storage Library Class """
	
	BASEPATH:Str = BASEPATH
	""" The Base Path of Kanashi Application """
	
	BASEVENV:Str = BASEVENV
	""" The Base Path of Virtual Environment """
	
	@staticmethod
	def fname() -> Str: return datetime.now().strftime( "%Y-%m-%d %H:%M:%S.json" )
	
	@staticmethod
	def cat( fname:Str, fmode:Str="r", stream:Bool=False ) -> Union[Str,TextIOWrapper]:
		
		"""
		Read the file contents
		
		:params Str fname
			The filename want to be read
		:params Str fmode
			The file read mode
		:params Bool stream
			Only return the wrapper
		
		:return Str|TextIOWrapper
		"""
		
		if fname[0] != "\x2f":
			fname = f"{Storage.BASEPATH}/{fname}"
		if stream is True:
			return open( fname, fmode )
		with open( fname, fmode ) as fopen:
			fread = fopen.read()
			fopen.close()
		return fread
	
	@staticmethod
	def catln( fname:Str, fmode:Str="r" ) -> List[Str]:
		
		"""
		Read file and split file contents with new line
		
		:params Str fname
			The filename want to be read
		:params Str fmode
			The file read mode
		
		:return List<Str>
		"""
		
		return Storage.cat( fname, fmode=fmode ).splitlines()
	
	@staticmethod
	def d( dname:Str ) -> Bool:
		if dname[0] != "\x2f":
			dname = f"{Storage.BASEPATH}/{dname}"
		return path.isdir( dname )
	
	@staticmethod
	def f( fname:Str ) -> Bool:
		if fname[0] != "\x2f":
			fname = f"{Storage.BASEPATH}/{fname}"
		return path.isfile( fname )
	
	@staticmethod
	def mime( fname:Str ) -> Str:
		if fname[0] != "\x2f":
			fname = f"{Storage.BASEPATH}/{fname}"
		return mimetype( fname )[0]
	
	@staticmethod
	def mkdir( dname:Str, mode:Int=511, existOk:Bool=True ) -> None:
		
		"""
		Make new directory
		
		:params Str dname
			The directory target
		:params Int mode
		:params Bool existOk
		
		:return None
		"""
		
		if dname[0] != "\x2f":
			dname = f"{Storage.BASEPATH}/{dname}"
		mkdir( dname, mode=mode, exist_ok=existOk )
	
	@staticmethod
	def touch( fname:Str, data:Any, fmode:Str="w" ) -> None:
		
		"""
		Create or append file contents.
		
		:params Str fname
		:params Any data
		:params Str fmode
		
		:return None
		"""
		
		if fname[0] != "\x2f":
			fname = f"{Storage.BASEPATH}/{fname}"
		with open( fname, fmode ) as fopen:
			fdata = data
			if not isinstance( data, ( Str, bytes ) ):
				try:
					fdata = encoder( data, indent=4 )
				except BaseException:
					fdata = str( data )
			fopen.write( fdata )
			fopen.close()
		...
	
	...
