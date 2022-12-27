#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashi Copyright (c) 2022 - Ari Setiawan <ari160824@gmail.com>
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
# Kanashi is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from requests import Session
from requests.exceptions import *

from kanashi.config import BaseConfig
from kanashi.context import Context
from kanashi.error import Error
from kanashi.utils import activity, File, JSONError, Util

#[kanashi.RequestError]
class RequestError( Error ):
	pass
	

#[kanashi.BaseRequest]
class BaseRequest( Context ):
	
	#[BaseRequest( Object app )]
	def __init__( self, app ):
		
		# Request response.
		self.response = False
		
		# Request history.
		self.history = []
		self.historyF = "response.json"
		try:
			self.history = File.json( self.historyF )
		except BaseException as e:
			try:
				File.write( self.historyF, "[]" )
			except BaseException as e:
				self.emit( Error( f"Failed create file {self.historyF}", e ) )
				exit()
		
		try:
			if app.config:
				pass
		except AttributeError:
			app.config = BaseConfig( app )
		
		# Create new Session.
		self.session = Session()
		self.session.headers.update({
			"Origin": "https://www.instagram.com",
			"Referer": "https://www.instagram.com/",
			"User-Agent": app.config.browser.default,
			"X-Asbd-Id": "198387",
			"X-IG-App-Id": "1217981644879628",
			"X-IG-WWW-Claim": "hmac.AR3Xr1WRl38gOuiPX1W-7xi7poRHnUgeLV6zVOzTivxj2QzA",
			"X-Instagram-Ajax": "1006758126",
			"X-Requested-With": "XMLHttpRequest"
		})
		
		# Allow other program for access request session.
		app.session = self.session
		
		# Call parent constructor.
		super().__init__( app )
		
	#[BaseRequest.reset()]
	def reset( self ):
		
		self.history = []
		self.response = None
		
		# Rewrite response logs.
		File.write(
			self.historyF,
			self.history
		)
		
	#[Request.erro( List error )]
	def error( self, error ):
		named = type( error ).__name__
		match named:
			case InvalidJSONError.__name__:
				error = RequestError( f"{named} A JSON error occured" )
			case JSONDecodeError.__name__:
				error = RequestError( f"{named} Couldn't decode the text into json" )
			case HTTPError.__name__:
				error = RequestError( f"{named} An HTTP error occurred" )
			case ConnectionError.__name__:
				error = RequestError( f"{named} A Connection error occurred" )
			case ProxyError.__name__:
				error = RequestError( f"{named} A proxy error occurred" )
			case SSLError.__name__:
				error = RequestError( f"{named} An SSL error occurred" )
			case Timeout.__name__:
				error = RequestError( f"{named} The request timed out" )
			case ConnectTimeout.__name__:
				error = RequestError( f"{named} The request timed out while trying to connect to the remote server" )
			case ReadTimeout.__name__:
				error = RequestError( f"{named} The server did not send any data in the allotted amount of time" )
			case URLRequired.__name__:
				error = RequestError( f"{named} A valid URL is required to make a request" )
			case TooManyRedirects.__name__:
				error = RequestError( f"{named} Too many redirects" )
			case MissingSchema.__name__:
				error = RequestError( f"{named} The URL scheme (e.g. http or https) is missing" )
			case InvalidSchema.__name__:
				error = RequestError( f"{named} The URL scheme provided is either invalid or unsupported" )
			case InvalidURL.__name__:
				error = RequestError( f"{named} The URL provided was somehow invalid" )
			case InvalidHeader.__name__:
				error = RequestError( f"{named} The header value provided was somehow invalid" )
			case InvalidProxyURL.__name__:
				error = RequestError( f"{named} The proxy URL provided is invalid" )
			case ChunkedEncodingError.__name__:
				error = RequestError( f"{named} The server declared chunked encoding but sent an invalid chunk" )
			case ContentDecodingError.__name__:
				error = RequestError( f"{named} Failed to decode response content" )
			case StreamConsumedError.__name__:
				error = RequestError( f"{named} The content for this response was already consumed" )
			case RetryError.__name__:
				error = RequestError( f"{named} Custom retries logic failed" )
			case UnrewindableBodyError.__name__:
				error = RequestError( f"{named} Requests encountered an error when trying to rewind a body" )
			case RequestsWarning.__name__:
				error = RequestError( f"{named} Base warning for Requests" )
			case FileModeWarning.__name__:
				error = RequestError( f"{named} A file was opened in text mode, but Requests determined its binary length" )
			case RequestsDependencyWarning.__name__:
				error = RequestError( f"{named} An imported dependency doesn't match the expected version range" )
			case _:
				error = RequestError( f"{named} There was an ambiguous exception that occurred while handling your request" )
		return( error )
		
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
		self.err = None
		self.response = False
		try:
			self.response = self.session.request( method, url=url, **kwargs )
			self.responseSave()
		except BaseException as e:
			self.err = Error(**{
				"message": "There was an error sending the request",
				"prev": self.error( e )
			})
			return( False )
		return( self.response )
		
	#[Request.responseSave()]
	def responseSave( self ):
		if self.response != False:
			try:
				try:
					content = self.response.json()
				except BaseException:
					content = None
				self.history.append({
					"target": self.response.url,
					"browser": self.session.headers['User-Agent'],
					"content": content,
					"cookies": {
						"request": dict( self.session.cookies ),
						"response": dict( self.response.cookies )
					},
					"headers": {
						"request": dict( self.session.headers ),
						"response": dict( self.response.headers )
					},
					"status": "{}".format( self.response )
				})
				File.write( self.historyF, self.history )
			except BaseException as e:
				self.err = Error( "Unable to log request sent", prev=e )
		return( self )
	

#[kanashi.Request]
class Request( BaseRequest, Util ):
	
	#[Request.reset()]
	def reset( self ):
		self.thread( "Clear request records", BaseRequest.reset, self )
		self.output( activity, "The request log has been cleaned up" )
		self.input( "Return to the main page", default="" )
		self.app.main()
		
	#[Request.request( String method, String url, **kwargs )]
	def request( self, method, url, **kwargs ):
		resp = self.thread( f"Request {method}: {url}", BaseRequest.request, self, method=method, url=url, **kwargs )
		if self.err:
			self.emit( self.err )
			if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				return( self.request( method, url, **kwargs ) )
			else:
				return( False )
		else:
			return( resp )
	