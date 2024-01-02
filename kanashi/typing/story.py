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


from typing import final
from yutiriti.object import Object
from yutiriti.readonly import Readonly
from yutiriti.typing import Typing

from kanashi.typing.user import User


#[kanashi.typing.story.Story]
class Story( Typing ):

	""" Story Identity """

	#[kanashi.typing.story.Story$.Type]
	@final
	class Type( Readonly ):

		""" Story Type """

		#[Type( Int type )]: None
		def __init__( self, type:int ) -> None:

			"""
			Construct method of class Type.

			:params Int type

			:return None
			"""

			match type:
				case 26552: name = "Timeline"
				case 66545: name = "Profile"
				case 81656: name = "Highlight"
				case _:
					raise ValueError( "Unknown story type" )
			
			self.__name__ = name
			self.__type__ = type
		
		#[Type.name]: Str
		@property
		def name( self ) -> str: return self.__name__

		#[Type.value]: Int
		@property
		def value( self ) -> int: return self.__type__

	HIGHLIGHT = Type( 81656 )
	PROFILE = Type( 66545 )
	TIMELINE = Type( 26552 )


#[kanashi.typing.story.StoryFeed<StoryFeedTray[]>]
@final
class StoryFeed( Story, Typing ):

	#[StoryFeed.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"broadcasts",
			"face_filter_nux_version",
			"has_new_nux_story",
			"quick_snaps",
			"refresh_window_ms",
			"response_timestamp",
			"sticker_version",
			"stories_viewer_gestures_nux_eligible",
			"story_likes_config",
			"story_ranking_token",
			"tray"
		]
	
	#[StoryFeed.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"tray": StoryFeedTray
		}
	

#[kanashi.typing.story.StoryFeedTray]
@final
class StoryFeedTray( Story, Typing ):

	#[StoryFeedTray.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"ad_expiry_timestamp_in_millis",
			"app_sticker_info",
			"can_gif_quick_reply",
			"can_react_with_avatar",
			"can_reply",
			"can_reshare",
			"disabled_reply_types",
			"expiring_at",
			"has_besties_media",
			"has_fan_club_media",
			"has_video",
			"id",
			"is_cta_sticker_available",
			"latest_besties_reel_media",
			"latest_reel_media",
			"media_count",
			"media_ids",
			"muted",
			"prefetch_count",
			"ranked_position",
			"ranker_scores",
			"reel_type",
			"seen",
			"seen_ranked_position",
			"should_treat_link_sticker_as_cta",
			"show_fan_club_stories_teaser",
			"story_duration_secs",
			"story_wedge_size",
			"strong_id__",
			"user"
		]
	
	#[StoryFeedTray.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"user": User
		}
	

#[kanashi.typing.story.StoryFeedTrayReels<StoryFeedTrayReel<StoryItem[]>, StoryFeedTrayReel<StoryItem[]>>]
class StoryFeedTrayReels( Story, Typing ):

	#[StoryFeedTrayReels.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"reels",
			"reels_media"
		]
	
	#[StoryFeedTrayReels.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"reels": {
				"*": StoryFeedTrayReel
			},
			"reels_media": StoryFeedTrayReel
		}
	

#[kanashi.typing.story.StoryFeedTrayReel<StoryItem[]>]
@final
class StoryFeedTrayReel( Story, Typing ):

	#[StoryFeedTrayReel.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"ad_expiry_timestamp_in_millis",
			"app_sticker_info",
			"can_gif_quick_reply",
			"can_react_with_avatar",
			"can_reply",
			"can_reshare",
			"disabled_reply_types",
			"expiring_at",
			"id",
			"is_cacheable",
			"is_cta_sticker_available",
			"items",
			"latest_reel_media",
			"media_count",
			"media_ids",
			"prefetch_count",
			"reel_type",
			"seen",
			"should_treat_link_sticker_as_cta",
			"strong_id__",
			"user"
		]
	
	#[StoryFeedTrayReel.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"items": StoryItem,
			"user": User
		}
	

