
from .aoe import *
from .buffer import Buffer
from .config import Config
from .signin import Signin
from .target import Target

class System( AoE ):
    """
    
    """
    def __init__( self, session: Session = None ):
        self.active = None
        self.change = None
        self.buffer = Buffer( self )
        self.config = Config( self )
        self.signin = Signin( self )
        self.target = Target( self )
        pass
        
    
    def facode( self, username: str, rjson: dict, rkuki: dict ) -> None:
        pass
        
    
    def others( self ) -> None:
        pass
        
    
    def switch( self ) -> None:
        self.out( "SignInSwitch", {
            "message": [
                "\033[4;37mDefault",
                "\033[4;37mCookie",
                "\033[4;37mOthers",
                "\033[4;37mClose",
                "\033[4;37mBack"
            ],
            "line": False,
            "list": True
        })
        try:
            switch = int( self.raw() )
            match switch:
                case 0:
                    self.signin.signin()
                case 1:
                    self.buffer.shared()
                case 2:
                    self.others()
                case 3:
                    self.exit( "Ejected", "Program completed." )
                case 4:
                    self.main()
                case _:
                    self.switch()
        except ValueError:
            self.switch()
        
    
    def main( self ) -> None:
        try:
            if self.active != None:
                self.out( "Main", {
                    "message": [
                        "\033[4;37mHome",
                        "\033[4;37mSearch",
                        "\033[4;37mCreate",
                        "\033[4;37mExtract",
                        "\033[4;37mProfile",
                        "\033[4;37mBrowser",
                        "\033[4;37mSetting",
                        "\033[4;37mConfigs",
                        "\033[4;37mSwitch",
                        "\033[4;37mLogout"
                    ],
                    "list": True
                })
            elif len( self.config.loggeds ) > 0:
                list = []
                for user in self.config.loggeds:
                    list.append( "\033[4;37m{}".format( user['username'] ) )
                self.out( "ONSavedUsers", {
                    "message": list,
                    "line": True,
                    "list": True
                })
                user = self.raw( None, "Y" )
                try:
                    user = self.config.loggeds[( int( user ) -1 )]
                    next = self.raw( "Update saved information [Y/n]", "y" )
                    if next == "Y" or next == "y":
                        self.buffer.shared( user )
                    else:
                        self.active = user
                        self.main()
                except IndexError:
                    self.main()
                except ValueError:
                    if user == "N" or user == "n":
                        self.switch()
                    else:
                        self.main()
            else:
                self.switch()
        except IOError as e:
            self.exit( TypeError, e )
        
    
