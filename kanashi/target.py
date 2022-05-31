
from .aoe import *

class URL:
    Host = "https://www.instagram.com/{}"
    AccountsLogin = Host.format( "accounts/login/" )
    AccountsLoginAjax = Host.format( "accounts/login/ajax/" )
    AccountsLoginAjax2FA = Host.format( "accounts/login/ajax/two_factor/" )
    CreateConfigure = Host.format( "create/configure" )
    ConfigureToStory = Host.format( "create/configure_to_story" )
    Post = Host.format( "p/{}" )
    RuploadIGPhoto = Host.format( "rupload_igphoto/fb_uploader_{}" )
    SharedData = Host.format( "data/shared_data/" )
    

class Target( AoE ):
    """
    
    """
    def __init__( self, context ):
        self.context = context
        self.trouble = None
        self.session = Session()
        self.session.headers.update({ "Referer": URL.AccountsLogin })
        self.session.headers.update({ "User-Agent": self.browser() })
        
        self.ping()
        
    
    def ping( self, target = None, timeout = 5 ) -> None:
        self.trouble = None
        if  target == None:
            target = "https://www.google.com"
        self.queue( "Perform network testing", self.__ping, [ target, timeout ] )
        if self.trouble != None:
            self.out( self.trouble[0], self.trouble[1] )
            next = self.raw( "Try again [Y/n]", "y", 4 )
            if next == "Y" or next == "y":
                self.ping( target, timeout )
        
    
    def __ping( self, target: str, timeout: int ) -> None:
        try:
            ping = requests.get( target.format( "" ), timeout=timeout )
            ping.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.trouble = [ "HTTPError", "Failed to check connection, status: {}".format( e.response.status_code ) ]
        except requests.exceptions.InvalidURL:
            self.trouble = [  "InvalidURL", "The link provided is invalid." ]
        except requests.exceptions.ConnectionError:
            self.trouble = [  "ConnectionError", "Internet connection is very bad." ]
        
    
    def browser( self, default: bool = True ) -> str:
        if default:
            browser = self.context.config.browser['default']
        else:
            browser = choice( self.context.config.browser['randoms'] )
        
        return( self.saveBrowser( browser ) )
        
    
    def saveBrowser( self, browser: str ) -> None:
        self.queue( "Save browser information", self.onSaveBrowser, [browser] )
        if self.trouble != None:
            self.out( self.trouble[0], self.trouble[1] )
            next = self.raw( "Try again [Y/n]", "Y", 4 )
            if next == "Y" or next == "y":
                return( self.saveBrowser( browser ) )
            else:
                self.trouble = None
                return( browser )
        else:
            return( browser )
        
    
    def onSaveBrowser( self, browser: str ) -> None:
        self.trouble = None
        try:
            with open( "kanashi/onsaved/browser.log", "a" ) as fopen:
                fopen.write( "[{}] {}\n".format( int( datetime.now().timestamp() ), ", ".join( useragent( browser ) ) ) )
                fopen.close()
        except Exception as e:
            self.trouble = [ Exception, e ]
        
    
