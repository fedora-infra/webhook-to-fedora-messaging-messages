# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import typing

from ..base import Webhook2FedMsgBase
from .utils import summarize_repository_event


class GitHubMessageV1(Webhook2FedMsgBase):
    @property
    def app_name(self) -> str:
        """Application name on Fedora Messaging"""
        return "GitHub"

    @property
    def target_id(self) -> str:
        """Webhook identifier specific to GitHub"""
        return self.body["headers"]["x-github-hook-installation-target-id"]

    @property
    def target_type(self) -> str:
        """Webhook type specific to GitHub"""
        return self.body["headers"]["x-github-hook-installation-target-type"]

    @property
    def delivery(self) -> str:
        """Unique identifier (GUID) for event"""
        return self.body["headers"]["x-github-delivery"]

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
        """Name of the GitHub event"""
        return self.body["headers"]["x-github-event"]

    @property
    def summary(self) -> str:
        """Summary of the GitHub event"""
        repo_name = self.body["body"]["repository"]["full_name"]
        text = f"{self.agent_name} created {self.event_name}"
        if repo_name is not None:
            text = f"{text} on {repo_name}"
        return text

    def __str__(self) -> str:
        """Specification of the GitHub event"""
        if self.target_type == "repository":
            return summarize_repository_event(self.event_name, self.body["body"])
        return "Event type not supported"

    body_schema: typing.ClassVar = {
        "id": "http://fedoraproject.org/message-schema/webhook-to-fedora-message",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from github via webhook",
        "type": "object",
        "required": ["body", "headers"],
        "properties": {
            "body": {
                "description": "The body of the webhook POST request from GitHub",
                "type": "object",
            },
            "headers": {
                "description": "The headers of the webhook POST request from GitHub",
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
