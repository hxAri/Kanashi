#!/usr/bin/env python

# @author hxAri
# @create 23.05-2022
# @update 01.06-2022
# @github https://github.com/hxAri/{Kanashi}
#

from kanashi.virtual import data
from kanashi.buffer import (
    Active,
    AoE,
    Config,
    datetime,
    findall,
    json,
    Object,
    Request,
    requests,
    Session,
    sys
)

class Kanashi( Object ):
    
    # URL Default Referer.
    URLReferer = "https://www.instagram.com/"
    
    # Get Cookie for login from here.
    URLAccountsLogin = "https://www.instagram.com/accounts/login/"
    
    # Post Data login in here.
    URLAccountsLogginAjax = "https://www.instagram.com/accounts/login/ajax/"
    
    # Post 2FA Code.
    URLAccountsLogginAjax2FA = "https://www.instagram.com/accounts/login/ajax/two_factor/"
    
    # ...
    APIUserProfile = "https://i.instagram.com/api/v1/users/{}/info/"
    
    # Class initialization
    def __init__( self ):
        self.actived = None
        self.emitted = None
        self.results = None
        self.configs = Config()
        self.request = Request( self )
        pass
        
    # Main method to be executed.
    def main( self ):
        if  self.actived == None:
            if  self.configs.users.default != None:
                self.actived = self.configs.users.default
                self.main()
            else:
                users = self.configs.users.loggeds
                if  len( users ) != 0:
                    self.output( "Select", "Choose one of your accounts." )
                    for i, v in enumerate( users ):
                        print( "{}[{}] {}".format( self.spaces( 6 ), i +1, v['username'] ) )
                    sys.stdout.write( "\r\n" )
                    sys.stdout.flush()
                    opt = self.input( "int" )
                    try:
                        idx = int( opt )
                        try:
                            self.actived = Active( users[( idx -1 )] )
                            self.output( Warning, "Update account information [Y/n]" )
                            next = self.input( "next", "Y" )
                            if  next.upper() == "Y":
                                self.signinCookieHandler( 
                                    self.actived.cookies.sessionid,
                                    self.actived.cookies.csrftoken
                                )
                            else:
                                self.main()
                        except IndexError as e:
                            self.output( IndexError, [ e, "Do you want to try again [Y/n]" ], False )
                            next = self.input( "try", "Y" )
                            if  next.upper() == "Y":
                                self.main()
                            else:
                                self.output( EOFError, "exit" )
                    except ValueError as e:
                        if  opt == "n" or opt == "N":
                            self.signinMethod()
                        else:
                            self.output( ValueError, [ e, "Do you want to try again [Y/n]" ], False )
                            next = self.input( "try", "Y" )
                            if  next.upper() == "Y":
                                self.main()
                            else:
                                self.output( EOFError, "exit" )
                else:
                    self.signinMethod()
        else:
            self.actived.display()
        
    # ...
    def profileInfoHandler( self, sessionid:str = None, id:int = None ) -> dict:
        if  sessionid == None:
            sessionid = self.input( "sessionid" )
            matches = findall( r"^([0-9]{10,11})\%(.*)$", sessionid )
            if  len( matches ) > 0:
                ds_user_id = matches[0][0]
            else:
                raise ValueError( "Invalid session id" )
        try:
            if  id == None:
                self.output( None, "Use default id {} [Y/n]".format( ds_user_id ) )
                next = self.input( "try", "Y" )
                if  next.upper() == "Y":
                    id = ds_user_id
                else:
                    id = int( self.input( "userid" ) )
            cookies = { "sessionid": sessionid }
            headers = { "User-Agent": self.configs.browser.private }
            if  self.thread( "Retrieve user profile information", self.request.get, [ Kanashi.APIUserProfile.format( id ), headers, cookies ] ): pass
            if  self.emitted == None:
                results = self.results.json()
                if "status" in results:
                    match results['status']:
                        case "ok":
                            return( self.results )
                        case "fail":
                            raise RuntimeError( results['message'] )
                raise RuntimeError( "An error occurred while retrieving user data." )
            else:
                raise RuntimeError( self.emitted )
        except Exception as e:
            self.output( e, [ e, "Do you want to try again [Y/n]" ], False )
            next = self.input( "try", "Y" )
            if  next.upper() == "Y":
                return( self.profileInfoHandler( sessionid, id ) )
            else:
                return
        
    # User Login Methods.
    def signinMethod( self ) -> None:
        self.output( "Switch", "Choose a login method." )
        opts = [
            "Login With Session",
            "Login With Password",
            "Close"
        ]
        for i, v in enumerate( opts ):
            print( "{}[{}] {}".format( "\x20" * 6, i +1, v ) )
            if  i == len( opts ) -1:
                print( "" )
        try:
            match int( self.input( "int", 0 ) ):
                case 0 | 1:
                    self.signinCookieHandler()
                case 2:
                    self.signinHandler()
                case 3:
                    sys.exit()
                case _:
                    raise IndexError( "List index out of range." )
        except Exception as e:
            self.output( e, [ e, "Do you want to try again [Y/n]" ], False )
            next = self.input( "try", "Y" )
            if  next.upper() == "Y":
                self.signinMethod()
            else:
                self.main()
        
    # Get CSRFToken for login.
    def signinCSRFToken( self ) -> str:
        return( self.request.session.get( Kanashi.URLAccountsLogin ).cookies['csrftoken'] )
        
    # Handle 2FA Verification.
    def signin2FAHandler( self, username:str, results:dict, cookie:dict ) -> None:
        try:
            code = int( self.input( "int" ) )
            headers = { "X-CSRFToken": cookie['csrftoken'] }
            payload = {
                "username": username,
                "identifier": results['two_factor_info']['two_factor_identifier'],
                "verificationCode": code
            }
            if  self.thread( "Verifying your 2FA code", self.request.post, [ Kanashi.URLAccountsLogginAjax2FA, payload, headers ] ): pass
            if  self.emitted == None:
                if  "authenticated" in self.results and self.results['authenticated']:
                    print( self.request.response.firead )
                elif  "status" in self.results and "message" in self.results:
                    raise RuntimeError( self.results['message'] )
                else:
                    raise RuntimeError( "Failed to verify 2FA code." )
            else:
                raise RuntimeError( self.emitted )
        except Exception as e:
            self.output( e, [ e, "Do you want to try again [Y/n]" ], False )
            next = self.input( "try", "Y" )
            if  next.upper() == "Y":
                self.signin2FAHandler( username, results, cookie )
            else:
                self.main()
        
    # Handle Checkpoint Signin.
    def signinCheckpointHandler( self, username:str, results:dict, cookies:dict ) -> None:
        print( results )
        print( cookies )
        pass
        
    # Verifyng Checkpoint security code.
    def signinCheckpoint( self ) -> None:
        pass
        
    # Handle User Signin with cookie.
    def signinCookieHandler( self, sessionid:str = None, csrftoken:str = None ) -> None:
        try:
            if  sessionid == None:
                sessionid = self.input( "sessionid" )
            matches = findall( r"^([0-9]{10,11})\%(.*)$", sessionid )
            if  len( matches ) > 0:
                ds_user_id = matches[0][0]
            else:
                raise ValueError( "Invalid session id" )
            if  csrftoken == None:
                csrftoken = self.input( "csrftoken" )
            if  self.profileInfoHandler( sessionid, ds_user_id ):
                user = {
                    **{
                        "cookies": {
                            "csrftoken": csrftoken,
                            "sessionid": sessionid,
                            "ds_user_id": ds_user_id
                        }
                    },
                    **self.results.json()['user']
                    #**json.loads( data ).pop()['response']['user']
                }
                self.output( self, line=False, message=[
                    "Welcome to the board {}".format( user['username'] ),
                    "Do you want to remember your login data [Y/n]"
                ])
                next = self.input( "try", "Y" )
                if  next.upper() == "Y":
                    if  len( self.configs.users.loggeds ) == 0:
                        self.configs.users.loggeds = [ user ]
                    else:
                        users = self.configs.users.loggeds
                        for i, v in enumerate( users ):
                            print( type( v['cookies'] ).__name__ ); exit()
                            if  v['cookies'].ds_user_id == ds_user_id:
                                self.configs.users.loggeds[i] = user; break
                            else:
                                if  i == len( users ) -1:
                                    self.configs.users.loggeds.append( user )
                                else:
                                    pass
                    self.configs.fisave()
                self.actived = Active( user )
                self.main()
            else:
                self.main()
        except Exception as e:
            self.output( e, [ e, "Do you want to try again [Y/n]" ], False )
            next = self.input( "try", "Y" )
            if  next.upper() == "Y":
                self.signinCookieHandler()
            else:
                self.main()
        
    # ...
    def signinCookie( self ) -> None:
        pass
        
    # Handle User Signin.
    def signinHandler( self, username:str = None, userpasw:str = None ) -> None:
        if  username == None:
            username = self.input( "username" )
        if  userpasw == None:
            userpasw = self.inpas( "password" )
        try:
            headers = { "X-CSRFToken": self.signinCSRFToken() }
            payload = {
                "username": username,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), userpasw ),
                "queryParams": {},
                "optIntoOneTap": "false"
            }
            if  self.thread( "Signin your account", self.request.post, [ Kanashi.URLAccountsLogginAjax, payload, headers ] ): pass
            if  self.emitted == None:
                results = self.results.json()
                cookies = self.results.cookies.get_dict()
                if  "two_factor_required" in results and results['two_factor_required']:
                    self.output( "SignIn2FA", line=False, message=[
                        "2-Factor Authentication enabled.",
                        "Do you want to verify your account [Y/n]"
                    ])
                    next = self.input( "try", "Y" )
                    if  next.upper() == "Y":
                        return( self.signin2FAHandler( username, results, cookies ) )
                    else:
                        self.main()
                if  "checkpoint_url" in results:
                    self.signinCheckpoinHandler( username, results, cookies )
                elif  "spam" in results:
                    raise RuntimeError( "Oops! Looks like you are considered SPAM!" )
                elif  "user" in results:
                    if  results['user']:
                        if  "authenticated" and results['authenticated']:
                            print( results )
                        else:
                            raise RuntimeError( "SigninError", "Incorrect password, or may have been changed." )
                    else:
                        raise RuntimeError( "User not found, or may be missing." )
                else:
                    if  "status" in results and "message" in results:
                        self.output( Warning, [ results['message'], "Do you want to try again [Y/n]" ], False )
                        next = self.input( "try", "Y" )
                        if  next.upper() == "Y":
                            return( self.signinHandler() )
                        else:
                            self.main()
                    else:
                        raise RuntimeError( "An error occurred while signing in." )
            else:
                raise RuntimeError( self.emitted )
        except Exception as e:
            self.output( e, [ e, "Do you want to try again [Y/n]" ], False )
            next = self.input( "try", "Y" )
            if  next.upper() == "Y":
                self.signinHandler()
            else:
                self.main()
        
    