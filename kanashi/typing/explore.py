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

from kanashi.object import Object
from kanashi.typing.media import Media
from kanashi.typing.typing import Typing
from kanashi.typing.user import User


#[kanashi.typing.explore.Explore<ExploreSection<ExploreLayout<ExploreClip<ExploreClipItem<ExploreClipMedia>[]>, ExploreFillItem<ExploreFillMedia>[]>>[]>]
@final
class Explore( Typing ):

	#[Explore.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"auto_load_more_enabled",
			"clusters",
			"max_id",
			"more_available",
			"next_max_id",
			"rank_token",
			"ranked_time_in_seconds",
			"sectional_items",
			"session_paging_token"
		]
	
	#[Explore.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"sectional_items": ExploreSection
		}
	

#[kanashi.typing.explore.ExploreSection<ExploreLayout<ExploreClip<ExploreClipItem<ExploreClipMedia>[]>, ExploreFillItem<ExploreFillMedia>[]>>]
@final
class ExploreSection( Typing ):

	#[ExploreSection.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"explore_item_info",
			"feed_type",
			"layout_content",
			"layout_type"
		]
	
	#[ExploreSection.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"layout_content": ExploreLayout
		}
	

#[kanashi.typing.explore.ExploreLayout<ExploreClip<ExploreClipItem<ExploreClipMedia>[]>,ExploreFillItem<ExploreFillMedia>[]>]
@final
class ExploreLayout( Typing ):

	#[ExploreLayout.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"fill_items",
    		"one_by_two_item"
		]
	
	#[ExploreLayout.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"fill_items": ExploreFillItem,
			"one_by_two_item": {
				"clips": ExploreClip
			}
		}
	

#[kanashi.typing.explore.ExploreClip<ExploreClipItem<ExploreClipMedia>[]>]
@final
class ExploreClip( Typing ):

	#[ExploreClip.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"badge_label",
			"chaining_info",
			"content_source",
			"design",
			"id",
			"items",
			"label",
			"max_id",
			"more_available",
			"type"
		]
	
	#[ExploreClip.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"items": ExploreClipItem
		}
	

#[kanashi.typing.explore.ExploreClipItem<ExploreClipMedia>[]]
class ExploreClipItem( Media, Typing ):

	#[ExploreClipItem.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"media"
		]
	
	#[ExploreClipItem.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"media": ExploreClipMedia
		}
	

#[kanashi.typing.explore.ExploreClipMedia]
@final
class ExploreClipMedia( Media, Typing ):

	#[ExploreClipMedia.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"can_see_insights_as_brand",
			"can_view_more_preview_comments",
			"can_viewer_reshare",
			"can_viewer_save",
			"caption",
			"caption_is_edited",
			"client_cache_key",
			"clips_delivery_parameters",
			"clips_metadata",
			"clips_tab_pinned_user_ids",
			"code",
			"comment_count",
			"comment_inform_treatment",
			"comment_likes_enabled",
			"comment_threading_enabled",
			"comments",
			"commerciality_status",
			"deleted_reason",
			"device_timestamp",
			"enable_media_notes_production",
			"enable_waist",
			"explore_hide_comments",
			"facepile_top_likers",
			"fb_user_tags",
			"filter_type",
			"has_audio",
			"has_delayed_metadata",
			"has_liked",
			"has_more_comments",
			"has_shared_to_fb",
			"hide_view_all_comment_entrypoint",
			"id",
			"ig_media_sharing_disabled",
			"image_versions2",
			"integrity_review_decision",
			"inventory_source",
			"invited_coauthor_producers",
			"is_artist_pick",
			"is_auto_created",
			"is_comments_gif_composer_enabled",
			"is_cutout_sticker_allowed",
			"is_dash_eligible",
			"is_in_profile_grid",
			"is_open_to_public_submission",
			"is_organic_product_tagging_eligible",
			"is_paid_partnership",
			"is_post_live_clips_media",
			"is_reshare_of_text_post_app_media_in_ig",
			"is_third_party_downloads_eligible",
			"is_unified_video",
			"is_visual_reply_commenter_notice_enabled",
			"like_and_view_counts_disabled",
			"like_count",
			"logging_info_token",
			"max_num_visible_preview_comments",
			"media_appreciation_settings",
			"media_cropping_info",
			"media_notes",
			"media_type",
			"mezql_token",
			"music_metadata",
			"next_max_id",
			"number_of_qualities",
			"organic_tracking_token",
			"original_height",
			"original_media_has_visual_reply_media",
			"original_width",
			"owner",
			"pk",
			"play_count",
			"preview_comments",
			"product_suggestions",
			"product_type",
			"profile_grid_control_enabled",
			"recommendation_data",
			"sharing_friction_info",
			"shop_routing_user_id",
			"should_request_ads",
			"social_context",
			"strong_id__",
			"subscribe_cta_visible",
			"taken_at",
			"top_likers",
			"user",
			"video_codec",
			"video_dash_manifest",
			"video_duration",
			"video_versions",
			"view_state_item_type"
		]
	
	#[ExploreClipMedia.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"owner": User,
			"user": User
		}
	

