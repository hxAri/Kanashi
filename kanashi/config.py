
from .aoe import *

class Config( AoE ):
    
    def __init__( self, context ):
        self.context = context
        self.trouble = None
        self.fname = "kanashi/onsaved/configs/settings.txt"
        self.queue( "Reading configuration file", self.__fread )
        if self.trouble != None:
            if self.trouble[0].__name__ == "FileNotFoundError":
                self.fread = {
                    "allowed": {
                        "save_image": True,
                        "save_login": True
                    },
                    "browser": {
                        "default": "Instagram 64.0.0.14.96",
                        "randoms": [
                            "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"
                        ]
                    },
                    "loggeds": [],
                    "onsaved": "kanashi/onsaved/images"
                }
                self.tree( self.fname )
                self.save()
            else:
                self.exit( self.trouble[0], self.trouble[1] )
        self.loggeds = self.fread['loggeds']
        self.allowed = self.fread['allowed']
        self.browser = self.fread['browser']
        self.onsaved = self.fread['onsaved']
        
    
    def __fread( self ) -> None:
        self.trouble = None
        try:
            with open( self.fname, "r", encoding = "utf8" ) as fopen:
                fread = fopen.read()
                fopen.close()
            if  fread != None and fread != "":
                try:
                    fread = json.loads( fread )
                except json.decoder.JSONDecodeError as e:
                    self.trouble = [ json.decoder.JSONDecodeError, e ]
                self.fread = fread
            else:
                self.trouble = [ ValueError, "The configuration file has been corrupted!" ]
        except ValueError as e:
            self.trouble = [ ValueError, e ]
        except FileNotFoundError as e:
            self.trouble = [ FileNotFoundError, e ]
        
    
    def __fsave( self ) -> None:
        self.trouble = None
        try:
            self.fread = {
                "allowed": self.allowed,
                "browser": self.browser,
                "loggeds": self.loggeds,
                "onsaved": self.onsaved
            }
        except AttributeError:
            self.allowed = self.fread['allowed']
            self.browser = self.fread['browser']
            self.loggeds = self.fread['loggeds']
            self.onsaved = self.fread['onsaved']
            self.__fsave()
            return
        try:
            fjson = json.dumps( self.fread, indent=4 )
            try:
                with open( self.fname, "w" ) as fopen:
                    fopen.write( fjson )
                    fopen.close()
            except Exception as e:
                self.trouble = [ Exception, e ]
        except Exception as e:
            self.trouble = [ Exception, e ]
        
    
    def __rewr( self ):
        pass
        
    
    def save( self ) -> None:
        self.queue( "Saving configuration", self.__fsave )
        if self.trouble == None:
            self.out( "ONSaved", "Successfully update configuration." )
            self.point( "Please wait", 4 )
        else:
            self.out( self.trouble[0], self.trouble[1] )
            next = self.raw( "Try again [Y/n]", "Y" )
            if next == "Y" or next == "y":
                self.save()
        
    
    def tree( self, path: str ) -> None:
        split = path.split( "/" )
        split.pop()
        self.queue( "Create a storage directory", self.__tree, [split] )
        if self.trouble != None:
            self.out( self.trouble[0], self.trouble[1] )
            next = self.raw( "Try again [Y/n]", "Y" )
            if next == "Y" or next == "y":
                self.tree( path )
        
    
    def __tree( self, path: list ) -> None:
        mkdir = "."
        self.trouble = None
        try:
            for dir in path:
                mkdir += "/"
                mkdir += dir
                if not os.path.isdir( mkdir ):
                    os.mkdir( mkdir )
        except Exception as e:
            self.trouble = [ Exception, e ]
        
    
