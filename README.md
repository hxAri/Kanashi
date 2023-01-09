
![Kanashi · Logo](https://raw.githubusercontent.com/hxAri/hxAri/main/assets/images/1654820424;51ydWrxRcv.png)

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
* Get User Info
* Get User Posts (Incoming)
* Get User Story (Incoming)
* Get User Reels (Incoming)
* Get User Followers (Incoming)
* Get User Following (Incoming)
* Fetch Timeline Posts (Incoming)
* Fetch Suggested Users (Incoming)
* Downloader
* Follow Account (Incoming)
* Unfollow Account (Incoming)
* Login with Password
* Login with Sessionid (Incoming)
* Login 2FA Verification (Bug)
* Login Checkpoint Handle (Incoming)
* Login Multiple Account
* Login Save Info
* Logout (Incoming)

## Examples

## Simple Usage
```sh
cd Kanashi && chmod +x main && ./main
```

## Simple Usage as Module
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
