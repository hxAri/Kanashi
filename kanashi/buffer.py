
from .aoe import *
from .target import URL

class Buffer( AoE ):
    """
    
    """
    def __init__( self, context ):
        self.context = context
        self.results = None
        self.trouble = None
        pass
        
    
    def shared( self, active = None ) -> None:
        self.clear()
        if  active == None:
            active = { "cookies": {} }
            active['cookies']['csrftoken'] = self.raw( "CSRFToken" )
            active['cookies']['sessionid'] = self.raw( "SessionID" )
            results = findall( r"^([0-9]{11})", active['cookies']['sessionid'] )
            if len( results ) > 0:
                active['cookies']['ds_user_id'] = self.raw( "ID [{}]".format( results[0] ), default = results[0] )
                active['cookies']['rur'] = self.raw( "RUR [PRN]", default = "PRN" )
            else:
                self.out( "SharedDataSessionIDError", [ "Oops! Looks like you entered", "The wrong session id." ] )
                self.raw( "Back", "*", 4 )
                self.shared()
                return
        self.queue( "Currently reapplying the user", self.__shared, [ active ] )
        if self.trouble == None:
            shared = self.results
            if "config" in shared:
                config = shared['config']
                if  config['viewer'] != None:
                    active['dshared'] = config['viewer']
                    if "password" not in active:
                        active['password'] = None
                    self.context.active = {
                        "cookies": active['cookies'],
                        "dshared": active['dshared'],
                        "username": active['dshared']['username'],
                        "password": active['password']
                    }
                    for i in range( len( self.context.config.loggeds ) ):
                        if  self.context.config.loggeds[i]['username'] == self.context.active['username']:
                            self.context.config.loggeds[i] = self.context.active
                            self.context.change = True
                    if  self.context.change != True:
                        self.context.config.loggeds.append( self.context.active )
                    self.context.change = False
                    self.context.config.save()
                    self.context.main()
                else:
                    self.out( "SharedDataCookieError", "Oops! Looks like your login session has ended." )
                    next = self.raw( "Try again [Y/n]", "y", 4 )
                    if next == "Y" or next == "y":
                        self.shared()
                    else:
                        self.context.main()
            else:
                self.out( "SharedDataError", "There was an error while retrieving data." )
                next = self.raw( "Try again [Y/n]", "y", 4 )
                if next == "Y" or next == "y":
                    self.shared( active )
                else:
                    self.context.main()
        else:
            self.exit( self.trouble[0], self.trouble[1] )
            next = self.raw( "Try again [Y/n]", "y" )
            if next == "Y" or next == "y":
                self.shared( active )
            else:
                self.context.main()
        
    
    def __shared( self, active ) -> None:
        self.results = None
        self.trouble = None
        try:
            self.results = self.context.target.session.get( URL.SharedData, cookies=active['cookies'] ).json()
        except KeyError as e:
            self.trouble = [ KeyError, "Failed to retrieve shared data, index cookies error." ]
        except requests.exceptions.HTTPError as e:
            self.trouble = [ "HTTPError", "Failed to check connection, status: {}".format( e.response.status_code ) ]
        except requests.exceptions.InvalidURL:
            self.trouble = [ "InvalidURL", "The link provided is invalid." ]
        except requests.exceptions.ConnectionError:
            self.trouble = [ "ConnectionError", "Internet connection is very bad." ]
        
    
