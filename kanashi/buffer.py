
import json
import os
import requests
import sys

from datetime import datetime
from getpass import getpass
from os import system
from random import choice
from re import findall
from requests import Session
from threading import Thread
from time import sleep

class AoE:
	
	# Clear terminal screen.
	def clear( self ) -> None:
		system( "clear" )
		
	# Close terminal program.
	def close( self, reference, message, line:bool = False ) -> None:
		self.output( reference, message, line )
		exit()
		
	# Get input from users.
	def input( self, label:str, default:str = None, ignoreKeyboardInterupt:bool = True ):
		if  label == "":
			place = "System.in"
		else:
			place = "System.in.{}".format( label )
		try:
			value = input( "{}:\x20".format( place ) )
			if  value == "":
				if  default != None:
					if  default != "":
						return( default )
				return( self.input( label, default, ignoreKeyboardInterupt ) )
			else:
				return( value )
		except EOFError:
			self.close( EOFError, "exit" )
		except KeyboardInterrupt:
			if  ignoreKeyboardInterupt:
				return( self.input( label, default, True ) )
			else:
				self.close( KeyboardInterrupt, "exit" )
		
	# Get input password type.
	def inpas( self, label:str, ignoreKeyboardInterupt:bool = True ):
		if  label == "":
			place = "System.in"
		else:
			place = "System.in.{}".format( label )
		try:
			value = getpass( "{}:\x20".format( place ) )
			if  value == "":
				return( self.inpas( label, ignoreKeyboardInterupt ) )
			else:
				return( value )
		except EOFError:
			self.close( EOFError, "exit", True )
		except KeyboardInterrupt:
			if  ignoreKeyboardInterupt:
				return( self.inpas( label, True ) )
			else:
				self.close( KeyboardInterrupt, "exit" )
		
	# Display output program.
	def output( self, reference, message, line:bool = True ) -> None:
		self.clear()
		base = reference
		try:
			reference = reference.__name__
		except AttributeError:
			refer = type( reference ).__name__
			match refer:
				case "str" | "int" | "float" | "complex" | "list" | "tuple" | "range" | "dict" | "set" | "frozenset" | "bool" | "bytes" | "bytearray" | "memoryview" | "NoneType":
					pass
				case _:
					reference = refer
		print( "System.out" )
		if isinstance( base, BaseException ):
			print( "{}{}.{} {}".format( self.spaces( 2 ), type( self ).__name__, reference, base.__traceback__.tb_lineno ) )
			print( "{}{}.{} {}".format( self.spaces( 2 ), type( self ).__name__, reference, __name__ ) )
		else:
			print( "{}{}.{}".format( self.spaces( 2 ), type( self ).__name__, reference ) )
		match type( message ).__name__:
			case "dict":
				for i, v in enumerate( message ):
					if  line:
						print( "{}{} >> {}".format( self.spaces( 4 ), i +1, message[v] ) )
					else:
						print( "{}{}".format( self.spaces( 4 ), message[v] ) )
			case "list":
				for i, v in enumerate( message ):
					if  line:
						print( "{}[{}] {}".format( self.spaces( 4 ), i +1, v ) )
					else:
						print( "{}{}".format( self.spaces( 4 ), v ) )
			case _:
				print( "{}{}".format( self.spaces( 4 ), message ) )
		print( "" )
		
	# Generate white spaces by length.
	def spaces( self, length:int ) -> str:
		return( "\x20" * length )
		
	# Work threads with animation.
	def thread( self, string:str, object, params=None ) -> None:
		self.clear()
		if  params != None:
			tasker = Thread( target=object, args=params )
		else:
			tasker = Thread( target=object )
		try:
			string = "{}".format( string )
			for e in string:
				sys.stdout.write( e )
				sys.stdout.flush()
				sleep( 00000.1 )
			self.clear()
			tasker.start()
			while tasker.is_alive():
				for i in "-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-":
					print( "\r{} {}".format( string, i ), end="" )
					sleep( 00000.1 )
			self.clear()
		except KeyboardInterrupt:
			print( "Task Aborted" )
		
	# Create directory.
	def tree( self, dir:str ) -> None:
		name = "."
		path = dir.split( "/" )
		for dir in path:
			name += "/"
			name += dir
			if  not os.path.isdir( name ):
				os.mkdir( name )
		
	
class Object( AoE ):
	
	# Class initialization.
	def __init__( self, data:dict, parent:object = None ):
		self.__parent__ = parent
		self.__method__ = {}
		self.__data__ = data
		
		# Inject the attribute.
		self.inject( data )
		
	# ...
	def __repr__( self ):
		return( "{}".format( self.__data__ ) )
		
	# ...
	def __str__( self ):
		return( "{}".format( self.__data__ ) )
		
	# Set class attributes.
	def inject( self, data:dict ) -> None:
		if  type( data ).__name__ != "dict":
			self.close( ValueError, "Object data must be type dict, {} given.".format( type( data ).__name__ ) )
		for i, v in enumerate( data ):
			if  v == "parent":
				continue
			if  type( data[v] ).__name__ == "dict":
				self.__dict__[v] = Object( data[v] )
				self.__data__[v] = self.__dict__[v]
			else:
				self.__dict__[v] = data[v]
				self.__data__[v] = data[v]
		self.reload()
		
	# Reload data.
	def reload( self ) -> None:
		if  self.__parent__ == None:
			return
		for i, v in enumerate( self.__dict__ ):
			self.__parent__.__dict__[v] = self.__dict__[v]
		
	
