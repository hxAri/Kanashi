
![Kanashi · Logo](https://raw.githubusercontent.com/hxAri/hxAri/main/assets/images/1654820424;51ydWrxRcv.png)

## Abouts
Kanashi is an open source project that can be used to login to real Instagram accounts via Linux Terminal and Android Termux, this also includes taking CSRF Tokens and Login Session IDs, besides that you can use Tokens and IDs to do various things like Instagram Web.

## Install
*Not available for PIP at this time.*
```sh
git clone https://github.com/hxAri/Kanashi && cd Kanashi && python setup* install
```

## Examples
## Simple Runtime
```sh
cd Kanashi && chmod +x main && ./main
```
## Extends Class
If you create your own class and want to use Modules like Request, SignIn, etc you should at least have a class description like the following
```py
from kanashi import *

# You can use Kanashi for Extends
class Test( Context ):
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
       
```

## Donate
Give spirit to the developer, no matter how many donations given will still be accepted

## Licence
All Kanashi source code is licensed under the GNU General Public License v3. Please [see](https://www.gnu.org/licenses) the original document for more details.

## Disclaimer
Kanashi is not affiliated with or endorsed, endorsed at all by Instagram or any other party, if you use the main account to use this tool we as Coders and Developers are not responsible for anything that happens to that account, use it at your own risk, and this is Strictly not for SPAM.
