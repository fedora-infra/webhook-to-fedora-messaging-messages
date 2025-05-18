# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitLab "issue" event
"""

summary = "testuser-w2fm created Merge Request Hook on w2fm-test"

specification = """Event: Pull Request
Repository: w2fm-test (https://gitlab.com/sdglitched/w2fm-test)
Title: Test merge request
URL: https://gitlab.com/sdglitched/w2fm-test/-/merge_requests/1
Author: sdglitched
Status: opened
Source Branch: test-branch
Destination Branch: main
Requested Reviewers: sdglitched"""
