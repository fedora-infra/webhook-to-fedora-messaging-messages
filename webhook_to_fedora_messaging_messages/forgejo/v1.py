# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import typing
import uuid

from ..base import Webhook2FedMsgBase
from .utils import summarize_repository_event


class ForgejoMessageV1(Webhook2FedMsgBase):
    @property
    def app_name(self):
        return "Forgejo"

    @property
    def target_id(self):
        return self.body["repository"]["id"]

    @property
    def signature(self):
        return hashlib.sha1(str(self.body).encode(encoding="utf-8")).hexdigest()

    @property
    def delivery(self):
        return self.body["headers"]["x-forgejo-delivery"]

    @property
    def signature_sha256(self):
        return hashlib.sha256(str(self.body).encode(encoding="utf-8")).hexdigest()

    @property
    def event_name(self):
        return self.body["headers"].get("x-forgejo-event")

    @property
    def event_type(self):
        return self.body["headers"].get("x-forgejo-event-type")

    @property
    def summary(self):
        repo_name = self.body["body"]["repository"]["full_name"]
        text = f"{self.agent_name} created {self.event_name}"
        if repo_name is not None:
            text = f"{text} on {repo_name}"
        return text

    @property
    def __str__(self):
        if self.event_type == "repository":
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
                ],
                "properties": {
                    "x-forgejo-event": {"type": "string"},
                    "x-forgejo-delivery": {"type": "string"},
                },
            },
        },
    }