#[kanashi.typing.story.StoryItem]
class StoryItem( Story, Typing ):
	
	#[StoryItem.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"accessibility_caption",
			"archive_story_deletion_ts",
			"attribution_content_url",
			"can_play_spotify_audio",
			"can_reply",
			"can_reshare",
			"can_see_insights_as_brand",
			"can_send_custom_emojis",
			"can_send_prompt",
			"can_viewer_save",
			"caption",
			"caption_is_edited",
			"caption_position",
			"client_cache_key",
			"clips_tab_pinned_user_ids",
			"code",
			"comment_inform_treatment",
			"commerciality_status",
			"created_from_add_yours_browsing",
			"deleted_reason",
			"device_timestamp",
			"enable_media_notes_production",
			"expiring_at",
			"explore_hide_comments",
			"fb_user_tags",
			"filter_type",
			"has_audio",
			"has_delayed_metadata",
			"has_liked",
			"has_shared_to_fb",
			"has_translation",
			"id",
			"ig_media_sharing_disabled",
			"image_versions2",
			"integrity_review_decision",
			"invited_coauthor_producers",
			"is_auto_created",
			"is_comments_gif_composer_enabled",
			"is_cutout_sticker_allowed",
			"is_dash_eligible",
			"is_fb_post_from_fb_story",
			"is_first_take",
			"is_in_profile_grid",
			"is_open_to_public_submission",
			"is_organic_product_tagging_eligible",
			"is_paid_partnership",
			"is_post_live_clips_media",
			"is_reel_media",
			"is_reshare_of_text_post_app_media_in_ig",
			"is_rollcall_v2",
			"is_superlative",
			"is_terminal_video_segment",
			"is_unified_video",
			"is_visual_reply_commenter_notice_enabled",
			"like_and_view_counts_disabled",
			"likers",
			"media_type",
			"music_metadata",
			"number_of_qualities",
			"open_carousel_submission_state",
			"organic_tracking_token",
			"original_height",
			"original_media_has_visual_reply_media",
			"original_width",
			"owner",
			"pk",
			"product_suggestions",
			"product_type",
			"profile_grid_control_enabled",
			"sharing_friction_info",
			"shop_routing_user_id",
			"should_render_soundwave",
			"should_request_ads",
			"show_one_tap_fb_share_tooltip",
			"story_bloks_stickers",
			"story_feed_media",
			"strong_id__",
			"supports_reel_reactions",
			"taken_at",
			"user",
			"video_codec",
			"video_dash_manifest",
			"video_duration",
			"video_versions"
		]
	
	#[StoryItem.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"owner": User,
			"user": User
		}
	

#[kanashi.typing.story.StoryHighlight<StoryItem[]>]
@final
class StoryHighlight( Story, Typing ):

	#[StoryHighlight.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"ad_expiry_timestamp_in_millis",
			"app_sticker_info",
			"can_gif_quick_reply",
			"can_react_with_avatar",
			"can_reply",
			"can_reshare",
			"cover_media",
			"created_at",
			"disabled_reply_types",
			"highlight_reel_type",
			"id",
			"is_cacheable",
			"is_converted_to_clips",
			"is_cta_sticker_available",
			"is_pinned_highlight",
			"items",
			"latest_reel_media",
			"media_count",
			"media_ids",
			"prefetch_count",
			"reel_type",
			"seen",
			"strong_id__",
			"user"
		]
	
	#[StoryHighlight.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"items": StoryItem,
			"user": User
		}
	

#[kanashi.typing.story.StoryHighlights<StoryHightlight<StoryItem[]>, StoryHightlight<StoryItem[]>>]
@final
class StoryHighlights( StoryFeedTrayReels, Typing ):
	
	#[StoryHighlights.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"reels": StoryHighlight,
			"reels_media": StoryHighlight
		}


#[kanashi.typing.story.StoryHighlightReels<StoryProfileEdge[]>]
@final
class StoryHighlightReels( Story, Typing ):

	#[StoryHighlightReels.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"edges"
		]
	
	#[StoryHighlightReels.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"edges": StoryProfileEdge,
			"owner": User
		}


#[kanashi.typing.story.StoryProfile<Chaining[], StoryHighlightReels<StoryProfileEdge[]>, StoryReel>]
@final
class StoryProfile( Story, Typing ):

	""" Result Story from Profile """

	#[StoryProfile.__nested__]: Bool
	@property
	def __nested__( self ) -> bool: return False

	#[StoryProfile.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return {
			"data": {
				"user": [
					"edge_chaining",
					"edge_highlight_reels",
					"is_live",
					"reel"
				]
			}
		}
	
	#[StoryProfile.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			# "edge_chaining": Chaining,
			"edge_highlight_reels": StoryHighlightReels,
			"reel": StoryReel
		}
	

#[kanashi.typing.story.StoryProfileEdge]
@final
class StoryProfileEdge( Story, Typing ):

	#[StoryProfileEdge.__nested__]: Bool
	@property
	def __nested__( self ) -> bool: return False
	
	#[StoryProfileEdge.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return {
			"node": [
				"cover_media",
				"cover_media_cropped_thumbnail",
				"id",
				"owner",
				"title"
			]
		}
	
	#[StoryProfileEdge.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object: return {
		"owner": User
	}
	

#[kanashi.typing.story.StoryReel]
@final
class StoryReel( Story, Typing ):
	
	#[StoryReel.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"expiring_at",
			"has_pride_media",
			"id",
			"latest_reel_media",
			"owner",
			"seen",
			"user"
		]
	
	#[StoryReel.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"owner": User,
			"user": User
		}
	

