#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Facebook, e.g Login. Logout, Profile Info,
# Follow, Unfollow, Media downloader, etc.
#
# Kanashi Copyright (c) 2024 - hxAri <hxari@proton.me>
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

from builtins import int as Int, str as Str
from click import Context, group, option as Option, pass_context as Initial
from click.types import DateTime as DateTimeParamType
from datetime import datetime
from json import loads as JsonDecoder
from typing import final, MutableMapping

from kanashi.client import Client, create as ClientBuilder
from kanashi.common import puts
from kanashi.manager import Manager
from kanashi.signup import SignUp


__all__ = [
	"Account"
]


JsonParamType = lambda v: JsonDecoder( v ) if isinstance( v, ( bytes, bytearray, str ) ) else v
""" Click Json Parameter Type """


@final
@group
class Account: """ Instagram account management """


def encryptor( TPEncFormat:Str, TPEncKeyId:Int, TPEncPublicKey:Str, TPEncVersion:Int, Password:Str ) -> Str:
	
	"""
	Password Encryptor Implementation
	
	Parameters:
		TPEncFormat (Str):
			Password formatter
		TPEncKeyId (Int):
			Password key id
		TPEncPublicKey (Str):
			Password public key
		TPEncVersion (Int):
			Password version
		Password (Str):
			Password plaintext
	
	Returns:
		Str:
			Encrypted instagram password
	"""
	
	raise NotImplementedError( "Function not implemented" )

@Account.command( help="Instagram anoymous id" )
@Initial
def anonymous( context:Context ) -> None:
	puts( f"Anoymous id={context.obj['manager'].anonymous}" )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

@Account.command( help="Instagram account refresh" )
@Initial
def lists( context:Context ) -> None:
	formatter = "{}. Account: authenticated={}; session={}; username={}"
	manager:Manager = context.obj['manager']
	for i, account in enumerate( manager.accounts(), 1 ):
		n = str( i )
		nl = len( n )
		ll = len( str( manager.length ) )
		n = "".join([ "0" * ( ll - nl ) if ll >= 2 else "0", n ])
		puts( formatter.format( n, account.authenticated, manager.encoder( account.auth.username if not account.anonymous else manager.anonymous ), account.auth.username if not account.anonymous else "anonymous" ) )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

@Account.command( help="Instagram account refresh" )
@Initial
def refresh( context:Context ) -> None:
	client:Client = context.obj['client']
	client.authenticate()
	manager:Manager = context.obj['manager']
	manager.append( client.account )
	puts( client.account )
	puts( "Account successfully updated" )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

@Account.command( help="Instagram account signin" )
@Initial
@Option( "--headers", help="Instagram account headers", prompt=True, required=True, type=JsonParamType )
@Option( "--password", help="Instagram account password", prompt=True, required=True, type=Str )
@Option( "--username", help="Instagram account username", required=True, type=Str )
def signin( context:Context, headers:MutableMapping[Str,Str], password:Str, username:Str ) -> None:
	client = ClientBuilder( 
		headers=headers,
		password=password,
		username=username
	)
	client.authenticate( encryptor=encryptor )
	manager:Manager = context.obj['manager']
	manager.append( client.account )
	puts( client.account )
	puts( "Account successfully authenticated" )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

@Account.command( help="Instagram account signup" )
@Initial
@Option( "--headers", help="Instagram account headers", prompt=True, required=True, type=JsonParamType )
@Option( "--usermail", help="Instagram account usermail", required=True, type=Str )
@Option( "--username", help="Instagram account username", required=True, type=Str )
def signup( context:Context, headers:MutableMapping[Str,Str], usermail:Str, username:Str ) -> None:
	manager:Manager = context.obj['manager']
	signup = SignUp( 
		birthday=None, 
		encryptor=None, 
		firstname=None, 
		usermail=usermail, 
		username=username, 
		password=None, 
		headers=headers 
	)
	signup.perform()
	manager.append( signup.client.account )
	puts( "Successfully send verification code" )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

@Account.command( "signup-verify", help="Instagram account signup verify" )
@Initial
@Option( "--birthday", help="Instagram account birthday", required=True, type=DateTimeParamType() )
@Option( "--firstname", help="Instagram account firstname", required=True, type=Str )
@Option( "--password", help="Instagram account password", prompt=True, required=True, type=Str )
@Option( "--usermail", help="Instagram account usermail", required=True, type=Str )
@Option( "--username", help="Instagram account username", required=True, type=Str )
def signupv( code:Int, context:Context, birthday:datetime, firstname:Str, usermail:Str, username:Str ) -> None:
	manager:Manager = context.obj['manager']
	account = manager.account( username )
	headers = dict( account.headers )
	headers['Cookie'] = Client.cookies
	password = account.auth.password
	signup = SignUp( 
		birthday=birthday, 
		encryptor=encryptor, 
		firstname=firstname, 
		usermail=usermail, 
		username=username, 
		password=password, 
		headers=headers 
	)
	signup.verify( code )
	manager.append( signup.client.account )
	puts( "Account successfully created and authenticated" )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

@Account.command( help="Instagram account switch" )
@Initial
@Option( "--username", help="Instagram account username", required=True, type=Str )
def switch( context:Context, username:Str ) -> None:
	manager:Manager = context.obj['manager']
	manager.switch( username )
	puts( "Successfully updated default account" )
	puts( "Program terminated", close=0, end="\x0a" * 2 )

