# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitHub "pull_request" event
"""

summary = "testuser-w2fm created pull_request on gridhead/test-repo"

specification = """Event: Pull Request
Repository: gridhead/test-repo (https://github.com/gridhead/test-repo)
Title: Add simple webhook receiver service - https://w2fm.gridhead.net
URL: https://github.com/gridhead/test-repo/pull/1
Author: gridhead
Status: opened
Source Branch: flsk
Destination Branch: main
Requested Reviewers: """
