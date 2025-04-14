# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "fork" event
"""

summary = "testuser-w2fm created fork on gridhead/w2fm-test"

specification = """Event: Fork
Repository: gridhead/w2fm-test (https://codeberg.org/gridhead/w2fm-test)
Forkee: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Owner: Fedora Project (https://codeberg.org/fedora)"""

hashes = {
    "sha160": "sha1=16d09a058d3319269d25855dfd69e79fd6afeb31",
    "sha256": "sha256=c207feee33f5a703cebae903e61d9a9d2347afc3c359f8872b612cceca1e1ded",
}
