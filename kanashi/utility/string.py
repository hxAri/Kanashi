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


from base64 import b64encode
from base64 import b64decode
from binascii import hexlify
from random import choice
from re import finditer
from string import ascii_lowercase, ascii_uppercase


#[kanashi.utility.string.Binary]
class Binary:
	
	#[Binary.bin2hex( String bin )]: String
	@staticmethod
	def bin2hex( bin ):
		
		"""
		Parse binary string to hexadecimal string.
		
		:params String bin
			Binary string
		
		:return String
		"""
		
		hex = hexlify( bytes( bin, "utf-8" ) )
		hexa = str( hex, "utf-8" )
		find = finditer( "([0-9a-fA-F]{2})", hexa )
		return "\\x{}".format( "\\x".join( i.group() for i in find ) )
	
	#[Binary.hex2bin( String hex )]: String
	@staticmethod
	def hex2bin( hex ):
		
		"""
		Parse hexadecimal string to binary string.
		
		:params String hex
			Hexadecimal string
		
		:return String
		"""
		
		hexa = hex.replace( "\\x", "" )
		byte = bytearray.fromhex( hexa )
		return byte.decode()
	

#[kanashi.utility.string.String]
class String( Binary ):
	
	#[String.encode( String text, String encode )]: String
	@staticmethod
	def encode( text, encode="ascii" ):
		ascii = text.encode( encode )
		b64en = b64encode( ascii )
		return String.bin2hex( b64en.decode( encode ) )
	
	#[String.decode( String enc )]: String
	@staticmethod
	def decode( enc ):
		return str( b64decode( bytes( String.hex2bin( enc ), "utf-8" ) ), "utf-8" )
	
	#[String.random( Int length )]: String
	def random( length=32 ):
		
		"""
		For the record, this does not generate a
		random string for security only file names.
		
		:params Int length
			Random string length
		
		:return String
		"""
		
		letter = ascii_lowercase
		letter += ascii_uppercase
		letter += ""
		return "".join( choice( letter ) for i in range( length ) )
	