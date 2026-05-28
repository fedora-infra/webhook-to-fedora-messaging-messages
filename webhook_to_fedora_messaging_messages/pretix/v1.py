# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import ClassVar, Optional, cast

from ..base import Webhook2FedMsgBase


class PretixMessageV1(Webhook2FedMsgBase):
    # See https://docs.pretix.eu/dev/api/webhooks.html#receiving-webhooks

    @property
    def app_name(self) -> str:
        """Application name on Fedora Messaging"""
        return "Pretix"

    @property
    def action_name(self) -> str:
        """Name of the Pretix action"""
        return cast(str, self.body["body"]["action"][len("pretix.") :])

    @property
    def event(self) -> str:
        """Slug name of the Pretix event"""
        return cast(str, self.body["body"]["event"])

    @property
    def instance_url(self) -> str:
        return cast(str, self.body["body"]["instance_url"])

    @property
    def instance_name(self) -> str:
        if self.instance_url == "https://rsvp.fedoraproject.org":
            return "Fedora ticket system"
        elif self.instance_url == "https://rsvp.stg.fedoraproject.org":
            return "Fedora ticket system (staging)"
        else:
            return "Pretix"

    @property
    def attendee_name(self) -> Optional[str]:
        return cast(Optional[str], self.body["body"]["attendee_name"])

    @property
    def summary(self) -> str:
        """Summary of the Pretix event"""
        agent = self.attendee_name or "A user"
        if self.agent_name:
            agent = f"{agent} ({self.agent_name})"
        if self.action_name == "event.checkin" and self.body["body"].get("type") == "entry":
            action = "entered"
        elif self.action_name == "event.checkin" and self.body["body"].get("type") == "exit":
            action = "exited"
        else:
            action = f"caused {self.action_name} in"
        return f"{agent} {action} {self.event} on {self.instance_name}"

    body_schema: ClassVar = {
        "id": "http://fedoraproject.org/message-schema/webhook-to-fedora-message",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from pretix via webhook",
        "type": "object",
        "required": ["body", "headers"],
        "properties": {
            "agent": {"type": ["string", "null"]},
            "body": {
                "description": "The body of the webhook POST request from Pretix",
                "type": "object",
                "properties": {
                    "notification_id": {"type": "integer"},
                    "organizer": {"type": "string"},
                    "event": {"type": "string"},
                    "code": {"type": ["string", "null"]},
                    "action": {"type": "string"},
                    "orderposition_id": {"type": "integer"},
                    "orderposition_positionid": {"type": "integer"},
                    "checkin_list": {"type": "integer"},
                    "type": {"type": "string"},
                    "attendee_name": {"type": ["string", "null"]},
                    "instance_url": {"type": "string"},
                },
                "required": [
                    "notification_id",
                    "organizer",
                    "event",
                    "code",
                    "action",
                    "instance_url",
                    "attendee_name",
                ],
            },
            "headers": {
                "description": "The headers of the webhook POST request from Pretix",
                "type": "object",
            },
        },
    }
