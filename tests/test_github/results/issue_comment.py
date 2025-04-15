# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitHub "issue_comment" event
"""

summary = "testuser-w2fm created issue_comment on gridhead/test-repo"

specification = """Event: Issue Comment
Repository: gridhead/test-repo (https://github.com/gridhead/test-repo)
Issue: This is a sample issue ticket (https://github.com/gridhead/test-repo/issues/2)
Comment Author: gridhead
Comment: Issue comment here
Comment URL: https://github.com/gridhead/test-repo/issues/2#issuecomment-2791741060"""
