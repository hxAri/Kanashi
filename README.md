
![Kanashī · Logo](https://raw.githubusercontent.com/hxAri/hxAri/main/public/images/1654820424;51ydWrxRcv.png)

Please note that this is not fully finished or not ready to use, if you are interested in using it please I don't require you to wait for this to finish because I am also busy.

## Abouts
Kanashī is an open source project that can be used to login to real Instagram accounts via Linux Terminal and Android Termux, this also includes taking CSRF Tokens and Login Session IDs, besides that you can use Tokens and ID to do various things like Instagram Web.

## History
Kanashī itself is a translation of the word from Japan which means Sadness, I built this program for the sadness that I have experienced so far, if you are wondering why that is? Don't ask! Just use this program if you are interested, no need to think about anyone's sadness or even me.

## Features
* Login with Password and Cookies
* Login Two Factor Authentication **Bug**
* Login Multiple Accounts
* Switch Accounts
* Download Instagram Media
* Extract Profile Info
* Block or Unblock User
* Follow or Unfollow User
* Bestie or Unbestie User **Bug**
* Favorite or Unfavorite User
* Restrict or Unrestrict User
* Mute Posts or Story User
* Report User **Deprecated**
* Profile Follows Info
* Settings Configuration
* Interactive CLI

## Requirements
* Python **>=3.10.4**
* [Requests](https://github.com/psf/requests) **>=2.28.1**

## Installation
Installing Kanashī is very easy, please clone or download this repository archive
```sh
git clone https://github.com/hxAri/Kanashi
```
If you want to install it as a module you can too, but right now Kanashī is not a complete version or perfectly finished so you can't install it from **PIP**, simply run the command below Kanashī will be installed as a python module which you can import
```sh
cd Kanashi && python3 setup.py install
```

## Interactive CLI
```sh
cd Kanashi && chmod +x main && ./main
```

## Example Usages
```py
from random import choice
from kanashi import Kanashi

engine = Kanashi()
engine.headers.update({
    
    # If you want to use the browser randomly.
    "User-Agent": choice( engine.settings.browser.randoms ),
    
    # The default browser will be applied automatically.
    "User-Agent": engine.settings.browser.default
})

# Credentials
username = "USERNAME"
password = "PASSWORD"

try:
    signin = engine.signin( username, password )
    if signin.success:
        print( signin.result )
    elif singin.two_factor:
        print( signin.two_factor )
    elif signin.checkpoint:
        print( signin.checkpoint )
    else:
        print( "Something wrong" )
except Exception as e:
    print( e )
```

#### Get CSRFToken
To take csrftoken is very easy.
```py
from kanashi import Client
from kanashi import CsrftokenError
from kanashi import Request

# Initialize Request Instance.
request = Request()

# Initialize Client Instance.
client = Client( request=request )

try:
    
    # The csrftoken method uses the property decoration
    # so you only need to type it, don't call it as method.
    print( client.csrftoken )
    
except CsrftokenError as e:
    print( e )
```

#### Get Profile Info
Retrieving user profile information is also very easy, to retrieve information the client must log in first.
```py
from kanashi import Kanashi

# Initialize Kanashi Instance.
engine = Kanashi()

# Login logic here.
# ...

try:
    
    # You can also retrieve the
    # client instance from Kanashi.
    client = engine.client
    
    # Trying to get profile info.
    profile = client.profile( username="USERNAME" )
    
    # Print profile info.
    print( profile.blockedByViewer )
    print( profile.hasBlockedViewer )
    print( profile.requestedByViewer )
    print( profile.followedByViewer )
    
    # Bestie/ unbestie user.
    profile.bestie()
    
    # Block/ unblock user.
    profile.block()
    
    # Favorite/ unfavorite user.
    profile.favorite()
    
    # Follow/ unfollow/ cancel request follow user.
    profile.follow()
    
    # Restrict/ unrestrict user.
    profile.restrict()
    
except Exception as e:
    
    #
    # For the record, if the user is found but
    # the data is not available, it will raise
    # kanashi.error.UserError( "Target \"{id|username}\" user found but user data not available" )
    #
    # This is purely not Kanashī's fault, this
    # happened because the account owner
    # deactivated his account.
    #
    print( e )
```

#### Request History
Please note that Kanashī stores all successful request results and stores all request logs in the `history` property and also writes them to the `~/response.json` file, you can use each request log for further analysis if you need it and make sure your directory allows it Kanashī to write the file.
```py
from kanashi import Request

# Initialize Request Instance
request = Request()

# Print request response.
# Return: Response|None
print( request.response )

# Print previous request.
# Return: Response|None
print( request.previous )

# Print previous request by time.
# This is supported unit time e.g s|m|h|w|M|y
# For example we use 5 minutes ago.
# Return: list<Response>
print( request.previously( "5m" ) )

# Print all histories.
# Return: list<Response>
print( request.history )

# Reset or remove all request histories.
# This is also include in `history|response|previous` property.
request.clean()
```

## Donate
Give spirit to the developer, no matter how many donations given will still be accepted<br/>
[paypal.me/hxAri](https://paypal.me/hxAri)

## Licence
All Kanashī source code is licensed under the GNU General Public License v3. Please [see](https://www.gnu.org/licenses) the original document for more details.

## Disclaimer
Kanashī is not affiliated with or endorsed, endorsed at all by Instagram or any other party, if you use the main account to use this tool we as Coders and Developers are not responsible for anything that happens to that account, use it at your own risk, and this is Strictly not for SPAM.