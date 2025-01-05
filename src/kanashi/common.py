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

from builtins import bool as Bool, int as Int, str as Str
from datetime import datetime
from inspect import getframeinfo, stack
from json import loads as JsonDecoder, JSONDecodeError
from pytz import timezone
from random import choice
from re import MULTILINE, S
from re import compile, match, split, sub as substr
from sys import exit
from time import sleep
from typing import ( 
	Any, 
	Iterable, 
	MutableMapping, 
	MutableSequence, 
	Union
)

from kanashi.constant import BasePath, BaseVenv


__all__ = [
	"colorize",
	"cserializer",
	"delays",
	"extractor",
	"puts",
	"sorter",
	"typeof"
]


def colorize( string:Str, base:Str=None ) -> Str:
	
	"""
	Automatic colorize the given stringa
	
	Parameters:
		string (Str):
		base (Str):
			The string base color ansi code
	
	Returns:
		result (Str):
			Colorized string
	"""
	
	result = ""
	strings = [ x for x in split( r"((?:\x1b|\033)\[[0-9\;]+m)", string ) if x != "" ]
	regexps = {
		"number": {
			"pattern": r"(?P<number>\b(?:\d+)\b)",
			"colorize": "\x1b[1;38;5;61m{}{}"
		},
		"define": {
			"handler": lambda matched: substr( r"(\.|\-){1,}", lambda m: "\x1b[1;38;5;69m{}\x1b[1;38;5;111m".format( m.group() ), matched.group( 0 ) ),
			"pattern": r"(?P<define>(?:@|\$)[a-zA-Z0-9_\-\.]+)",
			"colorize": "\x1b[1;38;5;111m{}{}"
		},
		"symbol": {
			"pattern": r"(?P<symbol>\\|\:|\*|-|\+|/|&|%|=|\;|,|\.|\?|\!|\||<|>|\~){1,}",
			"colorize": "\x1b[1;38;5;69m{}{}"
		},
		"bracket": {
			"pattern": r"(?P<bracket>\{|\}|\[|\]|\(|\)){1,}",
			"colorize": "\x1b[1;38;5;214m{}{}"
		},
		"boolean": {
			"pattern": r"(?P<boolean>\b(?:False|True|None)\b)",
			"colorize": "\x1b[1;38;5;199m{}{}"
		},
		"typedef": {
			"pattern": r"(?P<typedef>\b(?:ABCMeta|AbstractSet|Annotated|Any|AnyStr|ArithmeticError|AssertionError|AsyncContextManager|AsyncGenerator|AsyncIterable|AsyncIterator|AttributeError|Awaitable|BaseException|BinaryIO|BlockingIOError|BrokenPipeError|BufferError|ByteString|BytesWarning|Callable|ChainMap|ChildProcessError|ClassVar|Collection|Concatenate|ConnectionAbortedError|ConnectionError|ConnectionRefusedError|ConnectionResetError|Container|ContextManager|Coroutine|Counter|DefaultDict|DeprecationWarning|Deque|Dict|EOFError|Ellipsis|EncodingWarning|EnvironmentError|Exception|False|FileExistsError|FileNotFoundError|Final|FloatingPointError|ForwardRef|FrozenSet|FutureWarning|Generator|GeneratorExit|Generic|GenericAlias|Hashable|IO|IOError|ImportError|ImportWarning|IndentationError|IndexError|InterruptedError|IsADirectoryError|ItemsView|Iterable|Iterator|KT|Key|KeyError|KeyboardInterrupt|KeysView|List|Literal|LookupError|Mapping|MappingView|Match|MemoryError|MethodDescriptorType|MethodWrapperType|ModuleNotFoundError|MutableMapping|MutableSequence|MutableSet|NameError|NamedTuple|NamedTupleMeta|NewType|NoReturn|None|NotADirectoryError|NotImplemented|NotImplementedError|OSError|Optional|OrderedDict|OverflowError|ParamSpec|ParamSpecArgs|ParamSpecKwargs|Pattern|PendingDeprecationWarning|PermissionError|ProcessLookupError|Protocol|RecursionError|ReferenceError|ResourceWarning|Reversible|RuntimeError|RuntimeWarning|Sequence|Set|Sized|StopAsyncIteration|StopIteration|SupportsAbs|SupportsBytes|SupportsComplex|SupportsFloat|SupportsIndex|SupportsInt|SupportsRound|SyntaxError|SyntaxWarning|SystemError|SystemExit|T|TabError|Text|TextIO|TimeoutError|True|Tuple|Type|TypeAlias|TypeError|TypeGuard|TypeVar|TypedDict|UnboundLocalError|UnicodeDecodeError|UnicodeEncodeError|UnicodeError|UnicodeTranslateError|UnicodeWarning|Union|UserWarning|Val|alueError|ValuesView|Warning|WrapperDescriptorType|ZeroDivisionError|abs|abstractmethod|aiter|all|anext|any|ascii|bin|bool|breakpoint|bytearray|bytes|callable|cast|chr|classmethod|collections|compile|complex|contextlib|copyright|credits|delattr|dict|dir|divmod|enumerate|eval|exec|exit|filter|final|float|format|frozenset|functools|getattr|globals|hasattr|hash|help|hex|id|input|int|io|isinstance|issubclass|iter|len|license|list|locals|map|max|memoryview|min|next|object|oct|open|operator|ord|overload|pow|print|property|quit|range|re|repr|reversed|round|set|setattr|slice|sorted|staticmethod|str|sum|super|sys|tuple|type|types|vars|zip)\b)",
			"colorize": "\x1b[1;38;5;213m{}{}"
		},
		"linked": {
			"handler": lambda matched: substr( r"(\\|\:|\*|-|\+|/|&|%|=|\;|,|\.|\?|\!|\||<|>|\~){1,}", lambda m: "\x1b[1;38;5;69m{}\x1b[1;38;5;43m".format( m.group() ), matched.group( 0 ) ),
			"pattern": r"(?P<linked>\bhttps?://[^\s]+)",
			"colorize": "\x1b[1;38;5;43m\x1b[4m{}{}"
		},
		"version": {
			"handler": lambda matched: substr( r"([\d\.]+)", lambda m: "\x1b[1;38;5;190m{}\x1b[1;38;5;112m".format( m.group() ), matched.group( 0 ) ),
			"pattern": r"(?P<version>\b[vV][\d\.]+\b)",
			"colorize": "\x1b[1;38;5;112m{}{}"
		},
		"author": {
			"pattern": r"(?P<author>\b(?:hx[aA]ri)\b)",
			"colorize": "\x1b[1;38;5;111m{}{}"
		},
		"comment": {
			"pattern": r"(?P<comment>\#[^\n]*)",
			"colorize": "\x1b[1;38;5;250m{}{}"
		},
		"string": {
			"handler": lambda matched: substr( r"(?<!\\)(\\\"|\\\'|\\`|\\r|\\t|\\n|\\s)", lambda m: "\x1b[1;38;5;208m{}\x1b[1;38;5;220m".format( m.group() ), matched.group( 0 ) ),
			"pattern": r"(?P<string>(?<!\\)(\".*?(?<!\\)\"|\'.*?(?<!\\)\'|`.*?(?<!\\)`))",
			"colorize": "\x1b[1;38;5;220m{}{}"
		}
	}
	if not isinstance( base, Str ):
		base = "\x1b[0m"
	try:
		last = base
		escape = None
		pattern = "(?:{})".format( "|".join( regexp['pattern'] for regexp in regexps.values() ) )
		compiles = compile( pattern, MULTILINE|S )
		skipable = []
		for idx, string in enumerate( strings ):
			if idx in skipable:
				continue
			color = match( r"^(?:\x1b|\033)\[([^m]+)m$", string )
			if color is not None:
				index = idx +1
				escape = color.group( 0 )
				last = escape
				try:
					rescape = match( r"(?:\x1b|\033)\[([^m]+)m", strings[index] )
					while rescape is not None:
						skipable.append( index )
						escape += rescape.group( 0 )
						last = rescape.group( 0 )
						index += 1
						rescape = match( r"(?:\x1b|\033)\[([^m]+)m", strings[index] )
				except IndexError:
					break
				if index +1 in skipable:
					index += 1
				skipable.append( index )
			else:
				escape = last
				index = idx
			string = strings[index]
			search = 0
			matched = compiles.search( string, search )
			while matched is not None:
				if matched.groupdict():
					group = None
					groups = matched.groupdict().keys()
					for group in groups:
						if group in regexps and \
							isinstance( regexps[group], MutableMapping ) and \
							isinstance( matched.group( group ), str ):
							colorize = regexps[group]['colorize']
							break
					chars = matched.group( 0 )
					if "rematch" in regexps[group] and isinstance( regexps[group]['rematch'], MutableMapping ):
						pass
					if "handler" in regexps[group] and callable( regexps[group]['handler'] ):
						result += escape
						result += string[search:matched.end() - len( chars )]
						result += colorize.format( regexps[group]['handler']( matched ), escape )
						search = matched.end()
						matched = compiles.search( string, search )
						continue
					result += escape
					result += string[search:matched.end() - len( chars )]
					result += colorize.format( chars, escape )
					search = matched.end()
					matched = compiles.search( string, search )
				else:
					matched = None
			result += escape
			result += string[search:]
	except Exception as e:
		raise e
	return result

