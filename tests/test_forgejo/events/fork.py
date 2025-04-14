# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Event specification for Forgejo "fork" event
"""

headers = {
    "host": "w2fm.gridhead.net",
    "user-agent": "Go-http-client/1.1",
    "content-length": 10250,
    "accept": "*/*",
    "accept-encoding": "gzip",
    "connection": "keep-alive",
    "content-type": "application/json",
    "x-forgejo-event": "fork",
    "x-forgejo-delivery": "f09b1ff0-15d9-11f0-96fc-cdfc4c18328d",
    "x-forwarded-for": "217.197.91.145",
    "x-forwarded-proto": "https",
}

body = {
    "forkee": {
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
        "size": 50,
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
        "forks_count": 0,
        "watchers_count": 12,
        "open_issues_count": 2,
        "open_pr_counter": 1,
        "release_counter": 0,
        "default_branch": "main",
        "archived": False,
        "created_at": "2025-04-08T08:58:50Z",
        "updated_at": "2025-04-14T05:32:22Z",
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
    "repository": {
        "id": 437435,
        "owner": {
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
        "name": "w2fm-test",
        "full_name": "gridhead/w2fm-test",
        "description": "Testing repository of Forgejo Support for Webhook To Fedora Messaging",
        "empty": False,
        "private": False,
        "fork": True,
        "template": False,
        "parent": {
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
            "size": 50,
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
            "open_issues_count": 2,
            "open_pr_counter": 1,
            "release_counter": 0,
            "default_branch": "main",
            "archived": False,
            "created_at": "2025-04-08T08:58:50Z",
            "updated_at": "2025-04-14T05:32:22Z",
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
        "mirror": False,
        "size": 0,
        "language": "",
        "languages_url": "https://codeberg.org/api/v1/repos/gridhead/w2fm-test/languages",
        "html_url": "https://codeberg.org/gridhead/w2fm-test",
        "url": "https://codeberg.org/api/v1/repos/gridhead/w2fm-test",
        "link": "",
        "ssh_url": "git@codeberg.org:gridhead/w2fm-test.git",
        "clone_url": "https://codeberg.org/gridhead/w2fm-test.git",
        "original_url": "",
        "website": "",
        "stars_count": 0,
        "forks_count": 0,
        "watchers_count": 0,
        "open_issues_count": 0,
        "open_pr_counter": 0,
        "release_counter": 0,
        "default_branch": "main",
        "archived": False,
        "created_at": "2025-04-14T05:34:38Z",
        "updated_at": "2025-04-14T05:34:38Z",
        "archived_at": "1970-01-01T00:00:00Z",
        "permissions": {"admin": True, "push": True, "pull": True},
        "has_issues": False,
        "has_wiki": False,
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
}
