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

from brotli import decompress as BrotliDecompress, error as BrotliError
from builtins import bool as Bool, int as Int, str as Str
from gzip import BadGzipFile, decompress as GzipDecompress
from pyzstd import decompress as ZstdDecompress, ZstdError
from requests import Session
from requests.exceptions import (
	ConnectionError as RequestConnectionError, 
	ConnectTimeout as RequestConnectionTimeout, 
	RequestException as RequestError
)
from time import sleep
from traceback import format_exception
from typing import ( 
	Any, 
	MutableMapping, 
	Optional, 
	Tuple, 
	Union
)
from urllib.parse import urlparse
from urllib3.exceptions import (
	ConnectionError as UrllibConnectionError,
	ConnectTimeoutError as UrllibConnectTimeoutError,
	RequestError as UrllibRequestError,
	NewConnectionError as UrllibNewConnectionError
)

from kanashi.common import typeof
from kanashi.logger import Logger
from kanashi.typing import Response


__all__ = [
	"request"
]


_logger = Logger( __name__ )
""" Logger Instance """


def request( method:Str, url:Str, auth:Optional[Tuple[Str,Str]]=None, data:Optional[MutableMapping[Str,Any]]=None, files:Optional[MutableMapping[Str,Any]]=None, cookies:Optional[MutableMapping[Str,Str]]=None, headers:Optional[MutableMapping[Str,Str]]=None, params:Optional[MutableMapping[Str,Str]]=None, payload:Optional[MutableMapping[Str,Any]]=None, proxies:Optional[MutableMapping[Str,Str]]=None, stream:Bool=False, verify:Optional[Bool]=None, timeout:Optional[Int]=None, tries:Int=10, thread:Union[Int,Str]=0 ) -> Optional[Response]:
	
	"""
	Send HTTP Request
	
	Parameters:
		method (Str):
			Http request method
		url (Str):
			Http request url target
		auth (Optional[Tuple[Str,Str]]):
			Http request authentication
		data (Optional[MutableMapping[Str,Any]]):
			Http request application/x-www-form-urlencoded
		files (Optional[MutableMapping[Str,Any]]):
			Http request multipart form data
		cookies (Optional[MutableMapping[Str,Str]):
			Http request cookies
		headers (Optional[MutableMapping[Str,Str]):
			Http request headers
		params (Optional[MutableMapping[Str,Str]):
			Http request parameters
		payload (Optional[MutableMapping[Str,Any]]):
			Http request application/json
		proxies (Optional[MutableMapping[Str,Any]]):
			Http request proxies
		stream (Bool):
			Allow request stream
		verify (Optional[Bool]):
			Verify http request
		timeout (Optional[Int]):
			Http request timeout
		tries (Int):
			Http request timeout tries
		thread (Int|Str):
			Current thread position number
	
	Returns:
		response (Optional[Response]):
			Request response
	"""
	
	counter = 0
	session = Session()
	throwned = []
	throwable = [
		RequestConnectionError, 
		RequestConnectionTimeout, 
		RequestError,
		UrllibConnectionError,
		UrllibConnectTimeoutError,
		UrllibRequestError,
		UrllibNewConnectionError
	]
	continueable = ( 
		RequestConnectionError, 
		RequestConnectionTimeout, 
		UrllibConnectionError,
		UrllibConnectTimeoutError,
		UrllibNewConnectionError
	)
	if tries <= 0:
		tries = 10
	urlparsed = urlparse( url )
	urlsimple = f"{urlparsed.scheme}://{urlparsed.netloc}{urlparsed.path}"
	while counter <= 10:
		_logger.warning( "Request {} url=\"{}\"", method, urlsimple, thread=thread )
		try:
			response = session.request( 
				url=url, 
				auth=auth,
				data=data, 
				files=files,
				json=payload, 
				stream=stream,
				method=method, 
				cookies=cookies, 
				headers=headers, 
				timeout=timeout,
				proxies=proxies,
				params=params 
			)
			_logger.warning( "Response {} url=\"{}\" code={}", method, urlsimple, response.status_code, thread=thread )
			encoding = response.headers['Content-Encoding'] \
				if "Content-Encoding" in response.headers \
				else None
			contentType = None
			characterSet = None
			if "Content-Type" in response.headers:
				parts = response.headers['Content-Type'].split( "\x3b" )
				characterSet = parts[1].strip( "\x20" ).split( "\x3d" ).pop() if len( parts ) >= 2 else None
				contentType = parts[0].strip( "\x20" )
			try:
				if encoding is not None:
					_logger.warning( "Trying to decompress content={} url=\"{}\"", encoding, urlsimple, thread=thread )
					content = response._content
					match encoding:
						case "br":
							content = BrotliDecompress( response.content )
						case "gzip":
							content = GzipDecompress( response.content )
						case "zstd":
							content = ZstdDecompress( response.content )
					response._content = content
				...
			except( BadGzipFile, BrotliError, ZstdError ) as e:
				_logger.critical( "{}: {}", typeof( e ), "\x0a".join( format_exception( e ) ), thread=thread )
			return Response(
				url=response.url,
				text=response.text,
				type=contentType,
				status=response.status_code,
				payload=payload if payload is not None else data,
				content=response.content,
				cookies=response.cookies,
				headers=response.headers,
				charset=characterSet,
				encoding=encoding
			)
		except BaseException as e:
			instance = type( e )
			throwable.append( e )
			_logger.error( "{}: {}", typeof( e ), "\x0a".join( format_exception( e ) ), thread=thread )
			if instance in throwable:
				if isinstance( e, continueable ):
					counter += 1
					sleep( 2 )
					continue
			if throwned:
				raise ExceptionGroup( f"An error occurred while sending a {method} request to url=\"{urlsimple}\"", throwned ) from e
			raise e
	...

