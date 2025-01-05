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

__all__ = [
]

from builtins import int as Int, str as Str
from traceback import format_exception
from typing import Iterable, Optional

from kanashi.common import typeof


__all__ = [
	"ClientAqmError",
	"ClientAuthenticationError",
	"ClientError",
	"ClientOneTapLoginError",
	"ClientSplashError",
	"ClientSignUpError",
	"ClientUnauthorizedError",
	"ClientUsermailError",
	"ClientUsermailVerifyError",
	"ClientUsernameError",
	"EncryptionError",
	"GraphqlContentError",
	"GraphqlError",
	"GraphqlParserError",
	"KanashiError",
	"RateLimitError",
	"UnsupportedEncryptionVersion",
	"UserNotFoundError"
]


class KanashiError( Exception ):
	
	""" Base Kanashi Error Class """
	
	code:Int
	""" Error Code """
	
	message:Str
	""" Error Message """
	
	previous:Iterable[Exception]
	""" Error Previous Exception or Error """
	
	def __init__( self, message:Str, code:Int=0, previous:Optional[Iterable[Exception]]=None ) -> None:
		
		"""
		Construct method of class KanashiError
		
		Parameters:
			message (Str):
				Error message
			code (Int):
				Error code
			previous (Optional[Iterable[Exception]]):
				Previous error
		"""
		
		if not hasattr( previous, "__iter__" ):
			previous = []
		self.previous = previous
		self.message = message
		self.code = code
		
		Exception.__init__( self, message, code, previous )
	
	def __repr__( self ) -> Str:
		return "\x0a".join( format_exception( self ) )
	
	def __str__( self ) -> Str:
		return f"{typeof( self )}: {self.code}: {self.message}"
	
	...


class ClientError( KanashiError ): """ Raises when client error """

class ClientSplashError( ClientError ): ...

class ClientAqmError( ClientSplashError ): ...

class ClientAuthenticationError( ClientError ): """ Raises when client failed authenticate account """

class ClientOneTapLoginError( ClientAuthenticationError ): """ Raises when failed get login nonce token """

class ClientSignUpError( ClientError ): """ Raises when client failed signup account """

class ClientUnauthorizedError( ClientError ): """ Raises when client account is not authenticated """

class ClientUsermailError( ClientError ): """ Raises when email address is exists or invalid """

class ClientUsermailVerifyError( ClientError ): """ Raises when failed send verification code to email address or invalid verification code """

class ClientUsernameError( ClientError ): """ Raises when username is exists or invalid """

class EncryptionError( ClientError ): """ Raises when encryption error """

class GraphqlError( ClientError ): """ Raises when error serverity exists in response content """

class GraphqlContentError( ClientError ): """ Raises when response content is not parseable to python object e.g dict|list """

class GraphqlParserError( ClientError ): """ Raises when parser action failed parser response content """

class RateLimitError( ClientError ): """ Raises when rate limit detected """

class UnsupportedEncryptionVersion( KanashiError ): """ Raises when encryption version is invalid """

class UserNotFoundError( ClientError ): """ Raised when user not found """

