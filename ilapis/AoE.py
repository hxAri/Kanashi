#!/usr/bin/env python3

# 
# @author hxAri
# @create -
# @update 25.05-2022
# @github https://github.com/hxAri
# @upload https://github.com/hxAri/ILAPIs
# 

import os
import sys
import json
import requests

from os import system
from re import findall
from time import sleep
from getpass import getpass
from datetime import datetime
from requests import Session
from threading import Thread

# Various lists of Page URLs to perform actions.
URL = "https://www.instagram.com/{}"
URLAccountsLogin = URL.format( "accounts/login/" )
URLAccountsLoginAjax = URL.format( "accounts/login/ajax/" )
URLAccountsLoginAjax2FA = URL.format( "accounts/login/ajax/two_factor/" )
URLRuploadIGPhoto = URL.format( "rupload_igphoto/fb_uploader_{}" )
URLCreateConfigure = URL.format( "create/configure" )
URLConfigureToStory = URL.format( "create/configure_to_story" )
URLPost = URL.format( "p/{}" )

# User agent browser to create session.
UserAgent = "Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"

# A place to store active user data.
FSessionIn = "session.in"

# Uncaught exception stack trace.
traces = { "error": [] }

def color( string: str ) -> str:
    for code in findall( r"e\[([1|0])\;([1-9\;]+)m", string ):
        string = string.replace(
            "e[{};{}m".format( code[0], code[1] ),
            "\033[{};{}m".format( code[0], code[1] )
        )
    return( string )

class AoE:
    
    def __init__( self ):
        self.onsaved = None
        self.session = None
        pass
    
    def cout( self, object: str, message: str ) -> None:
        sys.stdout.write( color( f"e[1;33mSystemOutpute[1;34m:\n\x20\x20e[1;32m{object}e[1;34m:\n\x20\x20\x20\x20e[1;37m{message}\n" ) )
        sys.stdout.flush()
    
    def exit( self, object: str, message: str ) -> None:
        system( "clear" ); sys.exit( color( f"e[1;33mSystemEjectede[1;34m:\n\x20\x20e[1;32m{object}e[1;34m:\n\x20\x20\x20\x20e[1;37m{message}\n" ) )
    
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
            traces['error'].append([ "HTTPError", "Failed\x20to\x20check\x20connection,\x20status:\x20{}\n".format( e.response.status_code ) ])
        except requests.exceptions.InvalidURL:
            traces['error'].append([ "InvalidURL", "The\x20link\x20provided\x20is\x20invalid.\n" ])
        except requests.exceptions.ConnectionError:
            traces['error'].append([ "ConnectionError", "Internet\x20connection\x20is\x20very\x20bad.\n" ])
    
    def input( self, pholder: str, password=False, IgnoreKeyboard=False ) -> str:
        try:
            if password:
                value = getpass( prompt=color( pholder ) )
            else:
                value = input( color( pholder ) )
        except EOFError:
            self.exit( "EOFError", "Input\x20canceled\x20by\x20user." )
        except KeyboardInterrupt:
            if IgnoreKeyboard:
                value = self.input( pholder, password, IgnoreKeyboard )
            else:
                raise KeyboardInterrupt()
        if value == "":
            value = self.input( pholder, password, IgnoreKeyboard )
        return( value )
    
    def onsave( self, cookie, username ):
        try:
            with open( FSessionIn ) as fopen:
                onsaved = fopen.read()
                fopen.close()
            if  onsaved != "":
                onsaved = json.loads( onsaved )
            else:
                raise IOError
        except( IOError, json.decoder.JSONDecodeError ):
            onsaved = {}
        try:
            onsaved[username] = {
                "csrftoken": cookie['csrftoken'],
                "sessionid": cookie['sessionid']
            }
            with open( FSessionIn, "w" ) as fopen:
                 fopen.write( json.dumps( onsaved ) )
                 fopen.close()
        except IOError as e:
            self.exit( "ONSaveError", e )
        except KeyError as e:
            self.exit( "ONSaveError", e )
        
        return( onsaved )
    
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
        
        if "authenticated" in response2FAJSON:
            if response2FAJSON['authenticated']:
                return( self.onsave( response2FAKuki, username ) )
            else:
                self.cout( "Signin2FAError", "The\x20verification\x20code\x20provided\x20is\x20invalid." )
                next = self.input( "Want\x20to\x20try\x20to\x20verify\x20the\x20code\x20again\x20[Y/n] ", False, True )
                if next == "Y":
                    return( self.facode( session, responseJSON, username ) )
                elif next == "n":
                    self.exit( "Signin2FAError", "Verification\x20canceled\x20by\x20user." )
                else:
                    self.exit( "Signin2FAError", "Operation\x20aborted,\x20system\x20stopped." )
        else:
            self.cout( "Signin2FAError", "An\x20error\x20occurred\x20while\x20verifying\x20the\x20code." )
            next = self.input( "Want\x20to\x20try\x20to\x20verify\x20the\x20code\x20again\x20[Y/n] ", False, True )
            if next == "Y":
                return( self.facode( responseJSON, username ) )
            elif next == "n":
                self.exit( "Signin2FAError", "Verification\x20canceled\x20by\x20user." )
            else:
                self.exit( "Signin2FAError", "Operation\x20aborted,\x20system\x20stopped." )
    
    def signin( self, session ):
        try:
            session.headers.update({ "X-CSRFToken": session.get( URLAccountsLogin ).cookies['csrftoken'] })
        except KeyError:
            self.exit( "SigninError", "Oops!\x20Looks\x20like\x20you\x20are\x20considered\x20SPAM!" )
        
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
                if responseJSON['user']:
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
                            return( self.onsave( responseKuki, username ) )
                        else:
                            self.exit( "SigninError", "Incorrect\x20password,\x20or\x20may\x20have\x20been\x20changed." )
                else:
                    self.exit( "SigninError", "User\x20not\x20found,\x20or\x20may\x20be\x20missing." )
            else:
                if "spam" in responseJSON:
                    if responseJSON['spam']:
                        self.exit( "SigninError", "Oops!\x20Looks\x20like\x20you\x20are\x20considered\x20SPAM!" )
                self.exit( "SigninError", "An\x20error\x20occurred\x20while\x20signing\x20in." )
        except KeyError as e:
            self.exit( "KeyError", e )


