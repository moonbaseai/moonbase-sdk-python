# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    view,
    program,
    email_message,
    program_message,
    program_template,
    inbox_conversation,
    items_filter_or_group,
    items_filter_and_group,
    items_filter_not_group,
    view_relation_value_filter,
)
from .. import _compat
from .call import Call as Call
from .form import Form as Form
from .item import Item as Item
from .note import Note as Note
from .view import View as View
from .field import Field as Field
from .inbox import Inbox as Inbox
from .value import Value as Value
from .funnel import Funnel as Funnel
from .shared import Tag as Tag, Error as Error, FormattedText as FormattedText, TagPointerParam as TagPointerParam
from .tagset import Tagset as Tagset
from .address import Address as Address
from .meeting import Meeting as Meeting
from .program import Program as Program
from .activity import Activity as Activity
from .attendee import Attendee as Attendee
from .endpoint import Endpoint as Endpoint
from .geo_field import GeoField as GeoField
from .geo_value import GeoValue as GeoValue
from .organizer import Organizer as Organizer
from .url_field import URLField as URLField
from .url_value import URLValue as URLValue
from .collection import Collection as Collection
from .date_field import DateField as DateField
from .date_value import DateValue as DateValue
from .view_field import ViewField as ViewField
from .constituent import Constituent as Constituent
from .email_field import EmailField as EmailField
from .email_value import EmailValue as EmailValue
from .field_value import FieldValue as FieldValue
from .float_field import FloatField as FloatField
from .float_value import FloatValue as FloatValue
from .funnel_step import FunnelStep as FunnelStep
from .stage_field import StageField as StageField
from .unsubscribe import Unsubscribe as Unsubscribe
from .value_param import ValueParam as ValueParam
from .call_pointer import CallPointer as CallPointer
from .choice_field import ChoiceField as ChoiceField
from .choice_value import ChoiceValue as ChoiceValue
from .current_date import CurrentDate as CurrentDate
from .domain_field import DomainField as DomainField
from .domain_value import DomainValue as DomainValue
from .file_pointer import FilePointer as FilePointer
from .item_pointer import ItemPointer as ItemPointer
from .items_filter import ItemsFilter as ItemsFilter
from .note_pointer import NotePointer as NotePointer
from .subscription import Subscription as Subscription
from .boolean_field import BooleanField as BooleanField
from .boolean_value import BooleanValue as BooleanValue
from .email_message import EmailMessage as EmailMessage
from .field_pointer import FieldPointer as FieldPointer
from .integer_field import IntegerField as IntegerField
from .integer_value import IntegerValue as IntegerValue
from .moonbase_file import MoonbaseFile as MoonbaseFile
from .current_member import CurrentMember as CurrentMember
from .datetime_field import DatetimeField as DatetimeField
from .datetime_value import DatetimeValue as DatetimeValue
from .monetary_field import MonetaryField as MonetaryField
from .monetary_value import MonetaryValue as MonetaryValue
from .relation_field import RelationField as RelationField
from .relation_value import RelationValue as RelationValue
from .social_x_field import SocialXField as SocialXField
from .social_x_value import SocialXValue as SocialXValue
from .tagset_pointer import TagsetPointer as TagsetPointer
from .view_aggregate import ViewAggregate as ViewAggregate
from .call_transcript import CallTranscript as CallTranscript
from .geo_value_param import GeoValueParam as GeoValueParam
from .meeting_pointer import MeetingPointer as MeetingPointer
from .program_message import ProgramMessage as ProgramMessage
from .program_pointer import ProgramPointer as ProgramPointer
from .search_response import SearchResponse as SearchResponse
from .url_value_param import URLValueParam as URLValueParam
from .call_list_params import CallListParams as CallListParams
from .call_participant import CallParticipant as CallParticipant
from .current_datetime import CurrentDatetime as CurrentDatetime
from .date_value_param import DateValueParam as DateValueParam
from .file_list_params import FileListParams as FileListParams
from .form_list_params import FormListParams as FormListParams
from .identifier_field import IdentifierField as IdentifierField
from .identifier_value import IdentifierValue as IdentifierValue
from .note_list_params import NoteListParams as NoteListParams
from .percentage_field import PercentageField as PercentageField
from .percentage_value import PercentageValue as PercentageValue
from .program_template import ProgramTemplate as ProgramTemplate
from .telephone_number import TelephoneNumber as TelephoneNumber
from .view_field_param import ViewFieldParam as ViewFieldParam
from .view_list_params import ViewListParams as ViewListParams
from .email_value_param import EmailValueParam as EmailValueParam
from .field_value_param import FieldValueParam as FieldValueParam
from .float_value_param import FloatValueParam as FloatValueParam
from .funnel_step_value import FunnelStepValue as FunnelStepValue
from .inbox_list_params import InboxListParams as InboxListParams
from .call_create_params import CallCreateParams as CallCreateParams
from .call_pointer_param import CallPointerParam as CallPointerParam
from .call_upsert_params import CallUpsertParams as CallUpsertParams
from .choice_value_param import ChoiceValueParam as ChoiceValueParam
from .collection_pointer import CollectionPointer as CollectionPointer
from .current_date_param import CurrentDateParam as CurrentDateParam
from .domain_value_param import DomainValueParam as DomainValueParam
from .file_upload_params import FileUploadParams as FileUploadParams
from .form_create_params import FormCreateParams as FormCreateParams
from .form_update_params import FormUpdateParams as FormUpdateParams
from .funnel_list_params import FunnelListParams as FunnelListParams
from .inbox_conversation import InboxConversation as InboxConversation
from .item_pointer_param import ItemPointerParam as ItemPointerParam
from .items_filter_param import ItemsFilterParam as ItemsFilterParam
from .meeting_transcript import MeetingTranscript as MeetingTranscript
from .message_attachment import MessageAttachment as MessageAttachment
from .note_create_params import NoteCreateParams as NoteCreateParams
from .note_update_params import NoteUpdateParams as NoteUpdateParams
from .tagset_list_params import TagsetListParams as TagsetListParams
from .view_create_params import ViewCreateParams as ViewCreateParams
from .view_list_response import ViewListResponse as ViewListResponse
from .view_update_params import ViewUpdateParams as ViewUpdateParams
from .boolean_value_param import BooleanValueParam as BooleanValueParam
from .call_transcript_cue import CallTranscriptCue as CallTranscriptCue
from .choice_field_option import ChoiceFieldOption as ChoiceFieldOption
from .field_default_value import FieldDefaultValue as FieldDefaultValue
from .integer_value_param import IntegerValueParam as IntegerValueParam
from .meeting_list_params import MeetingListParams as MeetingListParams
from .program_list_params import ProgramListParams as ProgramListParams
from .unsubscribe_pointer import UnsubscribePointer as UnsubscribePointer
from .activity_list_params import ActivityListParams as ActivityListParams
from .call_retrieve_params import CallRetrieveParams as CallRetrieveParams
from .client_search_params import ClientSearchParams as ClientSearchParams
from .current_member_param import CurrentMemberParam as CurrentMemberParam
from .datetime_value_param import DatetimeValueParam as DatetimeValueParam
from .funnel_create_params import FunnelCreateParams as FunnelCreateParams
from .funnel_pointer_param import FunnelPointerParam as FunnelPointerParam
from .funnel_update_params import FunnelUpdateParams as FunnelUpdateParams
from .monetary_value_param import MonetaryValueParam as MonetaryValueParam
from .relation_value_param import RelationValueParam as RelationValueParam
from .social_x_value_param import SocialXValueParam as SocialXValueParam
from .tagset_create_params import TagsetCreateParams as TagsetCreateParams
from .tagset_update_params import TagsetUpdateParams as TagsetUpdateParams
from .view_aggregate_param import ViewAggregateParam as ViewAggregateParam
from .email_message_pointer import EmailMessagePointer as EmailMessagePointer
from .items_filter_or_group import ItemsFilterOrGroup as ItemsFilterOrGroup
from .meeting_pointer_param import MeetingPointerParam as MeetingPointerParam
from .meeting_update_params import MeetingUpdateParams as MeetingUpdateParams
from .multi_line_text_field import MultiLineTextField as MultiLineTextField
from .multi_line_text_value import MultiLineTextValue as MultiLineTextValue
from .collection_list_params import CollectionListParams as CollectionListParams
from .current_datetime_param import CurrentDatetimeParam as CurrentDatetimeParam
from .identifier_value_param import IdentifierValueParam as IdentifierValueParam
from .items_filter_and_group import ItemsFilterAndGroup as ItemsFilterAndGroup
from .items_filter_not_group import ItemsFilterNotGroup as ItemsFilterNotGroup
from .meeting_transcript_cue import MeetingTranscriptCue as MeetingTranscriptCue
from .percentage_value_param import PercentageValueParam as PercentageValueParam
from .single_line_text_field import SingleLineTextField as SingleLineTextField
from .single_line_text_value import SingleLineTextValue as SingleLineTextValue
from .social_linked_in_field import SocialLinkedInField as SocialLinkedInField
from .social_linked_in_value import SocialLinkedInValue as SocialLinkedInValue
from .social_profile_x_param import SocialProfileXParam as SocialProfileXParam
from .telephone_number_field import TelephoneNumberField as TelephoneNumberField
from .telephone_number_param import TelephoneNumberParam as TelephoneNumberParam
from .call_transcript_speaker import CallTranscriptSpeaker as CallTranscriptSpeaker
from .funnel_step_value_param import FunnelStepValueParam as FunnelStepValueParam
from .meeting_retrieve_params import MeetingRetrieveParams as MeetingRetrieveParams
from .program_message_pointer import ProgramMessagePointer as ProgramMessagePointer
from .program_retrieve_params import ProgramRetrieveParams as ProgramRetrieveParams
from .unsubscribe_list_params import UnsubscribeListParams as UnsubscribeListParams
from .collection_create_params import CollectionCreateParams as CollectionCreateParams
from .collection_list_response import CollectionListResponse as CollectionListResponse
from .collection_update_params import CollectionUpdateParams as CollectionUpdateParams
from .note_association_pointer import NoteAssociationPointer as NoteAssociationPointer
from .program_activity_metrics import ProgramActivityMetrics as ProgramActivityMetrics
from .program_template_pointer import ProgramTemplatePointer as ProgramTemplatePointer
from .funnel_step_pointer_param import FunnelStepPointerParam as FunnelStepPointerParam
from .inbox_message_list_params import InboxMessageListParams as InboxMessageListParams
from .items_filter_value_exists import ItemsFilterValueExists as ItemsFilterValueExists
from .stage_field_create_params import StageFieldCreateParams as StageFieldCreateParams
from .stage_field_update_params import StageFieldUpdateParams as StageFieldUpdateParams
from .unsubscribe_create_params import UnsubscribeCreateParams as UnsubscribeCreateParams
from .view_aggregate_item_count import ViewAggregateItemCount as ViewAggregateItemCount
from .constituent_entity_pointer import ConstituentEntityPointer as ConstituentEntityPointer
from .items_filter_value_matches import ItemsFilterValueMatches as ItemsFilterValueMatches
from .meeting_transcript_speaker import MeetingTranscriptSpeaker as MeetingTranscriptSpeaker
from .view_relation_value_filter import ViewRelationValueFilter as ViewRelationValueFilter
from .agent_setting_update_params import AgentSettingUpdateParams as AgentSettingUpdateParams
from .inbox_message_create_params import InboxMessageCreateParams as InboxMessageCreateParams
from .inbox_message_update_params import InboxMessageUpdateParams as InboxMessageUpdateParams
from .items_filter_or_group_param import ItemsFilterOrGroupParam as ItemsFilterOrGroupParam
from .multi_line_text_value_param import MultiLineTextValueParam as MultiLineTextValueParam
from .program_message_send_params import ProgramMessageSendParams as ProgramMessageSendParams
from .email_message_address_params import EmailMessageAddressParams as EmailMessageAddressParams
from .items_filter_and_group_param import ItemsFilterAndGroupParam as ItemsFilterAndGroupParam
from .items_filter_not_group_param import ItemsFilterNotGroupParam as ItemsFilterNotGroupParam
from .program_template_list_params import ProgramTemplateListParams as ProgramTemplateListParams
from .single_line_text_value_param import SingleLineTextValueParam as SingleLineTextValueParam
from .social_linked_in_value_param import SocialLinkedInValueParam as SocialLinkedInValueParam
from .webhook_endpoint_list_params import WebhookEndpointListParams as WebhookEndpointListParams
from .agent_setting_update_response import AgentSettingUpdateResponse as AgentSettingUpdateResponse
from .inbox_message_retrieve_params import InboxMessageRetrieveParams as InboxMessageRetrieveParams
from .date_field_default_value_param import DateFieldDefaultValueParam as DateFieldDefaultValueParam
from .inbox_conversation_list_params import InboxConversationListParams as InboxConversationListParams
from .social_profile_linked_in_param import SocialProfileLinkedInParam as SocialProfileLinkedInParam
from .view_aggregate_field_statistic import ViewAggregateFieldStatistic as ViewAggregateFieldStatistic
from .webhook_endpoint_create_params import WebhookEndpointCreateParams as WebhookEndpointCreateParams
from .webhook_endpoint_update_params import WebhookEndpointUpdateParams as WebhookEndpointUpdateParams
from .agent_setting_retrieve_response import AgentSettingRetrieveResponse as AgentSettingRetrieveResponse
from .items_filter_value_exists_param import ItemsFilterValueExistsParam as ItemsFilterValueExistsParam
from .view_aggregate_item_count_param import ViewAggregateItemCountParam as ViewAggregateItemCountParam
from .inbox_conversation_list_response import InboxConversationListResponse as InboxConversationListResponse
from .items_filter_value_matches_param import ItemsFilterValueMatchesParam as ItemsFilterValueMatchesParam
from .program_template_retrieve_params import ProgramTemplateRetrieveParams as ProgramTemplateRetrieveParams
from .view_relation_value_filter_param import ViewRelationValueFilterParam as ViewRelationValueFilterParam
from .choice_field_option_pointer_param import ChoiceFieldOptionPointerParam as ChoiceFieldOptionPointerParam
from .datetime_field_default_value_param import DatetimeFieldDefaultValueParam as DatetimeFieldDefaultValueParam
from .inbox_conversation_retrieve_params import InboxConversationRetrieveParams as InboxConversationRetrieveParams
from .relation_field_default_value_param import RelationFieldDefaultValueParam as RelationFieldDefaultValueParam
from .note_association_param_pointer_param import NoteAssociationParamPointerParam as NoteAssociationParamPointerParam
from .view_aggregate_field_statistic_param import ViewAggregateFieldStatisticParam as ViewAggregateFieldStatisticParam

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    items_filter_and_group.ItemsFilterAndGroup.update_forward_refs()  # type: ignore
    items_filter_not_group.ItemsFilterNotGroup.update_forward_refs()  # type: ignore
    items_filter_or_group.ItemsFilterOrGroup.update_forward_refs()  # type: ignore
    view.View.update_forward_refs()  # type: ignore
    view_relation_value_filter.ViewRelationValueFilter.update_forward_refs()  # type: ignore
    inbox_conversation.InboxConversation.update_forward_refs()  # type: ignore
    email_message.EmailMessage.update_forward_refs()  # type: ignore
    program.Program.update_forward_refs()  # type: ignore
    program_template.ProgramTemplate.update_forward_refs()  # type: ignore
    program_message.ProgramMessage.update_forward_refs()  # type: ignore
else:
    items_filter_and_group.ItemsFilterAndGroup.model_rebuild(_parent_namespace_depth=0)
    items_filter_not_group.ItemsFilterNotGroup.model_rebuild(_parent_namespace_depth=0)
    items_filter_or_group.ItemsFilterOrGroup.model_rebuild(_parent_namespace_depth=0)
    view.View.model_rebuild(_parent_namespace_depth=0)
    view_relation_value_filter.ViewRelationValueFilter.model_rebuild(_parent_namespace_depth=0)
    inbox_conversation.InboxConversation.model_rebuild(_parent_namespace_depth=0)
    email_message.EmailMessage.model_rebuild(_parent_namespace_depth=0)
    program.Program.model_rebuild(_parent_namespace_depth=0)
    program_template.ProgramTemplate.model_rebuild(_parent_namespace_depth=0)
    program_message.ProgramMessage.model_rebuild(_parent_namespace_depth=0)
