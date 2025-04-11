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


def _summarize_push_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    pusher = payload["pusher"]["full_name"]
    pusher_url = payload["pusher"]["html_url"]
    branch = payload["ref"].split("/")[-1]
    commits = "\n".join(
        [
            f"Commit: {commit["message"]} by {commit["author"]["name"]} ({commit["url"]})"
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
    forkee = payload["forkee"]["full_name"]
    forkee_url = payload["forkee"]["html_url"]
    owner = payload["forkee"]["owner"]["full_name"]
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
    pr_title = payload["pull_request"]["title"]
    pr_url = payload["pull_request"]["html_url"]
    pr_author = payload["pull_request"]["user"]["full_name"]
    pr_source_branch = payload["pull_request"]["head"]["ref"]
    pr_dest_branch = payload["pull_request"]["base"]["ref"]
    pr_reviewers = ", ".join([reviewer["login"] for reviewer in payload["pull_request"]["requested_reviewers"]])
    status = payload["action"]

    return (
        f"Event: Pull Request\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Title: {pr_title}\n"
        f"URL: {pr_url}\n"
        f"Author: {pr_author}\n"
        f"Status: {status}\n"
        f"Source Branch: {source_branch}\n"
        f"Destination Branch: {dest_branch}\n"
        f"Reviewers: {pr_reviewers}"
    )

def _summarize_issue_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    issue_title = payload["issue"]["title"]
    issue_url = payload["issue"]["html_url"]
    issue_author = payload["issue"]["user"]["full_name"]
    issue_labels = ", ".join([label["name"] for label in payload["issue"]["labels"]])
    status = payload["action"]

    return (
        f"Event: Issue\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Title: {issue_title}\n"
        f"URL: {issue_url}\n"
        f"Author: {issue_author}\n"
        f"Status: {status}\n"
        f"Labels: {issue_labels}"
    )

def _summarize_issue_comment_event(payload):
    repository = payload["repository"]["name"]
    repository_url = payload["repository"]["html_url"]
    issue_title = payload["issue"]["title"]
    issue_url = payload["issue"]["html_url"]
    comment_author = payload["comment"]["body"]
    comment_body = payload["comment"]["body"]
    comment_url = payload["comment"]["html_url"]

    return (
        f"Event: Issue Comment\n"
        f"Repository: {repository} ({repository_url})\n"
        f"Issue: {issue_title} ({issue_url})\n"
        f"Comment Author: {comment_author}\n"
        f"Comment: {comment_body}\n"
        f"Comment URL: {comment_url}"
    )
