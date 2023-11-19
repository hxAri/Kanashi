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


from yutiriti import Error

#[kanashi.error.FriendshipError]
class FriendshipError( Error ): ...

#[kanashi.error.BestieError]
class BestieError( FriendshipError ): ...

#[kanashi.error.BlockError]
class BlockError( FriendshipError ): ...

#[kanashi.error.FavoriteError]
class FavoriteError( FriendshipError ): ...

#[kanashi.error.FeedError]
class FeedError( Error ): ...

#[kanashi.error.ClientError]
class ClientError( Error ): ...

#[kanashi.error.CursorError]
class CursorError( Error ): ...

#[kanashi.error.GraphqlError]
class GraphqlError( ClientError ): ...

#[kanashi.error.FollowError]
class FollowError( FriendshipError ): ...

#[kanashi.error.FollowerError]
class FollowerError( FriendshipError ): ...

#[kanashi.error.LikeError]
class LikeError( Error ): ...

#[kanashi.error.LockedError]
class LockedError( Error ): ...

#[kanashi.error.CommentError]
class CommentError( Error ): ...

#[kanashi.error.RemoveError]
class RemoveError( Error ): ...

#[kanashi.error.MediaError]
class MediaError( Error ): ...

#[kanashi.error.MediaNotFoundError]
class MediaNotFoundError( Error ): ...

#[kanashi.error.RestrictError]
class RestrictError( FriendshipError ): ...

#[kanashi.error.UserError]
class UserError( Error ): ...

#[kanashi.error.UserNotFoundError]
class UserNotFoundError( UserError ): ...

#[kanashi.error.SignInError]
class SignInError( Error ): ...

#[kanashi.error.CsrftokenError]
class CsrftokenError( Error ): ...

#[kanashi.error.ConfigError]
class ConfigError( Error ): ...

#[kanashi.error.PasswordError]
class PasswordError( UserError ): ...

#[kanashi.error.ProfileError]
class ProfileError( Error ): ...

#[kanashi.error.SpamError]
class SpamError( Error ): ...

#[kanashi.error.StoryError]
class StoryError( Error ): ...

#[kanashi.error.StoryNotFoundError]
class StoryNotFoundError( StoryError ): ...
