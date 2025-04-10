# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from webhook_to_fedora_messaging_messages.github import GitHubMessageV1

from .events.push import body, headers


def test_repo_name_none():
    """
    Test the circumstances where the repository name is not provided
    """
    body["repository"]["full_name"] = None
    mesg = GitHubMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})
    assert mesg.summary == "testuser-w2fm created push"


def test_target_type_none():
    """
    Test the circumstances where the target type is not supported
    """
    headers["x-github-hook-installation-target-type"] = "misc"
    mesg = GitHubMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})
    assert str(mesg) == "Event type not supported"
