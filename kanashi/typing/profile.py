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
from yutiriti import Object, Typing

from kanashi.typing.user import User


#[Profile.typing.profile.Profile]
@final
class Profile(  Typing,User ):

	#[Profile.__items__]: List<Dict|List|Object|Str>
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"about_your_account_bloks_entrypoint_enabled",
			"account_badges",
			"account_category",
			"account_type",
			"ads_incentive_expiration_date",
			"ads_page_id",
			"ads_page_name",
			"aggregate_promote_engagement",
			"ai_agent_type",
			"all_media_count",
			"allow_mention_setting",
			"allow_tag_setting",
			"allowed_commenter_type",
			"audio_go_dark_events",
			"auto_expand_chaining",
			"besties_count",
			"bio_links",
			"biography",
			"biography_with_entities",
			"birthday_today_visibility_for_viewer",
			"blocked_by_viewer",
			"blocking",
			"break_reminder_interval",
			"business_address_json",
			"business_category_name",
			"business_contact_method",
			"business_email",
			"business_phone_number",
			"can_add_fb_group_link_on_profile",
			"can_be_tagged_as_sponsor",
			"can_boost_post",
			"can_convert_to_business",
			"can_create_new_standalone_fundraiser",
			"can_create_new_standalone_personal_fundraiser",
			"can_create_sponsor_tags",
			"can_follow_hashtag",
			"can_hide_category",
			"can_link_entities_in_bio",
			"can_see_organic_insights",
			"can_see_support_inbox",
			"can_see_support_inbox_v1",
			"can_tag_products_from_merchants",
			"can_use_affiliate_partnership_messaging_as_brand",
			"can_use_affiliate_partnership_messaging_as_creator",
			"can_use_branded_content_discovery_as_brand",
			"can_use_branded_content_discovery_as_creator",
			"category",
			"category_enum",
			"category_name",
			"connected_fb_page",
			"country_block",
			"creator_shopping_info",
			"creators_subscribed_to_count",
			"current_catalog_id",
			"daily_time_limit",
			"displayed_action_button_partner",
			"displayed_action_button_type",
			"edge_chaining",
			"edge_felix_combined_draft_uploads",
			"edge_felix_combined_post_uploads",
			"edge_felix_drafts",
			"edge_felix_pending_draft_uploads",
			"edge_felix_pending_post_uploads",
			"edge_felix_video_timeline",
			"edge_follow",
			"edge_followed_by",
			"edge_highlight_reels",
			"edge_media_collections",
			"edge_mutual_followed_by",
			"edge_owner_to_timeline_media",
			"edge_saved_media",
			"eimu_id",
			"eligible_shopping_formats",
			"eligible_shopping_signup_entrypoints",
			"existing_user_age_collection_enabled",
			"external_url",
			"external_url_linkshimmed",
			"fan_club_info",
			"fb_profile_biolink",
			"fbid",
			"fbid_v2",
			"fbpay_experience_enabled",
			"feed_post_reshare_disabled",
			"follow_friction_type",
			"followed_by",
			"followed_by_viewer",
			"follower_count",
			"following",
			"following_count",
			"following_tag_count",
			"follows_viewer",
			"full_name",
			"group_metadata",
			"guardian_id",
			"has_anonymous_profile_picture",
			"has_ar_effects",
			"has_blocked_viewer",
			"has_channel",
			"has_clips",
			"has_collab_collections",
			"has_exclusive_feed_content",
			"has_fan_club_subscriptions",
			"has_groups",
			"has_guides",
			"has_highlight_reels",
			"has_music_on_profile",
			"has_onboarded_to_text_post_app",
			"has_placed_orders",
			"has_private_collections",
			"has_public_tab_threads",
			"has_requested_viewer",
			"has_saved_items",
			"has_user_ever_set_break",
			"has_videos",
			"hd_profile_pic_url_info",
			"hd_profile_pic_versions",
			"hide_like_and_view_counts",
			"highlight_reel_count",
			"highlight_reshare_disabled",
			"id",
			"include_direct_blacklist_status",
			"incoming_request",
			"interop_messaging_user_fbid",
			"is_allowed_to_create_standalone_nonprofit_fundraisers",
			"is_allowed_to_create_standalone_personal_fundraisers",
			"is_api_user",
			"is_bestie",
			"is_blocking_reel",
			"is_business",
			"is_business_account",
			"is_call_to_action_enabled",
			"is_category_tappable",
			"is_direct_roll_call_enabled",
			"is_eligible_to_show_fb_cross_sharing_nux",
			"is_eligible_to_subscribe",
			"is_embeds_disabled",
			"is_favorite",
			"is_feed_favorite",
			"is_guardian_of_viewer",
			"is_hide_more_comment_enabled",
			"is_igd_product_picker_enabled",
			"is_in_canada",
			"is_interest_account",
			"is_joined_recently",
			"is_memorialized",
			"is_muted_words_custom_enabled",
			"is_muted_words_global_enabled",
			"is_muted_words_spamscam_enabled",
			"is_muting_media_notes",
			"is_muting_notes",
			"is_muting_reel",
			"is_needy",
			"is_new_to_instagram",
			"is_opal_enabled",
			"is_potential_business",
			"is_private",
			"is_professional_account",
			"is_profile_action_needed",
			"is_profile_broadcast_sharing_enabled",
			"is_profile_picture_expansion_enabled",
			"is_quiet_mode_enabled",
			"is_regulated_c18",
			"is_restricted",
			"is_secondary_account_creation",
			"is_shopping_auto_highlight_eligible",
			"is_shopping_catalog_source_selection_enabled",
			"is_shopping_community_content_enabled",
			"is_shopping_settings_enabled",
			"is_supervised_by_viewer",
			"is_supervised_user",
			"is_supervision_enabled",
			"is_supervision_features_enabled",
			"is_verified",
			"is_verified_by_mv4b",
			"is_whatsapp_linked",
			"last_seen_timezone",
			"limited_interactions_enabled",
			"linked_fb_info",
			"media_count",
			"mini_shop_seller_onboarding_status",
			"muting",
			"mutual_followers_count",
			"nametag",
			"needs_to_accept_shopping_seller_onboarding_terms",
			"num_of_admined_pages",
			"opal_info",
			"open_external_url_with_in_app_browser",
			"outgoing_request",
			"overall_category_name",
			"page_id",
			"page_name",
			"pinned_channels_info",
			"pinned_channels_list_count",
			"pk",
			"pk_id",
			"primary_profile_link_type",
			"professional_conversion_suggested_account_type",
			"profile_context",
			"profile_context_facepile_users",
			"profile_context_links_with_user_ids",
			"profile_context_mutual_follow_ids",
			"profile_pic_id",
			"profile_pic_url",
			"profile_pic_url_hd",
			"profile_type",
			"pronouns",
			"recently_bestied_by_count",
			"recs_from_friends",
			"reel_auto_archive",
			"remove_message_entrypoint",
			"requested_by_viewer",
			"restricted_by_viewer",
			"robi_feedback_source",
			"shopping_post_onboard_nux_type",
			"should_show_category",
			"should_show_public_contacts",
			"show_account_transparency_details",
			"show_besties_badge",
			"show_conversion_edit_entry",
			"show_fb_link_on_profile",
			"show_fb_page_link_on_profile",
			"show_insights_terms",
			"show_post_insights_entry_point",
			"show_together_pog",
			"smb_delivery_partner",
			"smb_support_delivery_partner",
			"smb_support_partner",
			"status",
			"strong_id__",
			"subscribed",
			"supervision_info",
			"third_party_downloads_enabled",
			"total_ar_effects",
			"total_clips_count",
			"total_igtv_videos",
			"transparency_label",
			"transparency_product",
			"transparency_product_enabled",
			"username",
			"usertag_review_enabled",
			"viewer",
			"whatsapp_number"
		]
	
	#[Kanashi.aboutYourAccountBloksEntrypointEnabled]: Bool
	@property
	def aboutYourAccountBloksEntrypointEnabled( self ) -> bool: return self['about_your_account_bloks_entrypoint_enabled'] if "about_your_account_bloks_entrypoint_enabled" in self else False
	
	#[Kanashi.accountBadges]: List
	@property
	def accountBadges( self ) -> list: return self['account_badges'] if "account_badges" in self else []
	
	#[Kanashi.accountCategory]: Str
	@property
	def accountCategory( self ) -> str: return self['account_category'] if "account_category" in self else None
	
	#[Kanashi.accountType]: Int
	@property
	def accountType( self ) -> int: return self['account_type'] if "account_type" in self else 0
	
	#[Kanashi.adsIncentiveExpirationDate]: Any
	@property
	def adsIncentiveExpirationDate( self ) -> any: return self['ads_incentive_expiration_date'] if "ads_incentive_expiration_date" in self else None
	
	#[Kanashi.adsPageId]: Any
	@property
	def adsPageId( self ) -> any: return self['ads_page_id'] if "ads_page_id" in self else None
	
	#[Kanashi.adsPageName]: Any
	@property
	def adsPageName( self ) -> any: return self['ads_page_name'] if "ads_page_name" in self else None
	
	#[Kanashi.aggregatePromoteEngagement]: Bool
	@property
	def aggregatePromoteEngagement( self ) -> bool: return self['aggregate_promote_engagement'] if "aggregate_promote_engagement" in self else False
	
	#[Kanashi.aiAgentType]: Any
	@property
	def aiAgentType( self ) -> any: return self['ai_agent_type'] if "ai_agent_type" in self else None
	
	#[Kanashi.allMediaCount]: Int
	@property
	def allMediaCount( self ) -> int: return self['all_media_count'] if "all_media_count" in self else 0
	
	#[Kanashi.allowMentionSetting]: Str
	@property
	def allowMentionSetting( self ) -> str: return self['allow_mention_setting'] if "allow_mention_setting" in self else None
	
	#[Kanashi.allowTagSetting]: Str
	@property
	def allowTagSetting( self ) -> str: return self['allow_tag_setting'] if "allow_tag_setting" in self else None
	
	#[Kanashi.allowedCommenterType]: Str
	@property
	def allowedCommenterType( self ) -> str: return self['allowed_commenter_type'] if "allowed_commenter_type" in self else None
	
	#[Kanashi.audioGoDarkEvents]: List
	@property
	def audioGoDarkEvents( self ) -> list: return self['audio_go_dark_events'] if "audio_go_dark_events" in self else []
	
	#[Kanashi.autoExpandChaining]: Any
	@property
	def autoExpandChaining( self ) -> any: return self['auto_expand_chaining'] if "auto_expand_chaining" in self else None
	
	#[Kanashi.bestiesCount]: Int
	@property
	def bestiesCount( self ) -> int: return self['besties_count'] if "besties_count" in self else 0
	
	#[Kanashi.bioLinks]: List
	@property
	def bioLinks( self ) -> list: return self['bio_links'] if "bio_links" in self else []
	
	#[Kanashi.biography]: Str
	@property
	def biography( self ) -> str: return self['biography'] if "biography" in self else None

	#[Profile.biographyEntities]: List
	@property
	def biographyEntities( self ) -> list:
		return self['biography_with_entities'].entities
	
	#[Profile.biographyEntityUsers]: List
	@property
	def biographyEntityUsers( self ) -> list:
		users = []
		entities = self.biographyEntities
		for entity in entities:
			if "user" not in entity: continue
			if user := entity.user:
				users.append( user.username )
		return users
	
	#[Profile.biographyEntityUsersFormat]: Str
	@property
	def biographyEntityUsersFormat( self ) -> str: return "-\x20@{}".format( "\x0a\x20\x20\x20\x20-\x20@".join( self.biographyEntityUsers ) )
	
	#[Profile.biographyEntityHashtags]: List
	@property
	def biographyEntityHashtags( self ) -> list:
		hashtags = []
		entities = self.biographyEntities
		for entity in entities:
			if "hasthtag" not in entity: continue
			if hashtag := entity.hashtag:
				hashtags.append( hashtag.name )
		return hashtags
	
	#[Profile.biographyEntityHashtagsFormat]: Str
	@property
	def biographyEntityHashtagsFormat( self ) -> str:
		return "-\x20#{}".format( "\x0a\x20\x20\x20\x20-\x20#".join( self.biographyEntityHashtags ) )
	
	#[Profile.biographyFormat]: Str
	@property
	def biographyFormat( self ) -> str: return "\x20\x20{}".format( self.biographyRawText.replace( "\n", "\x0a\x20\x20\x20\x20\x20\x20" ) )
	
	#[Profile.biographyRawText]: Str
	@property
	def biographyRawText( self ) -> str:
		if self['biography_with_entities'].raw_text == None:
			self['biography_with_entities'].raw_text = ""
		return self['biography_with_entities'].raw_text
	
	#[Kanashi.biographyWithEntities]: Object
	@property
	def biographyWithEntities( self ) -> Object: return self['biography_with_entities'] if "biography_with_entities" in self else Object({})
	
	#[Kanashi.birthdayTodayVisibilityForViewer]: Str
	@property
	def birthdayTodayVisibilityForViewer( self ) -> str: return self['birthday_today_visibility_for_viewer'] if "birthday_today_visibility_for_viewer" in self else None
	
	#[Kanashi.blockedByViewer]: Bool
	@property
	def blockedByViewer( self ) -> bool: return self['blocked_by_viewer'] if "blocked_by_viewer" in self else False
	
	#[Kanashi.blocking]: Bool
	@property
	def blocking( self ) -> bool: return self['blocking'] if "blocking" in self else False
	
	#[Kanashi.breakReminderInterval]: Int
	@property
	def breakReminderInterval( self ) -> int: return self['break_reminder_interval'] if "break_reminder_interval" in self else 0
	
	#[Kanashi.businessAddressJson]: Any
	@property
	def businessAddressJson( self ) -> any: return self['business_address_json'] if "business_address_json" in self else None
	
	#[Kanashi.businessCategoryName]: Any
	@property
	def businessCategoryName( self ) -> any: return self['business_category_name'] if "business_category_name" in self else None
	
	#[Kanashi.businessContactMethod]: Str
	@property
	def businessContactMethod( self ) -> str: return self['business_contact_method'] if "business_contact_method" in self else None
	
	#[Kanashi.businessEmail]: Any
	@property
	def businessEmail( self ) -> any: return self['business_email'] if "business_email" in self else None
	
	#[Kanashi.businessPhoneNumber]: Any
	@property
	def businessPhoneNumber( self ) -> any: return self['business_phone_number'] if "business_phone_number" in self else None
	
	#[Kanashi.canAddFbGroupLinkOnProfile]: Bool
	@property
	def canAddFbGroupLinkOnProfile( self ) -> bool: return self['can_add_fb_group_link_on_profile'] if "can_add_fb_group_link_on_profile" in self else False
	
	#[Kanashi.canBeTaggedAsSponsor]: Bool
	@property
	def canBeTaggedAsSponsor( self ) -> bool: return self['can_be_tagged_as_sponsor'] if "can_be_tagged_as_sponsor" in self else False
	
	#[Kanashi.canBoostPost]: Bool
	@property
	def canBoostPost( self ) -> bool: return self['can_boost_post'] if "can_boost_post" in self else False
	
	#[Kanashi.canConvertToBusiness]: Bool
	@property
	def canConvertToBusiness( self ) -> bool: return self['can_convert_to_business'] if "can_convert_to_business" in self else False
	
	#[Kanashi.canCreateNewStandaloneFundraiser]: Bool
	@property
	def canCreateNewStandaloneFundraiser( self ) -> bool: return self['can_create_new_standalone_fundraiser'] if "can_create_new_standalone_fundraiser" in self else False
	
	#[Kanashi.canCreateNewStandalonePersonalFundraiser]: Bool
	@property
	def canCreateNewStandalonePersonalFundraiser( self ) -> bool: return self['can_create_new_standalone_personal_fundraiser'] if "can_create_new_standalone_personal_fundraiser" in self else False
	
	#[Kanashi.canCreateSponsorTags]: Bool
	@property
	def canCreateSponsorTags( self ) -> bool: return self['can_create_sponsor_tags'] if "can_create_sponsor_tags" in self else False
	
	#[Kanashi.canFollowHashtag]: Bool
	@property
	def canFollowHashtag( self ) -> bool: return self['can_follow_hashtag'] if "can_follow_hashtag" in self else False
	
	#[Kanashi.canHideCategory]: Bool
	@property
	def canHideCategory( self ) -> bool: return self['can_hide_category'] if "can_hide_category" in self else False
	
	#[Kanashi.canLinkEntitiesInBio]: Bool
	@property
	def canLinkEntitiesInBio( self ) -> bool: return self['can_link_entities_in_bio'] if "can_link_entities_in_bio" in self else False
	
	#[Kanashi.canSeeOrganicInsights]: Bool
	@property
	def canSeeOrganicInsights( self ) -> bool: return self['can_see_organic_insights'] if "can_see_organic_insights" in self else False
	
	#[Kanashi.canSeeSupportInbox]: Bool
	@property
	def canSeeSupportInbox( self ) -> bool: return self['can_see_support_inbox'] if "can_see_support_inbox" in self else False
	
	#[Kanashi.canSeeSupportInboxV1]: Bool
	@property
	def canSeeSupportInboxV1( self ) -> bool: return self['can_see_support_inbox_v1'] if "can_see_support_inbox_v1" in self else False
	
	#[Kanashi.canTagProductsFromMerchants]: Bool
	@property
	def canTagProductsFromMerchants( self ) -> bool: return self['can_tag_products_from_merchants'] if "can_tag_products_from_merchants" in self else False
	
	#[Kanashi.canUseAffiliatePartnershipMessagingAsBrand]: Bool
	@property
	def canUseAffiliatePartnershipMessagingAsBrand( self ) -> bool: return self['can_use_affiliate_partnership_messaging_as_brand'] if "can_use_affiliate_partnership_messaging_as_brand" in self else False
	
	#[Kanashi.canUseAffiliatePartnershipMessagingAsCreator]: Bool
	@property
	def canUseAffiliatePartnershipMessagingAsCreator( self ) -> bool: return self['can_use_affiliate_partnership_messaging_as_creator'] if "can_use_affiliate_partnership_messaging_as_creator" in self else False
	
	#[Kanashi.canUseBrandedContentDiscoveryAsBrand]: Bool
	@property
	def canUseBrandedContentDiscoveryAsBrand( self ) -> bool: return self['can_use_branded_content_discovery_as_brand'] if "can_use_branded_content_discovery_as_brand" in self else False
	
	#[Kanashi.canUseBrandedContentDiscoveryAsCreator]: Bool
	@property
	def canUseBrandedContentDiscoveryAsCreator( self ) -> bool: return self['can_use_branded_content_discovery_as_creator'] if "can_use_branded_content_discovery_as_creator" in self else False
	
	#[Kanashi.category]: Any
	@property
	def category( self ) -> any: return self['category'] if "category" in self else None
	
	#[Kanashi.categoryEnum]: Any
	@property
	def categoryEnum( self ) -> any: return self['category_enum'] if "category_enum" in self else None
	
	#[Kanashi.categoryName]: Any
	@property
	def categoryName( self ) -> any: return self['category_name'] if "category_name" in self else None
	
	#[Kanashi.connectedFbPage]: Any
	@property
	def connectedFbPage( self ) -> any: return self['connected_fb_page'] if "connected_fb_page" in self else None
	
	#[Kanashi.countryBlock]: Bool
	@property
	def countryBlock( self ) -> bool: return self['country_block'] if "country_block" in self else False
	
	#[Kanashi.creatorShoppingInfo]: Object
	@property
	def creatorShoppingInfo( self ) -> Object: return self['creator_shopping_info'] if "creator_shopping_info" in self else Object({})
	
	#[Kanashi.creatorsSubscribedToCount]: Int
	@property
	def creatorsSubscribedToCount( self ) -> int: return self['creators_subscribed_to_count'] if "creators_subscribed_to_count" in self else 0
	
	#[Kanashi.currentCatalogId]: Any
	@property
	def currentCatalogId( self ) -> any: return self['current_catalog_id'] if "current_catalog_id" in self else None
	
	#[Kanashi.dailyTimeLimit]: Int
	@property
	def dailyTimeLimit( self ) -> int: return self['daily_time_limit'] if "daily_time_limit" in self else 0
	
	#[Kanashi.displayedActionButtonPartner]: Any
	@property
	def displayedActionButtonPartner( self ) -> any: return self['displayed_action_button_partner'] if "displayed_action_button_partner" in self else None
	
	#[Kanashi.displayedActionButtonType]: Any
	@property
	def displayedActionButtonType( self ) -> any: return self['displayed_action_button_type'] if "displayed_action_button_type" in self else None
	
	#[Kanashi.edgeChaining]: Object
	@property
	def edgeChaining( self ) -> Object: return self['edge_chaining'] if "edge_chaining" in self else Object({})

	#[Kanashi.edgeChainingCount]: Int
	@property
	def edgeChainingCount( self ) -> int: return self.edgeChaining.count if "count" in self.edgeChaining else 0

	#[Kanashi.edgeChainingEdges]: List<Object>
	@property
	def edgeChainingEdges( self ) -> list[Object]: return self.edgeChaining.edges if "edges" in self.edgeChaining else []

	#[Kanashi.edgeChainingPage]: Object
	@property
	def edgeChainingPage( self ) -> Object: return self.edgeChaining.page_info if "page_info" in self.edgeChaining else Object({})
	
	#[Kanashi.edgeFelixCombinedDraftUploads]: Object
	@property
	def edgeFelixCombinedDraftUploads( self ) -> Object: return self['edge_felix_combined_draft_uploads'] if "edge_felix_combined_draft_uploads" in self else Object({})

	#[Kanashi.edgeFelixCombinedDraftUploadsCount]: Int
	@property
	def edgeFelixCombinedDraftUploadsCount( self ) -> int: return self.edgeFelixCombinedDraftUploads.count if "count" in self.edgeFelixCombinedDraftUploads else 0

	#[Kanashi.edgeFelixCombinedDraftUploadsEdges]: List<Object>
	@property
	def edgeFelixCombinedDraftUploadsEdges( self ) -> list[Object]: return self.edgeFelixCombinedDraftUploads.edges if "edges" in self.edgeFelixCombinedDraftUploads else []

	#[Kanashi.edgeFelixCombinedDraftUploadsPage]: Object
	@property
	def edgeFelixCombinedDraftUploadsPage( self ) -> Object: return self.edgeFelixCombinedDraftUploads.page_info if "page_info" in self else Object({})
	
	#[Kanashi.edgeFelixCombinedPostUploads]: Object
	@property
	def edgeFelixCombinedPostUploads( self ) -> Object: return self['edge_felix_combined_post_uploads'] if "edge_felix_combined_post_uploads" in self else Object({})

	#[Kanashi.edgeFelixCombinedPostUploadsCount]: Int
	@property
	def edgeFelixCombinedPostUploadsCount( self ) -> int: return self.edgeFelixCombinedPostUploads.count if "count" in self.edgeFelixCombinedPostUploads else 0

	#[Kanashi.edgeFelixCombinedPostUploadsEdges]: List<Object>
	@property
	def edgeFelixCombinedPostUploadsEdges( self ) -> list[Object]: return self.edgeFelixCombinedPostUploads.edges if "edges" in self.edgeFelixCombinedPostUploads else []
	
	#[Kanashi.edgeFelixCombinedPostUploadsPage]: Object
	@property
	def edgeFelixCombinedPostUploadsPage( self ) -> Object: return self.edgeFelixCombinedPostUploads.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeFelixDrafts]: Object
	@property
	def edgeFelixDrafts( self ) -> Object: return self['edge_felix_drafts'] if "edge_felix_drafts" in self else Object({})

	#[Kanashi.edgeFelixDraftsCount]: Int
	@property
	def edgeFelixDraftsCount( self ) -> int: return self.edgeFelixDrafts.count if "count" in self.edgeFelixDrafts else 0

	#[Kanashi.edgeFelixDraftsEdges]: List<Object>
	@property
	def edgeFelixDraftsEdges( self ) -> list[Object]: return self.edgeFelixDrafts.edges if "edges" in self.edgeFelixDrafts else []

	#[Kanashi.edgeFelixDraftsPage]: Object
	@property
	def edgeFelixDraftsPage( self ) -> Object: return self.edgeFelixDrafts.page_info if "page_info" in self else Object({})
	
	#[Kanashi.edgeFelixPendingDraftUploads]: Object
	@property
	def edgeFelixPendingDraftUploads( self ) -> Object: return self['edge_felix_pending_draft_uploads'] if "edge_felix_pending_draft_uploads" in self else Object({})

	#[Kanashi.edgeFelixPendingDraftUploadsCount]: Int
	@property
	def edgeFelixPendingDraftUploadsCount( self ) -> int: return self.edgeFelixPendingDraftUploads.count if "count" in self.edgeFelixPendingDraftUploads else 0

	#[Kanashi.edgeFelixPendingDraftUploadsEdges]: List<Object>
	@property
	def edgeFelixPendingDraftUploadsEdges( self ) -> list[Object]: return self.edgeFelixPendingDraftUploads.edges if "edges" in self.edgeFelixPendingDraftUploads else []
	
	#[Kanashi.edgeFelixPendingDraftUploadsPage]: Object
	@property
	def edgeFelixPendingDraftUploadsPage( self ) -> Object: return self.edgeFelixPendingDraftUploads.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeFelixPendingPostUploads]: Object
	@property
	def edgeFelixPendingPostUploads( self ) -> Object: return self['edge_felix_pending_post_uploads'] if "edge_felix_pending_post_uploads" in self else Object({})

	#[Kanashi.edgeFelixPendingPostUploadsCOunt]: Int
	@property
	def edgeFelixPendingPostUploadsCount( self ) -> int: return self.edgeFelixPendingPostUploads.count if "count" in self.edgeFelixPendingPostUploads else 0

	#[Kanashi.edgeFelixPendingPostUploadsEdges]: List<Object>
	@property
	def edgeFelixPendingPostUploadsEdges( self ) -> list[Object]: return self.edgeFelixPendingPostUploads.edges if "edges" in self.edgeFelixPendingPostUploads else []

	#[Kanashi.edgeFelixPendingPostUploadsPage]: Object
	@property
	def edgeFelixPendingPostUploadsPage( self ) -> Object: return self.edgeFelixPendingPostUploads.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeFelixVideoTimeline]: Object
	@property
	def edgeFelixVideoTimeline( self ) -> Object: return self['edge_felix_video_timeline'] if "edge_felix_video_timeline" in self else Object({})

	#[Kanashi.edgeFelixVideoTimelineCount]: Int
	@property
	def edgeFelixVideoTimelineCount( self ) -> int: return self.edgeFelixVideoTimeline.count if "count" in self.edgeFelixVideoTimeline else 0

	#[Kanashi.edgeFelixVideoTimeline]: List<Object>
	@property
	def edgeFelixVideoTimelineEdges( self ) -> list[Object]: return self.edgeFelixVideoTimeline.edges if "edges" in self else []
	
	#[Kanashi.edgeFelixVideoTimelinePage]: Object
	@property
	def edgeFelixVideoTimelinePage( self ) -> Object: return self.edgeFelixVideoTimeline.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeFollow]: Object
	@property
	def edgeFollow( self ) -> Object: return self['edge_follow'] if "edge_follow" in self else Object({})

	#[Kanashi.edgeFollowCount]: Int
	@property
	def edgeFollowCount( self ) -> int: return self.edgeFollow.count if "count" in self.edgeFollow else 0

	#[Kanashi.edgeFollowEdges]: List<Object>
	@property
	def edgeFollowEdges( self ) -> list[Object]: return self.edgeFollow.edges if "edges" in self else []
	
	#[Kanashi.edgeFollowPage]: Object
	@property
	def edgeFollowPage( self ) -> Object: return self.edgeFollow.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeFollowedBy]: Object
	@property
	def edgeFollowedBy( self ) -> Object: return self['edge_followed_by'] if "edge_followed_by" in self else Object({})

	#[Kanashi.edgeFollowedByCount]: Int
	@property
	def edgeFollowedByCount( self ) -> int: return self.edgeFollowedBy.count if "count" in self.edgeFollowedBy else 0

	#[Kanashi.edgeFollowedByEdges]: List<Object>
	@property
	def edgeFollowedByEdges( self ) -> list[Object]: return self.edgeFollowedBy.edges if "edges" in self.edgeFollowedBy else []
	
	#[Kanashi.edgeFollowedByPage]: Object
	@property
	def edgeFollowedByPage( self ) -> Object: return self.edgeFollowedBy.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeHighlightReels]: Object
	@property
	def edgeHighlightReels( self ) -> Object: return self['edge_highlight_reels'] if "edge_highlight_reels" in self else Object({})

	#[Kanashi.edgeHighlightReelsCount]: Int
	@property
	def edgeHighlightReelsCount( self ) -> int: return self.edgeHighlightReels.count if "count" in self.edgeHighlightReels else 0

	#[Kanashi.edgeHighlightReelsEdges]: List<Object>
	@property
	def edgeHighlightReelsEdges( self ) -> list[Object]: return self.edgeHighlightReels.edges if "edges" in self.edgeHighlightReels else []
	
	#[Kanashi.edgeHighlightReelsPage]: Object
	@property
	def edgeHighlightReelsPage( self ) -> Object: return self.edgeHighlightReels.page_info if "page_info" in self else Object({})
	
	#[Kanashi.edgeMediaCollections]: Object
	@property
	def edgeMediaCollections( self ) -> Object: return self['edge_media_collections'] if "edge_media_collections" in self else Object({})

	#[Kanashi.edgeMediaCollectionsCount]: Int
	@property
	def edgeMediaCollectionsCount( self ) -> int: return self.edgeMediaCollections.count if "count" in self.edgeMediaCollections else 0

	#[Kanashi.edgeMediaCollectionsEdges]: List<Object>
	@property
	def edgeMediaCollectionsEdges( self ) -> list[Object]: return self.edgeMediaCollections.edges if "edges" in self.edgeMediaCollections else []
	
	#[Kanashi.edgeMediaCollectionsPage]: Object
	@property
	def edgeMediaCollectionsPage( self ) -> Object: return self.edgeMediaCollections.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeMutualFollowedBy]: Object
	@property
	def edgeMutualFollowedBy( self ) -> Object: return self['edge_mutual_followed_by'] if "edge_mutual_followed_by" in self else Object({})

	#[Kanashi.edgeMutualFollowedByCount]: Int
	@property
	def edgeMutualFollowedByCount( self ) -> int: return self.edgeMutualFollowedBy.count if "count" in self.edgeMutualFollowedBy else 0

	#[Kanashi.edgeMutualFollowedByEdges]: List<Object>
	@property
	def edgeMutualFollowedByEdges( self ) -> list[Object]: return self.edgeMutualFollowedBy.edges if "edges" in self.edgeMutualFollowedBy else []
	
	#[Kanashi.edgeMutualFollowedByPage]: Object
	@property
	def edgeMutualFollowedByPage( self ) -> Object: return self.edgeMutualFollowedBy.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeOwnerToTimelineMedia]: Object
	@property
	def edgeOwnerToTimelineMedia( self ) -> Object: return self['edge_owner_to_timeline_media'] if "edge_owner_to_timeline_media" in self else Object({})

	#[Kanashi.edgeOwnerToTimelineMediaCount]: Int
	@property
	def edgeOwnerToTimelineMediaCount( self ) -> int: return self.edgeOwnerToTimelineMedia.count if "count" in self.edgeOwnerToTimelineMedia else 0

	#[Kanashi.edgeOwnerToTimelineMediaEdges]: List<Object>
	@property
	def edgeOwnerToTimelineMediaEdges( self ) -> list[Object]: return self.edgeOwnerToTimelineMedia.edges if "edges" in self.edgeOwnerToTimelineMedia else []
	
	#[Kanashi.edgeOwnerToTimelineMediaPage]: Object
	@property
	def edgeOwnerToTimelineMediaPage( self ) -> Object: return self.edgeOwnerToTimelineMedia.page_info if "page_info" in self else Object({})

	#[Kanashi.edgeSavedMedia]: Object
	@property
	def edgeSavedMedia( self ) -> Object: return self['edge_saved_media'] if "edge_saved_media" in self else Object({})

	#[Kanashi.edgeSavedMediaCount]: Int
	@property
	def edgeSavedMediaCount( self ) -> int: return self.edgeSavedMedia.count if "count" in self.edgeSavedMedia else 0

	#[Kanashi.edgeSavedMediaEdges]: List<Object>
	@property
	def edgeSavedMediaEdges( self ) -> list[Object]: return self.edgeSavedMedia.edges if "edges" in self.edgeSavedMedia else []

	#[Kanashi.edgeSavedMediaPage]: Object
	@property
	def edgeSavedMediaPage( self ) -> Object: return self.edgeSavedMedia.page_info if "page_info" in self else Object({})
	
	#[Kanashi.eimuId]: Str
	@property
	def eimuId( self ) -> str: return self['eimu_id'] if "eimu_id" in self else None
	
	#[Kanashi.eligibleShoppingFormats]: List
	@property
	def eligibleShoppingFormats( self ) -> list: return self['eligible_shopping_formats'] if "eligible_shopping_formats" in self else []
	
	#[Kanashi.eligibleShoppingSignupEntrypoints]: List
	@property
	def eligibleShoppingSignupEntrypoints( self ) -> list: return self['eligible_shopping_signup_entrypoints'] if "eligible_shopping_signup_entrypoints" in self else []
	
	#[Kanashi.existingUserAgeCollectionEnabled]: Bool
	@property
	def existingUserAgeCollectionEnabled( self ) -> bool: return self['existing_user_age_collection_enabled'] if "existing_user_age_collection_enabled" in self else False
	
	#[Kanashi.externalUrl]: Str
	@property
	def externalUrl( self ) -> str: return self['external_url'] if "external_url" in self else None
	
	#[Kanashi.externalUrlLinkshimmed]: Any
	@property
	def externalUrlLinkshimmed( self ) -> any: return self['external_url_linkshimmed'] if "external_url_linkshimmed" in self else None
	
	#[Kanashi.fanClubInfo]: Object
	@property
	def fanClubInfo( self ) -> Object: return self['fan_club_info'] if "fan_club_info" in self else Object({})
	
	#[Kanashi.fbProfileBiolink]: Any
	@property
	def fbProfileBiolink( self ) -> any: return self['fb_profile_biolink'] if "fb_profile_biolink" in self else None
	
	#[Kanashi.fbid]: Str
	@property
	def fbid( self ) -> str: return self['fbid'] if "fbid" in self else None
	
	#[Kanashi.fbidV2]: Str
	@property
	def fbidV2( self ) -> str: return self['fbid_v2'] if "fbid_v2" in self else None
	
	#[Kanashi.fbpayExperienceEnabled]: Bool
	@property
	def fbpayExperienceEnabled( self ) -> bool: return self['fbpay_experience_enabled'] if "fbpay_experience_enabled" in self else False
	
	#[Kanashi.feedPostReshareDisabled]: Bool
	@property
	def feedPostReshareDisabled( self ) -> bool: return self['feed_post_reshare_disabled'] if "feed_post_reshare_disabled" in self else False
	
	#[Kanashi.followFrictionType]: Int
	@property
	def followFrictionType( self ) -> int: return self['follow_friction_type'] if "follow_friction_type" in self else 0
	
	#[Kanashi.followedBy]: Bool
	@property
	def followedBy( self ) -> bool: return self['followed_by'] if "followed_by" in self else False
	
	#[Kanashi.followedByViewer]: Bool
	@property
	def followedByViewer( self ) -> bool: return self['followed_by_viewer'] if "followed_by_viewer" in self else False
	
	#[Kanashi.followerCount]: Int
	@property
	def followerCount( self ) -> int: return self['follower_count'] if "follower_count" in self else 0
	
	#[Kanashi.following]: Bool
	@property
	def following( self ) -> bool: return self['following'] if "following" in self else False
	
	#[Kanashi.followingCount]: Int
	@property
	def followingCount( self ) -> int: return self['following_count'] if "following_count" in self else 0
	
	#[Kanashi.followingTagCount]: Int
	@property
	def followingTagCount( self ) -> int: return self['following_tag_count'] if "following_tag_count" in self else 0
	
	#[Kanashi.followsViewer]: Bool
	@property
	def followsViewer( self ) -> bool: return self['follows_viewer'] if "follows_viewer" in self else False
	
	#[Kanashi.fullName]: Str
	@property
	def fullName( self ) -> str: return self['full_name'] if "full_name" in self else None
	
	#[Kanashi.groupMetadata]: Any
	@property
	def groupMetadata( self ) -> any: return self['group_metadata'] if "group_metadata" in self else None
	
	#[Kanashi.guardianId]: Any
	@property
	def guardianId( self ) -> any: return self['guardian_id'] if "guardian_id" in self else None
	
	#[Kanashi.hasAnonymousProfilePicture]: Bool
	@property
	def hasAnonymousProfilePicture( self ) -> bool: return self['has_anonymous_profile_picture'] if "has_anonymous_profile_picture" in self else False
	
	#[Kanashi.hasArEffects]: Bool
	@property
	def hasArEffects( self ) -> bool: return self['has_ar_effects'] if "has_ar_effects" in self else False
	
	#[Kanashi.hasBlockedViewer]: Bool
	@property
	def hasBlockedViewer( self ) -> bool: return self['has_blocked_viewer'] if "has_blocked_viewer" in self else False
	
	#[Kanashi.hasChannel]: Bool
	@property
	def hasChannel( self ) -> bool: return self['has_channel'] if "has_channel" in self else False
	
	#[Kanashi.hasClips]: Bool
	@property
	def hasClips( self ) -> bool: return self['has_clips'] if "has_clips" in self else False
	
	#[Kanashi.hasCollabCollections]: Bool
	@property
	def hasCollabCollections( self ) -> bool: return self['has_collab_collections'] if "has_collab_collections" in self else False
	
	#[Kanashi.hasExclusiveFeedContent]: Bool
	@property
	def hasExclusiveFeedContent( self ) -> bool: return self['has_exclusive_feed_content'] if "has_exclusive_feed_content" in self else False
	
	#[Kanashi.hasFanClubSubscriptions]: Bool
	@property
	def hasFanClubSubscriptions( self ) -> bool: return self['has_fan_club_subscriptions'] if "has_fan_club_subscriptions" in self else False
	
	#[Kanashi.hasGroups]: Bool
	@property
	def hasGroups( self ) -> bool: return self['has_groups'] if "has_groups" in self else False
	
	#[Kanashi.hasGuides]: Bool
	@property
	def hasGuides( self ) -> bool: return self['has_guides'] if "has_guides" in self else False
	
	#[Kanashi.hasHighlightReels]: Bool
	@property
	def hasHighlightReels( self ) -> bool: return self['has_highlight_reels'] if "has_highlight_reels" in self else False
	
	#[Kanashi.hasMusicOnProfile]: Bool
	@property
	def hasMusicOnProfile( self ) -> bool: return self['has_music_on_profile'] if "has_music_on_profile" in self else False
	
	#[Kanashi.hasOnboardedToTextPostApp]: Bool
	@property
	def hasOnboardedToTextPostApp( self ) -> bool: return self['has_onboarded_to_text_post_app'] if "has_onboarded_to_text_post_app" in self else False
	
	#[Kanashi.hasPlacedOrders]: Bool
	@property
	def hasPlacedOrders( self ) -> bool: return self['has_placed_orders'] if "has_placed_orders" in self else False
	
	#[Kanashi.hasPrivateCollections]: Bool
	@property
	def hasPrivateCollections( self ) -> bool: return self['has_private_collections'] if "has_private_collections" in self else False
	
	#[Kanashi.hasPublicTabThreads]: Bool
	@property
	def hasPublicTabThreads( self ) -> bool: return self['has_public_tab_threads'] if "has_public_tab_threads" in self else False
	
	#[Kanashi.hasRequestedViewer]: Bool
	@property
	def hasRequestedViewer( self ) -> bool: return self['has_requested_viewer'] if "has_requested_viewer" in self else False
	
	#[Kanashi.hasSavedItems]: Bool
	@property
	def hasSavedItems( self ) -> bool: return self['has_saved_items'] if "has_saved_items" in self else False
	
	#[Kanashi.hasUserEverSetBreak]: Bool
	@property
	def hasUserEverSetBreak( self ) -> bool: return self['has_user_ever_set_break'] if "has_user_ever_set_break" in self else False
	
	#[Kanashi.hasVideos]: Bool
	@property
	def hasVideos( self ) -> bool: return self['has_videos'] if "has_videos" in self else False
	
	#[Kanashi.hdProfilePicUrlInfo]: Object
	@property
	def hdProfilePicUrlInfo( self ) -> Object: return self['hd_profile_pic_url_info'] if "hd_profile_pic_url_info" in self else Object({})
	
	#[Kanashi.hdProfilePicVersions]: List
	@property
	def hdProfilePicVersions( self ) -> list: return self['hd_profile_pic_versions'] if "hd_profile_pic_versions" in self else []
	
	#[Kanashi.hideLikeAndViewCounts]: Bool
	@property
	def hideLikeAndViewCounts( self ) -> bool: return self['hide_like_and_view_counts'] if "hide_like_and_view_counts" in self else False
	
	#[Kanashi.highlightReelCount]: Int
	@property
	def highlightReelCount( self ) -> int: return self['highlight_reel_count'] if "highlight_reel_count" in self else 0
	
	#[Kanashi.highlightReshareDisabled]: Bool
	@property
	def highlightReshareDisabled( self ) -> bool: return self['highlight_reshare_disabled'] if "highlight_reshare_disabled" in self else False
	
	#[Kanashi.id]: Str
	@property
	def id( self ) -> str: return self['id'] if "id" in self else self.pk
	
	#[Kanashi.includeDirectBlacklistStatus]: Bool
	@property
	def includeDirectBlacklistStatus( self ) -> bool: return self['include_direct_blacklist_status'] if "include_direct_blacklist_status" in self else False
	
	#[Kanashi.incomingRequest]: Bool
	@property
	def incomingRequest( self ) -> bool: return self['incoming_request'] if "incoming_request" in self else False
	
	#[Kanashi.interopMessagingUserFbid]: Str
	@property
	def interopMessagingUserFbid( self ) -> str: return self['interop_messaging_user_fbid'] if "interop_messaging_user_fbid" in self else None
	
	#[Kanashi.isAllowedToCreateStandaloneNonprofitFundraisers]: Bool
	@property
	def isAllowedToCreateStandaloneNonprofitFundraisers( self ) -> bool: return self['is_allowed_to_create_standalone_nonprofit_fundraisers'] if "is_allowed_to_create_standalone_nonprofit_fundraisers" in self else False
	
	#[Kanashi.isAllowedToCreateStandalonePersonalFundraisers]: Bool
	@property
	def isAllowedToCreateStandalonePersonalFundraisers( self ) -> bool: return self['is_allowed_to_create_standalone_personal_fundraisers'] if "is_allowed_to_create_standalone_personal_fundraisers" in self else False
	
	#[Kanashi.isApiUser]: Bool
	@property
	def isApiUser( self ) -> bool: return self['is_api_user'] if "is_api_user" in self else False
	
	#[Kanashi.isBestie]: Bool
	@property
	def isBestie( self ) -> bool: return self['is_bestie'] if "is_bestie" in self else False
	
	#[Kanashi.isBlockingReel]: Bool
	@property
	def isBlockingReel( self ) -> bool: return self['is_blocking_reel'] if "is_blocking_reel" in self else False
	
	#[Kanashi.isBusiness]: Bool
	@property
	def isBusiness( self ) -> bool: return self['is_business'] if "is_business" in self else False
	
	#[Kanashi.isBusinessAccount]: Bool
	@property
	def isBusinessAccount( self ) -> bool: return self['is_business_account'] if "is_business_account" in self else False
	
	#[Kanashi.isCallToActionEnabled]: Any
	@property
	def isCallToActionEnabled( self ) -> any: return self['is_call_to_action_enabled'] if "is_call_to_action_enabled" in self else None
	
	#[Kanashi.isCategoryTappable]: Bool
	@property
	def isCategoryTappable( self ) -> bool: return self['is_category_tappable'] if "is_category_tappable" in self else False
	
	#[Kanashi.isDirectRollCallEnabled]: Bool
	@property
	def isDirectRollCallEnabled( self ) -> bool: return self['is_direct_roll_call_enabled'] if "is_direct_roll_call_enabled" in self else False
	
	#[Kanashi.isEligibleToShowFbCrossSharingNux]: Bool
	@property
	def isEligibleToShowFbCrossSharingNux( self ) -> bool: return self['is_eligible_to_show_fb_cross_sharing_nux'] if "is_eligible_to_show_fb_cross_sharing_nux" in self else False
	
	#[Kanashi.isEligibleToSubscribe]: Bool
	@property
	def isEligibleToSubscribe( self ) -> bool: return self['is_eligible_to_subscribe'] if "is_eligible_to_subscribe" in self else False
	
	#[Kanashi.isEmbedsDisabled]: Bool
	@property
	def isEmbedsDisabled( self ) -> bool: return self['is_embeds_disabled'] if "is_embeds_disabled" in self else False
	
	#[Kanashi.isFavorite]: Bool
	@property
	def isFavorite( self ) -> bool: return self['is_favorite'] if "is_favorite" in self else False
	
	#[Kanashi.isFeedFavorite]: Bool
	@property
	def isFeedFavorite( self ) -> bool: return self['is_feed_favorite'] if "is_feed_favorite" in self else False
	
	#[Kanashi.isGuardianOfViewer]: Bool
	@property
	def isGuardianOfViewer( self ) -> bool: return self['is_guardian_of_viewer'] if "is_guardian_of_viewer" in self else False
	
	#[Kanashi.isHideMoreCommentEnabled]: Bool
	@property
	def isHideMoreCommentEnabled( self ) -> bool: return self['is_hide_more_comment_enabled'] if "is_hide_more_comment_enabled" in self else False
	
	#[Kanashi.isIgdProductPickerEnabled]: Bool
	@property
	def isIgdProductPickerEnabled( self ) -> bool: return self['is_igd_product_picker_enabled'] if "is_igd_product_picker_enabled" in self else False
	
	#[Kanashi.isInCanada]: Bool
	@property
	def isInCanada( self ) -> bool: return self['is_in_canada'] if "is_in_canada" in self else False
	
	#[Kanashi.isInterestAccount]: Bool
	@property
	def isInterestAccount( self ) -> bool: return self['is_interest_account'] if "is_interest_account" in self else False
	
	#[Kanashi.isJoinedRecently]: Bool
	@property
	def isJoinedRecently( self ) -> bool: return self['is_joined_recently'] if "is_joined_recently" in self else False
	
	#[Kanashi.isMemorialized]: Bool
	@property
	def isMemorialized( self ) -> bool: return self['is_memorialized'] if "is_memorialized" in self else False
	
	#[Kanashi.isMutedWordsCustomEnabled]: Bool
	@property
	def isMutedWordsCustomEnabled( self ) -> bool: return self['is_muted_words_custom_enabled'] if "is_muted_words_custom_enabled" in self else False
	
	#[Kanashi.isMutedWordsGlobalEnabled]: Bool
	@property
	def isMutedWordsGlobalEnabled( self ) -> bool: return self['is_muted_words_global_enabled'] if "is_muted_words_global_enabled" in self else False
	
	#[Kanashi.isMutedWordsSpamscamEnabled]: Bool
	@property
	def isMutedWordsSpamscamEnabled( self ) -> bool: return self['is_muted_words_spamscam_enabled'] if "is_muted_words_spamscam_enabled" in self else False
	
	#[Kanashi.isMutingMediaNotes]: Bool
	@property
	def isMutingMediaNotes( self ) -> bool: return self['is_muting_media_notes'] if "is_muting_media_notes" in self else False
	
	#[Kanashi.isMutingNotes]: Bool
	@property
	def isMutingNotes( self ) -> bool: return self['is_muting_notes'] if "is_muting_notes" in self else False
	
	#[Kanashi.isMutingReel]: Bool
	@property
	def isMutingReel( self ) -> bool: return self['is_muting_reel'] if "is_muting_reel" in self else False

	#[Profile.isMySelf]: Bool
	@property
	def isMySelf( self ) -> bool:
		if "viewer" in self:
			id = self.viewer.id if "id" in self.viewer else 0
			pk = self.id if "id" in self else self.pk if "pk" in self else 0
			return id != 0 and pk != 0 and id == pk
		return False
	
	#[Profile.isNotMySelf]: Bool
	@property
	def isNotMySelf( self ) -> bool: return self.isMySelf is False
	
	#[Kanashi.isNeedy]: Bool
	@property
	def isNeedy( self ) -> bool: return self['is_needy'] if "is_needy" in self else False
	
	#[Kanashi.isNewToInstagram]: Bool
	@property
	def isNewToInstagram( self ) -> bool: return self['is_new_to_instagram'] if "is_new_to_instagram" in self else False
	
	#[Kanashi.isOpalEnabled]: Bool
	@property
	def isOpalEnabled( self ) -> bool: return self['is_opal_enabled'] if "is_opal_enabled" in self else False
	
	#[Kanashi.isPotentialBusiness]: Bool
	@property
	def isPotentialBusiness( self ) -> bool: return self['is_potential_business'] if "is_potential_business" in self else False
	
	#[Kanashi.isPrivate]: Bool
	@property
	def isPrivate( self ) -> bool: return self['is_private'] if "is_private" in self else False
	
	#[Kanashi.isProfessionalAccount]: Bool
	@property
	def isProfessionalAccount( self ) -> bool: return self['is_professional_account'] if "is_professional_account" in self else False
	
	#[Kanashi.isProfileActionNeeded]: Bool
	@property
	def isProfileActionNeeded( self ) -> bool: return self['is_profile_action_needed'] if "is_profile_action_needed" in self else False
	
	#[Kanashi.isProfileBroadcastSharingEnabled]: Bool
	@property
	def isProfileBroadcastSharingEnabled( self ) -> bool: return self['is_profile_broadcast_sharing_enabled'] if "is_profile_broadcast_sharing_enabled" in self else False
	
	#[Kanashi.isProfilePictureExpansionEnabled]: Bool
	@property
	def isProfilePictureExpansionEnabled( self ) -> bool: return self['is_profile_picture_expansion_enabled'] if "is_profile_picture_expansion_enabled" in self else False
	
	#[Kanashi.isQuietModeEnabled]: Bool
	@property
	def isQuietModeEnabled( self ) -> bool: return self['is_quiet_mode_enabled'] if "is_quiet_mode_enabled" in self else False
	
	#[Kanashi.isRegulatedC18]: Bool
	@property
	def isRegulatedC18( self ) -> bool: return self['is_regulated_c18'] if "is_regulated_c18" in self else False
	
	#[Kanashi.isRestricted]: Bool
	@property
	def isRestricted( self ) -> bool: return self['is_restricted'] if "is_restricted" in self else False
	
	#[Kanashi.isSecondaryAccountCreation]: Bool
	@property
	def isSecondaryAccountCreation( self ) -> bool: return self['is_secondary_account_creation'] if "is_secondary_account_creation" in self else False
	
	#[Kanashi.isShoppingAutoHighlightEligible]: Bool
	@property
	def isShoppingAutoHighlightEligible( self ) -> bool: return self['is_shopping_auto_highlight_eligible'] if "is_shopping_auto_highlight_eligible" in self else False
	
	#[Kanashi.isShoppingCatalogSourceSelectionEnabled]: Bool
	@property
	def isShoppingCatalogSourceSelectionEnabled( self ) -> bool: return self['is_shopping_catalog_source_selection_enabled'] if "is_shopping_catalog_source_selection_enabled" in self else False
	
	#[Kanashi.isShoppingCommunityContentEnabled]: Bool
	@property
	def isShoppingCommunityContentEnabled( self ) -> bool: return self['is_shopping_community_content_enabled'] if "is_shopping_community_content_enabled" in self else False
	
	#[Kanashi.isShoppingSettingsEnabled]: Bool
	@property
	def isShoppingSettingsEnabled( self ) -> bool: return self['is_shopping_settings_enabled'] if "is_shopping_settings_enabled" in self else False
	
	#[Kanashi.isSupervisedByViewer]: Bool
	@property
	def isSupervisedByViewer( self ) -> bool: return self['is_supervised_by_viewer'] if "is_supervised_by_viewer" in self else False
	
	#[Kanashi.isSupervisedUser]: Bool
	@property
	def isSupervisedUser( self ) -> bool: return self['is_supervised_user'] if "is_supervised_user" in self else False
	
	#[Kanashi.isSupervisionEnabled]: Bool
	@property
	def isSupervisionEnabled( self ) -> bool: return self['is_supervision_enabled'] if "is_supervision_enabled" in self else False
	
	#[Kanashi.isSupervisionFeaturesEnabled]: Bool
	@property
	def isSupervisionFeaturesEnabled( self ) -> bool: return self['is_supervision_features_enabled'] if "is_supervision_features_enabled" in self else False
	
	#[Kanashi.isVerified]: Bool
	@property
	def isVerified( self ) -> bool: return self['is_verified'] if "is_verified" in self else False
	
	#[Kanashi.isVerifiedByMv4b]: Bool
	@property
	def isVerifiedByMv4b( self ) -> bool: return self['is_verified_by_mv4b'] if "is_verified_by_mv4b" in self else False
	
	#[Kanashi.isWhatsappLinked]: Bool
	@property
	def isWhatsappLinked( self ) -> bool: return self['is_whatsapp_linked'] if "is_whatsapp_linked" in self else False
	
	#[Kanashi.lastSeenTimezone]: Str
	@property
	def lastSeenTimezone( self ) -> str: return self['last_seen_timezone'] if "last_seen_timezone" in self else None
	
	#[Kanashi.limitedInteractionsEnabled]: Bool
	@property
	def limitedInteractionsEnabled( self ) -> bool: return self['limited_interactions_enabled'] if "limited_interactions_enabled" in self else False
	
	#[Kanashi.linkedFbInfo]: Object
	@property
	def linkedFbInfo( self ) -> Object: return self['linked_fb_info'] if "linked_fb_info" in self else Object({})
	
	#[Kanashi.mediaCount]: Int
	@property
	def mediaCount( self ) -> int: return self['media_count'] if "media_count" in self else 0
	
	#[Kanashi.miniShopSellerOnboardingStatus]: Any
	@property
	def miniShopSellerOnboardingStatus( self ) -> any: return self['mini_shop_seller_onboarding_status'] if "mini_shop_seller_onboarding_status" in self else None
	
	#[Kanashi.muting]: Bool
	@property
	def muting( self ) -> bool: return self['muting'] if "muting" in self else False
	
	#[Kanashi.mutualFollowersCount]: Int
	@property
	def mutualFollowersCount( self ) -> int: return self['mutual_followers_count'] if "mutual_followers_count" in self else 0
	
	#[Kanashi.nametag]: Any
	@property
	def nametag( self ) -> any: return self['nametag'] if "nametag" in self else None
	
	#[Kanashi.needsToAcceptShoppingSellerOnboardingTerms]: Bool
	@property
	def needsToAcceptShoppingSellerOnboardingTerms( self ) -> bool: return self['needs_to_accept_shopping_seller_onboarding_terms'] if "needs_to_accept_shopping_seller_onboarding_terms" in self else False
	
	#[Kanashi.numOfAdminedPages]: Any
	@property
	def numOfAdminedPages( self ) -> any: return self['num_of_admined_pages'] if "num_of_admined_pages" in self else None
	
	#[Kanashi.opalInfo]: Object
	@property
	def opalInfo( self ) -> Object: return self['opal_info'] if "opal_info" in self else Object({})
	
	#[Kanashi.openExternalUrlWithInAppBrowser]: Bool
	@property
	def openExternalUrlWithInAppBrowser( self ) -> bool: return self['open_external_url_with_in_app_browser'] if "open_external_url_with_in_app_browser" in self else False
	
	#[Kanashi.outgoingRequest]: Bool
	@property
	def outgoingRequest( self ) -> bool: return self['outgoing_request'] if "outgoing_request" in self else False
	
	#[Kanashi.overallCategoryName]: Any
	@property
	def overallCategoryName( self ) -> any: return self['overall_category_name'] if "overall_category_name" in self else None
	
	#[Kanashi.pageId]: Any
	@property
	def pageId( self ) -> any: return self['page_id'] if "page_id" in self else None
	
	#[Kanashi.pageName]: Any
	@property
	def pageName( self ) -> any: return self['page_name'] if "page_name" in self else None
	
	#[Kanashi.pinnedChannelsInfo]: Object
	@property
	def pinnedChannelsInfo( self ) -> Object: return self['pinned_channels_info'] if "pinned_channels_info" in self else Object({})
	
	#[Kanashi.pinnedChannelsListCount]: Int
	@property
	def pinnedChannelsListCount( self ) -> int: return self['pinned_channels_list_count'] if "pinned_channels_list_count" in self else 0
	
	#[Kanashi.pk]: Str
	@property
	def pk( self ) -> str: return self['pk'] if "pk" in self else self.id
	
	#[Kanashi.pkId]: Str
	@property
	def pkId( self ) -> str: return self['pk_id'] if "pk_id" in self else None
	
	#[Kanashi.primaryProfileLinkType]: Int
	@property
	def primaryProfileLinkType( self ) -> int: return self['primary_profile_link_type'] if "primary_profile_link_type" in self else 0
	
	#[Kanashi.professionalConversionSuggestedAccountType]: Int
	@property
	def professionalConversionSuggestedAccountType( self ) -> int: return self['professional_conversion_suggested_account_type'] if "professional_conversion_suggested_account_type" in self else 0
	
	#[Kanashi.profileContext]: Str
	@property
	def profileContext( self ) -> str: return self['profile_context'] if "profile_context" in self else None
	
	#[Kanashi.profileContextFacepileUsers]: List
	@property
	def profileContextFacepileUsers( self ) -> list: return self['profile_context_facepile_users'] if "profile_context_facepile_users" in self else []
	
	#[Kanashi.profileContextLinksWithUserIds]: List
	@property
	def profileContextLinksWithUserIds( self ) -> list: return self['profile_context_links_with_user_ids'] if "profile_context_links_with_user_ids" in self else []
	
	#[Kanashi.profileContextMutualFollowIds]: List
	@property
	def profileContextMutualFollowIds( self ) -> list: return self['profile_context_mutual_follow_ids'] if "profile_context_mutual_follow_ids" in self else []
	
	#[Kanashi.profilePicId]: Str
	@property
	def profilePicId( self ) -> str: return self['profile_pic_id'] if "profile_pic_id" in self else None
	
	#[Kanashi.profilePicUrl]: Str
	@property
	def profilePicUrl( self ) -> str: return self['profile_pic_url'] if "profile_pic_url" in self else None
	
	#[Kanashi.profilePicUrlHd]: Str
	@property
	def profilePicUrlHd( self ) -> str: return self['profile_pic_url_hd'] if "profile_pic_url_hd" in self else None
	
	#[Kanashi.profileType]: Int
	@property
	def profileType( self ) -> int: return self['profile_type'] if "profile_type" in self else 0
	
	#[Kanashi.pronouns]: List
	@property
	def pronouns( self ) -> list: return self['pronouns'] if "pronouns" in self else []

	#[Profile.pronounsFormat]: Str
	@property
	def pronounsFormat( self ) -> str: return "/".join( self.pronouns )
	
	#[Kanashi.recentlyBestiedByCount]: Int
	@property
	def recentlyBestiedByCount( self ) -> int: return self['recently_bestied_by_count'] if "recently_bestied_by_count" in self else 0
	
	#[Kanashi.recsFromFriends]: Object
	@property
	def recsFromFriends( self ) -> Object: return self['recs_from_friends'] if "recs_from_friends" in self else Object({})
	
	#[Kanashi.reelAutoArchive]: Str
	@property
	def reelAutoArchive( self ) -> str: return self['reel_auto_archive'] if "reel_auto_archive" in self else None
	
	#[Kanashi.removeMessageEntrypoint]: Bool
	@property
	def removeMessageEntrypoint( self ) -> bool: return self['remove_message_entrypoint'] if "remove_message_entrypoint" in self else False
	
	#[Kanashi.requestedByViewer]: Bool
	@property
	def requestedByViewer( self ) -> bool: return self['requested_by_viewer'] if "requested_by_viewer" in self else False
	
	#[Kanashi.restrictedByViewer]: Bool
	@property
	def restrictedByViewer( self ) -> bool: return self['restricted_by_viewer'] if "restricted_by_viewer" in self else False
	
	#[Kanashi.robiFeedbackSource]: Any
	@property
	def robiFeedbackSource( self ) -> any: return self['robi_feedback_source'] if "robi_feedback_source" in self else None
	
	#[Kanashi.shoppingPostOnboardNuxType]: Any
	@property
	def shoppingPostOnboardNuxType( self ) -> any: return self['shopping_post_onboard_nux_type'] if "shopping_post_onboard_nux_type" in self else None
	
	#[Kanashi.shouldShowCategory]: Bool
	@property
	def shouldShowCategory( self ) -> bool: return self['should_show_category'] if "should_show_category" in self else False
	
	#[Kanashi.shouldShowPublicContacts]: Bool
	@property
	def shouldShowPublicContacts( self ) -> bool: return self['should_show_public_contacts'] if "should_show_public_contacts" in self else False
	
	#[Kanashi.showAccountTransparencyDetails]: Bool
	@property
	def showAccountTransparencyDetails( self ) -> bool: return self['show_account_transparency_details'] if "show_account_transparency_details" in self else False
	
	#[Kanashi.showBestiesBadge]: Bool
	@property
	def showBestiesBadge( self ) -> bool: return self['show_besties_badge'] if "show_besties_badge" in self else False
	
	#[Kanashi.showConversionEditEntry]: Bool
	@property
	def showConversionEditEntry( self ) -> bool: return self['show_conversion_edit_entry'] if "show_conversion_edit_entry" in self else False
	
	#[Kanashi.showFbLinkOnProfile]: Bool
	@property
	def showFbLinkOnProfile( self ) -> bool: return self['show_fb_link_on_profile'] if "show_fb_link_on_profile" in self else False
	
	#[Kanashi.showFbPageLinkOnProfile]: Bool
	@property
	def showFbPageLinkOnProfile( self ) -> bool: return self['show_fb_page_link_on_profile'] if "show_fb_page_link_on_profile" in self else False
	
	#[Kanashi.showInsightsTerms]: Bool
	@property
	def showInsightsTerms( self ) -> bool: return self['show_insights_terms'] if "show_insights_terms" in self else False
	
	#[Kanashi.showPostInsightsEntryPoint]: Bool
	@property
	def showPostInsightsEntryPoint( self ) -> bool: return self['show_post_insights_entry_point'] if "show_post_insights_entry_point" in self else False
	
	#[Kanashi.showTogetherPog]: Bool
	@property
	def showTogetherPog( self ) -> bool: return self['show_together_pog'] if "show_together_pog" in self else False
	
	#[Kanashi.smbDeliveryPartner]: Any
	@property
	def smbDeliveryPartner( self ) -> any: return self['smb_delivery_partner'] if "smb_delivery_partner" in self else None
	
	#[Kanashi.smbSupportDeliveryPartner]: Any
	@property
	def smbSupportDeliveryPartner( self ) -> any: return self['smb_support_delivery_partner'] if "smb_support_delivery_partner" in self else None
	
	#[Kanashi.smbSupportPartner]: Any
	@property
	def smbSupportPartner( self ) -> any: return self['smb_support_partner'] if "smb_support_partner" in self else None
	
	#[Kanashi.status]: Str
	@property
	def status( self ) -> str: return self['status'] if "status" in self else None
	
	#[Kanashi.strongId]: Str
	@property
	def strongId( self ) -> str: return self['strong_id__'] if "strong_id__" in self else None
	
	#[Kanashi.subscribed]: Bool
	@property
	def subscribed( self ) -> bool: return self['subscribed'] if "subscribed" in self else False
	
	#[Kanashi.supervisionInfo]: Object
	@property
	def supervisionInfo( self ) -> Object: return self['supervision_info'] if "supervision_info" in self else Object({})
	
	#[Kanashi.thirdPartyDownloadsEnabled]: Int
	@property
	def thirdPartyDownloadsEnabled( self ) -> int: return self['third_party_downloads_enabled'] if "third_party_downloads_enabled" in self else 0
	
	#[Kanashi.totalArEffects]: Int
	@property
	def totalArEffects( self ) -> int: return self['total_ar_effects'] if "total_ar_effects" in self else 0
	
	#[Kanashi.totalClipsCount]: Int
	@property
	def totalClipsCount( self ) -> int: return self['total_clips_count'] if "total_clips_count" in self else 0
	
	#[Kanashi.totalIgtvVideos]: Int
	@property
	def totalIgtvVideos( self ) -> int: return self['total_igtv_videos'] if "total_igtv_videos" in self else 0
	
	#[Kanashi.transparencyLabel]: Any
	@property
	def transparencyLabel( self ) -> any: return self['transparency_label'] if "transparency_label" in self else None
	
	#[Kanashi.transparencyProduct]: Str
	@property
	def transparencyProduct( self ) -> str: return self['transparency_product'] if "transparency_product" in self else None
	
	#[Kanashi.transparencyProductEnabled]: Bool
	@property
	def transparencyProductEnabled( self ) -> bool: return self['transparency_product_enabled'] if "transparency_product_enabled" in self else False
	
	#[Kanashi.username]: Str
	@property
	def username( self ) -> str: return self['username'] if "username" in self else None
	
	#[Kanashi.usertagReviewEnabled]: Bool
	@property
	def usertagReviewEnabled( self ) -> bool: return self['usertag_review_enabled'] if "usertag_review_enabled" in self else False
	
	#[Kanashi.viewer]: Object
	@property
	def viewer( self ) -> Object: return self['viewer'] if "viewer" in self else Object({})
	
	#[Kanashi.whatsappNumber]: Str
	@property
	def whatsappNumber( self ) -> str: return self['whatsapp_number'] if "whatsapp_number" in self else None

