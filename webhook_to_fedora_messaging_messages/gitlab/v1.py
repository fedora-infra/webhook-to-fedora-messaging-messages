# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import typing

from ..base import Webhook2FedMsgBase
from .utils import summarize_repository_event


class GitLabMessageV1(Webhook2FedMsgBase):
    @property
    def app_name(self) -> str:
        """Application name on Fedora Messaging"""
        return "GitLab"

    @property
    def target_id(self) -> str:
        """Unique ID for each webhook"""
        return self.body["headers"]["x-gitlab-webhook-uuid"]

    @property
    def delivery(self) -> str:
        """Unique ID for webhooks events"""
        return self.body["headers"]["x-gitlab-event-uuid"]

    @property
    def event_name(self) -> str:
        """Name of the GitLab event"""
        return self.body["headers"]["x-gitlab-event"].replace(" Hook", "").replace(" ", "_").lower()

    @property
    def summary(self) -> str:
        """Summary of the GitLab event"""
        repo_name = self.body["body"]["repository"]["name"]
        text = f"{self.agent_name} created {self.event_name}"
        if repo_name is not None:
            text = f"{text} on {repo_name}"
        return text

    def __str__(self) -> str:
        """Specification of the GitLab event"""
        return summarize_repository_event(self.event_name, self.body["body"])

    body_schema: typing.ClassVar = {
        "id": "http://fedoraproject.org/message-schema/webhook-to-fedora-message",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from gitlab via webhook",
        "type": "object",
        "required": ["body", "headers"],
        "properties": {
            "body": {
                "description": "The body of the webhook POST request from GitLab",
                "type": "object",
            },
            "headers": {
                "description": "The headers of the webhook POST request from GitLab",
                "type": "object",
                "required": [
                    "x-gitlab-event",
                    "x-gitlab-webhook-uuid",
                    "x-gitlab-event-uuid",
                ],
                "properties": {
                    "x-gitlab-event": {"type": "string"},
                    "x-gitlab-webhook-uuid": {"type": "string"},
                    "x-gitlab-event-uuid": {"type": "string"},
                },
            },
        },
    }
