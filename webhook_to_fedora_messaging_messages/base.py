# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from fedora_messaging import message


SCHEMA_URL = "http://fedoraproject.org/message-schema/"

THING_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "foobar": {"type": ["string", "null"]},
        "url": {"type": "string", "format": "uri"},
    },
    "required": ["id", "name"],
}


class WebhookToFedoraMessagingMessage(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by Webhook To Fedora Messaging.
    """

    @property
    def app_name(self):
        return "Webhook To Fedora Messaging"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"

    @property
    def url(self):
        try:
            return self.body["thing"]["url"]
        except KeyError:
            return None

    @property
    def agent_name(self):
        """The username of the user who initiated the action that generated this message."""
        return self.body.get("agent")

    @property
    def usernames(self):
        """List of users affected by the action that generated this message."""
        return [self.agent_name]

    @property
    def groups(self):
        """List of groups affected by the action that generated this message."""
        group = self.body.get("group")
        return [group] if group else []

    @property
    def packages(self):
        """List of packages affected by the action that generated this message."""
        return []

    @property
    def containers(self):
        """List of containers affected by the action that generated this message."""
        return []

    @property
    def modules(self):
        """List of modules affected by the action that generated this message."""
        return []

    @property
    def flatpaks(self):
        """List of flatpaks affected by the action that generated this message."""
        return []
