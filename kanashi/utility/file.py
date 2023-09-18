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


from kanashi.utility.json import JSON
from kanashi.utility.path import Path


#[kanashi.utility.file.File]
class File:
	
	#[File.json( Str fname )]: Dict|List
	@staticmethod
	def json( fname:str ) -> dict|list:
		
		"""
		Read file and return decoded json contents.
		
		:params String fname
			Filename
		
		:return Dict|List
			Decoded json contents
		
		:raises JSONError
			When json is corrupted or syntax error
		"""
		
		return( JSON.decode( File.read( fname ) ) )
	
	#[File.read( Str fname )]: Str
	@staticmethod
	def read( fname:str ) -> str:
		
		"""
		Read file contents.
		
		:params String fname
			Filename
		
		:return String
			File contents
		"""
		
		with open( fname, "r" ) as fopen:
			fread = fopen.read()
			fopen.close()
		return( fread )
	
	#[File.readline( Str fname )]: List
	@staticmethod
	def readline( fname:str ) -> list:
		return File.read( fname ).split( "\n" )
	
	#[File.remove( Str fname )]: None
	def remove( fname:str ) -> None: ...
	
	#[File.write( Str fname, Str fdata, Str fmode )]: None
	@staticmethod
	def write( fname:str, fdata, fmode:str="w" ) -> None:
		
		"""
		Write content into file.
		
		:params String fname
			Filename
		:params Mixed fdata
			File contents to be write
		:params String fmode
			File open mode
		
		:return  None
		"""
		
		fpath = fname.split( "/" )
		fpath.pop()
		if len( fpath ) > 0:
			Path.mkdir( "/".join( fpath ) )
		match type( fdata ).__name__:
			case "dict" | "list":
				fdata = JSON.encode( fdata )
			case _:
				pass
		with open( fname, fmode ) as fopen:
			fopen.write( fdata )
			fopen.close()
	