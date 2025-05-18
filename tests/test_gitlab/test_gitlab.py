# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import pytest

from webhook_to_fedora_messaging_messages import GitLabMessageV1

from . import events, results


@pytest.mark.parametrize(
    "headers, body, summary, specification",
    [
        pytest.param(
            events.issue_comment.headers,
            events.issue_comment.body,
            results.issue_comment.summary,
            results.issue_comment.specification,
            id="Testing schema for GitLab 'issue_comment' event",
        ),
        pytest.param(
            events.issues.headers,
            events.issues.body,
            results.issues.summary,
            results.issues.specification,
            id="Testing schema for GitLab 'issues' event",
        ),
        pytest.param(
            events.pull_request.headers,
            events.pull_request.body,
            results.pull_request.summary,
            results.pull_request.specification,
            id="Testing schema for GitLab 'pull_request' event",
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
def test_gitlab_events(headers: dict, body: dict, summary: str, specification: str) -> None:
    """
    Test the GitLab schema across various GitLab events
    """
    mesg = GitLabMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})

    mesg.validate()
    assert mesg.app_name == "GitLab"
    assert mesg.target_id == headers["x-gitlab-webhook-uuid"]
    assert mesg.delivery == headers["x-gitlab-event-uuid"]
    assert mesg.event_name == headers["x-gitlab-event"]
    assert mesg.summary == summary
    assert (
        mesg.app_icon == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert mesg.usernames == ["testuser-w2fm"]
    assert mesg.groups == []
    assert str(mesg) == specification


def test_repo_name_none(
    headers: dict = events.push.headers,
    body: dict = events.push.body,
    summary: str = results.push.summary,
    specification: str = results.push.specification,
) -> None:
    """
    Test the circumstances where the repository name is not provided
    """
    body["repository"]["name"] = None
    specification = specification.replace("w2fm-test", "None", 1)
    summary = summary.replace(" on w2fm-test", "")

    mesg = GitLabMessageV1(body={"body": body, "headers": headers, "agent": "testuser-w2fm"})

    mesg.validate()
    assert mesg.app_name == "GitLab"
    assert mesg.target_id == headers["x-gitlab-webhook-uuid"]
    assert mesg.delivery == headers["x-gitlab-event-uuid"]
    assert mesg.event_name == headers["x-gitlab-event"]
    assert mesg.summary == summary
    assert (
        mesg.app_icon == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert mesg.usernames == ["testuser-w2fm"]
    assert mesg.groups == []
    assert str(mesg) == specification
