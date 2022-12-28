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

from kanashi.enpoint.profile import Profile
from kanashi.error import Error
from kanashi.request import RequestRequired
from kanashi.utils import activity, Util

#[kanashi.enpoint.UserError]
class UserError( Error ):
	pass

#[kanashi.enpoint.UserNotfoundError]
class UserNotFoundError( UserError ):
	pass
	
#[kanashi.enpoint.UserProfile]
class UserProfile( Profile ):
	pass

#[kanashi.enpoint.BaseUser]
class BaseUser( RequestRequired ):
	
	#[User.getById( Int id, String username )]
	def getById( self, id=None, username=None ):
		if username != None:
			self.session.headers.update({
				"Referer": f"https://www.instagram.com/{username}/"
			})
		resp = self.request.get( f"https://i.instagram.com/api/v1/users/{id}/info/" )
		if resp != False:
			match resp.status_code:
				case 200:
					return(
						UserProfile(**{
							"app": self.app,
							"user": resp.json()['user'],
							"fetch": Profile.FETCH_ID
						})
					)
				case 404:
					return( UserNotFoundError( f"Target /{id}/ user not found" ) )
				case _:
					return( UserError( f"An error occurred while fetching the user [{resp.status_code}]" ) )
		else:
			return( False )
		
	#[BaseUser.tools]
	def tools( self ):
		pass
	

#[kanashi.enpoint.User]
class User( BaseUser, Util ):
	
	#[User.getById( Int id, String username )]
	def getById( self, id=None, username=None ):
		if id == None:
			self.output( activity, "Enter the ID of the user you want to fetch" )
			id = self.input( "id", number=True )
		fetch = BaseUser.getById( self, id, username )
		if fetch != False:
			match type( fetch ).__name__:
				case UserProfile.__name__:
					pass
				case UserNotFoundError.__name__:
					pass
				case UserError.__name__:
					pass
		else:
			self.emit( self.request.err )
			if self.input( "Try again [Y/n]", default=[ "Y", "y", "N", "n" ] ).upper() == "Y":
				self.getById( id, username )
			else:
				self.main()
	
	#[User.tools]
	def tools( self ):
		self.output( activity, [
			"",
			"This tool is not used for illegal",
			"purposes like, data theft and so on,",
			"please use it properly",
			"",
			lists := [
				"Get my profile",
				"Get User by ID", [
					"Retrieving user info using ID will",
					"retrieve only username, primary key",
					"or id and profile picture, url,",
					"no contents retrieve"
				],
				"Get User by Username",
				"<<< Main"
			]
		])
		next = self.input( None, number=True, default=[ 1+ i for i in range( len( lists ) ) ] )
		match next:
			case 2:
				self.getById()
			case 1 | 3:
				self.getByUsername( self.app.active.signin.username if next == 1 else None )
			case _:
				self.main()