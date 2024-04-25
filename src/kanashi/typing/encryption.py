
from builtins import str as Str
from typing import final

from kanashi.typing.readonly import Readonly


@final
class Encryption( Readonly ):
	
	""" Instagram Password Encryption Typing """
	
	def __init__( self, keyId:Str, publicKey:Str, version:Str ) -> None:
		
		"""
		Construct method of class Encryption
		
		:params Str keyId
		:params Str publicKey
		:params Str version
		
		:return None
		"""
		
		self.keyId:Str = keyId
		""" Instagram passsword encryption Key Id """
		
		self.publicKey:Str = publicKey
		""" Instagram password encryption Public Key """
		
		self.version:Str = version
		""" Instagram password encryption Version """
	
	...
