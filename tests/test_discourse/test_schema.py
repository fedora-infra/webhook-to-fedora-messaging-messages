# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import pytest

from webhook_to_fedora_messaging_messages.discourse import DiscourseMessageV1


@pytest.fixture
def webhook_headers() -> dict[str, str]:
    return {
        "X-Discourse-Instance": "https://discussion.fedoraproject.org",
        "X-Discourse-Event-Id": "171",
        "X-Discourse-Event-Type": "fake",
        "X-Discourse-Event": "fake_action",
        "X-Discourse-Event-Signature": "sha256=01a27d2aa1a034cc11505bc2f2a7e8688bc2f3b",
    }


def test_DiscourseMessageV1(webhook_headers: dict[str, str]) -> None:
    """
    Test DiscourseMessageV1
    """
    msg = DiscourseMessageV1(
        body={"webhook_body": {}, "webhook_headers": webhook_headers},
        topic="discourse.fake.fake_action",
    )
    msg.validate()

    assert msg.app_name == "Discourse"
    assert msg.summary == "Fedora Discussion: fake.fake_action"
    assert msg.app_icon == "https://apps.fedoraproject.org/img/icons/discourse.png"
    assert msg.__str__() == msg.summary
    assert msg.agent_name is None


@pytest.mark.parametrize("event_type", ["post", "like", "topic", "solved"])
def test_event_type_matches_event_not(webhook_headers: dict[str, str], event_type: str) -> None:
    # test the case that the event type matches post, but event doenst
    webhook_headers["X-Discourse-Instance"] = "https://ask.fedoraproject.org"
    webhook_headers["X-Discourse-Event-Type"] = event_type
    msg = DiscourseMessageV1(
        body={"webhook_body": {}, "webhook_headers": webhook_headers},
        topic=f"discourse.{event_type}.fake_action",
    )
    msg.validate()
    assert msg.summary == f"Ask Fedora: {event_type}.fake_action"
    assert msg.agent_name is None


def test_unknown_instance(webhook_headers: dict[str, str]) -> None:
    webhook_headers["X-Discourse-Instance"] = "https://unknown.fedoraproject.org"
    msg = DiscourseMessageV1(
        body={"webhook_body": {}, "webhook_headers": webhook_headers},
        topic="discourse.fake.fake_action",
    )
    msg.validate()

    assert msg.instance_name is None
    assert msg.summary == "None: fake.fake_action"
