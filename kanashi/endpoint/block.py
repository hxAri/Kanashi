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

#[kanashi.endpoint.Block]
class Block( RequestRequired ):
	
	# Block and other account.
	BLOCK_MULTILEVEL = 78828
	
	# Block and report user.
	BLOCK_REPORT = 89282
	
	# Block only.
	BLOCK_ONLY = 99278
	
	#[Block.throws( Profile user )]
	def throws( self, user ):
		if user.isMySelf:
			raise FollowError( "Unable to block or unblock yourself" )
		
	#[Block.block()]
	def block( self, user, level=None, report=None ):
		self.throws( user )
	

#[kanashi.endpoint.BlockError]
class BlockError( Error ):
	pass
	

#[kanashi.endpoint.BlockSuccess]
class BlockSuccess( Object ):
	pass
	