# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Event specification for Forgejo "fork" event
"""

headers = {
    "host": "w2fm.gridhead.net",
    "user-agent": "Go-http-client/1.1",
    "content-length": "11132",
    "accept": "*/*",
    "accept-encoding": "gzip",
    "connection": "keep-alive",
    "content-type": "application/json",
    "x-forgejo-event": "issues",
    "x-forgejo-delivery": "a9f43ba1-b327-4076-aaee-f29bf753710c",
    "x-forwarded-for": "217.197.91.145",
    "x-forwarded-proto": "https",
    "x-hub-signature": "sha1=f9a6aae9f318fffeaab18ecb093fd2a5867839b6",
    "x-hub-signature-256": "sha256=be7518b5453cb3a6626726d301b2c80d53c04246e5d9a8e454b616d15a5e0b66",
}

body = {
    "action": "opened",
    "number": 5,
    "issue": {
        "id": 1300409,
        "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/issues/5",
        "html_url": "https://codeberg.org/fedora/w2fm-test/issues/5",
        "number": 5,
        "user": {
            "id": 262265,
            "login": "gridhead",
            "login_name": "",
            "source_id": 0,
            "full_name": "Akashdeep Dhar",
            "email": "testuser-w2fm@fedoraproject.org",
            "avatar_url": "https://codeberg.org/avatars/0ceeb8e5004de3aa16a074f2936f8bf4047de08ad9db934877ae9e1b2d0530f7",
            "html_url": "https://codeberg.org/gridhead",
            "language": "en-US",
            "is_admin": False,
            "last_login": "2025-04-14T03:36:11Z",
            "created": "2025-01-21T11:12:28Z",
            "restricted": False,
            "active": True,
            "prohibit_login": False,
            "location": "127.0.0.1",
            "pronouns": "he/him",
            "website": "https://gridhead.net/",
            "description": "Akashdeep Dhar is a software engineer in the Red Hat Community Linux Engineering team, working on researching and developing applications running on Fedora Infrastructure, and has served twice in Fedora Council.",
            "visibility": "public",
            "followers_count": 0,
            "following_count": 0,
            "starred_repos_count": 0,
            "username": "gridhead",
        },
        "original_author": "",
        "original_author_id": 0,
        "title": "Sample issue for webhook trigger checking",
        "body": "Sample issue for webhook trigger checking",
        "ref": "",
        "assets": [],
        "labels": [
            {
                "id": 352145,
                "name": "Kind/Bug",
                "exclusive": False,
                "is_archived": False,
                "color": "ee0701",
                "description": "Something is not working",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352145",
            },
            {
                "id": 352148,
                "name": "Kind/Feature",
                "exclusive": False,
                "is_archived": False,
                "color": "0288d1",
                "description": "New functionality",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352148",
            },
            {
                "id": 352151,
                "name": "Kind/Enhancement",
                "exclusive": False,
                "is_archived": False,
                "color": "84b6eb",
                "description": "Improve existing functionality",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352151",
            },
            {
                "id": 352154,
                "name": "Kind/Security",
                "exclusive": False,
                "is_archived": False,
                "color": "9c27b0",
                "description": "This is security issue",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352154",
            },
            {
                "id": 352157,
                "name": "Kind/Testing",
                "exclusive": False,
                "is_archived": False,
                "color": "795548",
                "description": "Issue or pull request related to testing",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352157",
            },
            {
                "id": 352160,
                "name": "Kind/Documentation",
                "exclusive": False,
                "is_archived": False,
                "color": "37474f",
                "description": "Documentation changes",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352160",
            },
            {
                "id": 352163,
                "name": "Compat/Breaking",
                "exclusive": False,
                "is_archived": False,
                "color": "c62828",
                "description": "Breaking change that won't be backward compatible",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352163",
            },
            {
                "id": 352169,
                "name": "Reviewed/Invalid",
                "exclusive": True,
                "is_archived": False,
                "color": "546e7a",
                "description": "Invalid issue",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352169",
            },
            {
                "id": 352178,
                "name": "Status/Need More Info",
                "exclusive": True,
                "is_archived": False,
                "color": "424242",
                "description": "Feedback is required to reproduce issue or to continue work",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352178",
            },
            {
                "id": 352187,
                "name": "Priority/Critical",
                "exclusive": True,
                "is_archived": False,
                "color": "b71c1c",
                "description": "The priority is critical",
                "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/labels/352187",
            },
        ],
        "milestone": "",
        "assignee": {
            "id": 262265,
            "login": "gridhead",
            "login_name": "",
            "source_id": 0,
            "full_name": "Akashdeep Dhar",
            "email": "gridhead@noreply.codeberg.org",
            "avatar_url": "https://codeberg.org/avatars/0ceeb8e5004de3aa16a074f2936f8bf4047de08ad9db934877ae9e1b2d0530f7",
            "html_url": "https://codeberg.org/gridhead",
            "language": "",
            "is_admin": False,
            "last_login": "0001-01-01T00:00:00Z",
            "created": "2025-01-21T11:12:28Z",
            "restricted": False,
            "active": False,
            "prohibit_login": False,
            "location": "127.0.0.1",
            "pronouns": "he/him",
            "website": "https://gridhead.net/",
            "description": "Akashdeep Dhar is a software engineer in the Red Hat Community Linux Engineering team, working on researching and developing applications running on Fedora Infrastructure, and has served twice in Fedora Council.",
            "visibility": "public",
            "followers_count": 0,
            "following_count": 0,
            "starred_repos_count": 0,
            "username": "gridhead",
        },
        "assignees": [
            {
                "id": 262265,
                "login": "gridhead",
                "login_name": "",
                "source_id": 0,
                "full_name": "Akashdeep Dhar",
                "email": "gridhead@noreply.codeberg.org",
                "avatar_url": "https://codeberg.org/avatars/0ceeb8e5004de3aa16a074f2936f8bf4047de08ad9db934877ae9e1b2d0530f7",
                "html_url": "https://codeberg.org/gridhead",
                "language": "",
                "is_admin": False,
                "last_login": "0001-01-01T00:00:00Z",
                "created": "2025-01-21T11:12:28Z",
                "restricted": False,
                "active": False,
                "prohibit_login": False,
                "location": "127.0.0.1",
                "pronouns": "he/him",
                "website": "https://gridhead.net/",
                "description": "Akashdeep Dhar is a software engineer in the Red Hat Community Linux Engineering team, working on researching and developing applications running on Fedora Infrastructure, and has served twice in Fedora Council.",
                "visibility": "public",
                "followers_count": 0,
                "following_count": 0,
                "starred_repos_count": 0,
                "username": "gridhead",
            }
        ],
        "state": "open",
        "is_locked": False,
        "comments": 0,
        "created_at": "2025-04-14T05:21:59Z",
        "updated_at": "2025-04-14T05:22:10Z",
        "closed_at": "",
        "due_date": "",
        "pull_request": "",
        "repository": {
            "id": 421133,
            "name": "w2fm-test",
            "owner": "fedora",
            "full_name": "fedora/w2fm-test",
        },
        "pin_order": 0,
    },
    "repository": {
        "id": 421133,
        "owner": {
            "id": 95691,
            "login": "fedora",
            "login_name": "",
            "source_id": 0,
            "full_name": "Fedora Project",
            "email": "",
            "avatar_url": "https://codeberg.org/avatars/8ee2d6b067d6e3f045b189a4ea76cd53103749e93ef96f76b61d2aad7ac97e40",
            "html_url": "https://codeberg.org/fedora",
            "language": "",
            "is_admin": False,
            "last_login": "0001-01-01T00:00:00Z",
            "created": "2023-05-06T12:36:00Z",
            "restricted": False,
            "active": False,
            "prohibit_login": False,
            "location": "",
            "pronouns": "",
            "website": "https://fedoraproject.org/",
            "description": "Fedora Project Space",
            "visibility": "public",
            "followers_count": 10,
            "following_count": 0,
            "starred_repos_count": 0,
            "username": "fedora",
        },
        "name": "w2fm-test",
        "full_name": "fedora/w2fm-test",
        "description": "Testing repository of Forgejo Support for Webhook To Fedora Messaging",
        "empty": False,
        "private": False,
        "fork": False,
        "template": False,
        "parent": "",
        "mirror": False,
        "size": 47,
        "language": "",
        "languages_url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test/languages",
        "html_url": "https://codeberg.org/fedora/w2fm-test",
        "url": "https://codeberg.org/api/v1/repos/fedora/w2fm-test",
        "link": "",
        "ssh_url": "git@codeberg.org:fedora/w2fm-test.git",
        "clone_url": "https://codeberg.org/fedora/w2fm-test.git",
        "original_url": "",
        "website": "",
        "stars_count": 0,
        "forks_count": 1,
        "watchers_count": 12,
        "open_issues_count": 1,
        "open_pr_counter": 0,
        "release_counter": 0,
        "default_branch": "main",
        "archived": False,
        "created_at": "2025-04-08T08:58:50Z",
        "updated_at": "2025-04-09T08:45:15Z",
        "archived_at": "1970-01-01T00:00:00Z",
        "permissions": {"admin": True, "push": True, "pull": True},
        "has_issues": True,
        "internal_tracker": {
            "enable_time_tracker": True,
            "allow_only_contributors_to_track_time": True,
            "enable_issue_dependencies": True,
        },
        "has_wiki": False,
        "wiki_branch": "main",
        "globally_editable_wiki": False,
        "has_pull_requests": True,
        "has_projects": False,
        "has_releases": False,
        "has_packages": False,
        "has_actions": False,
        "ignore_whitespace_conflicts": False,
        "allow_merge_commits": True,
        "allow_rebase": True,
        "allow_rebase_explicit": True,
        "allow_squash_merge": True,
        "allow_fast_forward_only_merge": True,
        "allow_rebase_update": True,
        "default_delete_branch_after_merge": False,
        "default_merge_style": "merge",
        "default_allow_maintainer_edit": False,
        "default_update_style": "merge",
        "avatar_url": "",
        "internal": False,
        "mirror_interval": "",
        "object_format_name": "sha1",
        "mirror_updated": "0001-01-01T00:00:00Z",
        "repo_transfer": "",
        "topics": "",
    },
    "sender": {
        "id": 262265,
        "login": "gridhead",
        "login_name": "",
        "source_id": 0,
        "full_name": "Akashdeep Dhar",
        "email": "gridhead@noreply.codeberg.org",
        "avatar_url": "https://codeberg.org/avatars/0ceeb8e5004de3aa16a074f2936f8bf4047de08ad9db934877ae9e1b2d0530f7",
        "html_url": "https://codeberg.org/gridhead",
        "language": "",
        "is_admin": False,
        "last_login": "0001-01-01T00:00:00Z",
        "created": "2025-01-21T11:12:28Z",
        "restricted": False,
        "active": False,
        "prohibit_login": False,
        "location": "127.0.0.1",
        "pronouns": "he/him",
        "website": "https://gridhead.net/",
        "description": "Akashdeep Dhar is a software engineer in the Red Hat Community Linux Engineering team, working on researching and developing applications running on Fedora Infrastructure, and has served twice in Fedora Council.",
        "visibility": "public",
        "followers_count": 0,
        "following_count": 0,
        "starred_repos_count": 0,
        "username": "gridhead",
    },
    "commit_id": "",
}
