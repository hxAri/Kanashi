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

from threading import Thread as BaseThread

#[kanashi.utils.Thread]
class Thread( BaseThread ):
	
	#[Thread()]
	def __init__( self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None ):
		BaseThread.__init__( self, group, target, name, args, kwargs )
		self._return = None
		
	#[Thread.run()]
	def run(self):
		if self._target is not None:
			self._return = self._target( *self._args, **self._kwargs)
		
	#[Thread.getReturn()]
	def getReturn( self ):
		return( self._return )
	
