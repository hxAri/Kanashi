
from .AoE import AoE

class AoEExp( AoE ):
    def __init__( self, settings: dict = None ):
        if  settings != None:
            self.FSSetting = settings
        else:
            super().__init__()
    
