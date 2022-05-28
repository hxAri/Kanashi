
class AoEURL:
    def __init__( self ):
        self.URL = "https://www.instagram.com/{}"
        self.AccountsLogin = self.URL.format( "accounts/login/" )
        self.AccountsLoginAjax = self.URL.format( "accounts/login/ajax/" )
        self.AccountsLoginAjax2FA = self.URL.format( "accounts/login/ajax/two_factor/" )
        self.RuploadIGPhoto = self.URL.format( "rupload_igphoto/fb_uploader_{}" )
        self.CreateConfigure = self.URL.format( "create/configure" )
        self.ConfigureToStory = self.URL.format( "create/configure_to_story" )
        self.Post = self.URL.format( "p/{}" )
        pass

AoEURL = AoEURL()
