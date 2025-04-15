# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Event specification for GitHub "misc" event
"""

headers = {
    "host": "w2fm.gridhead.net",
    "user-agent": "GitHub-Hookshot/1c76dbe",
    "content-length": 7553,
    "accept": "*/*",
    "accept-encoding": "gzip",
    "connection": "keep-alive",
    "content-type": "application/json",
    "x-github-event": "misc",
    "x-github-delivery": "90fe6c0e-15d5-11f0-855e-5d9265838243",
    "x-github-hook-id": "540197327",
    "x-github-hook-installation-target-id": "963737664",
    "x-github-hook-installation-target-type": "repository",
    "x-hub-signature": "sha1=6f9f28257060042b5c10a8dd63eb668d8c5a6562",
    "x-hub-signature-256": "sha256=42b61ffef877bd99a5ee9155635092b79128c1800d821bb1fb0703a80b5fc5a7",
    "x-forwarded-for": "140.82.115.194",
    "x-forwarded-proto": "https",
}

body = {
    "ref": "refs/heads/flsk",
    "before": "adc70406eee8531a680f9bd38b4dbfab1cc55653",
    "after": "bb793868750af565b35f79e756dc4fac1b444672",
    "repository": {
        "id": 963737664,
        "node_id": "R_kgDOOXF4QA",
        "name": "test-repo",
        "full_name": "gridhead/test-repo",
        "private": True,
        "owner": {
            "name": "gridhead",
            "email": "testuser-w2fm@fedoraproject.org",
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
        "created_at": 1744265815,
        "updated_at": "2025-04-10T06:16:59Z",
        "pushed_at": 1744266744,
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
        "open_issues_count": 0,
        "license": "",
        "allow_forking": True,
        "is_template": False,
        "web_commit_signoff_required": False,
        "topics": [],
        "visibility": "private",
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "main",
        "stargazers": 0,
        "master_branch": "main",
    },
    "pusher": {"name": "gridhead", "email": "testuser-w2fm@fedoraproject.org"},
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
    "created": False,
    "deleted": False,
    "forced": True,
    "base_ref": "",
    "compare": "https://github.com/gridhead/test-repo/compare/adc70406eee8...bb793868750a",
    "commits": [
        {
            "id": "bb793868750af565b35f79e756dc4fac1b444672",
            "tree_id": "6178bc65ba5e6e8813305a18e2da16a07a68a77b",
            "distinct": True,
            "message": "Add simple webhook receiver service - https://w2fm.gridhead.net\n\nSigned-off-by: Akashdeep Dhar <testuser-w2fm@fedoraproject.org>",
            "timestamp": "2025-04-10T06:32:19Z",
            "url": "https://github.com/gridhead/test-repo/commit/bb793868750af565b35f79e756dc4fac1b444672",
            "author": {
                "name": "Akashdeep Dhar",
                "email": "testuser-w2fm@fedoraproject.org",
                "username": "gridhead",
            },
            "committer": {
                "name": "Akashdeep Dhar",
                "email": "testuser-w2fm@fedoraproject.org",
                "username": "gridhead",
            },
            "added": ["flsk.py"],
            "removed": [],
            "modified": [],
        }
    ],
    "head_commit": {
        "id": "bb793868750af565b35f79e756dc4fac1b444672",
        "tree_id": "6178bc65ba5e6e8813305a18e2da16a07a68a77b",
        "distinct": True,
        "message": "Add simple webhook receiver service - https://w2fm.gridhead.net\n\nSigned-off-by: Akashdeep Dhar <testuser-w2fm@fedoraproject.org>",
        "timestamp": "2025-04-10T06:32:19Z",
        "url": "https://github.com/gridhead/test-repo/commit/bb793868750af565b35f79e756dc4fac1b444672",
        "author": {
            "name": "Akashdeep Dhar",
            "email": "testuser-w2fm@fedoraproject.org",
            "username": "gridhead",
        },
        "committer": {
            "name": "Akashdeep Dhar",
            "email": "testuser-w2fm@fedoraproject.org",
            "username": "gridhead",
        },
        "added": ["flsk.py"],
        "removed": [],
        "modified": [],
    },
}
