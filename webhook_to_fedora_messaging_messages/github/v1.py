# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import typing

from ..base import Webhook2FedMsgBase
from .utils import summarize_repository_event


class GithubMessageV1(Webhook2FedMsgBase):
    @property
    def app_name(self):
        return "Github"

    @property
    def target_id(self):
        return self.body["headers"]["x-github-hook-installation-target-id"]

    @property
    def signature(self):
        """SHA1 signature of the request"""
        return self.body["headers"]["x-hub-signature"]

    @property
    def delivery(self):
        """A globally unique identifier (GUID) to identify the event"""
        return self.body["headers"]["x-github-delivery"]

    @property
    def signature_sha256(self):
        """SHA1-256 signature of the request"""
        return self.body["headers"]["x-hub-signature-256"]

    @property
    def event_name(self):
        return self.body["headers"]["x-github-event"]

    @property
    def event_type(self):
        return self.body["headers"]["x-github-hook-installation-target-type"]

    @property
    def summary(self):
        repo_name = self.body["body"]["repository"]["full_name"]
        text = f"{self.agent_name} created {self.event_name}"
        if repo_name is not None:
            text += f" on {repo_name}"
        return text

    def __str__(self):
        if self.event_type == "repository":
            return summarize_repository_event(self.event_name, self.body["body"])

    body_schema: typing.ClassVar = {
        "id": "http://fedoraproject.org/message-schema/webhook-to-fedora-message",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from github via webhook",
        "type": "object",
        "required": ["body", "headers"],
        "properties": {
            "body": {
                "description": "The body of the webhook POST request from Github",
                "type": "object",
            },
            "headers": {
                "description": "The headers of the webhook POST request from Github",
                "type": "object",
                "required": [
                    "x-github-event",
                    "x-github-hook-installation-target-id",
                    "x-github-hook-installation-target-type",
                    "x-hub-signature",
                    "x-hub-signature-256",
                    "x-github-delivery",
                ],
                "properties": {
                    "x-github-event": {"type": "string"},
                    "x-github-hook-installation-target-id": {"type": "string"},
                    "x-github-hook-installation-target-type": {"type": "string"},
                    "x-hub-signature": {"type": "string"},
                    "x-hub-signature-256": {"type": "string"},
                    "x-github-delivery": {"type": "string"},
                },
            },
        },
    }
