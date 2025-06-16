# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import Any

import pytest

from webhook_to_fedora_messaging_messages import GitLabMessageV1

from . import events, results


@pytest.mark.parametrize(
    "headers, body, summary, specification",
    [
        pytest.param(
            events.note.headers,
            events.note.body,
            results.note.summary,
            results.note.specification,
            id="Testing schema for GitLab 'note' event",
        ),
        pytest.param(
            events.issue.headers,
            events.issue.body,
            results.issue.summary,
            results.issue.specification,
            id="Testing schema for GitLab 'issue' event",
        ),
        pytest.param(
            events.merge_request.headers,
            events.merge_request.body,
            results.merge_request.summary,
            results.merge_request.specification,
            id="Testing schema for GitLab 'merge_request' event",
        ),
        pytest.param(
            events.push.headers,
            events.push.body,
            results.push.summary,
            results.push.specification,
            id="Testing schema for GitLab 'push' event",
        ),
        pytest.param(
            events.misc.headers,
            events.misc.body,
            results.misc.summary,
            results.misc.specification,
            id="Testing schema for GitLab 'misc' event",
        ),
    ],
)
def test_gitlab_events(
    headers: dict[str, str], body: dict[str, Any], summary: str, specification: str
) -> None:
    """
    Test the GitLab schema across various GitLab events
    """
    mesg = GitLabMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})

    mesg.validate()
    assert mesg.app_name == "GitLab"
    assert mesg.target_id == headers["x-gitlab-webhook-uuid"]
    assert mesg.delivery == headers["x-gitlab-event-uuid"]
    assert (
        mesg.event_name == headers["x-gitlab-event"].replace(" Hook", "").replace(" ", "_").lower()
    )
    assert mesg.summary == summary
    assert (
        mesg.app_icon == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert mesg.usernames == ["testuser-w2fm"]
    assert mesg.groups == []
    assert str(mesg) == specification


def test_repo_name_none(
    headers: dict[str, str] = events.push.headers,
    body: dict[str, Any] = events.push.body,
    summary: str = results.push.summary.replace(" on w2fm-test", ""),
    specification: str = results.push.specification.replace("w2fm-test", "None", 1),
) -> None:
    """
    Test the circumstances where the repository name is not provided
    """
    body["repository"]["name"] = None
    mesg = GitLabMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})

    assert mesg.summary == summary
    assert str(mesg) == specification
