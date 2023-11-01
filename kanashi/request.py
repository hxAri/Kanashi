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


from datetime import datetime, timedelta
from re import match
from urllib.parse import parse_qs as queryparse, urlparse
from requests import Session, Response
from requests.cookies import RequestsCookieJar as Cookies
from requests.structures import CaseInsensitiveDict as Headers
from typing import final

from kanashi.config import Config
from kanashi.error import ( 
	RequestError, 
	RequestAuthError, 
	RequestDownloadError
)
from kanashi.object import Object
from kanashi.pattern import Pattern
from kanashi.readonly import Readonly
from kanashi.utility import (
	Cookie, 
	File, 
	Path, 
	typeof 
)


#[kanashi.request.Request]
class Request( Readonly ):

	# Default request headers.
	HEADERS = {
		"User-Agent": f"Kanashi/{Config.VERSION}"
	}

	# Default request timeouts.
	TIMEOUTS = 10
	
	#[Request( Cookies|Dict|Object cookies, Dict|Headers|Object headers, Int timeout, Bool history )]: None
	def __init__( self, cookies:Cookies|dict|Object=None, headers:dict|Headers|Object=None, timeout:int=15, history:bool=True ) -> None:
		
		"""
		Construct of method class Request.
		
		:params Cookies|Dict|Object cookies
			Request cookies
		:params Dict|Headers|Object headers
			Header settings for requests
		:params Int timeout
			Default timeout for requests
		:params Bool history
			Allow every successful request to save
		
		:return None
		:raises TypeError
			Raise when the value of parameter is invalid
		"""

		# Readonly exceptional.
		self.__except__ = [
			"__previous__",
			"__response__",
			"__timeout__",
			"__history__"
		]

		# History configurations.
		self.__history__ = []
		self.__historyAllow__ = history is True
		self.__historyFname__ = "requests/response.json"
		self.__historyFormat__ = "requests/{}/response\x20{}.json"
		self.__historyFormatHtml__ = "requests/{}/html/response\x20{}.html"

		# Request configurations.
		self.__session__ = Session()
		self.__cookies__ = self.session.cookies
		self.__headers__ = self.session.headers

		self.__previous__ = None
		self.__response__ = None
		
		# Default request timeout.
		self.__timeout__ = timeout if isinstance( timeout, int ) else Request.TIMEOUTS
		
		if headers is not None:
			if not isinstance( headers, ( dict, Headers, Object ) ):
				raise TypeError( "Invalid \"request\" parameter, value must be type Dict|Headers|Object, {} passed".format( typeof( headers ) ) )
			if isinstance( headers, Headers ):
				headers = dict( headers )
		else:
			headers = {}
		for header in Request.HEADERS.keys():
			if header not in headers:
				headers[header] = Request.HEADERS[header]
		for header in headers.keys():
			self.headers.update({ header: headers[header] })
		if cookies is not None:
			if not isinstance( cookies, ( Cookies, dict, Object ) ):
				raise TypeError( "Invalid \"request\" parameter, value must be type Cookies|Dict|Object, {} passed".format( typeof( cookies ) ) )
			if isinstance( cookies, Cookies ):
				cookie = dict( cookies )
			for cookie in cookies.keys():
				Cookie.set( self.cookies, cookie, cookies[cookie] )
		
		# If every successful request is allowed to save.
		if self.historyAllow:
			try:
				self.__history__ = File.json( self.historyFname )
			except FileNotFoundError as e:
				self.clean()
	
	#[Request.__error__( Exception error )]: Exception
	@final
	def __error__( self, error ):
		name = typeof( error )
		names = {
			"InvalidJSONError": "{name}: A JSON error occured",
			"JSONDecodeError": "{name}: Couldn't decode the text into json",
			"HTTPError ": "{name}: An HTTP error occurred",
			"ConnectionError ": "{name}: A Connection error occurred",
			"ProxyError ": "{name}: A proxy error occurred",
			"SSLError ": "{name}: An SSL error occurred",
			"Timeout ": "{name}: The request timed out",
			"ConnectTimeout ": "{name}: The request timed out while trying to connect to the remote server",
			"ReadTimeout ": "{name}: The server did not send any data in the allotted amount of time",
			"URLRequired ": "{name}: A valid URL is required to make a request",
			"TooManyRedirects ": "{name}: Too many redirects",
			"MissingSchema ": "{name}: The URL scheme (e.g. http or https) is missing",
			"InvalidSchema ": "{name}: The URL scheme provided is either invalid or unsupported",
			"InvalidURL ": "{name}: The URL provided was somehow invalid",
			"InvalidHeader ": "{name}: The header value provided was somehow invalid",
			"InvalidProxyURL ": "{name}: The proxy URL provided is invalid",
			"ChunkedEncodingError": "{name}: The server declared chunked encoding but sent an invalid chunk",
			"ContentDecodingError": "{name}: Failed to decode response content",
			"StreamConsumedError": "{name}: The content for this response was already consumed",
			"RetryError": "{name}: Custom retries logic failed",
			"UnrewindableBodyError": "{name}: Requests encountered an error when trying to rewind a body",
			"RequestsWarning": "{name}: Base warning for Requests",
			"FileModeWarning": "{name}: A file was opened in text mode, but Requests determined its binary length",
			"RequestsDependencyWarning": "{name}: An imported dependency doesn't match the expected version range"
		}
		if  name in names:
			string = names[name]
		else:
			string = "{name}: There was an ambiguous exception that occurred while handling your request"
			string += str( error )
		return RequestError( string.format( name=name ), prev=error )
	
	#[Request.__parse__( Str url )]: Dict<Str, Dict|Str>
	def __parse__( self, url:str ) -> dict[str:dict|str]:
		parsed = urlparse( url )
		query = queryparse( parsed.query )
		return {
			"path": parsed.path[1::] if parsed.path != "" else "/",
			"url": parsed.geturl(),
			"query": query
		}
	
	#[Request.__save__()]: Request
	@final
	def __save__( self ):
		
		"""
		Save every successful request
		
		:return Request
			Instance of class Request
		"""
		
		if  self.historyAllow is not True: return
		if  self.response != False and \
			self.response != None:
			try:
				content = self.response.json()
			except Exception:
				try:
					content = f"[{self.response.headers['Content-Type']}]"
				except Exception:
					content = None
			parsed = self.__parse__( self.response.url )
			query = parsed['query']
			time = datetime.now()
			file = self.historyFormat.format( parsed['path'], f"{time}" ).replace( "//", "/" )
			timestamp = datetime.timestamp( time )
			self.__history__.append({
				"url": parsed['url'],
				"file": file,
				"time": timestamp
			})
			File.write( self.historyFname, self.history )
			File.write( file, {
				"target": parsed['url'],
				"browser": self.response.request.headers['User-Agent'],
				"unixtime": timestamp,
				"request": {
					"cookies": dict( self.cookies ),
					"headers": dict( self.headers ),
					"method": self.response.request.method,
					"query": query,
					"body": self.response.request.body
				},
				"response": {
					"status": f"{self.response}",
					"cookies": dict( self.response.cookies ),
					"headers": dict( self.response.headers ),
					"content": content
				}
			})
			if match( Pattern.HTML, self.__response__.headers['Content-Type'] ) is not None:
				File.write( 
					self.historyFormatHtml.format( parsed['path'], f"{time}" ).replace( "//", "/" ), 
					self.response.content.decode( "utf-8" ) 
				)
		return( self )
	
	#[Request.clean()]: Bool
	def clean( self ) -> bool:
		Path.rmdir( "requests" )
		self.__history__ = []
		self.__previous__ = None
		self.__response__ = None
		try:
			File.write( self.historyFname, "[]" )
		except Exception:
			return False
		return True
	
	#[Request.cookies]: Cookies => RequestsCookieJar
	@final
	@property
	def cookies( self ) -> Cookies: return self.__cookies__

	#[Request.delete( String url, **kwargs )]: Response
	@final
	def delete( self, url, **kwargs ) -> Response:
		return( self.request( "DELETE", url=url, **kwargs ) )

	#[Request.download( String url, String name, String fmode, **kwargs )]: Bool
	def download( self, url, name, fmode="wb", **kwargs ):
		
		"""
		Download content from url.
		
		:params String url
			The target url of the content
		:params String name
			Content/ Filename
		:params String fmode
			File open mode
		:params Any **kwargs
			Request options
		
		:return Bool<True>
			When the content is successfully saved
		:raises RequestError
			When an error occurs while performing the request
		:raises RequestDownloadError
			When the download is failed
			When the content/ file can't save
		"""
		
		try:
			result = self.get( url )
		except RequestError as e:
			raise e
		if  result.status_code == 200:
			try:
				File.write( name, result.content, fmode )
			except Exception as e:
				raise RequestDownloadError( f"Failed write file \"{name}\"", prev=e )
			return True 
		else:
			raise RequestDownloadError( f"Failed get content from url, status [{result.status_code}]" )
	
	#[Request.get( String url, **kwargs )]: Response
	@final
	def get( self, url, **kwargs ) -> Response:
		return( self.request( method="GET", url=url, **kwargs ) )
	
	#[Request.head( String url, **kwargs )]: Response
	@final
	def head( self, url, **kwargs ) -> Response:
		return( self.request( method="HEAD", url=url, **kwargs ) )

	#[Request.headers]: Headers => CaseInsensitiveDict
	@final
	@property
	def headers( self ) -> Headers: return self.__headers__

	#[Request.history]: List
	@final
	@property
	def history( self ) -> list: return self.__history__
	
	#[Request.historyAllow]: Bool
	@final
	@property
	def historyAllow( self ) -> bool: return self.__historyAllow__
	
	#[Request.historyFname]: Str
	@final
	@property
	def historyFname( self ) -> str: return self.__historyFname__
	
	#[Request.historyFormat]: Str
	@final
	@property
	def historyFormat( self ) -> str: return self.__historyFormat__

	#[Request.historyFormatHtml]: Str
	@final
	@property
	def historyFormatHtml( self ) -> str: return self.__historyFormatHtml__

	#[Request.options( String url, **kwargs )]
	@final
	def options( self, url, **kwargs ):
		return( self.request( method="OPTIONS", url=url, **kwargs ) )
	
	#[Request.patch( String url, **kwargs )]: Response
	@final
	def patch( self, url, **kwargs ) -> Response:
		return( self.request( method="PATCH", url=url, **kwargs ) )
	
	#[Request.post( String url, **kwargs )]: Response
	@final
	def post( self, url, **kwargs ) -> Response:
		return( self.request( method="POST", url=url, **kwargs ) )
	
	#[Request.previous]: Response
	@final
	@property
	def previous( self ) -> Response: return self.__previous__
	
	#[Request.previously( Str time )]: List
	def previously( self, time:str ) -> list:
		
		"""
		Return previous request responses based on given time.
		
		:params String time
			Value must be like [0-9](s|m|h|d|w|M|y)
		
		:return List
			List of request responses
		:raises TypeError
			When the given string is invalid syntax
		:raises ValueError
			When the parameter passed is invalid value
		"""
		
		current = datetime.now()
		if  not isinstance( time, str ):
			raise ValueError( "Invalid time parameter, value must be type str, {} passed".format( typeof( time ) ) )
		if  valid := match( r"^(?P<diff>[1-9][0-9]*)(?P<unit>s|m|h|d|w|M|y)$", time ):
			diff = int( valid.group( "diff" ) )
			unit = valid.group( "unit" )
			data = []
			match unit:
				case "m":
					delta = timedelta( minutes=diff )
				case "h":
					delta = timedelta( hours=diff )
				case "d":
					delta = timedelta( days=diff )
				case "w":
					delta = timedelta( weeks=diff )
				case "M":
					delta = timedelta( days=diff * 30 )
				case "y":
					delta = timedelta( days=diff * 365 )
			for history in self.history:
				timestamp = datetime.fromtimestamp( history['time'] )
				if  timestamp >= current - delta:
					data.append( history )
			return data
		else:
			raise TypeError( "Invalid time syntax, value must be like \\d+(s|m|h|d|w|M|y)" )
	
	#[Request.put( String url, **kwargs )]: Response
	@final
	def put( self, url, **kwargs ) -> Response:
		return( self.request( method="PUT", url=url, **kwargs ) )
	
	#[Request.request( String method, String url, **kwargs )]: Response
	@final
	def request( self, method, url, **kwargs ) -> Response:
		
		"""
		Send request to url target.
		
		:params String method
			Request method name
		:params String url
			Request url target
		:params Any **kwargs
			Request options
		
		:return Any
		:raises RequestError
			When an error occurs while performing the request
		:raises RequestAuthError
			When the user login authentication required
		"""
		
		self.__previous__ = self.response
		self.__response__ = None
		
		if "timeout" not in kwargs:
			kwargs['timeout'] = self.timeout
		if "cookies" in kwargs:
			for cookie in list( kwargs['cookies'].keys() ):
				kwargs['cookies'][cookie] = str( kwargs['cookies'][cookie] )
		for cookie in self.cookies.keys():
			Cookie.set( self.cookies, cookie, str( self.cookies[cookie] ) )
		if "headers" in kwargs:
			for header in list( kwargs['headers'].keys() ):
				kwargs['headers'][header] = str( kwargs['headers'][header] )
		for header in list( self.headers.keys() ):
			self.headers.update({ 
				header: str( self.headers[header] )
			})
		try:
			self.__response__ = self.session.request( method=method, url=url, **kwargs )
			self.__response__.status = self.__response__.status_code
			self.__save__()
		except BaseException as e:
			raise RequestError(**{
				"message": "There was an error sending the request",
				"prev": self.__error__( e )
			})
		if self.response.status == 401:
			raise RequestAuthError( "Login authentication is required" )
		return self.response
	
	#[Request.response]: Response
	@final
	@property
	def response( self ) -> Response: return self.__response__

	#[Request.session]: Session
	@final
	@property
	def session( self ) -> Session: return self.__session__

	#[Request.response]: Int
	@final
	@property
	def timeout( self ) -> int: return self.__timeout__
	

