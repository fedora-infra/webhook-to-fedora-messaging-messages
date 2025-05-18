# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Event specification for GitLab "issues" event
"""

headers = {
    "host": "w2fm.gridhead.net",
    "user-agent": "GitLab/18.1.0-pre",
    "content-length": 1862,
    "accept": "*/*",
    "accept-encoding": "gzip, br",
    "connection": "keep-alive",
    "content-type": "application/json",
    "x-gitlab-event": "Push Hook",
    "x-gitlab-webhook-uuid": "61bde8ae-e9f9-49ab-b2a4-09c229c3fe1a",
    "x-gitlab-event-uuid": "1e1650fc-9bf2-4eec-bec7-2cd6301d3f6b",
    "x-forwarded-for": "34.74.226.2",
    "x-forwarded-proto": "https",
}

body = {
    "object_kind": "push",
    "event_name": "push",
    "before": "0000000000000000000000000000000000000000",
    "after": "7aa00b22e26de3efc8270aebc9ee51c40107d4ff",
    "ref": "refs/heads/test-branch",
    "ref_protected": False,
    "checkout_sha": "7aa00b22e26de3efc8270aebc9ee51c40107d4ff",
    "message": None,
    "user_id": 16997011,
    "user_name": "Shounak Dey",
    "user_username": "sdglitched",
    "user_email": None,
    "user_avatar": "https://secure.gravatar.com/avatar/9458b3a00e2f3f262b05309bd9a43a233c28689e6cbae811b198cd5ee9fb3653?s=80&d=identicon",
    "project_id": 69912300,
    "project": {
        "id": 69912300,
        "name": "w2fm-test",
        "description": None,
        "web_url": "https://gitlab.com/sdglitched/w2fm-test",
        "avatar_url": None,
        "git_ssh_url": "git@gitlab.com:sdglitched/w2fm-test.git",
        "git_http_url": "https://gitlab.com/sdglitched/w2fm-test.git",
        "namespace": "Shounak Dey",
        "visibility_level": 0,
        "path_with_namespace": "sdglitched/w2fm-test",
        "default_branch": "main",
        "ci_config_path": "",
        "homepage": "https://gitlab.com/sdglitched/w2fm-test",
        "url": "git@gitlab.com:sdglitched/w2fm-test.git",
        "ssh_url": "git@gitlab.com:sdglitched/w2fm-test.git",
        "http_url": "https://gitlab.com/sdglitched/w2fm-test.git",
    },
    "commits": [
        {
            "id": "7aa00b22e26de3efc8270aebc9ee51c40107d4ff",
            "message": "Test commit\n\nSigned-off-by: Shounak Dey <testaddr@testaddr.test>\n",
            "title": "Test commit",
            "timestamp": "2025-05-16T21:24:13+05:30",
            "url": "https://gitlab.com/sdglitched/w2fm-test/-/commit/7aa00b22e26de3efc8270aebc9ee51c40107d4ff",
            "author": {"name": "Shounak Dey", "email": "testaddr@testaddr.test"},
            "added": [],
            "modified": ["README.md"],
            "removed": [],
        }
    ],
    "total_commits_count": 1,
    "push_options": {},
    "repository": {
        "name": "w2fm-test",
        "url": "git@gitlab.com:sdglitched/w2fm-test.git",
        "description": None,
        "homepage": "https://gitlab.com/sdglitched/w2fm-test",
        "git_http_url": "https://gitlab.com/sdglitched/w2fm-test.git",
        "git_ssh_url": "git@gitlab.com:sdglitched/w2fm-test.git",
        "visibility_level": 0,
    },
}
