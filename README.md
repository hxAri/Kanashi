
![Kanashī · Logo](https://raw.githubusercontent.com/hxAri/hxAri/main/public/images/1654820424;51ydWrxRcv.png)

Please note that this is not fully finished or not ready to use, if you are interested in using it please I don't require you to wait for this to finish because I am also busy.

## Abouts
Kanashī is an independent open source project without any organizational involvement in it, this project is used to perform Instagram Login via the Command Line, it is capable of taking and also performing actions like Instagram Web in general however, not everything can be done here.

Because this is an open source project, the creators and developers of this project will not tolerate or be held responsible if it happens to any Instagram account that is used to log in or any user profiles that you collect information through this program.

## History
Kanashī itself is a translation of the word from Japan **悲しい** which means Sadness, I built this program for the sadness that I have experienced so far, if you are wondering why that is? Don't ask! Just use this program if you are interested, no need to think about anyone's sadness or even me.

## Warning
This program was created to be used by anyone, not to be sold for anyone's profit!

## Features
* **Access Manager**
  This allows you to retrieve information about each application and also web information connected to your Instagram account
* **Approve && Ignore Request Follow**
* **Bestie && Un-bestie**
  Make user as bestie or remove from bestie
* **Block && Unblock**
* **Bypassing Checkpoints**
  Currently under construction
* **CGI**
  Interactive Command Graphical user interface
* **Direct Message Inbox**
  Fetch direct messages inbox
* **Direct Presence**
* **Download Media**
* **Exploration**
  Fetch Instagram explore contents
* **Favorite && Un-Favorite**
  Make user as favorite or remove from favorite
* **Follow && Unfollow**
* **Follower && Following**
  Fetch followers and also following users
* **Friendship**
  Show user friendship status
* **Friendship Show Many**
  Show multiple users friendship status
* **Graphql**
  Create our custome graphql request
* **Inbox**
  Fetch inbox notifications
* **Logout**
* **Media**
  Fetch any instagram media e.g feed, story, highlight story, profile-picture, etc
* **Multiple Accounts**
  Support for login multiple accounts
* **Mute && Un-Mute**
  Mute or un-mute user feed and story
* **Notification Settings**
  Fetch notification settings include sms and push
* **Pending Request Follow**
  Fetch pending request follows
* **Privacy && Security Settings**
  Fetch privacy and security settings info
* **Profile**
  Fetch user profile
* **Remember Cookie**
  SignIn with cookies
* **Settings**
  Application settings can be configured and customized
* **SignIn**
  SignIn manual with username and password
* **Story**
  Fetch user timeline feed tray reel story and highlighted story
* **Story Feed**
  Fetch timeline feed tray reel story
* **Switch Account**

## Requirements
* Python **>=3.10.4**
* [Pytz](https://github.com/stub42/pytz) **>=2022.1**
* [Requests](https://github.com/psf/requests) **>=2.31.0**

## Installation
Installing Kanashī is very easy, please clone or download this repository archive
```sh
# Clonig Repository
git clone https://github.com/hxAri/Kanashi

# Change Current Working Directory
cd Kanashi;

# Install Requirement Dependency Modules
pip install -r requirements.txt
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

#### # SignIn Manual
I do not recommend logging in manually using the main account.
```py
from kanashi import Client, SignInError, Throwable

client = Client()
try:
	signin = client.signin( browser=str, username=str, password=str )
	if signin.authenticated is True:
		print( signin.user )
	elif "checkpoint" in signin:
		print( signin.checkpoint )
	elif "two_factor" in signin:
		print( signin.two_factor )
	else:
		raise SignInError( "Something wrong!" )
except Throwable as e:
	print( e )
```

#### # SignIn Cookie
Signing in with this method is highly recommended to avoid unwanted things.
```py
signin = client.remember( browser=str, cookies=Cookies|dict|Object|str, headers=dict|Headers|Object )
```

#### # Activate Session
When you successfully log in, Kanashī does not save your login value into the properties, this is done to avoid session collisions. To overcome this you need to activate it manually:
```py
client.activate( active=signin.user )
```
After that, you can check it in the following way
```py
client.authenticated()
```
It will return ```True``` if it has been authenticated, Meanwhile, to see who is being authenticated, you can print the value of the ```active``` property:
```py
print( repr( client.active ) )
```
It will print as below:
```py
Active(
    "id": int(12345678),
    "fullname": str("Example"),
    "username": str("example"),
    "usermail": str("example@example.io"),
    "password": NoneType(None),
    "csrftoken": str("xxxxxxxxxxxxxx"),
    "sessionid": str("xxxxxxxxxxxxxx"),
    "session": ObjectBuilder(
        "browser": str("xxxxxxxxxxxx"),
        "cookies": Object(
            "mid": str("xxxxxxxxxxxxxxxxxxx"),
            "ig_did": str("xxxxxxxxxxxxxxxx"),
            "ig_nrcb": int(1),
            "datr": str("xxxxxxxxxxxxxxxxxx"),
            "csrftoken": str("xxxxxxxxxxxxx"),
            "ds_user_id": int(12345678),
            "sessionid": str("xxxxxxxxxxxxxx"),
            "shbid": str("xxxxxxxxxxxxxxxxxx"),
            "shbts": str("xxxxxxxxxxxxxxxxxx"),
            "rur": str("\"xxxxxxxxxxxxxxxx\"")
        ),
        "headers": Object(
            "User-Agent": str("xxxxxxxxxxxxxxxxxxxxxxx"),
            "Accept-Encoding": str("gzip, deflate, br"),
            "Accept": str("*/*"),
            "Connection": str("close"),
            "Accept-Language": str("en-US,en;q=0.9"),
            "Authority": str("www.instagram.com"),
            "Origin": str("https://www.instagram.com"),
            "Referer": str("https://www.instagram.com/accounts/edit/"),
            "Sec-Fetch-Dest": str("empty"),
            "Sec-Fetch-Mode": str("cors"),
            "Sec-Fetch-Site": str("same-origin"),
            "Viewport-Width": int(980),
            "X-Asbd-Id": int(198387),
            "X-IG-App-Id": int(1217981644879628),
            "X-IG-WWW-Claim": str("hmac.AR04Hjqeow3ipAWpAcl8Q5Dc7eMtKr3Ff08SxTMJosgMAh-z"),
            "X-Instagram-Ajax": int(1007625843),
            "X-Requested-With": str("XMLHttpRequest"),
            "X-CSRFToken": str("xxxxxxxxxxxxxxxxxxx")
        )
    )
)
```

#### # Save Login Info
Save login info for future use.
```py
client.settings.signin.active = signin.user.username
client.settings.signin.switch[signin.user.username] = signin.user
client.config.save()
```

#### # Profile User
Fetch user profile is very easy, because you can use the user name and also the user ID or primary key.
```py
profile = client.profile( username=int|str )
```

## Request History
Please note that Kanashī stores all successful request results and stores all request logs in the `history` property and also writes them to the `~/requests/response.json` file, you can use each request log for further analysis if you need it and make sure your directory allows it Kanashī to write the file.

## Licence
All Kanashī source code is licensed under the GNU General Public License v3. Please [see](https://www.gnu.org/licenses) the original document for more details.

## Disclaimer
Kanashī is not affiliated with or endorsed, endorsed at all by Instagram or any other party, if you use the main account to use this tool we as Coders and Developers are not responsible for anything that happens to that account, use it at your own risk, and this is Strictly not for SPAM.

## Donate
Give spirit to the developer, no matter how many donations given will still be accepted<br/>
[paypal.me/hxAri](https://paypal.me/hxAri).
