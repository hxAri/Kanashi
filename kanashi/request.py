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

from datetime import datetime, timedelta
from re import match
from requests import Session

from kanashi.error import RequestError, RequestDownloadError
from kanashi.object import Object
from kanashi.readonly import Readonly
from kanashi.utility.file import File
	

#[kanashi.request.Request]
class Request( Readonly ):
	
	# Default header settings for requests.
	HEADERS = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "en-US,en;q=0.9",
		"Authority": "www.instagram.com",
		"Connection": "close",
		"Origin": "https://www.instagram.com",
		"Referer": "https://www.instagram.com/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"User-Agent": "Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/535.42 (KHTML, like Gecko)  Chrome/112.0.5615.137 Mobile Safari/600.3",
		"Viewport-Width": "980",
		"X-Asbd-Id": "198387",
		"X-IG-App-Id": "1217981644879628",
		"X-IG-WWW-Claim": "hmac.AR04Hjqeow3ipAWpAcl8Q5Dc7eMtKr3Ff08SxTMJosgMAh-z",
		"X-Instagram-Ajax": "1007625843",
		"X-Requested-With": "XMLHttpRequest"
	}
	
	#[Request( Dict headers, Int timeout, Bool history )]: None
	def __init__( self, headers=None, timeout=15, history=True ):
		
		"""
		Construct of method class Request.
		
		:params Dict headers
			Header settings for requests
		:params Int timeout
			Default timeout for requests
		:params Bool history
			Allow every successful request to save
		
		:return None
		"""
		
		if  headers == None:
			headers = {}
		
		# Resolve require headers.
		for i, k in enumerate( Request.HEADERS ):
			if  k not in headers:
				headers[k] = Request.HEADERS[k]
		
		# Request configurations.
		self.session = Session()
		self.cookies = self.session.cookies
		self.headers = self.session.headers
		self.headers.update({
			**headers
		})
		
		# Readonly exceptional.
		self.excepts = [
			"previous",
			"response",
			"timeout",
			"history"
		]
		
		# Previous request results.
		self.previous = None
		
		# Request results.
		self.response = None
		
		# Default request timeout.
		self.timeout = 10
		
		# History configurations.
		self.historyAllow = history == True
		self.historyFname = "response.json"
		self.history = []
		
		# If every successful request is allowed to save.
		if  history:
			try:
				self.history = File.json( self.historyFname )
			except Exception as e:
				self.clean()
	
	#[Request.clean()]: Bool
	def clean( self ):
		self.history = []
		self.previous = None
		self.response = None
		try:
			File.write( self.historyFname, "[]" )
		except Exception:
			return False
		return True
	
	#[Request.save( String url, String name, **kwargs )]: Bool
	def save( self, url, name, **kwargs ):
		
		"""
		Download content from url.
		
		:params String url
			The target url of the content
		:params String name
			Content/ Filename
		:params Mixed **kwargs
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
				File.write( name, result.content, "wb" )
			except Exception as e:
				raise RequestDownloadError( f"Failed write file \"{name}\"", prev=e )
			return True 
		else:
			raise RequestDownloadError( f"Failed get content from url, status [{result.status_code}]" )
	
	#[Request.error( Exception error )]: Exception
	def error( self, error ):
		name = type( error ).__name__
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
	
	#[Request.historySave()]: Request
	def historySave( self ):
		
		"""
		Save every successful request
		
		:return Request
			Instance of class Request
		"""
		
		if  self.historyAllow != True:
			return
		if  self.response != False and \
			self.response != None:
			try:
				try:
					content = self.response.json()
				except Exception:
					try:
						content = f"[{self.response.headers['Content-Type']}]"
					except Exception:
						content = None
				self.history.append({
					"target": self.response.url,
					"browser": self.session.headers['User-Agent'],
					"unixtime": datetime.timestamp( datetime.now() ),
					"request": {
						"cookies": dict( self.cookies ),
						"headers": dict( self.headers )
					},
					"response": {
						"status": f"{self.response}",
						"cookies": dict( self.response.cookies ),
						"headers": dict( self.response.headers ),
						"content": content
					}
				})
				File.write( self.historyFname, self.history )
			except Exception as e:
				pass
		return( self )
	
	#[Request.previously( time )]: List
	def previously( self, time ):
		
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
		if not isinstance( time, str ):
			raise ValueError( "Invalid time parameter, value must be type str, {} passed".format( type( time ).__name__ ) )
		if valid := match( r"^(?P<diff>[1-9][0-9]*)(?P<unit>s|m|h|d|w|M|y)$", time ):
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
				timestamp = datetime.fromtimestamp( history['unixtime'] )
				if timestamp >= current - delta:
					data.append( history )
			return data
		else:
			raise TypeError( "Invalid time syntax, value must be like \\d+(s|m|h|d|w|M|y)" )
	
	#[Request.delete( String url, **kwargs )]
	def delete( self, url, **kwargs ):
		return( self.request( "DELETE", url=url, **kwargs ) )
	
	#[Request.get( String url, **kwargs )]
	def get( self, url, **kwargs ):
		return( self.request( "GET", url=url, **kwargs ) )
	
	#[Request.head( String url, **kwargs )]
	def head( self, url, **kwargs ):
		return( self.request( "HEAD", url=url, **kwargs ) )
	
	#[Request.options( String url, **kwargs )]
	def options( self, url, **kwargs ):
		return( self.request( "OPTIONS", url=url, **kwargs ) )
	
	#[Request.patch( String url, **kwargs )]
	def patch( self, url, **kwargs ):
		return( self.request( "PATCH", url=url, **kwargs ) )
	
	#[Request.post( String url, **kwargs )]
	def post( self, url, **kwargs ):
		return( self.request( "POST", url=url, **kwargs ) )
	
	#[Request.put( String url, **kwargs )]
	def put( self, url, **kwargs ):
		return( self.request( "PUT", url=url, **kwargs ) )
	
	#[Request.request( String method, String url, **kwargs )]
	def request( self, method, url, **kwargs ):
		
		"""
		Send request to url target.
		
		:params String method
			Request method name
		:params String url
			Request url target
		:params Mixed **kwargs
			Request options
		
		:return Mixed
		:raises RequestError
			When an error occurs while performing the request
		"""
		
		self.previous = self.response
		self.response = None
		
		#if  "timeout" not in kwargs:
		#	kwargs['timeout'] = self.timeout
		try:
			self.response = self.session.request( method, url=url, **kwargs )
			self.historySave()
			return self.response
		except Exception as e:
			raise RequestError(**{
				"message": "There was an error sending the request",
				"prev": self.error( e )
			})
	

#[kanashi.request.RequestRequired]
class RequestRequired:
	
	#[RequestRequired( Request request )]
	def __init__( self, request ):
		
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
			
			# Trying to inject properties.
			self.request = request
			self.__setup__( request )
		else:
			raise ValueError( "Parameter request must be type Request, {} passed".format( type( request ).__name__ ) )
	
	#[RequestRequired.__setattr__( String name, Mixed value )]: None
	def __setattr__( self, name, value ):
		if name == "request":
			if isinstance( value, Request ):
				self.__dict__[name] = value
				self.__setup__( value )
				return
		if isinstance( self, Readonly ):
			Readonly.__setattr__( self, name, value )
		else:
			self.__dict__[name] = value
	
	#[RequestRequired.__setup__( Request request )]: None
	def __setup__( self, request ):
		try:
			self.cookies = request.cookies
			self.headers = request.headers
			self.session = request.session
		except AttributeError:
			pass
	