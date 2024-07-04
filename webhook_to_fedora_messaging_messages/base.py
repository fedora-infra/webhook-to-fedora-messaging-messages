# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from fedora_messaging import message


class Webhook2FedMsgBase(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by Webhook to Fedora Messaging.
    """

    @property
    def app_name(self):
        return "Webhook to Fedora Messaging"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"

    @property
    def agent_name(self):
        """The username of the user who initiated the action that generated this message."""
        return self.body.get("agent")

    @property
    def usernames(self):
        """List of users affected by the action that generated this message."""
        return [self.agent_name] if self.agent_name is not None else []

    @property
    def groups(self):
        """List of groups affected by the action that generated this message."""
        group = self.body.get("group")
        return [group] if group else []