#[kanashi.request.RequestRequired]
class RequestRequired:
	
	#[RequestRequired( Request request )]: None
	def __init__( self, request ) -> None:
		
		"""
		Construct method of class RequestRequired.
		
		:params Object app
			Application context
		:return None
		:raises TypeError
			When the class is inherit from Object
		:raises ValueError
			When invalid argument passed
		"""
		
		if  isinstance( self, Object ):
			raise TypeError( "Class \"{}\" may not inherit an Object if it has inherited a previous RequestRequired".format( type( self ).__name__ ) )
		if  isinstance( request, Request ):
			self.__request__ = request
			RequestRequired.__setup__( self, request )
		else:
			raise ValueError( "Parameter request must be type Request, {} passed".format( type( request ).__name__ ) )
	
	#[RequestRequired.__setattr__( String name, Any value )]: None
	@final
	def __setattr__( self, name, value ) -> None:
		if  name == "__request__":
			if  isinstance( value, Request ):
				self.__dict__[name] = value
				RequestRequired.__setup__( self, value )
				return
		if  isinstance( self, Readonly ):
			Readonly.__setattr__( self, name, value )
		else:
			self.__dict__[name] = value
	
	#[RequestRequired.__setup__( Request request )]: None
	@final
	def __setup__( self, request ) -> None:
		try:
			self.__cookies__ = request.cookies
			self.__headers__ = request.headers
			self.__session__ = request.session
		except AttributeError:
			pass
	
	#[RequestRequired.cookies]: Cookies => RequestsCookieJar
	@final
	@property
	def cookies( self ) -> Cookies: return self.__cookies__

	#[RequestRequired.headers]: Headers => CaseInsensitiveDict
	@final
	@property
	def headers( self ) -> Headers: return self.__headers__

	#[RequestRequired.request]: Request
	@final
	@property
	def request( self ) -> Request: return self.__request__

	#[RequestRequired.session]: Session
	@final
	@property
	def session( self ) -> Session: return self.__session__
	