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


from builtins import int as Int, str as Str
from socks import ProxyConnectionError
from stem.control import Controller
from stem import ControllerError, Signal, SocketError
from typing import Dict, final

from kanashi.library.stdio import stderr, stdout
from kanashi.request import request as Request


@final
class Torify:
	
	@staticmethod
	def ipInfo( proxies:Dict[Str,Str]=None ) -> Str:
		
		"""
		Get current ip address.
		
		:params Dict<Str,Str> proxies
		
		:return Str
			The str of ip address
		"""
		
		try:
			response = Request( "GET", "https://api.ipify.org/?format=json", proxies=proxies )
			content = response.json()
			if "ip" in content and content['ip']:
				return content['ip']
		except ProxyConnectionError as e:
			...
		return None
	
	@staticmethod
	def reNewTorIp( proxies:Dict[Str,Str], port:Int, password:Str ) -> None:
		
		"""
		Re-new or change the current ip address.
		
		:params Dict<Str,Str> proxies
			The tor proxy configurations
		:params Int port
			The tor port number
		:params Str password
			The tor proxy password
		
		:return None
		"""
		
		previousIp = Torify.ipInfo()
		stdout( Torify.reNewTorIp, f"Trying to re-new IP Address address={previousIp}" )
		try:
			with Controller.from_port( port=port ) as controller:
				controller.authenticate( password=password )
				controller.signal( Signal.NEWNYM )
		except SocketError as e:
			stderr( Torify.reNewTorIp, e, clear=True, buffers=[
				f"Uncaught SocketError: {e}",
				f"Failed to estabilish connection from={previousIp}",
		  		f"Failed to update Ip Address from={previousIp}"
			])
		except ControllerError as e:
			stderr( Torify.reNewTorIp, e, clear=True, buffers=[
				f"Uncaught ControllerError: {e}",
				f"Failed sending Signal from={previousIp}",
		  		f"Failed to update Ip Address from={previousIp}"
			])
		currentIp = Torify.ipInfo( proxies=proxies )
		if currentIp != previousIp:
			stdout( Torify.reNewTorIp, f"The IP Address has been updated from={currentIp}" )
		else:
			stdout( Torify.reNewTorIp, f"The IP Address does not change from={currentIp}" )
		...
	
	...
