# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitLab "issue_comment" event
"""

summary = "testuser-w2fm created Note Hook on w2fm-test"

specification = """Event: Issue Comment
Repository: w2fm-test (https://gitlab.com/sdglitched/w2fm-test)
Issue: [TITLE] Test Issue 1 (https://gitlab.com/sdglitched/w2fm-test/-/issues/1)
Comment Author: sdglitched
Comment: This is issue comment.
Comment URL: https://gitlab.com/sdglitched/w2fm-test/-/issues/1#note_2509662111"""
