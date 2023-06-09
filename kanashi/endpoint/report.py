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

from kanashi.error import Error
from kanashi.object import Object
from kanashi.request import RequestRequired


#[kanashi.endpoint.ReportError]
class ReportError( Error ):
	pass
	

#[kanashi.endpoint.ReportSuccess]
class ReportSuccess( Object ):
	pass
	

#[kanashi.endpoint.Report]
class Report( RequestRequired ):
	
	#[Report.throws( Profile user )]
	def throws( self, user ):
		if user.isMySelf:
			raise FollowError( "Unable to report yourself" )
	
	#[Report.report()]
	def report( self, user, report ):
		self.throws( user )
		
		# Content-Type application/x-www-form-urlencoded
		# Origin https://www.instagram.com
		# Referer https://www.instagram.com/{user.id}/
		# Post https://www.instagram.com/api/v1/web/reports/get_frx_prompt/
		
		# Payload<Option<1>>
		# container_module profilePage
		# entry_point 1
		# location 2
		# object_id {user.id}
		# object_type 5
		# context {}
		# selected_tag_types ["ig_user_impersonation_me"]
		# action_type 2
		# fix_prompt_request_type 2
	
	#[Report.reportPost()]
	def reportPost( self, user, post, report ):
		self.throws( user )
		pass
	