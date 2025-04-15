# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for GitHub "fork" event
"""

summary = "testuser-w2fm created fork on gridhead/test-repo"

specification = """Event: Fork
Repository: gridhead/test-repo (https://github.com/gridhead/test-repo)
Forkee: sumantro93/test-repo (https://github.com/sumantro93/test-repo)
Owner: sumantro93 (https://github.com/sumantro93)"""
