
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib

try:
    import requests
    import mechanize
except ImportError:
    sys.exit( "ImportError: Module Mechanize & Requests required!" )

from time import sleep

from requests.exceptions import InvalidURL
from requests.exceptions import ConnectionError

from mechanize import Browser
from mechanize._http import HTTPRefreshProcessor

class Animate:
    def __init__( self ):
        os.system( "clear" )
        pass
    
    def reset( self ):
        print( "\033[0m\n" )
    
    def point( self, string=None ):
        points = [ ".", ".", ".", "." ]
        
        if string != None:
            self.write( "\r{}".format( string ), False )
        
        for point in points:
            sys.stdout.write( point );
            sys.stdout.flush()
            
            time.sleep( 1 )
        
        self.reset()
    
    def write( self, string, reset=True ):
        for e in string:
            sys.stdout.write( e )
            sys.stdout.flush()
            
            time.sleep( 00000.1 )
        if reset:
            self.reset()
    
    def thread( self ):
        pass

class Results:
    def __init__( self ):
        self.myToken = False
        self.account = []
        self.success = []
        self.threads = []
        self.chpoint = []
        self.faileds = []
        pass

class Intafesu:
    def __init__( self ):
        self.animate = Animate()
        self.results = Results()
        self.browser = Browser()
        self.browser.set_handle_robots( False )
        self.browser.set_handle_refresh( HTTPRefreshProcessor(), max_time=1 )
        self.browser.set_header( "User-Agent", "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36" )
        pass
    
    def input( self, placeholder, interrupt=True ):
        try:
            form = input( placeholder )
        except KeyboardInterrupt:
            if interrupt:
                print( "KeyboardInterrupt: Input canceled." )
                print( "KeyboardInterrupt: System ejected." )
                exit()
            else:
                form = self.input( placeholder )
        return( form )
    
    def main( self ):
        if self.results.myToken:
            print( "Menu" )
        else:
            print( self.input( "User: " ) )
