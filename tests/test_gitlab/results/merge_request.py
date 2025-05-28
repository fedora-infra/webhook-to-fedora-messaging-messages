# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitLab "merge_request" event
"""

summary = "testuser-w2fm created merge_request on w2fm-test"

specification = """Event: Merge Request
Repository: w2fm-test (https://gitlab.com/sdglitched/w2fm-test)
Title: Test merge request
URL: https://gitlab.com/sdglitched/w2fm-test/-/merge_requests/1
Author: sdglitched
Status: opened
Source Branch: test-branch
Destination Branch: main
Requested Reviewers: sdglitched"""
