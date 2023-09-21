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


from datetime import datetime
from re import match


#[kanashi.utility.common.classmethods( Object obj, Bool wrapper )]: Dict<Str, Callable>
def classmethods( obj:object, wrapper:bool=False ) -> dict[str:callable]:

	"""
	Return dictionary method of class.

	:params Object obj
	:params Bool wrapper
		Include wrapper methods e.g __(init|repr)__
	
	:return Dict<Str, Callable>
	"""

	methods = {}
	for method in dir( obj ):
		if not wrapper:
			if  method.startswith( "__" ) and \
				method.endswith( "__" ):
				continue
		methods[method] = getattr( obj, method )
	return methods

#[kanashi.utility.common.droper( Dict|List|Object items, List<Dict|List|Object|Dict> keys )]: Dict
def droper( items:dict|list, keys:list ) -> dict:
	
	"""
	Drops item based keys given.
	
	:params Dict|List|Object items
	:params List<Dict|List|Object|Str> keys
	
	:return Dict
		Droped items
	
	:raises ValueError
		When keys parameter is invalid
	"""
	
	if typedef( keys, str ):
		keys = [keys]
	if typedef( keys, list, False ):
		raise ValueError( "Invalid keys parameter, value must be type List<Dict|List|Object|Str>, {} passed".format( typeof( keys ) ) )
	drops = {}
	for i, k in enumerate( keys ):
		if  typedef( k, dict ) or \
			typedef( k, "Object" ):
			for index, key in enumerate( k ):
				if  typedef( k, "Object" ):
					key = k.keys( key )
				if  key in items:
					drops = {
						**drops,
						**droper( items[key], k[key] )
					}
		elif typedef( k, list ):
			drops = {
				**drops,
				**droper( items, k )
			}
		else:
			if k in items:
				drops[k] = items[k]
	return drops

#[kanashi.utility.common.encpaswd( Str password )]: Str
def encpaswd( password:str ) -> str: return "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password )

#[kanashi.utility.common.isUserId( Int|Str id)]: Bool
def isUserId( id:int|str ) -> bool: return bool( match( r"^[1-9]{1}[0-9]{9,10}$", str( id ) ) )

#[kanashi.itility.common.typedef( Mixed instance, Mixed of, Bool opt )]: Bool
def typedef( instance, of=None, opt:bool=None ) -> bool:
	
	"""
	Returns if instance is instance of instead.
	
	:params Mixed instance
	:params Mixed of
	:params Bool opt
		Negative check
	
	:return Bool
	"""
	
	if  isinstance( opt, bool ):
		return typedef( instance, of ) == opt
	else:
		try:
			of = of.__name__
		except AttributeError:
			if  not isinstance( of, str ):
				of = type( of ).__name__
		instance = type( instance ).__name__
		if  instance == of:
			return True
		return False

#[kanashi.utility.common.typeof( Mixed instance )]: Str
def typeof( instance ) -> str:
	
	"""
	Return object instance name.
	
	:params Mixed instance
	
	:return Str
		Instance name
	"""
	
	return type( instance ).__name__
	