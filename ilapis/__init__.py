
import os
import sys
import json
import requests

from os import system
from time import sleep
from getpass import getpass
from datetime import datetime
from requests import Session
from threading import Thread

URL = "https://www.instagram.com/{}"
URLAccountsLogin = URL.format( "accounts/login/" )
URLAccountsLoginAjax = URL.format( "accounts/login/ajax/" )
URLAccountsLoginAjax2FA = URL.format( "accounts/login/ajax/two_factor/" )
URLRuploadIGPhoto = URL.format( "rupload_igphoto/fb_uploader_{}" )
URLCreateConfigure = URL.format( "create/configure" )
URLConfigureToStory = URL.format( "create/configure_to_story" )
URLPost = URL.format( "p/{}" )

UserAgent = "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"

traces = { "error": [] }

class AoE:
    
    def cout( self, object: str, message: str ) -> None:
        sys.stdout.write( f"SystemEjected:\n\x20\x20{object}:\n\x20\x20\x20\x20{message}\n" )
        sys.stdout.flush()
    
    def exit( self, object: str, message: str ) -> None:
        system( "clear" ); sys.exit( f"SystemEjected:\n\x20\x20{object}:\n\x20\x20\x20\x20{message}\n" )
    
    def point( self, string=None, re=False ) -> None:
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
                    print( f"\r{string} {i}", end="" )
                    sleep( 00000.1 )
        except KeyboardInterrupt:
            self.exit( "KeyboardInterrupt", "Operation aborted, system stopped." )
        
        system( "clear" )
    
    def ping( self, url=URL, timeout=5 ) -> None:
        try:
            ping = requests.get( url.format( "" ), timeout=timeout )
            ping.raise_for_status()
        except requests.exceptions.HTTPError as e:
            traces['error'].append([ "HTTPError", "Failed to check connection, status: {}".format( e.response.status_code ) ])
        except requests.exceptions.InvalidURL:
            traces['error'].append([ "InvalidURL", "The link provided is invalid." ])
        except requests.exceptions.ConnectionError:
            traces['error'].append([ "ConnectionError", "Internet connection is very bad." ])
    
    def input( self, pholder: str, password=False, IgnoreKeyboard=False ) -> str:
        try:
            if password:
                value = getpass( prompt=pholder )
            else:
                value = input( pholder )
        except EOFError:
            self.exit( "EOFError", "Input canceled by user." )
        except KeyboardInterrupt:
            if IgnoreKeyboard:
                value = self.input( pholder, password, IgnoreKeyboard )
            else:
                raise KeyboardInterrupt()
        if value == "":
            value = self.input( pholder, password, IgnoreKeyboard )
        return( value )

class Main( AoE ):
    
    def __init__( self ):
        self.session = None
        pass
    
    def onsave( self, json, cookie ):
        return( json )
    
    def facode( self, session, responseJSON, username ):
        
        _2facode = self.input( "2FACode: ", True )
        response2FA = session.post( URLAccountsLoginAjax2FA, data=
        {
            "username": username,
            "verificationCode": _2facode,
            "indentifier": responseJSON['two_factor_info']['two_factor_identifier']
        })
        
        response2FAJSON = response2FA.json()
        response2FAKuki = response2FA.cookies.get_dict()
        
        if response2FAJSON['authenticated']:
            return( session, self.onsave( response2FAJSON, response2FAKuki ) )
        else:
            print( response2FAJSON )
            exit()
    
    def signin( self ):
        print( "Please select the login option.\n" )
        print( "\x20\x20[] Login Default." )
        print( "\x20\x20[] Login Session." )
        print( "\x20\x20[] Visit Help." )
        print( "\x20\x20[] Close." )
        try:
            form = int( self.input( "\ninput: ", False, True ) )
        except ValueError:
            self.exit( "ValueError", "Input value must be type int." )
        match form:
            case 0:
                session = Session()
                session.headers.update({ "Referer": URLAccountsLogin })
                session.headers.update({ "User-Agent": UserAgent })
                session.headers.update({ "X-CSRFToken": session.get( URLAccountsLogin ).cookies['csrftoken'] })
                
                username = self.input( "username: ", False, True )
                password = self.input( "password: ", True, True )
                
                response = session.post( URLAccountsLoginAjax, data=
                {
                    "username": username,
                    "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password ),
                    "queryParams": {},
                    "optIntoOneTap": "false"
                })
                
                responseJSON = response.json()
                responseKuki = response.cookies.get_dict()
                
                try:
                    if "user" in responseJSON:
                        if "two_factor_required" in responseJSON and responseJSON['two_factor_required']:
                            next = self.input( "Do\x20you\x20want\x20to\x20verify\x20your\x20account\x20[Y/n]\x20", False, True )
                            if next == "Y":
                                return( self.facode( session, responseJSON, username ) )
                            elif next == "n":
                                self.exit( "SigninError", "Login\x20canceled\x20by\x20user." )
                            else:
                                self.exit( "SigninError", "Operation\x20aborted,\x20system\x20stopped." )
                        else:
                            if "authenticated" in responseJSON and responseJSON['authenticated']:
                                return( session, self.onsave( responseJSON, responseKuki ) )
                            else:
                                self.exit( "SigninError", "Incorrect\x20password,\x20or\x20may\x20have\x20been\x20changed." )
                    else:
                        self.exit( "SigninError", "An\x20error\x20occurred\x20while\x20signing\x20in." )
                except KeyError as e:
                    self.exit( "KeyError", e )
                
            case 1:
                print( "Session" )
            case 2:
                print( "Visit" )
            case 3:
                self.exit( "InputUser", "Program finished!" )
            case _:
                self.exit( "InputUser", f"Invalid value for input {form}" )
    
    def main( self ) -> None:
        self.queue( "Please wait...", self.ping )
        try:
            if len( traces['error'] ) == 0:
                try:
                    onsaved = open( "logged.in", "r" ).read()
                except( IOError, KeyError ):
                    onsaved = self.signin()
                if type( onsaved ).__name__ != "dict":
                    try:
                        onsaved = json.loads( onsaved )
                    except json.decoder.JSONDecodeError as e:
                        self.exit( "JSONDecodeError", e )
                print( onsaved )
            else:
                for i in traces['error']:
                    self.cout( i[0], i[1] )
        except EOFError as e:
            self.exit( "EOFError", e )
        except NameError as e:
            self.exit( "NameError", e )
        except TypeError as e:
            self.exit( "TypeError", e )
        except KeyboardInterrupt:
            self.exit( "KeyboardInterrupt", "Operation aborted, system stopped." )
    
