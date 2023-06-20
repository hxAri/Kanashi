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

from http.cookies import SimpleCookie
from re import findall

from kanashi.utility.string import String


#[kanashi.utililty.cookie.Cookie]
class Cookie:
	
	#[Cookie.parse( String raw )]
	@staticmethod
	def parse( raw ):
		expires = findall( r"expires\=([^\;]+)", raw )
		for expire in expires:
			raw = raw.replace( expire, String.bin2hex( expire ) )
		raw = raw.split( ", " )
		jar = []
		for item in raw:
			cookie = {
				"name": None,
				"value": None,
				"rest": {
					"HttpOnly": None
				}
			}
			attribute = item.split( "; " )
			for i in range( len( attribute ) ):
				attr = attribute[i].split( "=" )
				if i == 0:
					cookie['name'] = attr[0]
					cookie['value'] = attr[1]
				else:
					attrName = attr[0].lower()
					match attrName:
						case "secure":
							cookie['secure'] = True
						case "expires":
							cookie['expires'] = String.hex2bin( attr[1] )
						case "httponly":
							cookie['rest']['HttpOnly'] = True
						case "samesite":
							cookie['rest']['SameSite'] = attr[1]
						case _:
							try:
								cookie[attrName] = attr[1]
							except IndexError:
								pass
			jar.append( cookie )
		return jar
	
	#[Cookie.simple( String raw )]
	@staticmethod
	def simple( raw ):
		cookie = SimpleCookie()
		cookie.load( raw )
		parsed = {}
		for key, morsel in cookie.items():
			parsed[key] = morsel.value
		return parsed
	
	#[Cookie.string( RequestsCookieJar cookies )]
	@staticmethod
	def string( cookies ):
		return "\x3b\x20".join([ f"{key}={val}" for key, val in cookies.items() ])
	