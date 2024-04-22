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

from builtins import bool as Bool, int as Int, str as Str
from getpass import getpass
from multiprocessing import Process
from os import name as OSName, system
from re import MULTILINE, S
from re import compile, match, Pattern, split, sub as substr
from time import sleep
from typing import (
	Any, 
	Callable, 
	Dict,
	Final,  
	List, 
	MutableMapping, 
	MutableSequence, 
	TypeVar as Var, 
	Union
)

from kanashi.library.represent import Represent
from kanashi.library.storage import Storage
from kanashi.throwable import Throwable
from kanashi.typing.process import Process


Banner:Str = ""
""" Kanashi Banner """

Key = Var( "Key" )
""" Keyset Type """

Val = Var( "Val" )
""" Value Type """

banner = ""
filename = "\x62\x61\x6e\x6e\x65\x72\x2e\x68\x78"
if Storage.f( filename ):
	contents = Storage.cat( filename )
	chunks = len( contents )
	chunkSize = 2
	Banner:Final[Str] = "".join( list( bytes.fromhex( contents[i:i+chunkSize] ).decode( "ASCII" ) for i in range( 0, chunks, chunkSize ) ) )

# Delete unused variables.
del filename, banner


def arrange( buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], indent:Int=4, line:Bool=False ) -> Str:
	
	"""
	Builder to arrange the ouput template

	:params Dict<Str,Any>|List<Dict<Str,Any>>|Str buffers
		The output buffers
	:params Int indent
		The output indentation
	:params Bool line
		Allow current buffer with line

	:return Str
	"""
	
	outputs = []
	spaces = "\x20" * indent
	if buffers is None:
		return ""
	if isinstance( buffers, dict ):
		for keyset in buffers:
			values = buffers[keyset]
			if isinstance( values, ( set, tuple ) ):
				values = list( values )
			if isinstance( values, dict ):
				if "message" in values:
					outputs.append( arrange( values['message'], indent +4 if "line" in values and values['line'] else indent, "line" in values and not values['line'] ) )
				else:
					outputs.append( arrange( values, indent +4 if line else indent, not line ) )
			elif isinstance( values, list ):
				outputs.append( arrange( values, indent +4 if line else indent, not line ) )
			else:
				message = values if isinstance( values, str ) else repr( values )
				outputs.extend( list( "\x7b\x30\x7d\x7b\x31\x7d\x29\x20\x1b[1;38;5;252m\x7b\x32\x7d\x1b[0m".format( spaces, keyset, part ) if line is True else "\x7b\x30\x7d\x7b\x31\x7d".format( spaces, part ) for part in message.split( "\x0a" ) ) )
			...
		...
	elif isinstance( buffers, list ):
		index = 0
		length = len( buffers )
		for i in range( length ):
			values = buffers[i]
			if isinstance( values, ( set, tuple ) ):
				values = list( values )
			if isinstance( values, dict ):
				if "message" in values:
					outputs.append( arrange( values['message'], indent +4 if "line" in values and values['line'] else indent, "line" in values and not values['line'] ) )
				else:
					outputs.append( arrange( values, indent +4 if line else indent, not line ) )
				index += 1
			elif isinstance( values, list ):
				outputs.append( arrange( values, indent +4 if line else indent, not line ) )
				index += 1
			else:
				message = values if isinstance( values, str ) else repr( values )
				for part in message.split( "\x0a" ):
					if line is True:
						post = i +1 - index
						leng = len( str( length ) )
						leng = leng +1 if leng == 1 else leng
						outputs.append( f"\x7b\x30\x7d\x7b\x31\x3a\x30\x3e{leng}\x7d\x29\x20\x1b[1;38;5;252m\x7b\x32\x7d\x1b[0m".format( spaces, post, part ) )
					else:
						outputs.append( "\x7b\x30\x7d\x7b\x31\x7d".format( spaces, part ) )
				...
			...
		...
	else:
		message = buffers if isinstance( buffers, str ) else repr( buffers )
		outputs.extend( list( "\x7b\x30\x7d\x7b\x31\x7d".format( spaces, part ) for part in message.split( "\x0a" ) ) )
	return "\x0a".join( outputs )

