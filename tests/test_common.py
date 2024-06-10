# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""Unit tests for common properties of the message schemas."""

from webhook_to_fedora_messaging_messages.github.github import GithubMessageV1



def test_properties():
    """Assert some properties are correct."""
    body = {
        "agent": "dummy-user",

    }
    message = GithubMessageV1(body=body)

    assert message.app_name == "Github"
    assert (
        message.app_icon
        == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert message.agent_name == 'dummy-user'
    assert message.usernames == ["dummy-user"]
