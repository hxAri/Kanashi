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

from brotli import decompress as BrotliDecompress, error as BrotliError
from builtins import bool as Bool, int as Int, str as Str
from datetime import datetime
from dateutil.relativedelta import relativedelta
from getpass import getpass
from gzip import BadGzipFile, decompress as GzipDecompress
from hashlib import md5
from os import name as OSName, system
from pytz import timezone
from pyzstd import decompress as ZstdDecompress, ZstdError
from random import choice
from re import MULTILINE, S
from re import compile, match, Pattern, split, sub as substr
from requests import Session
from requests.exceptions import (
	ConnectionError as RequestConnectionError, 
	ConnectTimeout as RequestConnectionTimeout, 
	RequestException as RequestError
)
from time import sleep
from traceback import FrameSummary
from traceback import format_exc, extract_tb as ExtractTb
from typing import (
	Any, 
	Callable, 
	Dict, 
	Final,  
	List, 
	Tuple,  
	TypeVar as Var, 
	Union 
)
from urllib3.exceptions import (
	ConnectionError as UrllibConnectionError,
	ConnectTimeoutError as UrllibConnectTimeoutError,
	RequestError as UrllibRequestError,
	NewConnectionError as UrllibNewConnectionError
)

from kanashi.library.represent import Represent
from kanashi.library.storage import Storage
from kanashi.typing.response import Response


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

def camelCase( keyword:Str ) -> Str:
	if "_" in keyword:
		return "".join( list([ keyword.split( "_" )[0], *list( word.capitalize() for word in keyword[keyword.index( "_" ):].split( "_" ) ) ]) )
	return keyword

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
			"pattern": r"(?P<kanashi>\b(?:[kK]anash[iī]|hx[aA]ri)\b)",
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

def delays() -> None:
	
	""" Random delays """
	
	# sleep( choice([ 9, 8.2, 3.4, 6.6, 2.8, 4, 6.3, 3.6, 5.9, 7 ]) )

def download( source:Str, mediaType:Str, directory:Str=None, proxies:Dict[Str,Str]=None, stream:Bool=False, thread:Int=0 ) -> Str:

	"""
	Download media content e.g image, video

	:params Str source
		The media url source
	:params Str mediaType
		The file media type, e.g image, video
	:params Str directory
		The media directory save
	:params Dict<Str,Str> proxies
		The Http request proxies
	:params Bool stream
		Allow request stream
	:params Int thread
		Current thread position number
	
	:return Str
	"""
	
	response = request( "GET", url=source, proxies=proxies, stream=stream )
	response.json
	if response.status == 200:
		extename = extension( response, mediaType, "jpg" if mediaType == "image" else "mp4" if mediaType == "video" else "" )
		pathname = directory if directory is not None else f"history/contents"
		filename = md5( source.encode( "utf-8" ) ).hexdigest()
		fullname = f"{pathname}/{filename}.{extename}"
		try:
			Storage.mkdir( pathname )
			Storage.touch( fullname, response.content, fmode="wb" )
			return fullname
		except OSError as e:
			raise TypeError( f"Failed download media mediaType={mediaType}", e )
		...
	return None

def extension( response:Response, type:Str="image", default:Str="jpg", thread:Int=0 ) -> Str:

	"""
	Return file extension name by request response.

	:params Response response
	:params Str type
		The file media type, e.g image, video
	:params Str default
		The default file extension name when the response is unknown Content-Type
	:params Int thread
		Current thread position number
	
	:return Str
	"""
	
	contentType = response.headers['Content-Type']
	matched = match( r"^(?:(?P<image>image)\/(?P<image_extension>jpg|jpeg|png|webp)|(?P<video>video\/(?P<video_extension>mp4|webm)))$", contentType )
	if matched is not None:
		groups = matched.groupdict()
		group = f"{type}_extension"
		if group in groups and groups[group]:
			return groups[group]
		return default
	raise ValueError( f"Unsupported media type for Content-Type {contentType}" )

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
		try:
			exit( close )
		except SystemExit:
			...
		finally:
			...
	...