def cserializer( cookies:MutableMapping[Str,Str] ) -> Str:
	
	"""
	Cookie serializer
	
	Parameters:
		cookies (MutableMapping[Str,Str]):
			MutableMapping of cookies
	
	Returns:
		Str:
			String of serialized cookies
	"""
	
	return "\x3b\x20".join( list( f"{keyset}={value}" for keyset, value in cookies.items() ) )

def delays() -> None:
	
	""" Random delays """
	
	sleep( choice([ 9, 8.2, 3.4, 6.6, 1.6, 2.8, 4, 1.4, 6.3, 3.6, 5.9, 7, 1, 1.2 ]) )

def extractor( contents:Str ) -> Iterable[MutableMapping[Str,MutableSequence[Any]]]:
	
	"""
	Json html script tag
	
	Parameters:
		contents (Str):
			Html contents
	
	Returns:
		content (Iterable[MutableMapping[Str,MutableSequence[Any]]]):
			Iterable MutableMapping of contents
	"""
	
	position = 0
	while True:
		try:
			positionBegin = contents.index( "<script", position )
			positionBeginStop = contents.index( ">", positionBegin+1 )
			positionEnd = contents.index( "</script>", positionBeginStop )
			positionEndStop = positionEnd
			positionEndStop+= 1
			position = positionEndStop
			content = contents[positionBeginStop+1:positionEnd]
			if not content:
				continue
			try:
				yield JsonDecoder( content )
			except JSONDecodeError:
				...
			finally:
				...
			continue
		except ValueError:
			...
		finally:
			...
		break
	...

