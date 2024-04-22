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

from multiprocessing import Process as BaseProcess
from typing import Any, final, Tuple, TypeVar as Var


Value = Var( "Value" )
""" Initialize return values """


class Process( BaseProcess ):
	
	""" Process Support return value from target """
	
	def run( self ) -> None:
		
		""" Executing processs """
		
		if not callable( self._target ):
			raise TypeError( f"The process target must be Function|Method, {self._target} passed" )
		try:
			self._results = tuple([ self._target( *self._args, **self._kwargs ), None ])
		except BaseException as e:
			self._results = tuple([ None, e ])
		...
	
	@final
	@property
	def results( self ) -> Tuple[Value,BaseException]:
		if hasattr( self, "\x5f\x72\x65\x73\x75\x6c\x74\x73" ):
			return self._results
		return ( None, None )
	
	...