


from re import match
from typing import final

from kanashi.object import Object
from kanashi.utility import droper


#[kanashi.typing.Typing]
class Typing( Object ):

	"""
	The Typing class has almost the same way of working as the Object class
	from Kanashi, but Typing will only forward the items returned by the __items__
	method to its parent class, its Object from Kanashi, the aim is to avoid errors
	when checking response data and so on because, Kanashi treats dictionaries and also
	lists as objects will be very confusing considering that Instagram usually provides
	a fairly large response to be processed and, when the JSON response is passed to a
	class that extends the Typing class it will only take and also set the value that
	was returned by the previous __items__ method however, we can also set incompatible
	items from outside the class or inside except the instance.

	Apart from that, Typing also normalizes strings to int values ​​if the value only contains numbers.
	"""

	#[Typing( Dict|List|Object data, Object parent )]: None
	@final
	def __init__( self, data:dict|list|Object, parent:object=None ) -> None:
		if not isinstance( data, ( dict, Object ) ):
			raise TypeError()
		super().__init__( droper( data, self.__items__ ), parent )

	#[Typing.__items__()]: Dict<Str, Str>|List<Str>
	@property
	def __items__( self ) -> dict[str:str]|list[str]:
		raise NotImplementedError( "Property {} is not initialize or implemented".format( self.__allows__ ) )

	#[Typing.__resolver__( Any value )]: Any
	@final
	def __resolver__( self, value:any ) -> any:
		if isinstance( value, ( dict, list, Object ) ):
			indexs = [ idx for idx in range( len( value ) ) ]
			if isinstance( value, ( dict, Object ) ):
				indexs = value.keys()
			for index in indexs:
				value[indexs[index]] = self.__resolver__( value[indexs[index]] )
		elif isinstance( value, str ):
			matches = match( r"^(?:\d+)$", value )
			if matches is not None:
				value = int( value )
		return value