def puts( *values:Any, base:Str="\x1b[0m", end:Str="\x0a", sep:Str="\x20", start:Str="", thread:Union[Int,Str]=None, logging:Bool=False, close:Int=None ) -> None:
	
	"""
	Print the value into terminal screen
	
	Parameters:
		values (*Any):
		base (Str):
			The base color code
		end (Str):
			The end of line, default is newline (\\n)
		sep (Str):
			The separator of values, default is spaces (\\s)
		start (Str):
			Prefix of output
		thread (Int|Str):
			Current thread position number
		logging (Bool):
			Allow logging output
		close (Int):
			Close the program after text printed into terminal screen
	"""
	
	if logging is True:
		stacks = stack()
		position = 1 if len( stacks )>= 2 else 0
		currtime = datetime.now( timezone( "Asia/Jakarta" ) )
		current = currtime.strftime( "%d.%m-%Y %H:%M:%S" )
		formatter = "{start}-- {datetime} -- {file}:{func}:{line} {message}"
		if isinstance( thread, Int ) and thread >= 1 or \
		   isinstance( thread, Str ) and thread:
			formatter = "{start}-- {datetime} -- {file}:{func}:{line}:{thread} {message}"
			# position = 2 if len( stacks )>= 3 else 1
		tiframe = getframeinfo( stacks[position][0] )
		for value in values:
			message = value if isinstance( value, Str ) else repr( value )
			formatted = formatter.format(
				message=message,
				file=tiframe.filename.replace( f"{BasePath}/", "" ),
				func=tiframe.function,
				line=tiframe.lineno,
				datetime=current,
				thread=thread,
				start=start
			)
			formatted = formatted \
				.replace( BasePath, "{basepath}" ) \
				.replace( BaseVenv, "{virtual}" )
			print( colorize( base=base, string=formatted ), end=end )
	else:
		for value in values:
			value = value if isinstance( value, Str ) else repr( value )
			value = "".join([ start, value ])
			print( colorize( base=base, string=value ), end=end, sep=sep )
	if close is not None:
		exit( close )
	...

def sorter( content:MutableMapping[Str,Any] ) -> MutableMapping[Str,Any]:
	results = dict()
	keysets = sorted( list( content.keys() ) )
	for keyset in keysets:
		values = content[keyset]
		if isinstance( values, dict ):
			values = sorter( values )
		elif isinstance( values, list ):
			for i, value in enumerate( values ):
				if isinstance( value, dict ):
					values[i] = sorter( value )
		results[keyset] = values
	return results

def typeof( instance:Any ) -> Str:
	
	"""
	Return name type object
	
	Parameters:
		instance (Any):
			Value type
	
	Returns:
		name (Str):
	"""
	
	if not hasattr( instance, "__qualname__" ):
		instance = type( instance )
	if hasattr( instance, "__qualname__" ):
		return f"{instance.__module__}.{instance.__qualname__}"
	return f"{instance.__module__}.{instance.__name__}"

