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

#[kanashi.utility.common.droper( Dict|List|Object items, List<Dict|List|Object|Dict> keys )]: Dict
def droper( items, keys ):
	
	"""
	Drops item based keys given.
	
	:params Dict|List|Object items
	:params List<Dict|List|Object|Str> keys
	
	:return Dict
		Droped items
	
	:raises ValueError
		When keys parameter is invalid
	"""
	
	if  typedef( keys, str ):
		keys = [keys]
	if  typedef( keys, list, False ):
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
			if  k in items:
				drops[k] = items[k]
	return drops

#[kanashi.itility.common.typedef( Mixed instance, Mixed of, Bool opt )]: Bool
def typedef( instance, of=None, opt=None ):
	
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
def typeof( instance ):
	
	"""
	Return object instance name.
	
	:params Mixed instance
	
	:return Str
		Instance name
	"""
	
	return type( instance ).__name__
	