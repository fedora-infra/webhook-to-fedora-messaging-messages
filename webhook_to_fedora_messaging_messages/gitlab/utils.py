# SPDX-FileCopyrightText: 2024 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later


def summarize_repository_event(event_type: str, data: dict) -> str:
    """
    Obtain text specification based on event type
    """
    if event_type == "push":
        return _summarize_push_event(data)
    elif event_type == "merge_request":
        return _summarize_merge_request_event(data)
    elif event_type == "issue":
        return _summarize_issue_event(data)
    elif event_type == "note":
        return _summarize_note_event(data)
    else:
        return "Event type not supported"


def _summarize_push_event(data: dict) -> str:
    """
    Obtain text specification for push event
    """
    repository_name = data["repository"]["name"]
    repository_url = data["repository"]["homepage"]
    pusher = data["user_username"]
    pusher_url = f"https://gitlab.com/{pusher}"
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


def _summarize_merge_request_event(data: dict) -> str:
    """
    Obtain text specification for merge request event
    """
    repository_name = data["repository"]["name"]
    repository_url = data["repository"]["homepage"]
    pr_title = data["object_attributes"]["title"]
    pr_url = data["object_attributes"]["url"]
    pr_author = data["user"]["username"]
    pr_source_branch = data["object_attributes"]["source_branch"]
    pr_dest_branch = data["object_attributes"]["target_branch"]
    pr_reviewers = ", ".join([reviewer["username"] for reviewer in data["reviewers"]])
    status = data["object_attributes"]["state"]
    return (
        f"Event: Merge Request\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Title: {pr_title}\n"
        f"URL: {pr_url}\n"
        f"Author: {pr_author}\n"
        f"Status: {status}\n"
        f"Source Branch: {pr_source_branch}\n"
        f"Destination Branch: {pr_dest_branch}\n"
        f"Requested Reviewers: {pr_reviewers}"
    )


def _summarize_issue_event(data: dict) -> str:
    """
    Obtain text specification for issue event
    """
    repository_name = data["repository"]["name"]
    repository_url = data["repository"]["homepage"]
    issue_title = data["object_attributes"]["title"]
    issue_url = data["object_attributes"]["url"]
    issue_author = data["user"]["username"]
    issue_labels = ", ".join([label["title"] for label in data["object_attributes"]["labels"]])
    status = data["object_attributes"]["state"]
    return (
        f"Event: Issue\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Title: {issue_title}\n"
        f"URL: {issue_url}\n"
        f"Author: {issue_author}\n"
        f"Status: {status}\n"
        f"Labels: {issue_labels}"
    )


def _summarize_note_event(data: dict) -> str:
    """
    Obtain text specification for note event
    """
    repository_name = data["repository"]["name"]
    repository_url = data["repository"]["homepage"]
    issue_title = data["issue"]["title"]
    issue_url = data["issue"]["url"]
    comment_author = data["user"]["username"]
    comment_body = data["object_attributes"]["description"]
    comment_url = data["object_attributes"]["url"]
    return (
        f"Event: Note\n"
        f"Repository: {repository_name} ({repository_url})\n"
        f"Issue: {issue_title} ({issue_url})\n"
        f"Comment Author: {comment_author}\n"
        f"Comment: {comment_body}\n"
        f"Comment URL: {comment_url}"
    )
