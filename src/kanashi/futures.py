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

from builtins import int as Int, str as Str
from sys import argv
from time import sleep
from typing import Any, Callable, TypeVar as Var, Union

from kanashi.common import stderr, stdin, stdout, puts
from kanashi.typing import Process, Thread


Value = Var( "Value" )
""" Value Type """


def Processing( context:Any, target:Callable[[],Any], loading:Str, success:Str=None, group:Str=None, name:Str=None, *args:Any, **kwargs:Any ) -> Union[Value,BaseException]:
	
	"""
	Process handler
	
	:params Any context
	:params Callable<<>,Any> target
	:params Str loading
	:params Str success
	:params Str group
	:params Str name
	:params Any *args
	:params Any **kwargs
	
	:return Value|BaseException
	"""
	
	stdout( context, None, clear=True )
	process = Process( name=name, group=group, target=target, args=args, kwargs=kwargs )
	try:
		process.start()
		watcher( process, loading )
		results = process.results
		if results[1] is None or not isinstance( results[1], BaseException ):
			stdout( context, success if success is not None else loading, clear=True )
			return results[0]
		stderr( context, results[1], "The child process encountered an unhandled error", clear=True )
		return results[1]
	except ( EOFError, KeyboardInterrupt ) as e:
		process.kill()
		process.terminate()
		stderr( context, e, "The child process has been force terminated", clear=True )
	return None

def Threading( context:Any, target:Callable[[],Any], loading:Str, success:Str=None, group:Any=None, name:Str=None, *args:Any, **kwargs:Any ) -> Union[Value,BaseException]:
	
	"""
	Thread handler
	
	:params Any context
	:params Callable<<>,Any> target
	:params Str loading
	:params Str success
	:params Any group
	:params Str name
	:params Any *args
	:params Any **kwargs
	
	:return Value|BaseException
	"""
	
	stdout( context, None, clear=True )
	thread = Thread( name=name, group=group, target=target, args=args, kwargs=kwargs )
	thrown = None
	try:
		thread.start()
		while True:
			try:
				if thrown is not None:
					stderr( context, thrown, "Cannot kill child threads, while they are running", clear=True )
				watcher( thread, loading )
				returns = thread.returns
				if returns[1] is None or not isinstance( returns[1], BaseException ):
					stdout( context, success if success is not None else loading, clear=True )
					return returns[0]
				stderr( context, returns[1], "An unhandled error occurred in the child thread", clear=True )
				stdin( default="Y" )
				return returns[1]
			except ( EOFError, KeyboardInterrupt ) as e:
				thrown = e
			...
	except BaseException as e:
		stderr( context, e, "Looks like a problem child thread", clear=True )
	return None

def watcher( target:Union[Process,Thread], loading:Str ) -> None:
	
	"""
	Process or Thread watcher
	
	:params Callable<<>,Any> target
	:params Str loading
	
	:return None
	"""
	
	while target.is_alive():
		length = len( loading )
		position = -1
		for i in "\\|/-" * 8:
			if position >= length:
				position = -1
			position += 1
			messages = loading
			if position >= 1:
				messageChar = loading[position-1:position]
				messageChar = messageChar.lower() \
					if messageChar.isupper() \
					else messageChar.upper()
				messagePrefix = loading[0:position-1]
				messageSuffix = loading[position:]
				messages = "".join([
					messagePrefix, 
					messageChar, 
					messageSuffix
				])
			puts( f"    {messages} {i}", end="\x20", start="\x0d" )
			sleep( 0.1 )
		...
	...
