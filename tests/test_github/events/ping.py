# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Event specification for GitHub "ping" event
"""

headers = {
    "host": "w2fm.gridhead.net",
    "user-agent": "GitHub-Hookshot/1c76dbe",
    "accept": "*/*",
    "accept-encoding": "gzip",
    "connection": "keep-alive",
    "content-type": "application/json",
    "x-github-event": "ping",
    "x-github-delivery": "b5a2a7f0-15d9-11f0-8c3e-3d1c3a9a7f21",
    "x-github-hook-id": "540197327",
    "x-github-hook-installation-target-id": "963737664",
    "x-github-hook-installation-target-type": "repository",
    "x-hub-signature": "sha1=0000000000000000000000000000000000000000",
    "x-hub-signature-256": "sha256=0000000000000000000000000000000000000000000000000000000000000000",
    "x-forwarded-for": "140.82.115.194",
    "x-forwarded-proto": "https",
}

body = {
    "zen": "Keep it logically awesome.",
    "hook_id": 540197327,
    "hook": {
        "type": "Repository",
        "id": 540197327,
        "name": "web",
        "active": True,
        "events": ["push"],
        "config": {"content_type": "json", "insecure_ssl": "0"},
        "updated_at": "2025-04-10T06:16:59Z",
        "created_at": "2025-04-10T06:16:59Z",
    },
    "repository": {
        "id": 963737664,
        "name": "test-repo",
        "full_name": "gridhead/test-repo",
        "html_url": "https://github.com/gridhead/test-repo",
    },
    "sender": {
        "login": "gridhead",
        "id": 49605954,
        "html_url": "https://github.com/gridhead",
    },
}
