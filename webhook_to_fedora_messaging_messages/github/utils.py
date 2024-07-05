# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later


def summarize_repository_event(event_type: str, payload: dict) -> str:

    if event_type in ["push", "fork"]:
        summary = _summarize_repository_event(event_type, payload)
    elif event_type.startswith("pull_request"):
        summary = _summarize_pull_request_event(event_type, payload)
    elif event_type.startswith("issue"):
        summary = _summarize_issue_event(event_type, payload)
    else:
        summary = "Event type not supported"

    return summary


def _summarize_repository_event(event_type: str, payload: dict) -> str:
    if event_type == "push":
        return _summarize_push_event(payload)
    elif event_type == "fork":
        return _summarize_fork_event(payload)
    else:
        raise NotImplementedError


def _summarize_issue_event(event_type: str, payload: dict) -> str:
    if event_type == "issues":
        return _summarize_issues_event(payload)
    elif event_type == "issue_comment":
        return _summarize_issue_comment_event(payload)
    else:
        raise NotImplementedError


def _summarize_push_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    pusher = payload["pusher"]["name"]
    pusher_url = f"https://github.com/{payload['pusher']['name']}"
    branch = payload["ref"].split("/")[-1]
    commits = "\n".join(
        [
            f"Commit: {commit['message']} by {commit['author']['name']} ({commit['url']})"
            for commit in payload["commits"]
        ]
    )

    return (
        f"Event: Push\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Pusher: {pusher} ({pusher_url})\n"
        f"Branch: {branch}\n"
        f"Commits:\n{commits}"
    )


def _summarize_fork_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    forkee = payload["forkee"]["name"]
    forkee_url = payload["forkee"]["html_url"]
    owner = payload["forkee"]["owner"]["login"]
    owner_url = payload["forkee"]["owner"]["html_url"]

    return (
        f"Event: Fork\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Forkee: {forkee} ({forkee_url})\n"
        f"Owner: {owner} ({owner_url})"
    )


def _summarize_pull_request_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    pr = payload["pull_request"]
    title = pr["title"]
    pr_url = pr["html_url"]
    author = pr["user"]["login"]
    status = payload["action"]
    source_branch = pr["head"]["ref"]
    dest_branch = pr["base"]["ref"]
    reviewers = ", ".join([reviewer["login"] for reviewer in pr["requested_reviewers"]])

    return (
        f"Event: Pull Request\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Title: {title}\n"
        f"URL: {pr_url}\n"
        f"Author: {author}\n"
        f"Status: {status}\n"
        f"Source Branch: {source_branch}\n"
        f"Destination Branch: {dest_branch}\n"
        f"Reviewers: {reviewers}"
    )


def _summarize_issues_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    issue = payload["issue"]
    title = issue["title"]
    issue_url = issue["html_url"]
    author = issue["user"]["login"]
    status = payload["action"]
    labels = ", ".join([label["name"] for label in issue["labels"]])

    return (
        f"Event: Issue\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Title: {title}\n"
        f"URL: {issue_url}\n"
        f"Author: {author}\n"
        f"Status: {status}\n"
        f"Labels: {labels}"
    )


def _summarize_issue_comment_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    issue = payload["issue"]
    issue_title = issue["title"]
    issue_url = issue["html_url"]
    comment = payload["comment"]
    comment_author = comment["user"]["login"]
    comment_body = comment["body"]
    comment_url = comment["html_url"]

    return (
        f"Event: Issue Comment\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Issue: {issue_title} ({issue_url})\n"
        f"Comment Author: {comment_author}\n"
        f"Comment: {comment_body}\n"
        f"Comment URL: {comment_url}"
    )
