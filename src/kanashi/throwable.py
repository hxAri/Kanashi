#!/usr/bin/env python3

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

from abc import ABC as Abstract
from builtins import int as Int, str as Str
from typing import Any, Callable, Final, Dict, List
from typing import TypeVar as Var, TypeVarTuple as Tvt


Key = Var( "Key" )
""" Keyset Type """

Val = Var( "Val" )
""" Value Type """

Args = Tvt( "Args" )
""" Argument Type """


class Throwable( Abstract, BaseException ):

	""" A base exception for Identify if raised exception is from Kanashī """
	
	def __init__( self, message:Str, code:Int=0, context:Any=None, prev:BaseException=None, groups:List[BaseException]=None, callback:Callable[[*Args],Any]=None, **kwargs:Any ) -> None:
		
		"""
		Construct method of Throwable
		
		:params Str message
			The exception message
		:params Int code
			The exception code
		:params Any context
			The exception throwned
		:params BaseException prev
			The previous exception
		:params List<BaseException> groups
			The group of previous throwned exceptions
		:params Callable callback
			The callback for handle exception situation
		:params Any **kwargs
		
		:return None
		"""
		
		self.message:Final[Str] = message
		""" The exception message """
		
		self.code:Final[Int] = code
		""" The exception code """
		
		self.context:Final[Any] = context
		""" The exception throwned """
		
		self.prev:Final[BaseException] = prev
		""" The previous exception """
		
		self.group:Final[List[BaseException]] = groups if isinstance( groups, list ) else []
		""" The group of previous throwned exceptions """
		
		self.callback:Final[Callable] = callback
		""" The callback for handle exception situation """
		
		self.kwargs:Final[Dict[Key,Val]] = kwargs
		""" The Exception key arguments """
		
		super().__init__( message, code )
	
	...
