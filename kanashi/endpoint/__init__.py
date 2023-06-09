#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 23.05-2022
# @github https://github.com/hxAri/Kanashi
#
# Kanashī Copyright (c) 2022 - Ari Setiawan <hxari@proton.me>
# Kanashī Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Kanashī is not affiliated with or endorsed, endorsed at all by
# Instagram or any other party, if you use the main account to use this
# tool we as Coders and Developers are not responsible for anything that
# happens to that account, use it at your own risk, and this is Strictly
# not for SPAM.
#

from kanashi.endpoint.auth import AuthError
from kanashi.endpoint.block import Block, BlockError, BlockSuccess
from kanashi.endpoint.favorite import Favorite, FavoriteError, FavoriteSuccess
from kanashi.endpoint.follow import Follow, FollowError, FollowSuccess
from kanashi.endpoint.profile import Profile, ProfileError, ProfileSuccess
from kanashi.endpoint.report import Report, ReportError, ReportSuccess
from kanashi.endpoint.restrict import Restrict, RestrictError, RestrictSuccess
from kanashi.endpoint.signin import SignIn, SignInCheckpoint, SignInError, SignIn2FAError, SignInCsrftokenError, SignInPasswordError, SignInSpamError, SignInUserNotFoundError, SignInSuccess, SignIn2FARequired, SignIn2FASuccess
from kanashi.endpoint.user import User, UserError, UserInfoError, UserNotFoundError