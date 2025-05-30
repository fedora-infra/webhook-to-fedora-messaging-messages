# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitLab "issue" event
"""

summary = "testuser-w2fm created issue on w2fm-test"

specification = """Event: Issue
Repository: w2fm-test (https://gitlab.com/sdglitched/w2fm-test)
Title: [TITLE] Test Issue 1
URL: https://gitlab.com/sdglitched/w2fm-test/-/issues/1
Author: sdglitched
Status: opened
Labels: bug, critical, confirmed, documentation, support, discussion, suggestion, enhancement"""
