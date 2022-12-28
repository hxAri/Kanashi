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
from kanashi.object import Object
from kanashi.request import RequestRequired
from kanashi.utils import activity, Util

#[kanashi.enpoint.BaseProfile]
class BaseProfile( RequestRequired ):
	
	# Fetch Mode by ID
	FETCH_ID = 75619
	
	# Fetch Mode by Username
	FETCH_USERNAME = 85862
	
	#[Profile( Object app, Dict user, Int fetch )]
	def __init__( self, app, user, fetch ):
		
		# Save user info.
		self.user = Object( user )
		
		# Save fetch mode.
		self.fetch = fetch
		
		# Call parent constructor.
		super().__init__( app )
	

#[kanashi.enpoint.Profile]
class Profile( BaseProfile, Util ):
	
	#[Profile.getBase()]
	def getBase( self ):
		try:
			if self.base:
				return( self.base )
		except AttributeError:
			self.base = BaseProfile( self.app, self.user.dict(), self.fetch )
		return( self.base )
	
	