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

from kanashi.utility.common import typedef, typeof

#[kanashi.utility.tree.tree( Dict|List|Set|Tuple data, Int indent ]: String
def tree( data, indent=0 ):
	
	"""
	Convert data into tree structure.
	
	:params Dict|List|Set|Tuple data
	:params Int indent
		Indentation prefix
	
	:return String
	"""
	
	STR_LINE = "│   "
	MID_LINE = "├── "
	END_LINE = "└── "
	SPC = "\x20" * 4
	
	#[loopv( Mixed value, String space )]: String
	def loopv( value, space ):
		
		"""
		Handle data value.
		When data value is Dict|List|Set|Tuple
		loop function will called for handle that.
		
		:params Mixed value
		:params String space
			Previous space passed
		
		:return String
		"""
		
		if  typedef( value, dict ) or \
			typedef( value, list ) or \
			typedef( value, set ) or \
			typedef( value, tuple ):
			value = loop( value, space )
		else:
			value = "{}{}{}\n".format( space, END_LINE, value )
		return value
	
	#[loop( Dict|List|Set|Tuple data, String space )]: String
	def loop( data, space ):
		
		"""
		Handle data loop iteration.
		
		:params Dict|List|Set|Tuple data
		:params String space
			Indentation prefix
		
		:return String
		"""
		
		index = 0
		result = ""
		if length := len( data ):
			if typedef( data, list ):
				for value in data:
					index += 1
					if index == length:
						lk = END_LINE
						la = SPC
					else:
						lk = MID_LINE
						la = STR_LINE
					result += space
					result += lk
					if typedef( value, dict ):
						if lenv := len( value ):
							for idx, key in enumerate( value ):
								if idx == 0:
									if idx +1 == lenv:
										result += "+ "
										result += key
										result += "\n"
										if index != length:
											result += space + STR_LINE
										else:
											result += space + SPC
										result += END_LINE #+ "\n"
										result += loopv( value[key], space + STR_LINE + SPC )[len( space + STR_LINE + SPC ) + 4:]
									else:
										result += "+ "
										result += key
										result += "\n"
										result += space
										#result += SPC
										if index == length:
											result += SPC
										else:
											result += STR_LINE
										result += MID_LINE #+ "\n"
										result += loopv( value[key], space + STR_LINE * 2 )[len( space + STR_LINE * 2 ) + 4:]
									#result += "\n"
								elif index == length:
									result += space
									result += SPC
									if idx +1 == lenv:
										result += END_LINE
									else:
										result += MID_LINE
									result += key
									result += "\n"
									result += space
									result += SPC
									if idx +1 == lenv:
										result += SPC
										next = SPC
									else:
										result += STR_LINE
										next = STR_LINE
									if  typedef( value[key], dict ) or \
										typedef( value[key], list ):
										result += MID_LINE
									else:
										result += END_LINE #+ "\n"
									result += loopv( value[key], space + SPC + next )[len( space + SPC + next ) + 4:]
									#result += "\n"
								elif idx +1 == lenv:
									result += space
									result += STR_LINE
									result += END_LINE
									result += key
									result += "\n"
									result += space
									result += STR_LINE
									result += SPC
									if  typedef( value[key], dict ) or \
										typedef( value[key], list ):
										result += MID_LINE
									else:
										result += END_LINE #+ "\n"
									result += loopv( value[key], space + STR_LINE + SPC )[len( space + STR_LINE + SPC ) + 4:]
									#result += "\n"
								else:
									result += space
									result += STR_LINE
									result += MID_LINE
									result += key
									result += "\n"
									result += space
									result += STR_LINE * 2
									if  typedef( value[key], dict ) or \
										typedef( value[key], list ):
										result += MID_LINE
									else:
										result += END_LINE #+ "\n"
									result += loopv( value[key], space + STR_LINE * 2 )[len( space + STR_LINE * 2 ) + 4:]
									#result += "\n"
						else:
							result += str( value )
							result += "\n"
					elif typedef( value, list ):
						if lenv := len( value ):
							for idx, val in enumerate( value ):
								if idx == 0:
									if idx +1 == lenv:
										result += "+ "
										#result += str( idx )
										result += "\n"
										if index != length:
											result += space + STR_LINE
										else:
											result += space + SPC
										result += END_LINE + "+\n"
										result += loopv( val, space + STR_LINE + SPC )#[len( space + STR_LINE + SPC ) + 4:]
									else:
										result += "+ "
										#result += str( idx )
										result += "\n"
										result += space
										#result += SPC
										result += STR_LINE
										result += MID_LINE + "+\n"
										result += loopv( val, space + STR_LINE * 2 )#[len( space + STR_LINE * 2 ) + 4:]
									#result += "\n"
								elif index == length:
									result += space
									result += SPC
									if idx +1 == lenv:
										result += END_LINE
									else:
										result += MID_LINE
									#result += str( idx )
									result += "+\n"
									result += space
									result += SPC
									if idx +1 == lenv:
										result += SPC
										next = SPC
									else:
										result += STR_LINE
										next = STR_LINE
									if  typedef( val, dict ) or \
										typedef( val, list ):
										result += MID_LINE
									else:
										result += END_LINE + "+\n"
									result += loopv( val, space + SPC + next )#[len( space + SPC + next ) + 4:]
									#result += "\n"
								elif idx +1 == lenv:
									result += space
									result += STR_LINE
									result += END_LINE
									if  typedef( val, dict ) or \
										typedef( val, list ):
										result += ""#MID_LINE
										result += "+\n"
									else:
										result += END_LINE
										result += "+\n"
									result += loopv( val, space + STR_LINE + SPC )#[len( space + STR_LINE + SPC ) + 4:]
									#result += "\n"
								else:
									result += space
									result += STR_LINE
									result += MID_LINE
									#result += str( idx )
									result += "+\n"
									result += space
									result += STR_LINE * 2
									if  typedef( val, dict ) or \
										typedef( val, list ):
										result += MID_LINE
									else:
										result += END_LINE + "+\n"
									result += loopv( val, space + STR_LINE * 2 )#[len( space + STR_LINE * 2 ) + 4:]
									#result += "\n"
						else:
							result += str( value )
							result += "\n"
					else:
						result += value
						result += "\n"
			else:
				for idx, key in enumerate( data ):
					index += 1
					value = data[key]
					if index == length:
						lk = END_LINE
						la = SPC
					else:
						lk = MID_LINE
						la = STR_LINE
					result += space
					result += lk
					result += key
					result += "\n"
					if index == length:
						next = SPC
					else:
						next = STR_LINE
					result += loopv( value, space + next )
		else:
			result += space
			result += END_LINE
			result += str( data )
			result += "\n"
		return result
	return "\u00b7\n" + loop( data, "\x20" * indent )