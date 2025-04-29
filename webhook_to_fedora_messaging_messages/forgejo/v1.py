# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import typing

from ..base import Webhook2FedMsgBase
from .utils import summarize_repository_event


class ForgejoMessageV1(Webhook2FedMsgBase):
    @property
    def app_name(self) -> str:
        """Application name on Fedora Messaging"""
        return "Forgejo"

    @property
    def target_id(self) -> str:
        """Webhook identifier specific to Forgejo"""
        return self.body["body"]["repository"]["id"]

    @property
    def delivery(self) -> str:
        """Unique identifier (GUID) for event"""
        return self.body["headers"]["x-forgejo-delivery"]

    @property
    def signature(self) -> str:
        """SHA160 signature of the request"""
        return self.body["headers"]["x-hub-signature"]

    @property
    def signature_sha256(self) -> str:
        """SHA256 signature of the request"""
        return self.body["headers"]["x-hub-signature-256"]

    @property
    def event_name(self) -> str:
        """Name of the Forgejo event"""
        return self.body["headers"]["x-forgejo-event"]

    @property
    def summary(self) -> str:
        """Summary of the Forgejo event"""
        repo_name = self.body["body"]["repository"]["full_name"]
        text = f"{self.agent_name} created {self.event_name}"
        if repo_name is not None:
            text = f"{text} on {repo_name}"
        return text

    def __str__(self) -> str:
        """Specification of the Forgejo event"""
        return summarize_repository_event(self.event_name, self.body["body"])

    body_schema: typing.ClassVar = {
        "id": "http://fedoraproject.org/message-schema/webhook-to-fedora-message",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from forgejo via webhook",
        "type": "object",
        "required": ["body", "headers"],
        "properties": {
            "body": {
                "description": "The body of the webhook POST request from Forgejo",
                "type": "object",
            },
            "headers": {
                "description": "The headers of the webhook POST request from Forgejo",
                "type": "object",
                "required": [
                    "x-forgejo-event",
                    "x-forgejo-delivery",
                    "x-hub-signature",
                    "x-hub-signature-256",
                ],
                "properties": {
                    "x-forgejo-event": {"type": "string"},
                    "x-forgejo-delivery": {"type": "string"},
                    "x-hub-signature": {"type": "string"},
                    "x-hub-signature-256": {"type": "string"},
                },
            },
        },
    }