#[kanashi.typing.explore.ExploreFillItem<ExploreFillMedia>[]]
@final
class ExploreFillItem( ExploreClipItem ):

	#[ExploreFillItem.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"media": ExploreFillMedia
		}
	

#[kanashi.typing.explore.ExploreFillMedia]
@final
class ExploreFillMedia( Media, Typing ):

	#[ExploreFillMedia.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"algorithm",
			"all_previous_submitters",
			"can_see_insights_as_brand",
			"can_view_more_preview_comments",
			"can_viewer_reshare",
			"can_viewer_save",
			"caption",
			"caption_is_edited",
			"carousel_media",
			"carousel_media_count",
			"carousel_media_ids",
			"carousel_media_pending_post_count",
			"client_cache_key",
			"clips_tab_pinned_user_ids",
			"coauthor_producers",
			"code",
			"comment_count",
			"comment_inform_treatment",
			"comment_threading_enabled",
			"comments",
			"commerciality_status",
			"connection_id",
			"deleted_reason",
			"device_timestamp",
			"enable_media_notes_production",
			"enable_waist",
			"explore",
			"explore_context",
			"explore_hide_comments",
			"facepile_top_likers",
			"fb_user_tags",
			"filter_type",
			"has_delayed_metadata",
			"has_liked",
			"has_more_comments",
			"has_shared_to_fb",
			"hide_view_all_comment_entrypoint",
			"id",
			"ig_media_sharing_disabled",
			"image_versions2",
			"impression_token",
			"integrity_review_decision",
			"inventory_source",
			"invited_coauthor_producers",
			"is_auto_created",
			"is_comments_gif_composer_enabled",
			"is_cutout_sticker_allowed",
			"is_in_profile_grid",
			"is_open_to_public_submission",
			"is_organic_product_tagging_eligible",
			"is_paid_partnership",
			"is_post_live_clips_media",
			"is_reshare_of_text_post_app_media_in_ig",
			"is_unified_video",
			"is_visual_reply_commenter_notice_enabled",
			"like_and_view_counts_disabled",
			"like_count",
			"logging_info_token",
			"max_num_visible_preview_comments",
			"media_notes",
			"media_type",
			"mezql_token",
			"music_metadata",
			"organic_tracking_token",
			"original_height",
			"original_media_has_visual_reply_media",
			"original_width",
			"owner",
			"photo_of_you",
			"pk",
			"preview_comments",
			"product_suggestions",
			"product_type",
			"profile_grid_control_enabled",
			"recommendation_data",
			"sharing_friction_info",
			"shop_routing_user_id",
			"should_request_ads",
			"strong_id__",
			"taken_at",
			"top_likers",
			"user",
			"usertags"
		]
	
	#[ExploreFillMedia.__mapping__]: Dict|Object
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"owner": User,
			"user": User
		}
	
