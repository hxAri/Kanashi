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

from builtins import bool as Bool, str as Str
from multiprocessing import Pipe, Process as BaseProcess
from multiprocessing.connection import Connection
from typing import Any, Callable, Iterable, Mapping, final, Tuple, TypeVar as Var


Value = Var( "Value" )
""" Initialize return values """


class Process( BaseProcess ):
	
	""" Process Support return value from target """
	
	def __init__( self, group:Str=None, target:Callable[[],Any]=None, name:Str=None, args:Iterable[Any]=..., kwargs:Mapping[Str,Any]=..., *, daemon:Bool=None ) -> None:
		
		"""
		Construct method of class Process
		
		:params Str group
		:params Callable<<>,Any> target
		:params Str name
		:params Iterable<Any> args
		:params Mapping<Str,Any>kwargs
		:params Bool daemon
		
		:return None
		"""
		
		BaseProcess.__init__( self, group, target, name, args, kwargs, daemon=daemon )
		self._pipe = Pipe()
		self._child_conn:Connection = self._pipe[1]
		self._parent_conn:Connection = self._pipe[0]
	
	def run( self ) -> None:
		
		""" Executing processs """
		
		values = None
		thrown = None
		target = self._target
		if not callable( target ):
			raise TypeError( f"The process target must be Function|Method, {target} passed" )
		try:
			values = target( *self._args, **self._kwargs )
		except BaseException as e:
			thrown = e
		self._child_conn.send( ( values, thrown ) )
	
	@final
	@property
	def results( self ) -> Tuple[Value,BaseException]:
		if self._parent_conn.poll():
			return self._parent_conn.recv()
		return ( None, None )
	
	...