class Active( Object ):
	
	# Class initialization.
	def __init__( self, data:dict ):
		super().__init__( data )
		
	# Diaplay user info.
	def display( self ):
		self.clear()
		self.output( "UserLogged", line=False, message=[
			" ",
			"+",
			"+ Fullname >> {}".format( self.full_name ),
			"+ Username >> {}".format( self.username ),
			"+",
			"+ {}".format( self.biography.replace( "\n", "\n+ " ) ),
			"+",
			"+ { self.follower_count } \xb7 { self.following_count } \xb7 { self.media_count }",
			"+"
		])
		
	
class Config( Object ):
	
	# System configuration.
	DEFAULT = {
		"users": {
			"default": None,
			"loggeds": []
		},
		"browser": {
			"default": "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
			"randoms": [
				"Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
				"Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12F69 Safari/600.1.4",
				"Mozilla/5.0 (Android; Tablet; rv:40.0) Gecko/40.0 Firefox/40.0",
				"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5",
			],
			"private": "Instagram 64.0.0.14.96"
		},
		"language": []
	}
	
	# Method constructor class.
	def __init__( self ):
		self.emitted = None
		self.fidata = None
		self.finame = "kanashi/saveds/configs/settings.json"
		self.firead()
		
	# ....
	def firead( self ) -> None:
		if  self.thread( "Reading configuration file", self.__read ): pass
		if  self.emitted != None:
			if  isinstance( self.emitted, FileNotFoundError ) or isinstance( self.emitted, ValueError ):
				super().__init__( Config.DEFAULT )
				path = self.finame.split( "/" )
				path.pop()
				self.tree( "/".join( path ) )
				self.fisave()
			else:
				self.output( self.emitted, [ self.emitted, "Do you want to try again [Y/n]" ] )
				pass
		else:
			super().__init__( self.fidata )
		
	# Reading configuration file.
	def __read( self ) -> None:
		self.emitted = None
		try:
			with open( self.finame, "r", encoding = "utf8" ) as fiopen:
				fidata = fiopen.read()
				fiopen.close()
			if  fidata != None and fidata != "":
				self.fidata = json.loads( fidata )
			else:
				raise ValueError( "The configuration file has been corrupted!" )
		except Exception as e:
			self.emitted = e
		
	# ...
	def fisave( self ) -> None:
		self.fidata = {
			"users": {
				"default": self.users.default,
				"loggeds": self.users.loggeds,
			},
			"browser": {
				"default": self.browser.default,
				"private": self.browser.private,
				"randoms": self.browser.randoms
			},
			"language": self.language
		}
		if  self.thread( "Saving configuration file", self.__save ): pass
		if  self.emitted != None:
			self.output( self.emitted, [ self.emitted, "Do you want to try again [Y/n]" ], False )
			next = self.input( "try", "Y" )
			if  next.upper() == "Y":
				self.fisave()
		
	# Saving configuration file.
	def __save( self ) -> None:
		self.emitted = None
		try:
			with open( self.finame, "w" ) as fiopen:
				fiopen.write( json.dumps( self.fidata, indent=4 ) )
				fiopen.close()
		except FileNotFoundError:
			path = self.finame.split( "/" )
			path.pop( "/" )
			self.tree( "/".join( path ) )
			self.__save()
		except Exception as e:
			self.emitted = e
		
	
class Request( AoE ):
	
	# Class initialization.
	def __init__( self, context ):
		self.context = context
		self.session = Session()
		self.session.headers.update({ "Referer": "https://www.instagram.com/" })
		self.session.headers.update({ "UserAgent": self.context.configs.browser.private })
		self.response = Response()
		pass
		
	# Send HTTP Request GET.
	def get( self, url:str, headers:dict = {}, cookies:dict = {} ) -> None:
		self.context.emitted = None
		self.context.results = None
		try:
			self.context.results = self.session.get( url, headers=headers, cookies=cookies )
			self.response.save( self.context.results )
		except Exception as e:
			self.context.emitted = e
		
	# Send HTTP Request POST.
	def post( self, url:str, data:dict, headers:dict = [], cookies:dict = None ) -> None:
		self.context.emitted = None
		self.context.results = None
		try:
			self.context.results = self.session.post( url, data=data, headers=headers, cookies=cookies )
			self.response.save( self.context.results )
		except Exception as e:
			self.context.emitted = e
		
	
class Response( AoE ):
	
	# Class.initialization
	def __init__( self ):
		self.finame = "kanashi/saveds/response/response.json"
		try:
			with open( self.finame, "r" ) as fiopen:
				firead = fiopen.read()
				if  firead != "" or firead != None:
					firead = json.loads( firead )
				else:
					firead = []
				fiopen.close()
			self.firead = firead
		except FileNotFoundError:
			path = self.finame.split( "/" )
			path.pop()
			self.tree( "/".join( path ) )
			self.firead = []
		
	def save( self, response ) -> None:
		self.firead.append({
			"cookies": response.cookies.get_dict(),
			"response": response.json()
		})
		try:
			with open( self.finame, "w" ) as fiopen:
				fiopen.write( json.dumps( self.firead, indent=4 ) )
				fiopen.close()
		except:
			pass
		
	