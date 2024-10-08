# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from webhook_to_fedora_messaging_messages.github import GithubMessageV1


class TestRepo:

    def test_push(self):
        headers = {
            "host": "2e3d-31-223-50-82.ngrok-free.app",
            "user-agent": "GitHub-Hookshot/4e5b6c2",
            "content-length": 7226,
            "accept": "*/*",
            "content-type": "application/json",
            "x-forwarded-for": "140.82.115.123",
            "x-forwarded-host": "2e3d-31-223-50-82.ngrok-free.app",
            "x-forwarded-proto": "https",
            "x-github-delivery": "2a49023a-201c-11ef-94cd-dbd2347128d4",
            "x-github-event": "push",
            "x-github-hook-id": 481337580,
            "x-github-hook-installation-target-id": "807808293",
            "x-github-hook-installation-target-type": "repository",
            "accept-encoding": "gzip",
            "x-hub-signature": "sdflksdlfksdlfksdlfk",
            "x-hub-signature-256": "sdflksdlfksdlfksdlfk",
        }

        body = {
            "ref": "refs/heads/main",
            "before": "8017283d32098eb99dce6aeee3b93831efd0f517",
            "after": "d5fd1a6b22a3d65272f9ae6c18d4581a5747682c",
            "repository": {
                "id": 807808293,
                "node_id": "R_kgDOMCYtJQ",
                "name": "demo_repo",
                "full_name": "brngylni/demo_repo",
                "private": True,
                "owner": {
                    "name": "brngylni",
                    "email": "66281850+brngylni@users.noreply.github.com",
                    "login": "brngylni",
                    "id": 66281850,
                    "node_id": "MDQ6VXNlcjY2MjgxODUw",
                    "avatar_url": "https://avatars.githubusercontent.com/u/66281850?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/brngylni",
                    "html_url": "https://github.com/brngylni",
                    "followers_url": "https://api.github.com/users/brngylni/followers",
                    "following_url": "https://api.github.com/users/brngylni/following{/other_user}",
                    "gists_url": "https://api.github.com/users/brngylni/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/brngylni/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/brngylni/subscriptions",
                    "organizations_url": "https://api.github.com/users/brngylni/orgs",
                    "repos_url": "https://api.github.com/users/brngylni/repos",
                    "events_url": "https://api.github.com/users/brngylni/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/brngylni/received_events",
                    "type": "User",
                    "site_admin": False,
                },
                "html_url": "https://github.com/brngylni/demo_repo",
                "description": None,
                "fork": False,
                "url": "https://github.com/brngylni/demo_repo",
                "forks_url": "https://api.github.com/repos/brngylni/demo_repo/forks",
                "keys_url": "https://api.github.com/repos/brngylni/demo_repo/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/brngylni/demo_repo/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/brngylni/demo_repo/teams",
                "hooks_url": "https://api.github.com/repos/brngylni/demo_repo/hooks",
                "issue_events_url": "https://api.github.com/repos/brngylni/demo_repo/issues/events{/number}",
                "events_url": "https://api.github.com/repos/brngylni/demo_repo/events",
                "assignees_url": "https://api.github.com/repos/brngylni/demo_repo/assignees{/user}",
                "branches_url": "https://api.github.com/repos/brngylni/demo_repo/branches{/branch}",
                "tags_url": "https://api.github.com/repos/brngylni/demo_repo/tags",
                "blobs_url": "https://api.github.com/repos/brngylni/demo_repo/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/brngylni/demo_repo/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/brngylni/demo_repo/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/brngylni/demo_repo/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/brngylni/demo_repo/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/brngylni/demo_repo/languages",
                "stargazers_url": "https://api.github.com/repos/brngylni/demo_repo/stargazers",
                "contributors_url": "https://api.github.com/repos/brngylni/demo_repo/contributors",
                "subscribers_url": "https://api.github.com/repos/brngylni/demo_repo/subscribers",
                "subscription_url": "https://api.github.com/repos/brngylni/demo_repo/subscription",
                "commits_url": "https://api.github.com/repos/brngylni/demo_repo/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/brngylni/demo_repo/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/brngylni/demo_repo/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/brngylni/demo_repo/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/brngylni/demo_repo/contents/{+path}",
                "compare_url": "https://api.github.com/repos/brngylni/demo_repo/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/brngylni/demo_repo/merges",
                "archive_url": "https://api.github.com/repos/brngylni/demo_repo/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/brngylni/demo_repo/downloads",
                "issues_url": "https://api.github.com/repos/brngylni/demo_repo/issues{/number}",
                "pulls_url": "https://api.github.com/repos/brngylni/demo_repo/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/brngylni/demo_repo/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/brngylni/demo_repo/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/brngylni/demo_repo/labels{/name}",
                "releases_url": "https://api.github.com/repos/brngylni/demo_repo/releases{/id}",
                "deployments_url": "https://api.github.com/repos/brngylni/demo_repo/deployments",
                "created_at": 1717013663,
                "updated_at": "2024-06-01T13:34:37Z",
                "pushed_at": 1717249080,
                "git_url": "git://github.com/brngylni/demo_repo.git",
                "ssh_url": "git@github.com:brngylni/demo_repo.git",
                "clone_url": "https://github.com/brngylni/demo_repo.git",
                "svn_url": "https://github.com/brngylni/demo_repo",
                "homepage": None,
                "size": 0,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": None,
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": False,
                "has_pages": False,
                "has_discussions": False,
                "forks_count": 0,
                "mirror_url": None,
                "archived": False,
                "disabled": False,
                "open_issues_count": 0,
                "license": None,
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
            "pusher": {"name": "brngylni", "email": "66281850+brngylni@users.noreply.github.com"},
            "sender": {
                "login": "brngylni",
                "id": 66281850,
                "node_id": "MDQ6VXNlcjY2MjgxODUw",
                "avatar_url": "https://avatars.githubusercontent.com/u/66281850?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/brngylni",
                "html_url": "https://github.com/brngylni",
                "followers_url": "https://api.github.com/users/brngylni/followers",
                "following_url": "https://api.github.com/users/brngylni/following{/other_user}",
                "gists_url": "https://api.github.com/users/brngylni/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/brngylni/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/brngylni/subscriptions",
                "organizations_url": "https://api.github.com/users/brngylni/orgs",
                "repos_url": "https://api.github.com/users/brngylni/repos",
                "events_url": "https://api.github.com/users/brngylni/events{/privacy}",
                "received_events_url": "https://api.github.com/users/brngylni/received_events",
                "type": "User",
                "site_admin": False,
            },
            "created": False,
            "deleted": False,
            "forced": False,
            "base_ref": None,
            "compare": "https://github.com/brngylni/demo_repo/compare/8017283d3209...d5fd1a6b22a3",
            "commits": [
                {
                    "id": "d5fd1a6b22a3d65272f9ae6c18d4581a5747682c",
                    "tree_id": "a0c50af2ba2cbf7afc61e4d1801ec51473452503",
                    "distinct": True,
                    "message": "djs",
                    "timestamp": "2024-06-01T16:37:54+03:00",
                    "url": "https://github.com/brngylni/demo_repo/commit/d5fd1a6b22a3d65272f9ae6c18d4581a5747682c",
                    "author": {
                        "name": "Super User",
                        "email": "barankara5@gmail.com",
                        "username": "brngylni",
                    },
                    "committer": {
                        "name": "Super User",
                        "email": "barankara5@gmail.com",
                        "username": "brngylni",
                    },
                    "added": [],
                    "removed": [],
                    "modified": ["README.md"],
                }
            ],
            "head_commit": {
                "id": "d5fd1a6b22a3d65272f9ae6c18d4581a5747682c",
                "tree_id": "a0c50af2ba2cbf7afc61e4d1801ec51473452503",
                "distinct": True,
                "message": "djs",
                "timestamp": "2024-06-01T16:37:54+03:00",
                "url": "https://github.com/brngylni/demo_repo/commit/d5fd1a6b22a3d65272f9ae6c18d4581a5747682c",
                "author": {
                    "name": "Super User",
                    "email": "barankara5@gmail.com",
                    "username": "brngylni",
                },
                "committer": {
                    "name": "Super User",
                    "email": "barankara5@gmail.com",
                    "username": "brngylni",
                },
                "added": [],
                "removed": [],
                "modified": ["README.md"],
            },
        }

        msg = GithubMessageV1(
            body={"body": body, "headers": headers, "agent": "fasUsernameExample"}
        )
        msg.validate()
        assert msg.app_name == "Github"
        assert msg.agent_name == "fasUsernameExample"
        assert msg.event_name == "push"
        assert msg.event_type == "repository"
        assert msg.signature == "sdflksdlfksdlfksdlfk"
        assert msg.signature_sha256 == "sdflksdlfksdlfksdlfk"
        assert (
            msg.app_icon
            == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
        )
        assert msg.target_id == "807808293"
        assert msg.summary == "fasUsernameExample created push on brngylni/demo_repo"
        assert str(msg) == (
            "Event: Push\nRepository: demo_repo (https://github.com/brngylni/demo_repo)\n"
            "Pusher: brngylni (https://github.com/brngylni)\nBranch: main\n"
            "Commits:\nCommit: djs by Super User (https://github.com/brngylni/demo_repo/commit/d5fd1a6b22a3d65272f9ae6c18d4581a5747682c)"
        )
        assert msg.usernames == ["fasUsernameExample"]
        assert msg.groups == []

    def test_fork(self):

        headers = {
            "host": "1300-31-223-43-169.ngrok-free.app",
            "user-agent": "GitHub-Hookshot/9729b30",
            "content-length": "10946",
            "accept": "*/*",
            "content-type": "application/json",
            "x-forwarded-for": "140.82.115.96",
            "x-forwarded-host": "1300-31-223-43-169.ngrok-free.app",
            "x-forwarded-proto": "https",
            "x-github-delivery": "2c88f570-360e-11ef-8a8c-b7d8d6902e14",
            "x-github-event": "fork",
            "x-github-hook-id": "481337580",
            "x-github-hook-installation-target-id": "807808293",
            "x-github-hook-installation-target-type": "repository",
            "x-hub-signature": "sha1=3b290912b53d4eb42a604b1a900e5818ab54f3df",
            "x-hub-signature-256": (
                "sha256=4449c05bc6e50e075c9962a04227527045ba0e85a04327a64d0aabf141497e19"
            ),
            "accept-encoding": "gzip",
        }

        body = {
            "forkee": {
                "id": 821774289,
                "node_id": "R_kgDOMPtH0Q",
                "name": "demo_repo",
                "full_name": "Demo-Webhook/demo_repo",
                "private": True,
                "owner": {
                    "login": "Demo-Webhook",
                    "id": 174186591,
                    "node_id": "O_kgDOCmHgXw",
                    "avatar_url": "https://avatars.githubusercontent.com/u/174186591?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/Demo-Webhook",
                    "html_url": "https://github.com/Demo-Webhook",
                    "followers_url": "https://api.github.com/users/Demo-Webhook/followers",
                    "following_url": "https://api.github.com/users/Demo-Webhook/following{/other_user}",
                    "gists_url": "https://api.github.com/users/Demo-Webhook/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/Demo-Webhook/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/Demo-Webhook/subscriptions",
                    "organizations_url": "https://api.github.com/users/Demo-Webhook/orgs",
                    "repos_url": "https://api.github.com/users/Demo-Webhook/repos",
                    "events_url": "https://api.github.com/users/Demo-Webhook/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/Demo-Webhook/received_events",
                    "type": "Organization",
                    "site_admin": False,
                },
                "html_url": "https://github.com/Demo-Webhook/demo_repo",
                "description": None,
                "fork": True,
                "url": "https://api.github.com/repos/Demo-Webhook/demo_repo",
                "forks_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/forks",
                "keys_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/teams",
                "hooks_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/hooks",
                "issue_events_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/issues/events{/number}",
                "events_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/events",
                "assignees_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/assignees{/user}",
                "branches_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/branches{/branch}",
                "tags_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/tags",
                "blobs_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/languages",
                "stargazers_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/stargazers",
                "contributors_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/contributors",
                "subscribers_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/subscribers",
                "subscription_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/subscription",
                "commits_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/contents/{+path}",
                "compare_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/merges",
                "archive_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/downloads",
                "issues_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/issues{/number}",
                "pulls_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/labels{/name}",
                "releases_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/releases{/id}",
                "deployments_url": "https://api.github.com/repos/Demo-Webhook/demo_repo/deployments",
                "created_at": "2024-06-29T11:53:17Z",
                "updated_at": "2024-06-29T11:53:17Z",
                "pushed_at": "2024-06-03T16:50:00Z",
                "git_url": "git://github.com/Demo-Webhook/demo_repo.git",
                "ssh_url": "git@github.com:Demo-Webhook/demo_repo.git",
                "clone_url": "https://github.com/Demo-Webhook/demo_repo.git",
                "svn_url": "https://github.com/Demo-Webhook/demo_repo",
                "homepage": None,
                "size": 34,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": None,
                "has_issues": False,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": False,
                "has_pages": False,
                "has_discussions": False,
                "forks_count": 0,
                "mirror_url": None,
                "archived": False,
                "disabled": False,
                "open_issues_count": 0,
                "license": None,
                "allow_forking": False,
                "is_template": False,
                "web_commit_signoff_required": False,
                "topics": [],
                "visibility": "private",
                "forks": 0,
                "open_issues": 0,
                "watchers": 0,
                "default_branch": "main",
                "public": False,
            },
            "repository": {
                "id": 807808293,
                "node_id": "R_kgDOMCYtJQ",
                "name": "demo_repo",
                "full_name": "brngylni/demo_repo",
                "private": True,
                "owner": {
                    "login": "brngylni",
                    "id": 66281850,
                    "node_id": "MDQ6VXNlcjY2MjgxODUw",
                    "avatar_url": "https://avatars.githubusercontent.com/u/66281850?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/brngylni",
                    "html_url": "https://github.com/brngylni",
                    "followers_url": "https://api.github.com/users/brngylni/followers",
                    "following_url": "https://api.github.com/users/brngylni/following{/other_user}",
                    "gists_url": "https://api.github.com/users/brngylni/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/brngylni/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/brngylni/subscriptions",
                    "organizations_url": "https://api.github.com/users/brngylni/orgs",
                    "repos_url": "https://api.github.com/users/brngylni/repos",
                    "events_url": "https://api.github.com/users/brngylni/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/brngylni/received_events",
                    "type": "User",
                    "site_admin": False,
                },
                "html_url": "https://github.com/brngylni/demo_repo",
                "description": None,
                "fork": False,
                "url": "https://api.github.com/repos/brngylni/demo_repo",
                "forks_url": "https://api.github.com/repos/brngylni/demo_repo/forks",
                "keys_url": "https://api.github.com/repos/brngylni/demo_repo/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/brngylni/demo_repo/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/brngylni/demo_repo/teams",
                "hooks_url": "https://api.github.com/repos/brngylni/demo_repo/hooks",
                "issue_events_url": "https://api.github.com/repos/brngylni/demo_repo/issues/events{/number}",
                "events_url": "https://api.github.com/repos/brngylni/demo_repo/events",
                "assignees_url": "https://api.github.com/repos/brngylni/demo_repo/assignees{/user}",
                "branches_url": "https://api.github.com/repos/brngylni/demo_repo/branches{/branch}",
                "tags_url": "https://api.github.com/repos/brngylni/demo_repo/tags",
                "blobs_url": "https://api.github.com/repos/brngylni/demo_repo/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/brngylni/demo_repo/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/brngylni/demo_repo/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/brngylni/demo_repo/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/brngylni/demo_repo/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/brngylni/demo_repo/languages",
                "stargazers_url": "https://api.github.com/repos/brngylni/demo_repo/stargazers",
                "contributors_url": "https://api.github.com/repos/brngylni/demo_repo/contributors",
                "subscribers_url": "https://api.github.com/repos/brngylni/demo_repo/subscribers",
                "subscription_url": "https://api.github.com/repos/brngylni/demo_repo/subscription",
                "commits_url": "https://api.github.com/repos/brngylni/demo_repo/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/brngylni/demo_repo/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/brngylni/demo_repo/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/brngylni/demo_repo/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/brngylni/demo_repo/contents/{+path}",
                "compare_url": "https://api.github.com/repos/brngylni/demo_repo/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/brngylni/demo_repo/merges",
                "archive_url": "https://api.github.com/repos/brngylni/demo_repo/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/brngylni/demo_repo/downloads",
                "issues_url": "https://api.github.com/repos/brngylni/demo_repo/issues{/number}",
                "pulls_url": "https://api.github.com/repos/brngylni/demo_repo/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/brngylni/demo_repo/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/brngylni/demo_repo/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/brngylni/demo_repo/labels{/name}",
                "releases_url": "https://api.github.com/repos/brngylni/demo_repo/releases{/id}",
                "deployments_url": "https://api.github.com/repos/brngylni/demo_repo/deployments",
                "created_at": "2024-05-29T20:14:23Z",
                "updated_at": "2024-06-03T16:50:03Z",
                "pushed_at": "2024-06-03T16:50:00Z",
                "git_url": "git://github.com/brngylni/demo_repo.git",
                "ssh_url": "git@github.com:brngylni/demo_repo.git",
                "clone_url": "https://github.com/brngylni/demo_repo.git",
                "svn_url": "https://github.com/brngylni/demo_repo",
                "homepage": None,
                "size": 34,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": None,
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": False,
                "has_pages": False,
                "has_discussions": False,
                "forks_count": 1,
                "mirror_url": None,
                "archived": False,
                "disabled": False,
                "open_issues_count": 0,
                "license": None,
                "allow_forking": True,
                "is_template": False,
                "web_commit_signoff_required": False,
                "topics": [],
                "visibility": "private",
                "forks": 1,
                "open_issues": 0,
                "watchers": 0,
                "default_branch": "main",
            },
            "sender": {
                "login": "Demo-Webhook",
                "id": 174186591,
                "node_id": "O_kgDOCmHgXw",
                "avatar_url": "https://avatars.githubusercontent.com/u/174186591?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/Demo-Webhook",
                "html_url": "https://github.com/Demo-Webhook",
                "followers_url": "https://api.github.com/users/Demo-Webhook/followers",
                "following_url": "https://api.github.com/users/Demo-Webhook/following{/other_user}",
                "gists_url": "https://api.github.com/users/Demo-Webhook/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/Demo-Webhook/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/Demo-Webhook/subscriptions",
                "organizations_url": "https://api.github.com/users/Demo-Webhook/orgs",
                "repos_url": "https://api.github.com/users/Demo-Webhook/repos",
                "events_url": "https://api.github.com/users/Demo-Webhook/events{/privacy}",
                "received_events_url": "https://api.github.com/users/Demo-Webhook/received_events",
                "type": "Organization",
                "site_admin": False,
            },
        }

        msg = GithubMessageV1(
            body={"body": body, "headers": headers, "agent": "fasUsernameExample"}
        )
        msg.validate()
        print(msg)
        print("printedd")
        assert msg.app_name == "Github"
        assert msg.agent_name == "fasUsernameExample"
        assert msg.event_name == "fork"
        assert msg.event_type == "repository"
        assert msg.signature == ("sha1=3b290912b53d4eb42a604b1" "a900e5818ab54f3df")
        assert msg.signature_sha256 == (
            "sha256=4449c05bc6e50e075c9962a042" "27527045ba0e85a04327a64d0aabf141497e19"
        )
        assert msg.target_id == "807808293"
        assert msg.summary == "fasUsernameExample created fork on brngylni/demo_repo"
        assert str(msg) == (
            "Event: Fork\nRepository: demo_repo (https://github.com/brngylni/demo_repo)\n"
            "Forkee: demo_repo (https://github.com/Demo-Webhook/demo_repo)\n"
            "Owner: Demo-Webhook (https://github.com/Demo-Webhook)"
        )
        assert (
            msg.app_icon
            == "https://apps.fedoraproject.org/img/icons/webhook-to-fedora-messaging.png"
        )
        assert msg.usernames == ["fasUsernameExample"]
        assert msg.groups == []
