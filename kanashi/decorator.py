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


from re import match

from kanashi.error import ClientError, ProfileError


#[kanashi.utility.decorator.avoidForMySelf]: Callable
def avoidForMySelf( handle ) -> callable:

	"""
	Decorator to prevent performing actions that
	should not be performed for yourself.
	"""

	from kanashi.pattern import Pattern
	from kanashi.typing.profile import Profile
	from kanashi.typing.user import User

	#[kanashi.utility.avoidForMySelf( Self@Client slef, Any *args, Any **kwargs )]: Any
	def wrapper( self, *args, **kwargs ) -> any:
		throws = lambda: ProfileError( "This action is not intended for your self" )
		match handle.__name__:
			case "approve"|"bestie"|"block"|"favorite"|"follow"|"remove"|"report"|"restrict":
				try:
					user = args[0]
				except IndexError:
					user = kwargs.get( "user", None )
				if isinstance( user, int ):
					if user == self.active.id: raise throws()
				elif isinstance( user, str ):
					if match( Pattern.USERNAME, user ):
						if user == self.active.username:
							raise throws()
				elif isinstance( user, ( Profile, User ) ):
					user = user.id if "id" in user \
						else user.pk if "pk" in user \
						else user.username
					if isinstance( user, int ):
						if user == self.active.id: raise throws()
					else:
						if user == self.active.username:
							raise throws()
			case _:
				...
		return handle( self, *args, **kwargs )
	wrapper.__name__ = handle.__name__
	return wrapper

#[kanashi.utility.decorator.logged]: Callable
def logged( handle ) -> callable:
	
	"""
	A decoration to check whether the client is
	logged in or not, if the function or method
	being called requires login first it
	will throw an error.
	
	Every method that uses this decoration must
	have a method named `authenticated` with `@property`
	decoration to check whether it is logged in or not,
	this is because the flow of each class is different
	when checking login or not.
	
	:return Function
		A wrapper to check if login or not
	:raises ClientError
		When a function or method requires login authentication
	"""
	
	#[kanash.utility.logged@wrapper( Self@Client slef, Any *args, Any **kwargs )]: Any
	def wrapper( self, *args, **kwargs ) -> any:
		if  not self.authenticated:
			raise ClientError( "Login authentication required for method {}".format( handle.__name__ ) )
		return handle( self, *args, **kwargs )
	wrapper.__name__ = handle.__name__
	return wrapper

