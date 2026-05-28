# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from typing import Any

import pytest

from webhook_to_fedora_messaging_messages import PretixMessageV1


@pytest.mark.parametrize(
    "body, agent, summary",
    [
        pytest.param(
            {
                "type": "entry",
                "attendee_name": "Test User",
                "instance_url": "https://example.com",
            },
            None,
            "Test User entered flock-2026 on Pretix",
            id="Pretix: attendee but no agent, no instance",
        ),
        pytest.param(
            {
                "type": "entry",
                "attendee_name": "Test User",
                "instance_url": "https://example.com",
            },
            "testuser",
            "Test User (testuser) entered flock-2026 on Pretix",
            id="Pretix: attendee and agent, but no instance",
        ),
        pytest.param(
            {
                "type": "entry",
                "attendee_name": None,
                "instance_url": "https://example.com",
            },
            None,
            "A user entered flock-2026 on Pretix",
            id="Pretix: no agent, no attendee, no instance",
        ),
        pytest.param(
            {
                "type": "exit",
                "attendee_name": None,
                "instance_url": "https://example.com",
            },
            None,
            "A user exited flock-2026 on Pretix",
            id="Pretix: exit",
        ),
        pytest.param(
            {
                "type": "entry",
                "attendee_name": None,
                "instance_url": "https://rsvp.fedoraproject.org",
            },
            None,
            "A user entered flock-2026 on Fedora ticket system",
            id="Pretix: no agent, no attendee, instance is RSVP",
        ),
        pytest.param(
            {
                "type": "entry",
                "attendee_name": None,
                "instance_url": "https://rsvp.stg.fedoraproject.org",
            },
            None,
            "A user entered flock-2026 on Fedora ticket system (staging)",
            id="Pretix: no agent, no attendee, instance is RSVP staging",
        ),
    ],
)
def test_pretix_actions(
    body: dict[str, Any],
    agent: str,
    summary: str,
) -> None:
    """
    Test the Pretix schema across various Pretix action events
    """
    body.update(
        {
            "notification_id": 10514,
            "organizer": "community",
            "event": "flock-2026",
            "code": "YTSDG",
            "action": "pretix.event.checkin",
            "orderposition_id": 905,
            "orderposition_positionid": 1,
            "checkin_list": 15,
            "first_checkin": None,
        },
    )

    msg = PretixMessageV1(body={"body": body, "headers": {}, "agent": agent})
    msg.validate()
    assert msg.app_name == "Pretix"
    assert msg.action_name == "event.checkin"
    assert msg.summary == summary
    assert (
        msg.app_icon == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
    )
    assert msg.usernames == [a for a in [agent] if a is not None]
    assert msg.groups == []


def test_pretix_unknown_action() -> None:
    """
    Test the Pretix schema on an unknown action
    """
    body = {
        "notification_id": 10514,
        "organizer": "community",
        "event": "flock-2026",
        "code": "YTSDG",
        "action": "pretix.event.dummy",
        "attendee_name": None,
        "instance_url": "https://example.com",
    }
    msg = PretixMessageV1(body={"body": body, "headers": {}, "agent": None})
    msg.validate()
    assert msg.app_name == "Pretix"
    assert msg.action_name == "event.dummy"
    assert msg.summary == "A user caused event.dummy in flock-2026 on Pretix"
