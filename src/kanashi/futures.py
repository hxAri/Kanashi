#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
# Follow, Unfollow, Media downloader, etc.
#
# Kanashi Copyright (c) 2024 - hxAri <hxari@proton.me>
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

from builtins import int as Int, str as Str
from concurrent.futures import (
	CancelledError as ThreadCancelledError, 
	Future, 
	ThreadPoolExecutor, 
	TimeoutError as ThreadTimeoutError
)
from multiprocessing import parent_process as ProcessParent
from os import getpid
from time import sleep
from traceback import format_exception
from typing import ( 
	Any, 
	Callable, 
	Iterable, 
	MutableSequence, 
	Optional, 
	TypeVar as Var
)

from kanashi.common import puts, typeof


__all__ = [
	"ThreadExecutor"
]


Args = Var( "Args" )
""" Arguments Type """

D = Var( "D" )
""" Dataset Type """

Kwargs = Var( "Kwargs" )
""" Key Arguments Type """

T = Var( "T" )
""" Return Type """


def ThreadExecutor( name:Str, callback:Callable[[D,Args,Kwargs,Int],T], dataset:Iterable[D], delays:Int=10, sleepy:Int=1, timeout:Int=4, workers:Int=2, *args:Any, **kwargs:Any ) -> Iterable[T]:
	
	"""
	Short ThreadPoolExecutor
	
	Parameters:
		name (Str):
			Thread prefix name
		callback (Callable[[D,Args,Kwargs],T]):
			Thread callback handler
		dataset (Iterable[D]):
			Datasets
		delays (Int):
			Thread delat per-workers
		sleepy (Int):
			Thread delay per-thread
		timeout (Int):
			Thread timeout
		workers (Int):
			Thread workers
		args (*Any):
			Callback handler arguments
		kwargs (**Any):
			Callback handler key arguments
	
	Returns:
		results (Iterable[T]):
			Iterable of callback return
	
	Examples:
	>>> datasets = [ ... ]
	>>> executor = ThreadExecutor(
	>>>     name="Bawaslu Crawler",
	>>>     callback=handler,
	>>>     dataset=datasets,
	>>>     sleepy=0,
	>>>     workers=10,
	>>>     workerDelays=4,
	>>>     workerTimeout=120
	>>> )
	>>> for execution in executor:
	>>>     print( execution )
	"""
	
	totals:Int = 0
	with ThreadPoolExecutor( workers, name ) as executor:
		futures:MutableSequence[Future] = []
		process = getpid()
		parent = ProcessParent()
		puts( f"Building ThreadPoolExecutor with {workers} workers for {name}", start="\x0d" )
		try:
			for thread, data in enumerate( dataset, 1 ):
				if parent is not None and parent:
					thread = f"P<I<{process}>,T<{thread}>>"
				puts( f"Starting thread for {name}", start="\x0d", thread=thread )
				future = executor.submit( callback, data, *args, thread=thread, **kwargs )
				futures.append( future )
				sleep( delays if ( thread ) % workers == 0 else sleepy )
			while futures and all( future.done() for future in [ *futures ] ) is False:
				for thread, future in enumerate( [ *futures ], 1 ):
					if future.running() is True:
						loading = f"Future thread worker T<{thread}> is running..."
						length = len( loading )
						position = -1
						for i in "\|/-" * 16:
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
							puts( messages, end="\x20", start="\x0d", thread=i )
					try:
						throwned = future.exception( 0 )
						if isinstance( throwned, BaseException ):
							traceback = "\x0a".join( format_exception( e ) )
							puts( f"Future thread worker T<{thread}> is raised {typeof( throwned )}: {traceback}", thread=thread, start="\x0d" )
							puts( f"Future thread worker T<{thread}> is deleted from futures", thread=thread, start="\x0d" )
							if future in futures:
								del futures[futures.index( future )]
					except ThreadCancelledError:
						...
					except TimeoutError:
						...
					finally:
						...
					...
				...
		except BaseException as e:
			executor.shutdown()
			traceback = "\x0a".join( format_exception( e ) )
			puts( f"Uncaught {typeof( e )}: {traceback}", start="\x0d" )
			puts( f"ThreadPoolExecutor has been shuting down", start="\x0a" )
		puts( "ThreadPoolExecutor enumerating futures", start="\x0d", thread="T" )
		for thread, future in enumerate( futures, 1 ):
			puts( f"Yielding from future thread worker T<{thread}> WT<{timeout}>", start="\x0d", end="", thread=thread )
			if future.cancelled() is True:
				puts( f"Future thread worker T<{i+1}> is cancelled", start="\x0d", thread=thread )
				continue
			try:
				yield future.result( timeout )
				totals+= 1
			except ThreadCancelledError:
				puts( f"Future thread worker T<{i+1}> is cancelled", start="\x0d", thread=thread )
			except ThreadTimeoutError:
				puts( f"Future thread worker T<{i+1}> is timeout", start="\x0d", thread=thread )
			except BaseException as e:
				traceback = "\x0a".join( format_exception( e ) )
				puts( f"{typeof( e )}: {traceback}", start="\x0d", thread=thread )
			...
		...
	puts( f"", start="\x0a", thread="T" )
	puts( f"A total of {totals} worker threads have been completed", start="\x0d", thread="T" )
	puts( f"ThreadPoolExecutor for {name} stoped", start="\x0d", thread="T" )
