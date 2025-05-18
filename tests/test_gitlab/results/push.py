# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitLab "issue" event
"""

summary = "testuser-w2fm created Push Hook on w2fm-test"

specification = """Event: Push
Repository: w2fm-test (https://gitlab.com/sdglitched/w2fm-test)
Pusher: sdglitched (https://gitlab.com/sdglitched)
Branch: test-branch
Commits:
- 7aa00b2: Test commit by Shounak Dey (https://gitlab.com/sdglitched/w2fm-test/-/commit/7aa00b22e26de3efc8270aebc9ee51c40107d4ff)"""
