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

from kanashi.utils.json import JSON
from kanashi.utils.path import Path

#[kanashi.utils.File]
class File():
	
	#[File.json( String fname )]
	@staticmethod
	def json( fname ):
		return( JSON.decode( File.read( fname ) ) )
		
	#[File.read( String fname )]
	@staticmethod
	def read( fname ):
		with open( fname, "r" ) as fopen:
			fread = fopen.read()
			fopen.close()
		return( fread )
		
	#[File.write( String fname, String fdata, String fmode )]
	@staticmethod
	def write( fname, fdata, fmode="w" ):
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
	