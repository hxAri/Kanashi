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
	
	#[Throwable( String message, Int code, Context throw, BaseException prev, List group, **data )]
	def __init__( self, message, code=0, throw=None, prev=None, group=[], **data ):
		
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
		
		# Exception data passed.
		self.data = data
		
		# Call parent constructor.
		super().__init__( message, code )
	pass
	

#[kanashi.error.Alert]
class Alert( Throwable, Warning ):
	pass
	

#[kanashi.erorr.Error]
class Error( Throwable, TypeError ):
	pass
	
class AuthError( Error ):
	pass

class BestiesError( Error ):
	pass

class BlockError( Error ):
	pass

class FavoriteError( Error ):
	pass

class FollowError( Error ):
	pass

class ReportError( Error ):
	pass

class RestrictError( Error ):
	pass

class UserError( Error ):
	pass

class UserNotFoundError( UserError ):
	pass

class SignInError( Error ):
	pass

class CsrftokenError( Error ):
	pass

class ConfigError( Error ):
	pass

class PasswordError( UserError ):
	pass

class ProfileError( Error ):
	pass

class SpamError( Error ):
	pass

class RequestError( Error ):
	pass

class RequestDownloadError( RequestError ):
	pass