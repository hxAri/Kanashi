
from .module import *

class AoE:
    """
    
    """
    
    def out( self, command, message, object = None, system: str = "out", close: bool = False ) -> None:
        self.clear()
        match type( message ).__name__:
            case "dict":
                options = message
                message = options['message']
                if type( message ).__name__ == "list":
                    if "list" in options and options['list']:
                        if "line" in options and options['line']:
                            for i in range( len( message ) ):
                                message[i] = "\033[1;38;5;111m--\x20\033[1;38;5;214m[\033[1;37m{}\033[1;38;5;214m]\x20\033[1;37m{}\033[1;0m".format( i +1, message[i] )
                        else:
                            for i in range( len( message ) ):
                                message[i] = "\033[1;38;5;111m--\x20\033[1;38;5;214m[\033[1;37m·\033[1;38;5;214m]\x20\033[1;37m{}\033[1;0m".format( message[i] )
                    self.out( command, message, object, system, close )
                    return
            case "list":
                message = "\n\x20\x20\x20\x20\033[1;37m".join( message )
        if  object == None:
            object = self
        try:
            object = object.__name__
        except AttributeError:
            object = type( object ).__name__
        if type( command ).__name__ != "str":
            command = command.__name__
        print( color( f"\033[1;38;5;36mSystem\033[1;38;5;214m.\033[1;32m{system}\033[1;38;5;111m:" ) )
        print( color( f"\x20\x20\033[1;38;5;36m{object}\033[1;38;5;214m.\033[1;32m{command}\033[1;38;5;111m:" ) )
        print( color( f"\x20\x20\x20\x20\033[1;37m{message}\n" ) )
        if close:
            sys.exit()
        
    
    def exit( self, command, message: str, object = None ) -> None:
        self.out( command, message, object, "exit", True )
        
    
    def clear( self ) -> None:
        system( "clear" )
        
        
    def ascii( self, fname: string, width: int = 0, height: int = 0 ) -> str:
        pass
        
    
    def point( self, string: str = None, space: int = 0, re: bool = False ) -> None:
        points = [ ".", ".", ".", "." ]
        spaces = ""
        string = color( string )
        if space != 0:
            for i in range( space ):
                spaces += "\x20"
        if string != None:
            self.write( "\r{}{}".format( spaces, string ), False )
        for point in points:
            sys.stdout.write( "\033[1;38;5;214m." );
            sys.stdout.flush()
            sleep( 00000.5 )
        if re:
            self.clear()
        print( "\033[0m\n" )
        
    
    def write( self, string: str, re: bool = False ) -> None:
        string = color( "\033[1;37m{}\033[0m".format( string ) )
        for e in string:
            sys.stdout.write( e )
            sys.stdout.flush()
            sleep( 00000.1 )
        if re:
            self.clear()
        
    
    def queue( self, string: str, object, params=None ) -> None:
        self.clear()
        if params != None:
            work = Thread( target=object, args=params )
        else:
            work = Thread( target=object )
        work.start()
        try:
            while work.is_alive():
                for i in "-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-":
                    print( color( f"\r\033[1;37m{string} \033[1;33m{i}" ), end="" )
                    sleep( 00000.1 )
            self.clear()
        except KeyboardInterrupt:
            self.exit( "KeyboardInterrupt", "Operation aborted, system stopped." )
        
    
    def raw( self, label: str = None, default = False, space: int = 0, IgnoreKeyboard: bool = True ) -> str:
        spaces = ""
        if  label == None or label == "":
            label = "\033[1;38;5;36mSystem\033[1;38;5;214m.\033[1;32mraw"
        if  space != 0:
            for i in range( space ):
                spaces += "\x20"
        try:
            ltype = ""
            if len( findall( r"\[Y\/n\]$", label ) ) > 0:
                
                label = label.replace( "[Y/n]", "\033[1;38;5;214m[\033[1;37mY\033[1;38;5;111m/\033[1;37mn\033[1;38;5;214m]" )
            else:
                ltype = "\033[1;38;5;111m:"
            value = input( color( f"{spaces}\033[1;37m{label}{ltype}\x20" ) )
        except EOFError:
            self.exit( "EOFError", "Input canceled by user." )
        except KeyboardInterrupt:
            if  IgnoreKeyboard:
                value = self.raw( label, default, space, IgnoreKeyboard )
            else:
                raise KeyboardInterrupt
        if  value.replace( " ", "" ) == "":
            if  default:
                value = default
            else:
                value = self.raw( label, default, space, IgnoreKeyboard )
        
        return( value )
        
    
    def passw( self, label: str = None, space: int = 0, IgnoreKeyboard: bool = True ) -> str:
        if  space != 0:
            for i in range( space ):
                spaces += "\x20"
        if  label == None or label == "":
            label = "\033[1;38;5;36mGetpass\033[1;38;5;214m.\033[1;32mraw"
        try:
            value = getpass( color( f"{label}\033[1;38;5;111m:\x20" ) )
        except EOFError:
            self.exit( "EOFError", "Input canceled by user." )
        except KeyboardInterrupt:
            if  IgnoreKeyboard:
                value = self.passw( label, space, IgnoreKeyboard )
            else:
                raise KeyboardInterrupt
        if  value.replace( " ", "" ) == "":
            value = self.passw( label, space, IgnoreKeyboard )
        
        return( value )
        
    

def color( string: str ) -> str:
    for code in findall( r"e\[([0-9])\;([0-9\;]+)m", string ):
        string = string.replace(
            "e[{};{}m".format( code[0], code[1] ),
            "\033[{};{}m".format( code[0], code[1] )
        )
    return( "{}\033[0m".format( string ) )
    