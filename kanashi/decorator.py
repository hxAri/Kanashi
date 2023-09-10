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


from kanashi.error import ClientError
from kanashi.error import ProfileError


#[kanashi.decorator.avoidForMySelf]
def avoidForMySelf( handle ):
	def avoid( self ):
		if  self.isMySelf:
			raise ProfileError( "This action is not intended for self" )
		return handle( self )
	return avoid

#[kanashi.decorator.logged]
def logged( handle ):
	
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
	
	#[wrapper()]: Mixed
	def wrapper( self, *args, **kwargs ):
		if  not self.authenticated:
			raise ClientError( "Login authentication required for method {}".format( handle.__name__ ) )
		return handle( self, *args, **kwargs )
	
	return wrapper
