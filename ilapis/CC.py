
from .aoe import *

class CC( AoE ):
    
    def __init__( self, session: Session = None ):
        
        super().__init__()
        
        if  session == None:
            session = Session()
            session.headers.update({ "Referer": AoEURL.AccountsLogin })
            session.headers.update({ "User-Agent": self.browser() })
        
        try:
            self.session
        except AttributeError:
            self.session = session
        
        self.queue( "e[1;37mPlease\x20wait...", self.ping )
        pass
    
    
    
