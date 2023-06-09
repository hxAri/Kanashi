
![Kanashi · Logo](https://raw.githubusercontent.com/hxAri/hxAri/main/public/images/1654820424;51ydWrxRcv.png)

Please note that this is not fully finished or not ready to use, if you are interested in using it please I don't require you to wait for this to finish because I am also busy.

## Abouts
Kanashi is an open source project that can be used to login to real Instagram accounts via Linux Terminal and Android Termux, this also includes taking CSRF Tokens and Login Session IDs, besides that you can use Tokens and IDs to do various things like Instagram Web.

## Install
```sh
git clone https://github.com/hxAri/Kanashi && cd Kanashi && pip install -r requirements.txt
```
## Install with PIP
*Not available for PIP at this time.*
## Install as Module
```sh
git clone https://github.com/hxAri/Kanashi && cd Kanashi && python setup* install
```

## Requires
* Python **>=3.10.4**
* [Requests](https://github.com/psf/requests) **>=2.28.1**

## Features
I did not expect this ^_*

##### Get User Info
Display user profiles such as how many followers and following they have, number of edges e.g posts, reels, etc., find out whether the account owner has blocked your account or not and vice versa, and much more.

##### Get User Posts
Onworking

##### Get User Story
Onworking

##### Get User Reels
Onworking

##### Get User Followers
Onworking

##### Get User Following
Onworking

##### Fetch Timeline Posts
Incoming/ Deprecated

##### Fetch Suggested Users
Incoming/ Deprecated

##### Downloader
Download media from Instagram users i.g Posts, Reels, Stories, Highlights, Profile Photos, and etc.

##### Block Account
Block or unblock instagram account.

##### Follow Account
Follow or unfollow instagram account.

##### Restrict Account
Onworking

##### Favorite Account
Onworking

##### Report Account
Onworking

##### Login with Password
Login as usual using credentials such as your username and password.

##### Login with Cookie
If you are afraid that your account will be suspended from Instagram because logging in from a third party is a fairly safe way because you don't need to enter your credentials, just paste your Instagram login cookie.

If you are an Android user, please use Kiwi Browser to get your Instagram login cookies.
Please login as usual, after successfully logging in please open the **Deloper Tools** menu and select **Console** then run the JavaScript code below to copy your Instagram login cookie:
```js
navigator.clipboard.writeText( document.cookie );
```

##### Login 2FA Verification
This feature is under development, it is highly recommended not to log in with an account that has two factor security.

##### Login Checkpoint Handle
Incoming

##### Login Multiple Account
You can be the same as Instagram in general which has more than one account, now Kanashi supports it.

##### Login Save Info
Save your login information in a configuration file for future use.

##### Logout
Incoming

## Examples

## Simple Usage
```sh
cd Kanashi && chmod +x main && ./main
```

## Usage as Module
```py
# This is a simple class usage,
# you can extend Kanashi class or not

# Import the required modules
from kanashi import Kanashi, Object

# You can expand or not
class Example( Kanashi ):
    
    @property
    def getUserActive( self ) -> Object | None:
        """ Get current user active """
        return( self.active )
        
    @property
    def getUserActiveFromConfig( self ) -> str | False:
        """ Get current user default login """
        return( self.settings.signin.active )
    

# Create new Instance
example = Example()
example.getUserActive
example.getUserActiveFromConfig
```

## Trying to Login
```py
# Import the required modules
from kanashi import (
    Error,
    Kanashi, 
    SignInError, 
    SignInSuccess, 
    SignInCheckpoint, 
    SignIn2FARequired
)

# Create new Instance.
app = Kanashi()
username = "USERNAME"
password = "PASSWORD"

try:
    login = app.signin.password( username, password )
    if isinstance( login, SignInSuccess ):
        print( f"You are logged as {login.username} ({login.id})" )
    elif isinstance( login, SignInCheckpoint ):
        print( "Your account has ben Checkpoint" )
    elif isinstance( login, SignIn2FARequired ):
        print( "Your account require to verify 2FA" )
    else:
        raise SignInError( "Something wrong!" )
except SignInError as e:
    print( e )
```

## Classes
| From | Class | Context | Extends |
| ------------- |:-------------|:-------------|:-------------|
| kanashi | Main | True | kanashi.cli.Cli |
| kanashi.cli | Cli | True | kanashi.kanashi.Kanashi, kanashi.utils.util.Util |
| kanashi.config | Config | True | kanashi.context.Context |
| kanashi.context | Context | False | None |
| kanashi.endpoint.auth | AuthError | False | kanashi.error.Error |
| kanashi.endpoint.block | Block | True | kanashi.request.RequestRequired |
| kanashi.endpoint.favorite | Favorite | True | kanashi.request.RequestRequired |
| kanashi.endpoint.follow | Follow | True | kanashi.request.RequestRequired |
| kanashi.endpoint.profile | Profile | True | kanashi.context.Context |
| kanashi.endpoint.restrict | Restrict | True | kanashi.request.RequestRequired |
| kanashi.endpoint.signin | SignIn | True | kanashi.request.RequestRequired |
| kanashi.endpoint.user | User | True | kanashi.request.RequestRequired |
| kanashi.error | Alert | False | kanashi.error.Throwable, Warning |
| kanashi.error | Error | False | kanashi.error.Throwable, TypeError |
| kanashi.error | Throwable | False | Exception |
| kanashi.kanashi | Kanashi | True|False | kanashi.context.Context |
| kanashi.object | Object | False | None |
| kanashi.request | Request | True | kanashi.context.Context |
| kanashi.request | RequestRequired | True | kanashi.context.Context |
| kanashi.update | Update | True | kanashi.request.RequestRequired |
| kanashi.utils.cookie | Cookie | False | None |
| kanashi.utils.file | File | False | kanashi.utils.path.Path |
| kanashi.utils.json | JSON | False | None |
| kanashi.utils.json | JSONError | False | json.JSONDecodeError |
| kanashi.utils.path | Path | False | None |
| kanashi.utils.string | Binary | False | None |
| kanashi.utils.string | String | False | kanashi.utils.string.Binary |
| kanashi.utils.thread | Thread | False | threading.Thread |
| kanashi.utils.util | Util | False | None |

## Donate
Give spirit to the developer, no matter how many donations given will still be accepted<br/>
[paypal.me/hxAri](https://paypal.me/hxAri)

## Licence
All Kanashi source code is licensed under the GNU General Public License v3. Please [see](https://www.gnu.org/licenses) the original document for more details.

## Disclaimer
Kanashi is not affiliated with or endorsed, endorsed at all by Instagram or any other party, if you use the main account to use this tool we as Coders and Developers are not responsible for anything that happens to that account, use it at your own risk, and this is Strictly not for SPAM.
