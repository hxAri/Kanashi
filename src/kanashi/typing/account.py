#!/usr/bin/env python3

#
# @author hxAri (hxari)
# @create 23-12-2024 17:30
# @github https://github.com/hxAri/Kanashi
#
# Kanashi is an Open-Source project for doing various
# things related to Instagram, e.g Login. Logout, Profile Info,
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

from builtins import bool as Bool, str as Str
from json import dumps as JsonEncoder
from typing import Any, final, MutableMapping, Optional, Union
from urllib.parse import unquote as urldecoder


__all__ = [
	"Account"
]


@final
class _Authentication:
	
	password:Str
	""" Password Authentication """
	
	username:Str
	""" Username Authentication """
	
	def __init__( self, password:Optional[Str]=None, username:Optional[Str]=None ):
		self.password = password
		self.username = username
	
	@property
	def mapping( self ) -> MutableMapping[Str,Any]:
		return dict(
			password=self.password,
			username=self.username
		)
	
	...


class Account:
	
	""" Account Typing Implementation """
	
	auth:_Authentication
	""" Account Authentication """
	
	configs:MutableMapping[Str,Any]
	""" Account Configuration """
	
	cookies:MutableMapping[Str,Str]
	""" Account Cookies """
	
	headers:MutableMapping[Str,Str]
	""" Account Headers """
	
	def __init__( self, configs:MutableMapping[Str,Any], cookies:Union[MutableMapping[Str,Str],Str], headers:MutableMapping[Str,Str], password:Optional[Str]=None, username:Optional[Str]=None ) -> None:
		
		"""
		Construct method of class Account
		
		Parameters:
			configs (MutableMapping[Str,Any]):
				Account configurations
			cookies (Union[MutableMapping[Str,Str],Str]):
				Account cookies
			headers (MutableMapping[Str,Str]):
				Account headers
			password (Optional[Str]):
				Account password
			username (Optional[Str]):
				Account username
		"""
		
		if cookies is None or not cookies:
			if "Cookie" in headers:
				cookies = headers['Cookie']
				del headers['Cookie']
		if isinstance( cookies, Str ):
			explode = cookies.split( "\x3b" )
			cookies = {}
			for item in explode:
				parts = item \
					.removeprefix( "\x20" ) \
					.removesuffix( "\x20" ) \
					.split( "\x3d" )
				cookies[parts[0]] = urldecoder( parts[1] )
		self.auth = _Authentication(
			username=username,
			password=password
		)
		self.configs = configs
		self.cookies = cookies
		self.headers = headers
	
	def __repr__( self ) -> Str:
		instance = type( self )
		nmodule = instance.__module__
		quaname = instance.__qualname__
		return f"<{nmodule}.{quaname} object at 0x{self.__hash__()}>"
	
	def __str__( self ) -> Str:
		return JsonEncoder( self.mapping, indent=4 )
	
	@property
	def anonymous( self ) -> Bool:
		return self.auth.username is None and \
			   self.auth.password is None
	
	@final
	@property
	def authenticated( self ) -> Bool:
		cookies = [ "csrftoken", "ig_did", "mid" ]
		if not self.configs: return False
		if "ScheduledServerJS" not in self.configs: return False
		if "CurrentUserInitialData" not in self.configs['ScheduledServerJS']: return False
		if "LSD" not in self.configs['ScheduledServerJS']: return False
		if not self.anonymous:
			if self.configs['ScheduledServerJS']['CurrentUserInitialData'] in [ 0, "0" ]: return False
			cookies.extend([
				"ds_user_id",
				"sessionid"
			])
		return all( cookie in self.cookies and self.cookies[cookie] for cookie in cookies )
	
	@property
	def mapping( self ) -> MutableMapping[Str,Any]:
		return dict(
			configs=self.configs,
			cookies=self.cookies,
			headers=self.headers,
			password=self.auth.password,
			username=self.auth.username
		)
	
	@property
	def payload( self ) -> MutableMapping[Str,Any]:
		if self.configs['ScheduledServerJS']['JSErrorLoggingConfig']['jssesw'] is None:
			self.configs['ScheduledServerJS']['JSErrorLoggingConfig']['jssesw'] = 0
		return dict(
			__a=self.configs['query']['__a'],
			__ccg=self.configs['ScheduledServerJS']['WebConnectionClassServerGuess']['ccg'],
			__comet_req=self.configs['query']['__comet_req'],
			__csr="",
			__dyn="",
			__hs=self.configs['ScheduledServerJS']['SiteData']['haste_session'],
			__hsi=self.configs['ScheduledServerJS']['SiteData']['hsi'],
			__jssesw=self.configs['ScheduledServerJS']['JSErrorLoggingConfig']['jssesw'],
			__req="m",
			__rev=self.configs['ScheduledServerJS']['SiteData']['spin']['r'],
			__s="ntlrwu:6o5sts:zxbyqe",
			__spin_b=self.configs['ScheduledServerJS']['SiteData']['spin']['b'],
			__spin_r=self.configs['ScheduledServerJS']['SiteData']['spin']['r'],
			__spin_t=self.configs['ScheduledServerJS']['SiteData']['spin']['t'],
			__user=self.configs['query']['__user'],
			av=self.configs['ScheduledServerJS']['CurrentUserInitialData']['NON_FACEBOOK_USER_ID'],
			doc_id=None,
			dpr=1,
			fb_api_caller_class="RelayModern",
			fb_api_req_friendly_name=None,
			fb_dtsg=self.configs['ScheduledServerJS']['DTSGInitData']['token'],
			jazoest=self.configs['query']['jazoest'],
			lsd=self.configs['ScheduledServerJS']['LSD'],
			server_timestamps=True,
			variables=None
		)
	
	...
