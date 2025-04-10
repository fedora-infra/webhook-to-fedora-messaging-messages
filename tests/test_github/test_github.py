# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import pytest

from webhook_to_fedora_messaging_messages import GitHubMessageV1

from .events import (
    event_fork_body,
    event_fork_headers,
    event_fork_string,
    event_fork_summary,
    event_issue_comment_body,
    event_issue_comment_headers,
    event_issue_comment_string,
    event_issue_comment_summary,
    event_issues_body,
    event_issues_headers,
    event_issues_string,
    event_issues_summary,
    event_misc_body,
    event_misc_headers,
    event_misc_string,
    event_misc_summary,
    event_pull_request_body,
    event_pull_request_headers,
    event_pull_request_string,
    event_pull_request_summary,
    event_push_body,
    event_push_headers,
    event_push_string,
    event_push_summary,
)


@pytest.mark.parametrize(
    "headers, body, summary, string",
    [
        pytest.param(
            event_fork_headers,
            event_fork_body,
            event_fork_summary,
            event_fork_string,
            id="Testing schema for GitHub 'fork' event",
        ),
        pytest.param(
            event_issue_comment_headers,
            event_issue_comment_body,
            event_issue_comment_summary,
            event_issue_comment_string,
            id="Testing schema for GitHub 'issue_comment' event",
        ),
        pytest.param(
            event_issues_headers,
            event_issues_body,
            event_issues_summary,
            event_issues_string,
            id="Testing schema for GitHub 'issues' event",
        ),
        pytest.param(
            event_pull_request_headers,
            event_pull_request_body,
            event_pull_request_summary,
            event_pull_request_string,
            id="Testing schema for GitHub 'pull_request' event",
        ),
        pytest.param(
            event_push_headers,
            event_push_body,
            event_push_summary,
            event_push_string,
            id="Testing schema for GitHub 'push' event",
        ),
        pytest.param(
            event_misc_headers,
            event_misc_body,
            event_misc_summary,
            event_misc_string,
            id="Testing schema for GitHub 'misc' event",
        ),
    ],
)
def test_github_events(headers, body, summary, string):
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
    for item in string:
        assert item in str(mesg)
