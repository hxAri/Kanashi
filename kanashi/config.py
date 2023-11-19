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


from typing import final
from yutiriti import File, JSONError, Object, Readonly

from kanashi.error import ConfigError
from kanashi.typing import Settings


#[kanashi.config.Config]
@final
class Config( Readonly ):
	
	# Kanashī Abouts.
	ABOUTS = "Kanashī is an open source project that can be used to login to real Instagram accounts via Linux Terminal and Android Termux, this also includes taking CSRF Tokens and Login Session IDs, besides that you can use Tokens and ID to do various things like Instagram Web."
	
	# Author Info.
	AUTHOR = "Ari Setiawan (hxAri)"
	AUTHOR_EMAIL = "hxari@proton.me"
	
	# Another Authors and Helpers.
	AUTHORS = [
		{
			"name": "Ari Setiawan",
			"email": "hxari@proton.me",
			"section": "Kanashī Creator and Developer",
			"github": "https://github.com/hxAri",
			"linkedin": "https://linkedin.com/in/hxAri"
		},
		{
			"name": "Aisyah Diesliana Putri",
			"section": "Assists Login Testing",
			"github": "https://github.com/AisyahDiesliana"
		},
		{
			"name": "Falsa Fadilah Nugraha",
			"section": "Helpers"
		}
	]
	
	# DISCLAIMER
	DISCLAIMER = "Kanashī is not affiliated with or endorsed, endorsed at all by Instagram or any other party, if you use the main account to use this tool we as Coders and Developers are not responsible for anything that happens to that account, use it at your own risk, and this is Strictly not for SPAM."

	# Application Environment
	ENVIRONMENT = "development"
	
	# Default Filename.
	FILENAME = "settings.json"
	
	# Kanashī History.
	HISTORY = "Kanashī itself is a translation from Japanese which means Sad people might ask \"why is that?\""
	
	# Kanashī License.
	LICENSE = "GNU General Public License v3"
	LICENSE_URL = "https://www.gnu.org/licenses/gpl-3.0.html"
	LICENSE_DOC = [
		"All Kanashī source code is licensed under the GNU General Public License v3.",
		"Please see the \"LICENSE\" document for more details."
	]
	
	# Kanashī media stored.
	ONSAVED = Object({
		"media": {
   			"image": "onsaved/{user}/{media}/{name}.jpg",
			"video": "onsaved/{user}/{media}/{name}.mp4"
		},
		"export": {
			"json": "onsaved/{user}/exports/{name} - {date}.json"
		}
	})
	
	# Kanashī Reporistory.
	REPOSITORY = "https://github.com/hxAri/Kanashi"

	# Kanashī Settings.
	SETTINGS = {
		"browser": {
			"default": "Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/535.42 (KHTML, like Gecko)  Chrome/51.0.1292.319 Mobile Safari/600.3",
			"randoms": [
				"Mozilla/5.0 (Linux; U; Android 7.1.1; Nexus 7 Build/NME91E) AppleWebKit/602.14 (KHTML, like Gecko)  Chrome/52.0.1453.331 Mobile Safari/533.3",
				"Mozilla/5.0 (Windows NT 10.1; Win64; x64; en-US) AppleWebKit/535.27 (KHTML, like Gecko) Chrome/50.0.2636.355 Safari/601",
				"Mozilla/5.0 (Linux; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/535.33 (KHTML, like Gecko)  Chrome/51.0.2137.322 Mobile Safari/534.3",
				"Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/600.4 (KHTML, like Gecko) Chrome/50.0.2484.350 Safari/600",
				"Mozilla/5.0 (Linux x86_64) AppleWebKit/535.32 (KHTML, like Gecko) Chrome/53.0.2302.360 Safari/533",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_9; like Mac OS X) AppleWebKit/600.25 (KHTML, like Gecko)  Chrome/55.0.2587.177 Mobile Safari/602.8",
				"Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.2; Win64; x64; en-US Trident/4.0)",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_3; en-US) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/49.0.2469.359 Safari/537",
				"Mozilla/5.0 (Linux; U; Android 7.1; Nexus 6X Build/NPD90G) AppleWebKit/536.47 (KHTML, like Gecko)  Chrome/52.0.2374.359 Mobile Safari/533.7",
				"Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 10.3; x64 Trident/4.0)",
				"Mozilla/5.0 (Android; Android 7.1.1; GT-I9600 Build/KTU84P) AppleWebKit/602.19 (KHTML, like Gecko)  Chrome/50.0.1969.345 Mobile Safari/601.7",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_2_5) Gecko/20100101 Firefox/72.1",
				"Mozilla/5.0 (Linux i651 ; en-US) AppleWebKit/600.27 (KHTML, like Gecko) Chrome/51.0.1747.350 Safari/533",
				"Mozilla/5.0 (Linux; U; Linux i554 ; en-US) Gecko/20100101 Firefox/58.4",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_6; like Mac OS X) AppleWebKit/602.13 (KHTML, like Gecko)  Chrome/54.0.3019.235 Mobile Safari/535.3",
				"Mozilla/5.0 (Windows NT 10.0;; en-US) AppleWebKit/601.20 (KHTML, like Gecko) Chrome/52.0.1681.384 Safari/534",
				"Mozilla/5.0 (Linux; U; Linux x86_64; en-US) AppleWebKit/535.14 (KHTML, like Gecko) Chrome/55.0.3659.247 Safari/603",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_0_3) AppleWebKit/602.17 (KHTML, like Gecko) Chrome/47.0.1645.316 Safari/602",
				"Mozilla/5.0 (Windows; Windows NT 10.5;) Gecko/20100101 Firefox/66.1",
				"Mozilla/5.0 (Android; Android 7.1; GT-I9700 Build/KTU84P) AppleWebKit/536.47 (KHTML, like Gecko)  Chrome/50.0.2702.385 Mobile Safari/535.9",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_2; like Mac OS X) AppleWebKit/535.25 (KHTML, like Gecko)  Chrome/51.0.1810.100 Mobile Safari/533.8",
				"Mozilla/5.0 (iPod; CPU iPod OS 8_4_5; like Mac OS X) AppleWebKit/535.15 (KHTML, like Gecko)  Chrome/51.0.3428.210 Mobile Safari/600.5",
				"Mozilla/5.0 (Windows; Windows NT 10.3;) Gecko/20100101 Firefox/46.8",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_0; en-US) AppleWebKit/536.27 (KHTML, like Gecko) Chrome/51.0.1145.266 Safari/603",
				"Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 10.3; x64 Trident/6.0)",
				"Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.2; x64; en-US Trident/5.0)",
				"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64 Trident/6.0)",
				"Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 9 Build/LMY48B) AppleWebKit/534.49 (KHTML, like Gecko)  Chrome/52.0.2825.249 Mobile Safari/534.6",
				"Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/534.33 (KHTML, like Gecko)  Chrome/54.0.1451.232 Mobile Safari/537.2",
				"Mozilla/5.0 (Windows; Windows NT 10.3; x64) Gecko/20130401 Firefox/48.7",
				"Mozilla/5.0 (iPad; CPU iPad OS 9_0_4 like Mac OS X) AppleWebKit/603.22 (KHTML, like Gecko)  Chrome/53.0.3623.345 Mobile Safari/603.9",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_4_8) AppleWebKit/601.19 (KHTML, like Gecko) Chrome/49.0.2506.218 Safari/603",
				"Mozilla/5.0 (Windows NT 6.3; x64; en-US) AppleWebKit/603.24 (KHTML, like Gecko) Chrome/53.0.1742.296 Safari/603",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_3_2) Gecko/20130401 Firefox/46.0",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 8_7_9; en-US) Gecko/20100101 Firefox/48.6",
				"Mozilla/5.0 (Android; Android 7.0; Nexus 8P Build/NPD90G) AppleWebKit/602.19 (KHTML, like Gecko)  Chrome/48.0.1217.239 Mobile Safari/602.7",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_4; like Mac OS X) AppleWebKit/534.35 (KHTML, like Gecko)  Chrome/48.0.2909.254 Mobile Safari/537.4",
				"Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G935FD Build/MMB29M) AppleWebKit/534.26 (KHTML, like Gecko)  Chrome/47.0.3356.144 Mobile Safari/535.6",
				"Mozilla/5.0 (Linux; U; Android 7.0; Xperia Build/NDE63X) AppleWebKit/603.21 (KHTML, like Gecko)  Chrome/54.0.1187.192 Mobile Safari/600.5",
				"Mozilla/5.0 (Linux; U; Android 7.1.1; Nexus 8P Build/NPD90G) AppleWebKit/601.46 (KHTML, like Gecko)  Chrome/52.0.1104.398 Mobile Safari/535.1",
				"Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/601.6 (KHTML, like Gecko) Chrome/52.0.3517.248 Safari/602",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 9_4_8; en-US) Gecko/20130401 Firefox/59.2",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2; like Mac OS X) AppleWebKit/600.31 (KHTML, like Gecko)  Chrome/47.0.1358.373 Mobile Safari/600.0",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_1_2; en-US) AppleWebKit/533.29 (KHTML, like Gecko) Chrome/48.0.2722.191 Safari/603",
				"Mozilla/5.0 (Linux; U; Linux i666 x86_64) Gecko/20100101 Firefox/73.5",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_0; like Mac OS X) AppleWebKit/537.4 (KHTML, like Gecko)  Chrome/55.0.1158.286 Mobile Safari/536.0",
				"Mozilla/5.0 (Android; Android 4.4; Nexus5 V7.1 Build/KOT49H) AppleWebKit/534.41 (KHTML, like Gecko)  Chrome/54.0.2478.170 Mobile Safari/535.4",
				"Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 10.0;; en-US Trident/4.0)",
				"Mozilla/5.0 (Linux; Android 4.4.4; SM-T531 Build/KOT49H) AppleWebKit/601.23 (KHTML, like Gecko)  Chrome/54.0.3258.244 Mobile Safari/537.0",
				"Mozilla/5.0 (iPod; CPU iPod OS 9_3_3; like Mac OS X) AppleWebKit/535.25 (KHTML, like Gecko)  Chrome/55.0.1076.368 Mobile Safari/533.8",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_2; like Mac OS X) AppleWebKit/600.29 (KHTML, like Gecko)  Chrome/49.0.2245.311 Mobile Safari/537.6",
				"Mozilla/5.0 (U; Linux x86_64) AppleWebKit/603.36 (KHTML, like Gecko) Chrome/48.0.3959.195 Safari/536",
				"Mozilla/5.0 (iPad; CPU iPad OS 7_8_6 like Mac OS X) AppleWebKit/602.14 (KHTML, like Gecko)  Chrome/49.0.2527.140 Mobile Safari/602.6",
				"Mozilla/5.0 (Android; Android 4.4.1; Nexus5 V7.1 Build/KOT49H) AppleWebKit/602.16 (KHTML, like Gecko)  Chrome/51.0.2758.182 Mobile Safari/533.1",
				"Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.1; WOW64 Trident/6.0)",
				"Mozilla/5.0 (Windows; U; Windows NT 6.1;) Gecko/20100101 Firefox/70.7",
				"Mozilla/5.0 (Windows NT 10.1; x64) Gecko/20100101 Firefox/54.5",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_6_0; en-US) Gecko/20100101 Firefox/59.3",
				"Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/55.0.3470.167 Safari/537",
				"Mozilla/5.0 (Windows; U; Windows NT 10.3; x64) Gecko/20100101 Firefox/66.1",
				"Mozilla/5.0 (Linux; Android 7.0; GT-I9400 Build/KTU84P) AppleWebKit/600.29 (KHTML, like Gecko)  Chrome/48.0.3991.138 Mobile Safari/534.3",
				"Mozilla/5.0 (Linux x86_64) AppleWebKit/533.46 (KHTML, like Gecko) Chrome/55.0.3339.331 Safari/533",
				"Mozilla/5.0 (Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/54.0.1192.168 Safari/536",
				"Mozilla/5.0 (U; Linux i674 x86_64) AppleWebKit/600.43 (KHTML, like Gecko) Chrome/49.0.3622.131 Safari/536",
				"Mozilla/5.0 (Linux i583 x86_64) AppleWebKit/603.38 (KHTML, like Gecko) Chrome/55.0.2186.173 Safari/601",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_2; like Mac OS X) AppleWebKit/601.25 (KHTML, like Gecko)  Chrome/54.0.3364.236 Mobile Safari/603.5",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 7_0_4; en-US) Gecko/20100101 Firefox/64.9",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_3_4; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/48.0.2087.265 Safari/537",
				"Mozilla/5.0 (Windows NT 10.5; WOW64; en-US) AppleWebKit/600.11 (KHTML, like Gecko) Chrome/55.0.2464.233 Safari/536",
				"Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/535.42 (KHTML, like Gecko)  Chrome/51.0.1292.319 Mobile Safari/600.3",
				"Mozilla/5.0 (Linux i653 ; en-US) Gecko/20100101 Firefox/74.9",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_8; like Mac OS X) AppleWebKit/534.6 (KHTML, like Gecko)  Chrome/50.0.3403.249 Mobile Safari/600.1",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) Gecko/20100101 Firefox/46.6",
				"Mozilla/5.0 (Android; Android 4.4; ALCATEL ONETOUCH 7044X Build/KOT49H) AppleWebKit/603.44 (KHTML, like Gecko)  Chrome/55.0.2022.320 Mobile Safari/533.0",
				"Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64) Gecko/20100101 Firefox/68.5",
				"Mozilla/5.0 (iPod; CPU iPod OS 9_9_1; like Mac OS X) AppleWebKit/535.22 (KHTML, like Gecko)  Chrome/50.0.3820.286 Mobile Safari/535.7",
				"Mozilla/5.0 (Linux; Android 7.1.1; LG-H930 Build/NRD90C) AppleWebKit/536.45 (KHTML, like Gecko)  Chrome/53.0.3156.281 Mobile Safari/603.2",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/533.26 (KHTML, like Gecko)  Chrome/52.0.2754.299 Mobile Safari/600.7",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_8; like Mac OS X) AppleWebKit/533.14 (KHTML, like Gecko)  Chrome/55.0.1258.194 Mobile Safari/534.8",
				"Mozilla/5.0 (U; Linux i664 x86_64; en-US) Gecko/20100101 Firefox/74.0",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_3_2; en-US) AppleWebKit/600.46 (KHTML, like Gecko) Chrome/55.0.2564.382 Safari/537",
				"Mozilla/5.0 (Linux; U; Android 4.4.4; Lenovo P785 Build/Lenovo) AppleWebKit/602.41 (KHTML, like Gecko)  Chrome/54.0.2414.291 Mobile Safari/602.8",
				"Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) Gecko/20100101 Firefox/48.8",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_1) Gecko/20130401 Firefox/68.3",
				"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_1_6; en-US) AppleWebKit/600.5 (KHTML, like Gecko) Chrome/52.0.1498.223 Safari/535",
				"Mozilla/5.0 (Linux; Linux x86_64) Gecko/20130401 Firefox/73.5",
				"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64 Trident/6.0)",
				"Mozilla/5.0 (U; Linux i654 x86_64; en-US) Gecko/20100101 Firefox/61.8",
				"Mozilla/5.0 (iPad; CPU iPad OS 11_4_6 like Mac OS X) AppleWebKit/602.43 (KHTML, like Gecko)  Chrome/54.0.1070.182 Mobile Safari/603.6",
				"Mozilla/5.0 (U; Linux i576 ) AppleWebKit/603.27 (KHTML, like Gecko) Chrome/52.0.1664.173 Safari/600",
				"Mozilla/5.0 (Linux; U; Android 7.0; Nexus 9X Build/NME91E) AppleWebKit/600.19 (KHTML, like Gecko)  Chrome/54.0.3395.202 Mobile Safari/534.4",
				"Mozilla/5.0 (Windows; Windows NT 6.3; x64) Gecko/20130401 Firefox/51.7",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 8_5_6; en-US) AppleWebKit/600.4 (KHTML, like Gecko) Chrome/47.0.3302.166 Safari/603",
				"Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64) Gecko/20100101 Firefox/57.7",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 9_0_9; en-US) AppleWebKit/534.23 (KHTML, like Gecko) Chrome/48.0.2041.352 Safari/603",
				"Mozilla/5.0 (Windows; U; Windows NT 6.0; x64) Gecko/20100101 Firefox/61.9",
				"Mozilla/5.0 (Linux; U; Linux i571 x86_64) Gecko/20130401 Firefox/71.2",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 9_3_3; en-US) AppleWebKit/603.44 (KHTML, like Gecko) Chrome/55.0.3961.343 Safari/533",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2_9) AppleWebKit/600.14 (KHTML, like Gecko) Chrome/49.0.3881.188 Safari/534",
				"Mozilla/5.0 (Windows; Windows NT 10.2;) Gecko/20100101 Firefox/45.5"
			]
		},
		"signin": {
			"active": False,
			"switch": {}
		},
		"timeout": 15,
		"version": "1.1.5",
		"version-release": "1.1"
	}
	
	# Kanashī Issues.
	ISSUES = "https://github.com/hxAri/Kanashi/issues"
	
	# Kanashī Versions.
	VERSION = "1.1.5"
	VERSION_RELEASE = "1.1"
	
	#[Config( String fname )]: None
	def __init__( self, fname=None ) -> None:
		
		"""
		Construct method of class Config.
		
		:params String fname
			Configuration filename
		
		:return None
		"""
		
		if  fname == None:
			fname = Config.FILENAME
		
		self.__filename__ = fname
		self.__settings__ = Settings({})
	
	#[Config.filename]: Str
	@property
	def filename( self ) -> str: return self.__filename__
	
	#[Config.read()]: None
	def load( self ) -> None:
		
		"""
		Load configuration file.
		
		:return None
		:raises ConfigError
			When the configuration file is corrupt or not found
		"""
		
		try:
			read = File.json( self.filename )
		except FileNotFoundError as e:
			raise ConfigError( "Configuration file not found", throw=self, prev=e )
		except JSONError as e:
			raise ConfigError( "Configuration file has corrupted", throw=self, prev=e )
		self.settings.set( read )
	
	#[Config.save()]: None
	def save( self ) -> None:
		self.settings.set({
			"version": Config.VERSION,
			"version-release": Config.VERSION_RELEASE
		})
		try:
			File.write( self.filename, self.settings.dict() )
		except Exception as e:
			raise ConfigError( "Failed save configuration", throw=self, prev=e )
	
	#[Config.settings]
	@property
	def settings( self ) -> Settings: return self.__settings__
	

# Avoid typo.
Config.GITHUB = Config.REPOSITORY
