# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitHub "push" event
"""

summary = "testuser-w2fm created push on gridhead/test-repo"

specification = """Event: Push
Repository: gridhead/test-repo (https://github.com/gridhead/test-repo)
Pusher: gridhead (https://github.com/gridhead)
Branch: flsk
Commits:
- bb79386: Add simple webhook receiver service - https://w2fm.gridhead.net by Akashdeep Dhar (https://github.com/gridhead/test-repo/commit/bb793868750af565b35f79e756dc4fac1b444672)"""
