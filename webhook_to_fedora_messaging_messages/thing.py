# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from .base import SCHEMA_URL, WebhookToFedoraMessagingMessage, THING_SCHEMA


class NewThingV1(WebhookToFedoraMessagingMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by Webhook To Fedora Messaging when a new thing is created.
    """

    topic = "webhook-to-fedora-messaging.new"

    body_schema = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a new thing is created",
        "type": "object",
        "properties": {"agent": {"type": "string"}, "thing": THING_SCHEMA},
        "required": ["agent", "thing"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        return "New Thing: {thing}\nBy: {agent}\n".format(
            thing=self.body["thing"]["name"],
            agent=self.agent_name,
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return '{agent} created thing "{name}" ({id})'.format(
            agent=self.agent_name,
            name=self.body["thing"]["name"],
            id=self.body["thing"]["id"],
        )
