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

#[kanashi.error.Throwable]
class Throwable( Exception ):
	
	#[Throwable( String message, Int code, Context throw, BaseException prev, List group, Function|Method callback, **data )]
	def __init__( self, message, code=0, throw=None, prev=None, group=[], callback=None, **data ):
		
		# Exception message.
		self.message = message
		
		# Exception code.
		self.code = code
		
		# Exception thrown.
		self.throw = throw
		
		# Exception previous.
		self.prev = prev
		
		# Sxception groups.
		self.group = group
		
		# Exception callback.
		self.callback = callback
		
		# Exception data passed.
		self.data = data
		
		# Call parent constructor.
		super().__init__( message, code )
	

#[kanashi.error.Alert]
class Alert( Throwable, Warning ):
	pass
	

#[kanashi.erorr.Error]
class Error( Throwable, TypeError ):
	pass
	

#[kanashi.error.AuthError]
class AuthError( Error ):
	
	"""
	Raise when there is an authentication error.
	This error will be thrown more often because,
	almost all reactions require authentication.
	"""
	

#[kanashi.error.BestiesError]
class BestiesError( Error ):
	pass
	

#[kanashi.error.BlockError]
class BlockError( Error ):
	pass
	

#[kanashi.error.FavoriteError]
class FavoriteError( Error ):
	pass
	

#[kanashi.error.FollowError]
class FollowError( Error ):
	
	"""
	Raise when there is an error while
	following or unfollowing
	"""
	

#[kanashi.error.ReportError]
class ReportError( Error ):
	pass
	

#[kanashi.error.RestrictError]
class RestrictError( Error ):
	pass
	

#[kanashi.error.UserError]
class UserError( Error ):
	pass
	

#[kanashi.error.UserNotFoundError]
class UserNotFoundError( UserError ):
	pass
	

#[kanashi.error.SignInError]
class SignInError( Error ):
	pass
	

#[kanashi.error.CsrftokenError]
class CsrftokenError( Error ):
	
	"""
	Raises when there is no CSRFToken relogin
	"""
	

#[kanashi.error.ConfigError]
class ConfigError( Error ):
	pass
	

#[kanashi.error.PasswordError]
class PasswordError( UserError ):
	
	"""
	Raise when the user inputs the wrong password
	"""
	

#[kanashi.error.ProfileError]
class ProfileError( Error ):
	pass
	

#[kanashi.error.SpamError]
class SpamError( Error ):
	
	"""
	Increases when too many login attempts,
	which is recommended not to do too many
	login attempts.
	
	But it can also be possible when something
	else is also done too often to experiment.
	"""
	

#[kanashi.error.RequestError]
class RequestError( Error ):
	
	"""
	Raise when there is an error during request
	"""
	

#[kanashi.error.RequestDownloadError]
class RequestDownloadError( RequestError ):
	
	"""
	Raise when there is an error while
	downloading the file or contents.
	"""
	
