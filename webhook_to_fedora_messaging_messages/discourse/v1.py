# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import Any, ClassVar, Optional, TypedDict, cast

from fedora_messaging import message


class BaseSchema(TypedDict):
    webhook_body: dict[str, Any]
    webhook_headers: dict[str, str]


class DiscourseMessageV1(message.Message):
    body: BaseSchema

    @property
    def app_name(self) -> Optional[str]:
        """Application name on Fedora Messaging"""
        return "Discourse"

    @property
    def app_icon(self) -> Optional[str]:
        return "https://apps.fedoraproject.org/img/icons/discourse.png"

    @property
    def instance(self) -> str:
        return self.body["webhook_headers"]["X-Discourse-Instance"]

    @property
    def event(self) -> str:
        return self.body["webhook_headers"]["X-Discourse-Event"]

    @property
    def event_type(self) -> str:
        return self.body["webhook_headers"]["X-Discourse-Event-Type"]

    @property
    def webhook_contents(self) -> Any:
        return self.body["webhook_body"].get(self.event_type, {})

    @property
    def post_contents(self) -> Any:
        if self.event_type == "like":
            return self.webhook_contents.get("post", {})
        else:
            return self.webhook_contents

    @property
    def instance_name(self) -> Optional[str]:
        if self.instance == "https://discussion.fedoraproject.org":
            return "Fedora Discussion"
        elif self.instance == "https://ask.fedoraproject.org":
            return "Ask Fedora"
        else:
            return None

    @property
    def category(self) -> str:
        return cast(str, self.post_contents.get("category_slug"))

    @property
    def summary(self) -> str:
        username = self.post_contents.get("username")
        topic_title = self.post_contents.get("topic_title")
        if self.event_type == "post":
            if self.event == "post_created":
                return f"New Post on {self.instance_name}: {username} posted in '{topic_title}'"
            elif self.event == "post_edited":
                return f"Post Edited on {self.instance_name}: {username}'s post on '{topic_title}'"
            elif self.event == "post_recovered":
                return (
                    f"Post Recovered on {self.instance_name}:"
                    f" {username}'s post on '{topic_title}'"
                )
            elif self.event == "post_destroyed":
                return (
                    f"Post Destroyed on {self.instance_name}:"
                    f" {username}'s post on '{topic_title}'"
                )
        elif self.event_type == "like":
            liker = self.webhook_contents.get("user", {}).get("username")
            if self.event == "post_liked":
                return (
                    f"Post Liked on {self.instance_name}:"
                    f" {liker} liked {username}'s post on '{topic_title}'"
                )
        elif self.event_type == "topic":
            username = self.webhook_contents.get("created_by", {}).get("username")
            topic_title = self.webhook_contents.get("title")
            if self.event == "topic_created":
                return (
                    f"New Topic on {self.instance_name}:"
                    f" {username} created the topic '{topic_title}'"
                )
            elif self.event == "topic_edited":
                return (
                    f"Topic Edited on {self.instance_name}:" f" {username}'s topic '{topic_title}'"
                )
            elif self.event == "topic_destroyed":
                return (
                    f"Topic Destroyed on {self.instance_name}:"
                    f" {username}'s topic '{topic_title}'"
                )
            elif self.event == "topic_recovered":
                return (
                    f"Topic Recovered on {self.instance_name}:"
                    f" {username}'s topic '{topic_title}'"
                )
        elif self.event_type == "solved":
            if self.event == "accepted_solution":
                return (
                    f"Accepted Solution on {self.instance_name}:"
                    f" {username}'s post on topic '{topic_title}' marked as the solution."
                )

        # return a generic summary if not matching above
        return f"{self.instance_name}: {self.event_type}.{self.event}"

    def __str__(self) -> str:
        return self.summary

    @property
    def agent_name(self) -> Optional[str]:
        if self.event_type == "post":
            if (
                self.event == "post_created"
                or self.event == "post_destroyed"
                or self.event == "post_recovered"
                or self.event == "post_edited"
            ):
                return cast(Optional[str], self.webhook_contents.get("username"))
            else:
                return None
        elif self.event_type == "like":
            if self.event == "post_liked":
                return cast(Optional[str], self.webhook_contents.get("user", {}).get("username"))
            else:
                return None
        elif self.event_type == "topic":
            if (
                self.event == "topic_created"
                or self.event == "topic_edited"
                or self.event == "topic_destroyed"
                or self.event == "topic_recovered"
            ):
                return cast(
                    Optional[str], self.webhook_contents.get("created_by", {}).get("username")
                )
            else:
                return None
        elif self.event_type == "solved":
            # Marking a question as solved is done by the question's author,
            # not the answer's author, and we don't have the former in the
            # webhook's contents.
            return None
        else:
            return None

    @property
    def usernames(self) -> list[str]:
        value = set(super().usernames)
        if self.event_type == "solved":
            # Add the author of the solution
            value.add(self.webhook_contents.get("username"))
        elif self.event_type == "like":
            # Add the author of the post that was liked
            value.add(self.webhook_contents.get("post", {}).get("username"))
        return list(sorted(value))

    body_schema: ClassVar = {
        "id": "http://fedoraproject.org/message-schema/discourse2fedmsg",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from discourse instances via webhook",
        "type": "object",
        "required": ["webhook_body", "webhook_headers"],
        "properties": {
            "webhook_body": {
                "description": "The body of the webhook POST request from Discourse",
                "type": "object",
            },
            "webhook_headers": {
                "description": "The headers of the webhook POST request from Discourse",
                "type": "object",
                "required": [
                    "X-Discourse-Instance",
                    "X-Discourse-Event-Id",
                    "X-Discourse-Event",
                    "X-Discourse-Event-Type",
                    "X-Discourse-Event-Signature",
                ],
                "properties": {
                    "X-Discourse-Instance": {"type": "string"},
                    "X-Discourse-Event-Id": {"type": "string"},
                    "X-Discourse-Event": {"type": "string"},
                    "X-Discourse-Event-Type": {"type": "string"},
                    "X-Discourse-Event-Signature": {"type": "string"},
                },
            },
        },
    }