class Main( AoE ):
    
    def main( self ) -> None:
        self.queue( "e[1;37mPlease\x20wait...", self.ping )
        try:
            if len( traces['error'] ) == 0:
                session = Session()
                session.headers.update({ "Referer": URLAccountsLogin })
                session.headers.update({ "User-Agent": UserAgent })
                try:
                    with open( FSessionIn, "r" ) as fopen:
                        onsaved = fopen.read()
                        fopen.close()
                    if  onsaved != "":
                        onsaved = json.loads( onsaved )
                    else:
                        raise IOError
                except( IOError, KeyError ):
                    print( color( "e[1;37mPlease\x20select\x20the\x20login\x20option.\n" ) )
                    print( color( "\x20\x20e[1;38;5;214m[]\x20e[1;37mLogin\x20Default." ) )
                    print( color( "\x20\x20e[1;38;5;214m[]\x20e[1;37mLogin\x20Session." ) )
                    print( color( "\x20\x20e[1;38;5;214m[]\x20e[1;37mVisit\x20Help." ) )
                    print( color( "\x20\x20e[1;38;5;214m[]\x20e[1;37mClose." ) )
                    try:
                        form = int( self.input( "\ninput: ", False, True ) )
                    except ValueError:
                        self.exit( "ValueError", "Input\x20value\x20must\x20be\x20type\x20int." )
                    match form:
                        case 0:
                            onsaved = self.signin( session )
                        case 1:
                            print( "Session" )
                        case 2:
                            print( "Visit" )
                        case 3:
                            self.exit( "InputUser", "Program\x20finished!" )
                        case _:
                            self.exit( "InputUser", f"Invalid\x20value\x20for\x20input\x20{form}" )
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
            self.exit( "KeyboardInterrupt", "Operation\x20aborted,\x20system\x20stopped." )
        
    
if __name__ == "__main__":
    main = Main()
    main.main()
