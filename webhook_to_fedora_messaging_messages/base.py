# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import Any, Optional, TypedDict, cast

from fedora_messaging import message


class BaseSchema(TypedDict):
    body: dict[str, Any]
    headers: dict[str, str]


class Webhook2FedMsgBase(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by Webhook to Fedora Messaging.
    """

    body: BaseSchema

    @property
    def app_name(self) -> str:
        return "Webhook to Fedora Messaging"  # pragma: no cover

    @property
    def app_icon(self) -> str:
        return "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"

    @property
    def agent_name(self) -> Optional[str]:
        """The username of the user who initiated the action that generated this message."""
        return cast(Optional[str], self.body.get("agent"))

    @property
    def usernames(self) -> list[str]:
        """List of users affected by the action that generated this message."""
        return [self.agent_name] if self.agent_name is not None else []

    @property
    def groups(self) -> list[str]:
        """List of groups affected by the action that generated this message."""
        group = cast(Optional[str], self.body.get("group"))
        return [group] if group else []
