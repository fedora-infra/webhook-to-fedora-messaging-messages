# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import Any

import pytest

from webhook_to_fedora_messaging_messages import ForgejoMessageV1

from . import events, results


@pytest.mark.parametrize(
    "headers, body, summary, specification, hashes",
    [
        pytest.param(
            events.fork.headers,
            events.fork.body,
            results.fork.summary,
            results.fork.specification,
            results.fork.hashes,
            id="Testing schema for Forgejo 'fork' event",
        ),
        pytest.param(
            events.issue_comment.headers,
            events.issue_comment.body,
            results.issue_comment.summary,
            results.issue_comment.specification,
            results.issue_comment.hashes,
            id="Testing schema for Forgejo 'issue_comment' event",
        ),
        pytest.param(
            events.issues.headers,
            events.issues.body,
            results.issues.summary,
            results.issues.specification,
            results.issues.hashes,
            id="Testing schema for Forgejo 'issues' event",
        ),
        pytest.param(
            events.pull_request.headers,
            events.pull_request.body,
            results.pull_request.summary,
            results.pull_request.specification,
            results.pull_request.hashes,
            id="Testing schema for Forgejo 'pull_request' event",
        ),
        pytest.param(
            events.push.headers,
            events.push.body,
            results.push.summary,
            results.push.specification,
            results.push.hashes,
            id="Testing schema for Forgejo 'push' event",
        ),
        pytest.param(
            events.misc.headers,
            events.misc.body,
            results.misc.summary,
            results.misc.specification,
            results.misc.hashes,
            id="Testing schema for Forgejo 'misc' event",
        ),
    ],
)
def test_forgejo_events(
    headers: dict[str, str],
    body: dict[str, Any],
    summary: str,
    specification: str,
    hashes: dict[str, str],
) -> None:
    """
    Test the Forgejo schema across various Forgejo events
    """
    mesg = ForgejoMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})

    mesg.validate()
    assert mesg.app_name == "Forgejo"
    assert mesg.target_id == body["repository"]["id"]
    assert mesg.delivery == headers["x-forgejo-delivery"]
    assert mesg.signature == hashes["sha160"]
    assert mesg.signature_sha256 == hashes["sha256"]
    assert mesg.event_name == headers["x-forgejo-event"]
    assert mesg.summary == summary
    assert (
        mesg.app_icon == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert mesg.usernames == ["testuser-w2fm"]
    assert mesg.groups == []
    assert str(mesg) == specification


def test_repo_name_none(
    body: dict[str, Any] = events.push.body, headers: dict[str, str] = events.push.headers
) -> None:
    """
    Test the circumstances where the repository name is not provided
    """
    body["repository"]["full_name"] = None
    mesg = ForgejoMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})
    assert mesg.summary == "testuser-w2fm created push"
