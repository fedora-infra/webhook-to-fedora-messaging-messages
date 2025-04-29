# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later


def summarize_repository_event(event_type: str, data: dict) -> str:
    """
    Obtain text specification based on event type
    """
    if event_type == "push":
        return _summarize_push_event(data)
    elif event_type == "fork":
        return _summarize_fork_event(data)
    elif event_type == "pull_request":
        return _summarize_pull_request_event(data)
    elif event_type == "issues":
        return _summarize_issues_event(data)
    elif event_type == "issue_comment":
        return _summarize_issue_comment_event(data)
    else:
        return "Event type not supported"


def _summarize_push_event(data: dict) -> str:
    """
    Obtain text specification for push event
    """
    repository_name = data["repository"]["full_name"]
    repository_url = data["repository"]["html_url"]
    pusher = data["pusher"]["full_name"] or data["pusher"]["login"]
    pusher_url = data["pusher"]["html_url"]
    branch = data["ref"].split("/")[-1]
    commits = "\n".join(
        [
            f"- {commit['id'][0:7]}: {commit['message'].splitlines()[0]} by {commit['author']['name']} ({commit['url']})"  # noqa: E501
            for commit in data["commits"]
        ]
    )
    return (
        f"Event: Push\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Pusher: {pusher} ({pusher_url})\n"
        f"Branch: {branch}\n"
        f"Commits:\n{commits}"
    )


def _summarize_fork_event(data: dict) -> str:
    """
    Obtain text specification for fork event
    """
    repository_name = data["repository"]["full_name"]
    repository_url = data["repository"]["html_url"]
    forkee = data["forkee"]["full_name"]
    forkee_url = data["forkee"]["html_url"]
    owner = data["forkee"]["owner"]["full_name"] or data["forkee"]["owner"]["login"]
    owner_url = data["forkee"]["owner"]["html_url"]
    return (
        f"Event: Fork\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Forkee: {forkee} ({forkee_url})\n"
        f"Owner: {owner} ({owner_url})"
    )


def _summarize_pull_request_event(data: dict) -> str:
    """
    Obtain text specification for pull request event
    """
    repository_name = data["repository"]["full_name"]
    repository_url = data["repository"]["html_url"]
    pr_title = data["pull_request"]["title"]
    pr_url = data["pull_request"]["html_url"]
    pr_author = data["pull_request"]["user"]["full_name"] or data["pull_request"]["user"]["login"]
    pr_source_branch = data["pull_request"]["head"]["ref"]
    pr_dest_branch = data["pull_request"]["base"]["ref"]
    pr_reviewers = ", ".join(
        [
            (reviewer["full_name"] or reviewer["login"])
            for reviewer in data["pull_request"]["requested_reviewers"]
        ]
    )
    status = data["action"]
    return (
        f"Event: Pull Request\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Title: {pr_title}\n"
        f"URL: {pr_url}\n"
        f"Author: {pr_author}\n"
        f"Status: {status}\n"
        f"Source Branch: {pr_source_branch}\n"
        f"Destination Branch: {pr_dest_branch}\n"
        f"Requested Reviewers: {pr_reviewers}"
    )


def _summarize_issues_event(data: dict) -> str:
    """
    Obtain text specification for issues event
    """
    repository_name = data["repository"]["full_name"]
    repository_url = data["repository"]["html_url"]
    issue_title = data["issue"]["title"]
    issue_url = data["issue"]["html_url"]
    issue_author = data["issue"]["user"]["full_name"] or data["issue"]["user"]["login"]
    issue_labels = ", ".join([label["name"] for label in data["issue"]["labels"]])
    status = data["action"]
    return (
        f"Event: Issue\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Title: {issue_title}\n"
        f"URL: {issue_url}\n"
        f"Author: {issue_author}\n"
        f"Status: {status}\n"
        f"Labels: {issue_labels}"
    )


def _summarize_issue_comment_event(data: dict) -> str:
    """
    Obtain text specification for issue comment event
    """
    repository_name = data["repository"]["full_name"]
    repository_url = data["repository"]["html_url"]
    issue_title = data["issue"]["title"]
    issue_url = data["issue"]["html_url"]
    comment_author = data["comment"]["user"]["full_name"] or data["comment"]["user"]["login"]
    comment_body = data["comment"]["body"]
    comment_url = data["comment"]["html_url"]
    return (
        f"Event: Issue Comment\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Issue: {issue_title} ({issue_url})\n"
        f"Comment Author: {comment_author}\n"
        f"Comment: {comment_body}\n"
        f"Comment URL: {comment_url}"
    )
