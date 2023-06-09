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

#[kanashi.Throwable]
class Throwable( Exception ):
	
	#[Throwable( String message, Int code, Context throw, BaseException prev, List group, **data )]
	def __init__( self, message, code=0, throw=None, prev=None, group=[], **data ):
		
		# Set exception message.
		self.message = message
		
		# Set exception code.
		self.code = code
		
		# Set exception throw.
		self.throw = throw
		
		# Set exception previous.
		self.prev = prev
		
		# Set exception groups.
		self.group = group
		
		# Set exception data passed.
		self.data = data
		
		# Call parent constructor.
		Exception.__init__( self, message, code )
	
#[kanashi.Alert]
class Alert( Throwable, Warning ):
	pass
	
#[kanashi.Error]
class Error( Throwable, TypeError ):
	pass
	