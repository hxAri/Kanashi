
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