def request( method:Str, url:Str, data:Dict[Str,Any]=None, cookies:Dict[Str,Str]=None, headers:Dict[Str,Str]=None, params:Dict[Str,Str]=None, payload:Dict[Str,Any]=None, proxies:Dict[Str,Str]=None, stream:Bool=False, timeout:Int=None, tries:Int=10 ) -> Response:
	
	"""
	Send HTTP Request
	
	:params Str method
		Http request method
	:params Str url
		Http request url target
	:params Dict<Str, Any> data
		Http request multipart form data
	:params Dict<Str, Str> cookies
		Http request cookies
	:params Dict<Str, Str> headers
		Http request headers
	:params Dict<Str, Str> params
		Http request parameters
	:params Dict<Str, Any> payload
		Http request json payload data
	:params Dict<Str, Any> proxies
		Http request proxies
	:params Bool stream
		Allow request stream
	:params Int timeout
		Http request timeout
	:params Int tries
		Http request timeout tries
	
	:return Response
	"""
	
	counter = 0
	session = Session()
	throwned = []
	throwable = [
		RequestConnectionError, 
		RequestConnectionTimeout, 
		RequestError,
		UrllibConnectionError,
		UrllibConnectTimeoutError,
		UrllibRequestError,
		UrllibNewConnectionError
	]
	continueable = ( 
		RequestConnectionError, 
		RequestConnectionTimeout, 
		UrllibConnectionError,
		UrllibConnectTimeoutError,
		UrllibNewConnectionError
	)
	if tries <= 0:
		tries = 10
	while counter <= 10:
		puts( f"Trying {method} Request url=\"{url}\"", start="\x20" * 4 )
		try:
			response = session.request( 
				url=url, 
				data=data, 
				json=payload, 
				stream=stream,
				method=method, 
				cookies=cookies, 
				headers=headers, 
				timeout=timeout,
				proxies=proxies,
				params=params 
			)
			encoding = response.headers['Content-Encoding'] \
				if "Content-Encoding" in response.headers \
				else None
			contentType = None
			characterSet = None
			if "Content-Type" in response.headers:
				parts = response.headers['Content-Type'].split( "\x3b" )
				characterSet = parts[1].strip( "\x20" ).split( "\x3d" ).pop() if len( parts ) >= 2 else None
				contentType = parts[0].strip( "\x20" )
			try:
				if encoding is not None:
					content = response._content
					match encoding:
						case "br":
							content = BrotliDecompress( response.content )
						case "gzip":
							content = GzipDecompress( response.content )
						case "zstd":
							content = ZstdDecompress( response.content )
						case _:
							puts( f"Encoding {encoding}: {response.content}", start="\x20" * 4 )
							puts( f"Unsupported content encoding {encoding}", start="\x20" * 4 )
					response._content = content
				...
			except( BadGzipFile, BrotliError, ZstdError ):
				...
			return Response(
				url=response.url,
				raw=response.text,
				type=contentType,
				status=response.status_code,
				payload=payload if payload is not None else data,
				content=response.content,
				cookies=response.cookies,
				headers=response.headers,
				charset=characterSet,
				encoding=encoding
			)
		except BaseException as e:
			instance = type( e )
			throwable.append( e )
			puts( f"{typeof( e )}: {format_exc()}", start="\x20" * 4 )
			if instance in throwable:
				if isinstance( e, continueable ):
					counter += 1
					sleep( 2 )
					continue
			if throwned:
				raise ExceptionGroup( f"An error occurred while sending a {method} request to url=\"{url}\"", throwned )
			raise e
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
	print( Banner )
	puts( "System.err:" )
	puts( "\x20\x20{}:".format( stdctx( context, "err" ) ) )
	puts( arrange( stderrno( thrown ), line=False ) \
		.replace( f"{Storage.BASEPATH}/", "" ) \
		.replace( f"{Storage.BASEVENV}/", "" )
	)
	puts( arrange( buffers, line=False ) \
		.replace( f"{Storage.BASEPATH}/", "" ) \
		.replace( f"{Storage.BASEVENV}/", "" ), 
		close=close 
	)

