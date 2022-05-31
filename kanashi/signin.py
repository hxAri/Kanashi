
from .aoe import *
from .target import URL

class Signin( AoE ):
    """
    
    """
    def __init__( self, context ):
        self.context = context
        self.results = None
        self.trouble = None
        pass
        
    
    def signin( self, username: str = None, password: str = None ) -> None:
        self.clear()
        if  username == None:
            username = self.raw( "Username" )
        if  password == None:
            password = self.passw( "Password" )
        self.queue( "Signin your account", self.__signin, [ username, password ] )
        if self.trouble == None:
            rjson = self.results.json()
            rkuki = self.results.cookies.get_dict()
            try:
                if "two_factor_required" in rjson and rjson['two_factor_required']:
                    next = self.raw( "Do you want to verify your account [Y/n]", "y", 4 )
                    if next == "Y" or next == "y":
                        self.facode( username, rjson, rkuki )
                    else:
                        self.context.main()
                else:
                    if "spam" in rjson and rjson['spam']:
                        self.out( "SigninError", "Oops! Looks like you are considered SPAM!" )
                        self.point( "Redirect", 4 )
                        self.context.main()
                    else:
                        if "user" in rjson:
                            if rjson['user']:
                                if "authenticated" in rjson and rjson['authenticated']:
                                    self.context.buffer.shared({
                                        "cookies": rkuki,
                                        "dshared": None,
                                        "username": username,
                                        "password": password
                                    })
                                else:
                                    self.out( "SigninError", "Incorrect password, or may have been changed." )
                                    self.point( "Redirect", 4 )
                                    self.signin( username )
                            else:
                                self.out( "SigninError", "User not found, or may be missing." )
                                self.point( "Redirect", 4 )
                                self.signin()
                        else:
                            if "status" in rjson and rjson['status'] == "fail" and rjson['message'] != "":
                                self.out( "SigninError", rjson['message'] )
                                next = self.raw( "Try again [Y/n]", "y", 4 )
                                if next == "Y" or next == "y":
                                    self.signin( username, password )
                                else:
                                    self.context.main()
                            else:
                                self.out( "SigninError", "An error occurred while signing in." )
                                next = self.raw( "Try again [Y/n]", "y", 4 )
                                if next == "Y" or next == "y":
                                    self.signin( username, password )
                                else:
                                    self.context.main()
            except KeyError as e:
                self.exit( "KeyError", e )
        else:
            self.out( self.trouble[0], self.trouble[1] )
            next = self.raw( "Try again [Y/n]", "y", 4 )
            if next == "Y" or next == "y":
                self.signin( username, password )
            else:
                self.context.main()
        
    
    def __signin( self, username, password ) -> None:
        self.results = None
        self.trouble = None
        try:
            self.context.target.session.headers.update({ "X-CSRFToken": self.context.target.session.get( URL.AccountsLogin ).cookies['csrftoken'] })
            self.results = self.context.target.session.post( URL.AccountsLoginAjax, data=
            {
                "username": username,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format( int( datetime.now().timestamp() ), password ),
                "queryParams": {},
                "optIntoOneTap": "false"
            })
        except KeyError as e:
            self.trouble = [ KeyError, "Failed to retrieve shared data, index cookies error." ]
        except requests.exceptions.HTTPError as e:
            self.trouble = [ "HTTPError", "Failed to check connection, status: {}".format( e.response.status_code ) ]
        except requests.exceptions.InvalidURL:
            self.trouble = [ "InvalidURL", "The link provided is invalid." ]
        except requests.exceptions.ConnectionError:
            self.trouble = [ "ConnectionError", "Internet connection is very bad." ]
    
