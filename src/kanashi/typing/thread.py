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

from threading import Thread as Threading
from typing import final, Tuple, TypeVar as Var


Value = Var( "Value" )
""" Initialize return values """


class Thread( Threading ):
	
	""" Thread class support data return """
	
	def run( self ) -> None:
		
		""" Executing thread target """
		
		values = None
		thrown = None
		try:
			if not callable( self._target ):
				raise TypeError( f"The thread target must be Function|Method, {self._target} passed" )
			values = self._target( *self._args, **self._kwargs )
		except BaseException as e:
			thrown = e
		del self._target
		del self._args
		del self._kwargs
		self._returns:Tuple[Value,BaseException] = ( values, thrown )
	
	@final
	@property
	def returns( self ) -> Tuple[Value,BaseException]:
		results = ( None, None )
		attribute = "\x5f\x72\x65\x74\x75\x72\x6e\x73"
		if hasattr( self, attribute ):
			results = getattr( self, attribute )
		return results
	
	...