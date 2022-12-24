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

from kanashi.error import Error

#[kanashi.Context]
class Context:
	
	#[Context( Object app )]
	def __init__( self, app ):
		if isinstance( app, Context ):
			if type( app ).__name__ != "Context":
				self.app = app
				self.err = None
			else:
				raise Error( "The main context cannot be used as a context" )
		else:
			raise Error( "Application context should extend the Context class" )
		
	#[Context.__getattr__( String key )]
	def __getattr__( self, key ):
		try:
			return( self.__dict__[key] )
		except KeyError as e:
			raise( AttributeError( "Class {} has no attribute {}".format( type( self ).__name__, key ) ) )
		
	#[Context.__setattr__( String key, Mixed val )]
	def __setattr__( self, key, val ):
		
		# -----------------------------------
		# This is a list of class attributes
		# Whose values cannot be overwritten.
		# -----------------------------------
		attributes = [
			"app",
			"fattr",
			"request",
			"session"
		]
		
		try:
			if attributes.index( key ) >= 0:
				pass
			try:
				if self.__dict__[key]:
					raise Error( f"Do not override the attribute {key}" )
			except KeyError:
				self.__dict__[key] = val
		except ValueError:
			self.__dict__[key] = val
		return( self )
	