# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import pytest

from webhook_to_fedora_messaging_messages import GitHubMessageV1

from . import events, results


@pytest.mark.parametrize(
    "headers, body, summary, specification",
    [
        pytest.param(
            events.fork.headers,
            events.fork.body,
            results.fork.summary,
            results.fork.specification,
            id="Testing schema for GitHub 'fork' event",
        ),
        pytest.param(
            events.issue_comment.headers,
            events.issue_comment.body,
            results.issue_comment.summary,
            results.issue_comment.specification,
            id="Testing schema for GitHub 'issue_comment' event",
        ),
        pytest.param(
            events.issues.headers,
            events.issues.body,
            results.issues.summary,
            results.issues.specification,
            id="Testing schema for GitHub 'issues' event",
        ),
        pytest.param(
            events.pull_request.headers,
            events.pull_request.body,
            results.pull_request.summary,
            results.pull_request.specification,
            id="Testing schema for GitHub 'pull_request' event",
        ),
        pytest.param(
            events.push.headers,
            events.push.body,
            results.push.summary,
            results.push.specification,
            id="Testing schema for GitHub 'push' event",
        ),
        pytest.param(
            events.misc.headers,
            events.misc.body,
            results.misc.summary,
            results.misc.specification,
            id="Testing schema for GitHub 'misc' event",
        ),
    ],
)
def test_github_events(headers: dict, body: dict, summary: str, specification: str) -> None:
    """
    Test the GitHub schema across various GitHub events
    """
    mesg = GitHubMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})

    mesg.validate()
    assert mesg.app_name == "GitHub"
    assert mesg.target_id == headers["x-github-hook-installation-target-id"]
    assert mesg.target_type == headers["x-github-hook-installation-target-type"]
    assert mesg.delivery == headers["x-github-delivery"]
    assert mesg.signature == headers["x-hub-signature"]
    assert mesg.signature_sha256 == headers["x-hub-signature-256"]
    assert mesg.event_name == headers["x-github-event"]
    assert mesg.summary == summary
    assert (
        mesg.app_icon == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert mesg.usernames == ["testuser-w2fm"]
    assert mesg.groups == []
    assert str(mesg) == specification


def test_repo_name_none(body: dict = events.push.body, headers: dict = events.push.headers) -> None:
    """
    Test the circumstances where the repository name is not provided
    """
    body["repository"]["full_name"] = None
    mesg = GitHubMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})
    assert mesg.summary == "testuser-w2fm created push"


def test_target_type_none(
    body: dict = events.push.body, headers: dict = events.push.headers
) -> None:
    """
    Test the circumstances where the target type is not supported
    """
    headers["x-github-hook-installation-target-type"] = "misc"
    mesg = GitHubMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})
    assert str(mesg) == "Event type not supported"
