
import os
import sys
import json
import requests

from os import system
from re import findall
from time import sleep
from random import choice
from getpass import getpass
from datetime import datetime
from requests import Session
from threading import Thread

def color( string: str ) -> str:
    for code in findall( r"e\[([1|0])\;([1-9\;]+)m", string ):
        string = string.replace(
            "e[{};{}m".format( code[0], code[1] ),
            "\033[{};{}m".format( code[0], code[1] )
        )
    return( "{}\033[0m".format( string ) )

class AoE:
    
    def __init__( self ):
        self.FNSetting = "ilapis/settings.txt"
        self.StackTrace = []
        self.UserActive = {}
        try:
            with open( self.FNSetting, "rb" ) as FOSetting:
                FRSetting = FOSetting.read()
                FOSetting.close()
            if  FRSetting != None and FRSetting != "":
                try:
                    FRSetting = json.loads( FRSetting )
                except json.decoder.JSONDecodeError as e:
                    self.exit( "JSONDecodeError", e )
                self.FSSetting = FRSetting
            else:
                self.exit( "SettingError", "The\x20configuration\x20file\x20has\x20been\x20corrupted!" )
        except ValueError as e:
            self.exit( "ValueError", e )
        except FileNotFoundError as e:
            self.exit( "FileNotFoundError", e )
        pass
    
    def cout( self, object: str, message: str ) -> None:
        sys.stdout.write( color( "e[1;33mSysteme[1;31m.e[1;33moute[1;34m:\n\x20\x20e[1;32m{}{}e[1;34m:\n\x20\x20\x20\x20e[1;37m{}\n".format( type( self ).__name__, object, message ) ) )
        sys.stdout.flush()
    
    def exit( self, object: str, message: str ) -> None:
        #system( "clear" );
        sys.exit( color( "e[1;33mSysteme[1;31m.e[1;33mexite[1;34m:\n\x20\x20e[1;32m{}{}e[1;34m:\n\x20\x20\x20\x20e[1;37m{}\n".format( type( self ).__name__, object, message ) ) )
    
    def point( self, string: str = None, re: bool = False ) -> None:
        points = [ ".", ".", ".", "." ]
        if string != None:
            self.write( "\r{}".format( string ), False )
        for point in points:
            sys.stdout.write( point );
            sys.stdout.flush()
            sleep( 00000.5 )
        if re:
            system( "clear" )
    
    def write( self, string: str, re=False ) -> None:
        for e in string:
            sys.stdout.write( e )
            sys.stdout.flush()
            
            sleep( 00000.1 )
        
        if re:
            system( "clear" )
    
    def queue( self, string: str, object, params=None ) -> None:
        if params != None:
            work = Thread( target=object, args=(params,) )
        else:
            work = Thread( target=object )
        
        work.start()
        
        try:
            while work.is_alive():
                for i in "-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-":
                    print( color( f"\r{string}\x20e[1;33m{i}" ), end="" )
                    sleep( 00000.1 )
        except KeyboardInterrupt:
            self.exit( "KeyboardInterrupt", "Operation\x20aborted,\x20system\x20stopped." )
        
        system( "clear" )
    
    def ping( self, url="https://www.google.com/", timeout=5 ) -> None:
        try:
            ping = requests.get( url.format( "" ), timeout=timeout )
            ping.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.StackTrace.append([ "HTTPError", "Failed\x20to\x20check\x20connection,\x20status:\x20{}\n".format( e.response.status_code ) ])
        except requests.exceptions.InvalidURL:
            self.StackTrace.append([ "InvalidURL", "The\x20link\x20provided\x20is\x20invalid.\n" ])
        except requests.exceptions.ConnectionError:
            self.StackTrace.append([ "ConnectionError", "Internet\x20connection\x20is\x20very\x20bad.\n" ])
    
    def input( self, pholder: str, password=False, IgnoreKeyboard=False ) -> str:
        try:
            if  password:
                value = getpass( prompt=color( f"{pholder} " ) )
            else:
                value = input( color( f"{pholder} " ) )
        except EOFError:
            self.exit( "EOFError", "Input\x20canceled\x20by\x20user." )
        except KeyboardInterrupt:
            if  IgnoreKeyboard:
                value = self.input( pholder, password, IgnoreKeyboard )
            else:
                raise KeyboardInterrupt
        if  value.replace( " ", "" ) == "":
            value = self.input( pholder, password, IgnoreKeyboard )
        
        return( value )
    
    def onsave( self ) -> None:
        try:
            with open( self.FNSetting, "wb" ) as FOSetting:
                FOSetting.write( json.parse( self.FSSetting, indent=4 ) )
                FOSetting.close()
        except:
            print( "" )
    
    def izin( self, image: bool = False, login: bool = False ) -> bool:
        try:
            if  image:
                return( self.FSSetting['permission']['save_image'] )
            if  login:
                return( self.FSSetting['permission']['save_login'] )
        except KeyError as e:
            self.exit( "KeyError", e )
        except AttributeError as e:
            self.exit( "AttributeError", e )
        
        return( False )
    
    def path( self, path: str = None ) -> str:
        if  path != None:
            self.FSSetting['onsaved'] = path
            self.onsave()
        
        return( self.FSSetting['onsaved'] )
    
    def user( self, onsaved: dict = None, default: bool = False, delete: str = None ) -> dict:
        try:
            if  onsaved != None:
                onsaved = {
                    "headers": {
                        "User-Agent": onsaved['user-agent'],
                        "X-CSRFToken": onsaved['x-csrftoken']
                    },
                    "response": onsaved['response'],
                    "username": onsaved['username'],
                    "password": onsaved['password']
                }
                if  default:
                    self.FSSetting['users']['default'] = onsaved
                    self.FSSetting['users']['onsaved'].append( onsaved )
                else:
                    self.FSSetting['users']['onsaved'].append( onsaved )
                
                self.onsave()
                
            if  delete != None:
                userls = self.FSSetting['users']['onsaved']
                for i in range( len( userls ) ):
                    if userls['username'] == delete:
                        del self.FSSetting['users']['onsaved'][i]; self.onsave()
                
            return( self.FSSetting['users']['onsaved'] )
            
        except KeyError as e:
            self.exit( "KeyError", e )
        except AttributeError as e:
            self.exit( "AttributeError", e )
    
    def browser( self, default = None ) -> str:
        try:
            match type( default ).__name__:
                case "str":
                    self.FSSetting['browser']['default'] = default
                    self.onsave()
                case "bool":
                    default = self.FSSetting['browser']['default']
                case "NoneType":
                    default = choice( self.FSSetting['browser']['randoms'] )
            
            return( default )
            
        except KeyError as e:
            self.exit( "KeyError", e )
        except AttributeError as e:
            self.exit( "AttributeError", e )
    