def callback( prompt:Str=None, handler:Callable[[],Any]=None, *args:Any, **kwargs:Any ) -> Any:
	
	"""
	Callback handler
	
	:params Str prompt
	:params Callable<<>,Any> handler
	:params Any *args
	:params Any **kwargs
	
	:return Any
	"""
	
	try:
		if not callable( handler ):
			raise TypeError( f"Invalid \"handler\" parameter, parameter value type must be Callable<<*Args,**Kwargs>,Any>, {typeof( handler )} passed" )
	except TypeError as e:
		stderr( callback, e, None, close=1 )
	if prompt is None or not prompt:
		prompt = "Back to {} >>>".format( stdctx( handler, "in" ) )
	print( end="\x20\x20" )
	stdin( prompt, default="Y", repeated=True, ignore=False )
	return handler( *args, **kwargs )

def colorize( string:Str, base:Str=None ) -> Str:
	
	"""
	Automatic colorize the given strings
	
	:params Str string
	:params Str base
		The string base color ansi code
	
	:return Str
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
			"pattern": r"(?P<typedef>\b(?:ABCMeta|AbstractSet|Annotated|Any|AnyStr|ArithmeticError|AssertionError|AsyncContextManager|AsyncGenerator|AsyncIterable|AsyncIterator|AttributeError|Awaitable|BaseException|BinaryIO|BlockingIOError|BrokenPipeError|BufferError|ByteString|BytesWarning|Callable|ChainMap|ChildProcessError|ClassVar|Collection|Concatenate|ConnectionAbortedError|ConnectionError|ConnectionRefusedError|ConnectionResetError|Container|ContextManager|Coroutine|Counter|DefaultDict|DeprecationWarning|Deque|Dict|EOFError|Ellipsis|EncodingWarning|EnvironmentError|Exception|False|FileExistsError|FileNotFoundError|Final|FloatingPointError|ForwardRef|FrozenSet|FutureWarning|Generator|GeneratorExit|Generic|GenericAlias|Hashable|IO|IOError|ImportError|ImportWarning|IndentationError|IndexError|InterruptedError|IsADirectoryError|ItemsView|Iterable|Iterator|KT|Key|KeyError|KeyboardInterrupt|KeysView|List|Literal|LookupError|Mapping|MappingView|Match|MemoryError|MethodDescriptorType|MethodWrapperType|ModuleNotFoundError|MutableMapping|MutableSequence|MutableSet|NameError|NamedTuple|NamedTupleMeta|NewType|NoReturn|None|NotADirectoryError|NotImplemented|NotImplementedError|OSError|Optional|OrderedDict|OverflowError|ParamSpec|ParamSpecArgs|ParamSpecKwargs|Pattern|PendingDeprecationWarning|PermissionError|ProcessLookupError|Protocol|RecursionError|ReferenceError|ResourceWarning|Reversible|RuntimeError|RuntimeWarning|Sequence|Set|Sized|StopAsyncIteration|StopIteration|SupportsAbs|SupportsBytes|SupportsComplex|SupportsFloat|SupportsIndex|SupportsInt|SupportsRound|SyntaxError|SyntaxWarning|SystemError|SystemExit|T|TabError|Text|TextIO|TimeoutError|True|Tuple|Type|TypeAlias|TypeError|TypeGuard|TypeVar|TypedDict|UnboundLocalError|UnicodeDecodeError|UnicodeEncodeError|UnicodeError|UnicodeTranslateError|UnicodeWarning|Union|UserWarning|Val|alueError|ValuesView|Warning|WrapperDescriptorType|ZeroDivisionError|abs|abstractmethod|aiter|all|anext|any|ascii|bin|[bB]ool|breakpoint|bytearray|bytes|callable|cast|chr|classmethod|collections|compile|complex|contextlib|copyright|credits|delattr|dict|dir|divmod|enumerate|eval|exec|exit|filter|final|[fF]loat|format|frozenset|functools|getattr|globals|hasattr|hash|help|hex|id|input|[iI]nt|(?:[iI]o|IO)|isinstance|issubclass|iter|len|license|list|locals|map|max|memoryview|min|next|[oO]bject|oct|open|operator|ord|overload|pow|print|property|quit|range|re|repr|reversed|round|[sS]et|setattr|slice|sorted|staticmethod|[sS]tr|sum|super|sys|[tT]uple|type|types|vars|zip)\b)",
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
		"kanashi": {
			"pattern": r"(?P<kanashi>\b(?:[kK]anash[iī])\b)",
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
							isinstance( regexps[group], dict ) and \
							isinstance( matched.group( group ), str ):
							colorize = regexps[group]['colorize']
							break
					chars = matched.group( 0 )
					if "rematch" in regexps[group] and isinstance( regexps[group]['rematch'], dict ):
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

def droper( items:Union[MutableMapping[Key,Val],MutableSequence[Val]], search:List[Union[Dict[Str,Any],Str]], nested:Bool=False ) -> Dict[Key,Val]:
	
	"""
	Drops item based keys given.
	
	:params MutableMapping<Key,Val>|MutableSequence<Val> items
	:params List<Dict<Str,Any>|Str> search
	:params Bool nested
	
	:return Dict<Key,Val>
		Droped items
	:raises TypeError
		When the value type if parameter is invalid
	"""
	
	if isinstance( search, ( MutableMapping, str ) ):
		search:List[Union[Dict[Str,Any],Str]] = [search]
	if not isinstance( items, ( MutableMapping, MutableSequence ) ):
		raise TypeError( "Invalid items parameter, value must be type MutableMapping<Key,Val>|MutableSequence<Val>, {} passed".format( typeof( items ) ) )
	if not isinstance( search, list ):
		raise TypeError( "Invalid search parameter, value must be type List<Dict<Str,Any>|Str>, {} passed".format( typeof( search ) ) )
	drops = {}
	for index in search:
		if isinstance( index, dict ) or \
			typeof( index ) in [ "Map", "Mapping", "MapBuilder" ]:
			for key in index.keys():
				if key not in items: continue
				droping = droper( items[key], index[key], nested=nested )
				if nested is True:
					drops[key] = droping
				else:
					drops = { **drops, **droping }
		elif isinstance( index, list ):
			drops = { **drops, **droper( items[key], index[key], nested=nested ) }
		elif isinstance( index, str ):
			if index in items:
				drops[index] = items[index]
		else:
			raise TypeError( "Invalid keys parameter, value must be type List<Dict|List|Object|Str>, {} passed in items".format( typeof( key ) ) )
	return drops

def puts( *values:Any, base:Str="\x1b[0m", end:Str="\x0a", sep:Str="\x20", start:Str="", close:Union[Bool,Int]=False ) -> None:
	
	"""
	Print colorize text into terminal screen
	
	:params Any *values
	:params Str base
		The string base color ansi code
	:params Str end
		The end of line outputs
	:params Str sep
		The value separator
	:params Str start
		The prefix of output line
	:params Bool|Int close
		The exit code
	"""
	
	print( *[ "".join([ start, colorize( base=base, string=value if isinstance( value, Str ) else repr( value ) ) ]) for value in values ], end=end, sep=sep )
	if close is not False:
		exit( close )
	...

def serializeable( value:Any ) -> Bool:
	
	"""
	Return whether if the value is serializable.
	
	:params Any value
	
	:return Bool
	"""
	
	return isinstance( value, ( dict, list, tuple, str, int, float, bool ) ) or value is None

def stdctx( context:Any, std:Str ) -> Str:
	if context is None:
		return f"Std{std}"
	if not isinstance( context, str ):
		typing = typeof( context )
		if isinstance( context, type ):
			return context.__qualname__
		elif typing in [ "function" ]:
			if hasattr( context, "__func__" ):
				return context.__qualname__
			return context.__qualname__
		elif typing in [ "method" ]:
			if hasattr( context, "__func__" ):
				return context.__func__.__qualname__
			return context.__class__.__qualname__
		else:
			for standar in [ ( "in", "input" ), ( "out", "output" ), ( "err", "error" ) ]:
				if std in standar:
					std = standar[1]
					break
			return f"{typing}.{std}"
	return context.strip( "\x20\x0a" )

def stderr( context:Any, thrown:BaseException, buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], clear:Bool=True, line:Bool=False, close:Union[Bool,Int]=False ) -> None:
	
	"""
	Kanashi standar error command line output
	
	:params BaseException context
	:params Dict<Str,Any>|List<Dict<Str,Any>>|Str buffers
	:params Bool clear
	:params Bool line
	:params Bool|Int close
	
	:return None
	"""
	
	if clear is True:
		system( "cls" if OSName in [ "nt", "windows" ] else "clear" )
	errors = stderrno( thrown )
	print( Banner )
	puts( "System.err:" )
	puts( "\x20\x20{}:".format( stdctx( context, "err" ) ) )
	puts( arrange( errors, line=False ) \
		.replace( f"{Storage.BASEPATH}/", "" ) \
		.replace( f"{Storage.BASEVENV}/", "" )
	)
	puts( arrange( buffers, line=False ) \
		.replace( f"{Storage.BASEPATH}/", "" ) \
		.replace( f"{Storage.BASEVENV}/", "" ), 
		close=close 
	)

def stderrno( thrown:BaseException, indent:Int=0 ) -> List[Str]:
	
	"""
	Error iterator
	
	:params BaseException thrown
	:params Int indent
	
	:return List<Str>
	"""
	
	results = []
	prefix = "\x20" * indent
	if isinstance( thrown, BaseException ):
		results.append( f"{prefix}{typeof( thrown )}:" )
		traceback = thrown.__traceback__
		filename = None
		message = None
		lineno = None
		code = None
		if traceback is not None:
			frame = traceback.tb_frame
			lineno = traceback.tb_lineno
			filename = frame.f_code.co_filename
		details = []
		if hasattr( thrown, "code" ):
			code = thrown.code
		if hasattr( thrown, "msg" ):
			message = thrown.msg
		if hasattr( thrown, "message" ):
			message = thrown.message
		if hasattr( thrown, "prev" ):
			prevInfo = stderrno( thrown.prev, indent=indent+2 )
			details.append( f"{prefix}  · prev:" )
			details.extend( prevInfo )
		groups = []
		if isinstance( thrown, Throwable ):
			groups = thrown.group
		if isinstance( thrown, ExceptionGroup ):
			groups = thrown.exceptions
		if groups:
			details.append( f"{prefix}  · groups:" )
		for i, group in enumerate( groups ):
			groupInfo = stderrno( group, indent=indent+2 )
			groupInfo[0] = "\x20".join([ groupInfo[0], f"{i}" ])
			details.extend( groupInfo )
		if code is not None:
			results.append( f"{prefix}  · code {code}" )
		if filename is not None:
			if lineno is not None:
				details.append( f"{prefix}  · raise in {filename} on line {lineno}" )
			else:
				details.append( f"{prefix}  · raise in {filename}" )
		if message is not None:
			details.append( f"{prefix}  · message \"{message}\"" )
		elif len( thrown.args ) >= 1:
			represent = Represent.convert( thrown.args, indent=4 )
			position = len( represent ) -1
			if represent[position] in [ "\x29", "\x7d", "\x5d" ]:
				represent = f"{represent[:position]}\x20\x20{represent[position:]}"
			details.append( f"{prefix}  · args {represent}" )
		if len( details ) >= 1:
			results.append( f"{prefix}  Traceback" )
			results.extend( details )
		...
	return results

def stdin( context:Any=None, prompt:Str=None, default:Union[Int,List[Union[Int,Str]],Str]=None, filters:Union[Callable[[Union[Int,Str]],Bool],List[Union[Callable[[Union[Int,Str]],Bool],Pattern]],Pattern]=None, separator:Str="\x2e", number:Bool=False, password:Bool=False, ignore:Bool=True, repeated:Bool=False ) -> Union[Int,Str]:
	
	"""
	Kanashi standar command line input
	
	:params Any context
	:params Str prompt
	:params Int|List<Int|Str>|Str default
	:params Callable<<Int|Str>,Bool>|List<Callable<<Int|Str>,Bool>|Pattern>|Pattern filters
	:params Str separator
	:params Bool number
	:params Bool password
	:params Bool ignore
	:params Bool repeated
	
	:return Int|Str
	"""
	
	if repeated is False:
		puts( "System.in:" )
	ending = "\x20"
	context = stdctx( context, "in" )
	characters = [ "\x3e", "\x5d", "\x3a" ]
	if prompt is not None:
		if not isinstance( prompt, Str ):
			prompt = stdctx( prompt, "in" )
			if prompt == context:
				parts = prompt.split( "\x2e" )
				prompt = "\x2e".join([ *list( v for i, v in enumerate( parts ) if i >= 1 ), "input" ])
			...
		if repeated is False:
			puts( f"\x20\x20{context}:" )
		if prompt[-1] not in characters:
			ending = "\x3a\x20"
		puts( f"\x20\x20\x20\x20{prompt}", end=ending )
	else:
		if context[-1] not in characters:
			ending = "\x3a\x20"
		puts( f"\x20\x20{context}", end=ending )
	try:
		values = getpass() if password is True else input()
		if not values.strip( "\x0a\x20" ):
			if default is None:
				return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True )
			if isinstance( default, list ):
				return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True ) if not default else default[0]
			return default
		elif filters is not None:
			filters = filters if isinstance( filters, list ) else [filters]
			filtered = False
			for i, filter in enumerate( filters ):
				if isinstance( filter, Pattern ):
					if filter.match( values ) is not None:
						filtered = True
						break
				elif callable( filter ) is True:
					if filter( values ) is True:
						filtered = True
						break
				else:
					raise TypeError( "Invalid input \"filters\", filters must be Callable|List<Callable|Pattern>|Pattern, {}:{} passed".format( i, typeof( filter ) ) )
			if filtered is False:
				return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True )
			return values if number is False else int( values )
		elif isinstance( default, list ):
			if number is True:
				values = int( values )
			if values not in default:
				return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True )
			return values
		return values
	except EOFError as e:
		stderr( context, e, "Force close", close=True )
	except KeyboardInterrupt as e:
		if ignore is False:
			stderr( context, e, "Force close", close=True )
		print( "\x0d" )
		return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True )
	except ValueError as e:
		return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True )
	return None

def stdout( context:Any, buffers:Union[Dict[Str,Any],List[Dict[Str,Any]],Str], clear:Bool=True, line:Bool=False, close:Union[Bool,Int]=False ) -> None:
	
	"""
	Kanashi standar command line output
	
	:params Any context
	:params Dict<Str,Any>|List<Dict<Str,Any>>|Str buffers
	:params Bool clear
	:params Bool line
	:params Bool|Int close
	
	:return None
	"""
	
	if clear is True:
		system( "cls" if OSName in [ "nt", "windows" ] else "clear" )
	arranged = arrange( buffers, line=line ) \
		.replace( f"{Storage.BASEPATH}/", "" ) \
		.replace( f"{Storage.BASEVENV}/", "" )
	print( Banner )
	puts( "System.out:" )
	puts( "\x20\x20{}:".format( stdctx( context, "out" ) ) )
	if arranged:
		puts( arranged, close=close )
	...

def Processing( context:Any, target:Callable[[],Any], loading:Str, success:Str=None, group:Str=None, name:Str=None, *args:Any, **kwargs:Any ) -> Union[Val,Exception]:
	
	"""
	Processing
	
	:params Any context
	:params Callable<<>,Any> target
	:params Str loading
	:params Str success
	:params Str group
	:params Str name
	:params Any *args
	:params Any** kwargs
	
	:return Val|Exception
	"""
	
	stdout( context, None, clear=True )
	process = Process( name=name, group=group, target=target, args=args, kwargs=kwargs )
	try:
		process.start()
		while process.is_alive():
			length = len( loading )
			position = -1
			for i in "\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-":
				if position >= length:
					position = -1
				position += 1
				messages = loading
				if position >= 1:
					messageChar = loading[position-1:position]
					messageChar = messageChar.lower() \
						if messageChar.isupper() \
						else messageChar.upper()
					messagePrefix = loading[0:position-1]
					messageSuffix = loading[position:]
					messages = "".join([
						messagePrefix, 
						messageChar, 
						messageSuffix
					])
				puts( f"    {messages} {i}", end="\x20", start="\x0d" )
				sleep( 0.1 )
		results = process.results
		if results[1] is None or not isinstance( results[1], BaseException ):
			stdout( context, success if success is not None else loading, clear=True )
			return results[0]
		stderr( context, results[1], None, clear=True )
		return results[1]
	except ( EOFError, KeyboardInterrupt ) as e:
		process.kill()
		process.terminate()
		stderr( context, e, "Program stoped", clear=True, close=1 )
	return None

def typeof( value:Any ) -> Str:
	
	"""
	Return object named type.
	
	:params Any value
	
	:return Str
	"""
	
	return value.__name__ if isinstance( value, type ) else  type( value ).__name__