def stderrca( thrown:BaseException ) -> Dict[Str,Union[Str,List[Dict[Str,Any]]]]:
	caused = None
	groups = []
	traceback = None
	if thrown is not None:
		if hasattr( thrown, "__cause__" ):
			caused = thrown.__cause__
		if hasattr( thrown, "__traceback__" ):
			traceback = thrown.__traceback__
		if hasattr( thrown, "groups" ):
			...
		if hasattr( thrown, "exceptions" ):
			...
		message = thrown.args
		if hasattr( thrown, "message" ):
			message = thrown.message
		elif hasattr( thrown, "msg" ):
			message = thrown.msg
		return {
			"typing": typeof( thrown ),
			"groups": groups,
			"message": message,
			"causes": stderrca( caused ) \
				if caused is not None \
				else None,
			"traceback": list( stderrxt( tb ) for tb in ExtractTb( traceback ) ) \
				if traceback is not None \
				else []
		}
	return None

def stderrit( traceback:Dict[Str,Union[Str,List[Dict[Str,Any]]]], indent:Tuple[Int,Int]=(4,4) ) -> List[Str]:
	spaces = "\x20" * indent[0]
	indent = ( indent[0] if indent[0] >= 4 else 4, indent[1] )
	results = []
	causes = []
	results.append( f"{traceback['typing']}:" )
	if traceback['causes'] is not None:
		causes = stderrit( traceback['causes'], indent=( indent[0], indent[1]+indent[0] ) )
		if causes:
			results.append( "· cause:" )
			results.extend( causes )
	if traceback['traceback']:
		results.append( "· traceback:" )
		for tb in traceback['traceback']:
			results.append( f"  · file {tb['file']}, on line {tb['line']}" )
			results.append( f"    · code {tb['code']['hardcode']}" )
	if traceback['message']:
		if isinstance( traceback['message'], ( bool, float, int, str ) ):
			results.append( f"· message: {traceback['message']}" )
		else:
			represent = Represent.convert( traceback['message'], indent=indent[1] )
			position = len( represent ) -1
			if represent[position] in [ "\x29", "\x7d", "\x5d" ]:
				represent = f"{represent[:position]}\x20\x20{represent[position:]}"
			represent = f"\x0a{spaces}".join( list( split for split in represent.splitlines() ) )
			results.append( f"· message: {represent}" )
	return list( "".join([ spaces, result ]) for result in results )

def stderrxt( frame:FrameSummary ) -> Dict[Str,Any]:
	anotated = None
	hardcode = frame.line
	positionStart = frame.colno
	positionEnd = positionStart + len( hardcode ) - 1
	if positionStart is not None and positionStart is not None:
		anotated = ""
	return {
		"file": frame.filename,
		"line": frame.lineno,
		"code": {
			"hardcode": hardcode,
			"anotated": anotated
		},
		"position": {
			"start": positionStart,
			"end": positionEnd
		}
	}

def stderrno( thrown:BaseException, indent=0 ) -> List[Str]:
	return stderrit( stderrca( thrown ), indent=( indent, 4 ) )

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
		elif isinstance( default, list ) and default:
			if number is True:
				values = int( values )
			if values not in default:
				return stdin( context, prompt, default, filters, separator, number, password, ignore, repeated=True )
			return values
		return values
	except EOFError as e:
		stderr( context, e, "Force close", close=1 )
	except KeyboardInterrupt as e:
		if ignore is False:
			stderr( context, e, "Force close", close=1 )
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

def timestamp( minutes:Int=0, hours:Int=0, days=0, weeks:Int=0, months:Int=0, years:Int=0, tm:Bool=False ) -> Int:
	
	"""
	Timestamp minus generator
	
	:params Int minutes
	:params Int hours
	:params Int days
	:params Int weeks
	:params Int months
	:params Int years
	:params Bool tm
		Return timestamp with *1000
	
	:return Int
		Current timestamp or current timestamp minus time
	"""
	
	zone = timezone( "Asia/Jakarta" )
	currtime = datetime.now( zone )
	relative = relativedelta( minutes=minutes, hours=hours, months=months, years=years, weeks=weeks, days=days )
	try:
		current = currtime - relative
	except ValueError:
		current = currtime
	if tm is True:
		return int( current.timestamp() * 1000 )
	return int( current.timestamp() )

def titleCase( keyword:Str ) -> Str:
	return "\x20".join( list( word.capitalize() for word in f"{keyword}".split( "_" ) ) )

def typeof( value:Any ) -> Str:
	
	"""
	Return object named type.
	
	:params Any value
	
	:return Str
	"""
	
	return value.__name__ if isinstance( value, type ) else  type( value ).__name__
