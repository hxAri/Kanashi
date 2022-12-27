
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
* Python **3xx**
* Python **requests**

## Examples
## Simple Usage
```sh
cd Kanashi && chmod +x main && ./main
```
## Extends Class 1x
If you create your own class and want to use Modules like Request, SignIn, etc you should at least have a class description like the following
```py
from kanashi import *

# You can use Kanashi for Extends
class Main( Kanashi ):
    def __init__( self ):
        self.config = Config( self )
        self.request = Request( self )
        self.signin = SignIn( self )
        # Etc...
        
        super().__init__( self )
    
    def main( self ):
        # Todo code here!
        # The main method must be in the main class
        # Because classes that don't start with Base
        # are closely related to the Main class
        pass
```
## Extends Class 2x
This is an example of extending a class yourself freely, This is almost the same as the first example, but here you are not required to use a class that does not start with Base, but you must still provide an instance of the first class as the application context to each new instance
```py
from kanashi import *

class Main( Kanashi ):
    def __init__( self ):
        
        # Also be aware that class Base
        # doesn't use Thread at all (Should)
        self.config = BaseConfig( self )
        self.request = BaseRequest( self )
        self.signin = BaseSignIn( self )
        # Etc...
        
        super().__init__( self )
    
    def run( self ):
        # Todo code here!
        # Main method name can be changed to anything here
        pass
```

## Others
## kanashi.Object
kanashi.Object is a class that supports Stringable and is able to convert Dictionary values ​​to Object, when the class is represented as a String it will become JSON Strings, To use it, simply create a new instance with the Dictionary parameter
```py
from kanashi import JSON, Object

# Dictionary data
dict = {
    "x": "X",
    "y": {
        "y": "Y"
    },
    "z": [{
        "x": "X",
        "y": "Y",
        "z": "Z"
    }]
}

# Json Strings
json = JSON.encode( dict )

# Just create new Instance
# JSON Strings is supported
object = Object( dict or json )
object.x # Output X
object.y.y # Output Y
object.z[0].z # Output Z

# You can also share Dictionary values ​​to other classes
parent = Something()
object = Object( dict, parent )

parent.x # Output X
parent.y.y # Output Y
parent.z[0].z # Output Z

# Update or Set new Data
object.set( Dict{ ... } )

# Update or Set new Data with JSON Strings
object.set( Json'{ ... }' )

# Get Dictionary Values
object.dict()
```

## Donate
Give spirit to the developer, no matter how many donations given will still be accepted<br/>
[paypal.me/hxAri](https://paypal.me/hxAri)

## Licence
All Kanashi source code is licensed under the GNU General Public License v3. Please [see](https://www.gnu.org/licenses) the original document for more details.

## Disclaimer
Kanashi is not affiliated with or endorsed, endorsed at all by Instagram or any other party, if you use the main account to use this tool we as Coders and Developers are not responsible for anything that happens to that account, use it at your own risk, and this is Strictly not for SPAM.
