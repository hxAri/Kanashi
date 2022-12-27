
from base64 import b64encode
from base64 import b64decode
from binascii import hexlify
from re import finditer

#[kanashi.Binary]
class Binary:
	
	@staticmethod
	def bin2hex( bin ):
		hex = hexlify( bytes( bin, "utf-8" ) )
		hexa = str( hex, "utf-8" )
		find = finditer( "([0-9a-fA-F]{2})", hexa )
		return( "\\x{}".format( "\\x".join( i.group() for i in find ) ) )
		
	@staticmethod
	def hex2bin( hex ):
		hexa = hex.replace( "\\x", "" )
		byte = bytearray.fromhex( hexa )
		return( byte.decode() )
	
#[kanashi.String]
class String( Binary ):
		
	#[String.encode()]
	@staticmethod
	def encode( text, encode="ascii" ):
		ascii = text.encode( encode )
		b64en = b64encode( ascii )
		return( String.bin2hex( b64en.decode( encode ) ) )
		
	#[String.decode()]
	@staticmethod
	def decode( enc ):
		return( str( b64decode( bytes( String.hex2bin( enc ), "utf-8" ) ), "utf-8" ) )
	
		