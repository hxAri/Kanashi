#!/usr/bin/env python3

# 
# @author hxAri
# @create -
# @update 28.05-2022
# @github https://github.com/hxAri/{ILAPIs}
# 

from .cc import *

class ILAPis( CC ):
    
    def menu( self ):
        pass
    
    def main( self ):
        try:
            if len( self.StackTrace ) == 0:
                if len( self.UserActive ) != 0:
                    print( "Logged!" )
                else:
                    default = self.FSSetting['users']['default']
                    onsaved = self.FSSetting['users']['onsaved']
                    if len( default ) !=0:
                        next = self.input( "e[1;37mContinue\x20as\x20e[1;38;5;111m{}\x20e[1;38;5;214m[e[1;37mYe[1;38;5;214m/e[1;37mne[1;38;5;214m]".format( default['username'] ), False, True )
                        if next == "Y":
                            print( "Nice!" )
                        elif next == "n":
                            print( "Onsaved!" )
                        else:
                            self.exit( "Error", "Operation\x20aborted,\x20system\x20stopped." )
                    else:
                        print( "Onsaved!" )
            else:
                for i in self.StackTrace:
                    self.cout( i[0], i[1] )
        except EOFError as e:
            self.exit( "EOFError", e )
        except NameError as e:
            self.exit( "NameError", e )
        except TypeError as e:
            self.exit( "TypeError", e )
        except KeyboardInterrupt:
            self.exit( "KeyboardInterrupt", "Operation\x20aborted,\x20system\x20stopped." )
    
