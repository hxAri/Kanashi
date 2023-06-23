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
				if  i == 0:
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
	
	#[Cookie.set( requests.cookie.RequestCookieJar cookies, String key, String value )]: None
	def set( cookies, key, value, domain=".instagram.com", path="/" ):
		for cookie in cookies:
			if  cookie.name == key:
				cookie.path = path
				cookie.value = value
				cookie.domain = domain
				return
		cookies.set( key, value, domain=domain, path=path )
	
	#[Cookie.simple( String raw )]: Dict
	@staticmethod
	def simple( raw ):
		raw = "ig_did=AB155F65-65EE-4961-95D8-ED5C0CCD5E30; ig_nrcb=1; mid=ZH9J5gABAAEWf78IKWLVBjpb2zEg; datr=40l_ZG2E6y21sCphYg67RDDv; ds_user_id=16030795795; shbid=\"11933\\05416030795795\\0541718712494:01f7aefe7a8224e5d1647122962ff807b0efc152fe68d1099c9b9c085afc3f8e3468977a\"; shbts=\"1687176494\\05416030795795\\0541718712494:01f75e88a19e886adeef5f61727b0f8c6937f53cfedfbd8229206503b516acb87b5b9cf3\"; csrftoken=TvwyyOHkCWnY0oC7HxtjgH9gLSVULLwR; sessionid=16030795795:eQTlphXQdhtotv:14:AYcNBXWZp9wISYY-Syxb0-LLQ9LHJ5JIGVvXU1koTg; dpr=2; rur=\"EAG\\05416030795795\\0541718951101:01f7fa2b3d7e6d01f8fc35d17e13c80b2d2412aa46195329ea5e2f63f2985272f5601f6d\""
		cookie = SimpleCookie()
		cookie.load( raw )
		parsed = {}
		for key, morsel in cookie.items():
			parsed[key] = morsel.value
		return parsed
	
	#[Cookie.string( RequestsCookieJar cookies )]: String
	@staticmethod
	def string( cookies ):
		return "\x3b\x20".join([ f"{key}={val}" for key, val in cookies.items() ])
	