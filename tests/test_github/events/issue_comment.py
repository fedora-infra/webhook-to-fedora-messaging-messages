# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Event specification for GitHub "issue_comment" event
"""

headers = {
    "host": "w2fm.gridhead.net",
    "user-agent": "GitHub-Hookshot/1c76dbe",
    "content-length": 11736,
    "accept": "*/*",
    "accept-encoding": "gzip",
    "connection": "keep-alive",
    "content-type": "application/json",
    "x-github-event": "issue_comment",
    "x-github-delivery": "bf246cc0-15d8-11f0-8018-4e9445c82643",
    "x-github-hook-id": "540197327",
    "x-github-hook-installation-target-id": "963737664",
    "x-github-hook-installation-target-type": "repository",
    "x-hub-signature": "sha1=e3d33370c9bcec3c56663879b2236bc2b7ac0468",
    "x-hub-signature-256": "sha256=5982a7b0c952a608351a47e19ce456ae6308f1d629571974b002c85b668f7b03",
    "x-forwarded-for": "140.82.115.196",
    "x-forwarded-proto": "https",
}

body = {
    "action": "created",
    "issue": {
        "url": "https://api.github.com/repos/gridhead/test-repo/issues/2",
        "repository_url": "https://api.github.com/repos/gridhead/test-repo",
        "labels_url": "https://api.github.com/repos/gridhead/test-repo/issues/2/labels{/name}",
        "comments_url": "https://api.github.com/repos/gridhead/test-repo/issues/2/comments",
        "events_url": "https://api.github.com/repos/gridhead/test-repo/issues/2/events",
        "html_url": "https://github.com/gridhead/test-repo/issues/2",
        "id": 2984635457,
        "node_id": "I_kwDOOXF4QM6x5exB",
        "number": 2,
        "title": "This is a sample issue ticket",
        "user": {
            "login": "gridhead",
            "id": 49605954,
            "node_id": "MDQ6VXNlcjQ5NjA1OTU0",
            "avatar_url": "https://avatars.githubusercontent.com/u/49605954?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/gridhead",
            "html_url": "https://github.com/gridhead",
            "followers_url": "https://api.github.com/users/gridhead/followers",
            "following_url": "https://api.github.com/users/gridhead/following{/other_user}",
            "gists_url": "https://api.github.com/users/gridhead/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/gridhead/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/gridhead/subscriptions",
            "organizations_url": "https://api.github.com/users/gridhead/orgs",
            "repos_url": "https://api.github.com/users/gridhead/repos",
            "events_url": "https://api.github.com/users/gridhead/events{/privacy}",
            "received_events_url": "https://api.github.com/users/gridhead/received_events",
            "type": "User",
            "user_view_type": "public",
            "site_admin": False,
        },
        "labels": [
            {
                "id": 8432864129,
                "node_id": "LA_kwDOOXF4QM8AAAAB9qNLgQ",
                "url": "https://api.github.com/repos/gridhead/test-repo/labels/bug",
                "name": "bug",
                "color": "d73a4a",
                "default": True,
                "description": "Something isn't working",
            }
        ],
        "state": "open",
        "locked": False,
        "assignee": {
            "login": "gridhead",
            "id": 49605954,
            "node_id": "MDQ6VXNlcjQ5NjA1OTU0",
            "avatar_url": "https://avatars.githubusercontent.com/u/49605954?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/gridhead",
            "html_url": "https://github.com/gridhead",
            "followers_url": "https://api.github.com/users/gridhead/followers",
            "following_url": "https://api.github.com/users/gridhead/following{/other_user}",
            "gists_url": "https://api.github.com/users/gridhead/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/gridhead/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/gridhead/subscriptions",
            "organizations_url": "https://api.github.com/users/gridhead/orgs",
            "repos_url": "https://api.github.com/users/gridhead/repos",
            "events_url": "https://api.github.com/users/gridhead/events{/privacy}",
            "received_events_url": "https://api.github.com/users/gridhead/received_events",
            "type": "User",
            "user_view_type": "public",
            "site_admin": False,
        },
        "assignees": [
            {
                "login": "gridhead",
                "id": 49605954,
                "node_id": "MDQ6VXNlcjQ5NjA1OTU0",
                "avatar_url": "https://avatars.githubusercontent.com/u/49605954?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/gridhead",
                "html_url": "https://github.com/gridhead",
                "followers_url": "https://api.github.com/users/gridhead/followers",
                "following_url": "https://api.github.com/users/gridhead/following{/other_user}",
                "gists_url": "https://api.github.com/users/gridhead/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/gridhead/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/gridhead/subscriptions",
                "organizations_url": "https://api.github.com/users/gridhead/orgs",
                "repos_url": "https://api.github.com/users/gridhead/repos",
                "events_url": "https://api.github.com/users/gridhead/events{/privacy}",
                "received_events_url": "https://api.github.com/users/gridhead/received_events",
                "type": "User",
                "user_view_type": "public",
                "site_admin": False,
            }
        ],
        "milestone": "",
        "comments": 1,
        "created_at": "2025-04-10T06:45:29Z",
        "updated_at": "2025-04-10T06:55:11Z",
        "closed_at": "",
        "author_association": "OWNER",
        "sub_issues_summary": {"total": 0, "completed": 0, "percent_completed": 0},
        "active_lock_reason": "",
        "body": "This is a sample issue ticket",
        "reactions": {
            "url": "https://api.github.com/repos/gridhead/test-repo/issues/2/reactions",
            "total_count": 0,
            "+1": 0,
            "-1": 0,
            "laugh": 0,
            "hooray": 0,
            "confused": 0,
            "heart": 0,
            "rocket": 0,
            "eyes": 0,
        },
        "timeline_url": "https://api.github.com/repos/gridhead/test-repo/issues/2/timeline",
        "performed_via_github_app": "",
        "state_reason": "",
    },
    "comment": {
        "url": "https://api.github.com/repos/gridhead/test-repo/issues/comments/2791741060",
        "html_url": "https://github.com/gridhead/test-repo/issues/2#issuecomment-2791741060",
        "issue_url": "https://api.github.com/repos/gridhead/test-repo/issues/2",
        "id": 2791741060,
        "node_id": "IC_kwDOOXF4QM6mZpaE",
        "user": {
            "login": "gridhead",
            "id": 49605954,
            "node_id": "MDQ6VXNlcjQ5NjA1OTU0",
            "avatar_url": "https://avatars.githubusercontent.com/u/49605954?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/gridhead",
            "html_url": "https://github.com/gridhead",
            "followers_url": "https://api.github.com/users/gridhead/followers",
            "following_url": "https://api.github.com/users/gridhead/following{/other_user}",
            "gists_url": "https://api.github.com/users/gridhead/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/gridhead/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/gridhead/subscriptions",
            "organizations_url": "https://api.github.com/users/gridhead/orgs",
            "repos_url": "https://api.github.com/users/gridhead/repos",
            "events_url": "https://api.github.com/users/gridhead/events{/privacy}",
            "received_events_url": "https://api.github.com/users/gridhead/received_events",
            "type": "User",
            "user_view_type": "public",
            "site_admin": False,
        },
        "created_at": "2025-04-10T06:55:09Z",
        "updated_at": "2025-04-10T06:55:09Z",
        "author_association": "OWNER",
        "body": "Issue comment here",
        "reactions": {
            "url": "https://api.github.com/repos/gridhead/test-repo/issues/comments/2791741060/reactions",
            "total_count": 0,
            "+1": 0,
            "-1": 0,
            "laugh": 0,
            "hooray": 0,
            "confused": 0,
            "heart": 0,
            "rocket": 0,
            "eyes": 0,
        },
        "performed_via_github_app": "",
    },
    "repository": {
        "id": 963737664,
        "node_id": "R_kgDOOXF4QA",
        "name": "test-repo",
        "full_name": "gridhead/test-repo",
        "private": False,
        "owner": {
            "login": "gridhead",
            "id": 49605954,
            "node_id": "MDQ6VXNlcjQ5NjA1OTU0",
            "avatar_url": "https://avatars.githubusercontent.com/u/49605954?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/gridhead",
            "html_url": "https://github.com/gridhead",
            "followers_url": "https://api.github.com/users/gridhead/followers",
            "following_url": "https://api.github.com/users/gridhead/following{/other_user}",
            "gists_url": "https://api.github.com/users/gridhead/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/gridhead/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/gridhead/subscriptions",
            "organizations_url": "https://api.github.com/users/gridhead/orgs",
            "repos_url": "https://api.github.com/users/gridhead/repos",
            "events_url": "https://api.github.com/users/gridhead/events{/privacy}",
            "received_events_url": "https://api.github.com/users/gridhead/received_events",
            "type": "User",
            "user_view_type": "public",
            "site_admin": False,
        },
        "html_url": "https://github.com/gridhead/test-repo",
        "description": "Test repository for Webhook To Fedora Messaging",
        "fork": False,
        "url": "https://api.github.com/repos/gridhead/test-repo",
        "forks_url": "https://api.github.com/repos/gridhead/test-repo/forks",
        "keys_url": "https://api.github.com/repos/gridhead/test-repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/gridhead/test-repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/gridhead/test-repo/teams",
        "hooks_url": "https://api.github.com/repos/gridhead/test-repo/hooks",
        "issue_events_url": "https://api.github.com/repos/gridhead/test-repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/gridhead/test-repo/events",
        "assignees_url": "https://api.github.com/repos/gridhead/test-repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/gridhead/test-repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/gridhead/test-repo/tags",
        "blobs_url": "https://api.github.com/repos/gridhead/test-repo/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/gridhead/test-repo/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/gridhead/test-repo/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/gridhead/test-repo/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/gridhead/test-repo/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/gridhead/test-repo/languages",
        "stargazers_url": "https://api.github.com/repos/gridhead/test-repo/stargazers",
        "contributors_url": "https://api.github.com/repos/gridhead/test-repo/contributors",
        "subscribers_url": "https://api.github.com/repos/gridhead/test-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/gridhead/test-repo/subscription",
        "commits_url": "https://api.github.com/repos/gridhead/test-repo/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/gridhead/test-repo/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/gridhead/test-repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/gridhead/test-repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/gridhead/test-repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/gridhead/test-repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/gridhead/test-repo/merges",
        "archive_url": "https://api.github.com/repos/gridhead/test-repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/gridhead/test-repo/downloads",
        "issues_url": "https://api.github.com/repos/gridhead/test-repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/gridhead/test-repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/gridhead/test-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/gridhead/test-repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/gridhead/test-repo/labels{/name}",
        "releases_url": "https://api.github.com/repos/gridhead/test-repo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/gridhead/test-repo/deployments",
        "created_at": "2025-04-10T06:16:55Z",
        "updated_at": "2025-04-10T06:53:18Z",
        "pushed_at": "2025-04-10T06:46:48Z",
        "git_url": "git://github.com/gridhead/test-repo.git",
        "ssh_url": "git@github.com:gridhead/test-repo.git",
        "clone_url": "https://github.com/gridhead/test-repo.git",
        "svn_url": "https://github.com/gridhead/test-repo",
        "homepage": "",
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "has_discussions": False,
        "forks_count": 0,
        "mirror_url": "",
        "archived": False,
        "disabled": False,
        "open_issues_count": 2,
        "license": "",
        "allow_forking": True,
        "is_template": False,
        "web_commit_signoff_required": False,
        "topics": [],
        "visibility": "public",
        "forks": 0,
        "open_issues": 2,
        "watchers": 0,
        "default_branch": "main",
    },
    "sender": {
        "login": "gridhead",
        "id": 49605954,
        "node_id": "MDQ6VXNlcjQ5NjA1OTU0",
        "avatar_url": "https://avatars.githubusercontent.com/u/49605954?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/gridhead",
        "html_url": "https://github.com/gridhead",
        "followers_url": "https://api.github.com/users/gridhead/followers",
        "following_url": "https://api.github.com/users/gridhead/following{/other_user}",
        "gists_url": "https://api.github.com/users/gridhead/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/gridhead/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/gridhead/subscriptions",
        "organizations_url": "https://api.github.com/users/gridhead/orgs",
        "repos_url": "https://api.github.com/users/gridhead/repos",
        "events_url": "https://api.github.com/users/gridhead/events{/privacy}",
        "received_events_url": "https://api.github.com/users/gridhead/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": False,
    },
}
