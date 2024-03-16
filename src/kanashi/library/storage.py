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

from datetime import datetime
from io import TextIOWrapper
from json import dumps as encoder
from os import makedirs as mkdir, path
from typing import Any, List

from kanashi.constant import BASEPATH
from kanashi.typing.builtins import Bool, Int, Str

	
class Storage:

	@staticmethod
	def fname() -> Str: return datetime.now().strftime( "%Y-%m-%d %H:%M:%S.json" )

	@staticmethod
	def cat( fname:Str, stream:Bool=False ) -> Str|TextIOWrapper:
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		if stream is True:
			return open( fname, "r" )
		with open( fname, "r" ) as fopen:
			fread = fopen.read()
			fopen.close()
		return fread

	def catln( fname:Str ) -> List[Str]:
		return Storage.cat( fname ).splitlines()

	def d( dname:Str ) -> Bool:
		if dname[0] != "\x2f":
			dname = f"{BASEPATH}/{dname}"
		return path.isdir( dname )

	def f( fname:Str ) -> Bool:
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		return path.isfile( fname )

	def mkdir( dname:Str, mode:Int=511, existOk:Bool=True ) -> None:
		if dname[0] != "\x2f":
			dname = f"{BASEPATH}/{dname}"
		mkdir( dname, mode=mode, exist_ok=existOk )

	@staticmethod
	def touch( fname:Str, data:Any, fmode:Str="w" ) -> None:
		if fname[0] != "\x2f":
			fname = f"{BASEPATH}/{fname}"
		with open( fname, fmode ) as fopen:
			fdata = data
			if not isinstance( data, ( str, bytes ) ):
				try:
					fdata = encoder( data, indent=4 )
				except BaseException:
					fdata = str( data )
			fopen.write( fdata )
			fopen.close()
		...

	...
