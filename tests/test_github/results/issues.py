# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitHub "issues" event
"""

summary = "testuser-w2fm created issues on gridhead/test-repo"

specification = """Event: Issue
Repository: gridhead/test-repo (https://github.com/gridhead/test-repo)
Title: This is a sample issue ticket
URL: https://github.com/gridhead/test-repo/issues/3
Author: gridhead
Status: opened
Labels: bug, documentation, duplicate, enhancement, help wanted, good first issue, invalid, question, wontfix"""
