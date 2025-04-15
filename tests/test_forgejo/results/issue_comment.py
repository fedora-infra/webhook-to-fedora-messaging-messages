# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "issue_comment" event
"""

summary = "testuser-w2fm created issue_comment on fedora/w2fm-test"

specification = """Event: Issue Comment
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Issue: Sample issue for webhook trigger checking (https://codeberg.org/fedora/w2fm-test/issues/5)
Comment Author: Akashdeep Dhar
Comment: Here comes the issue comment HAHA
Comment URL: https://codeberg.org/fedora/w2fm-test/issues/5#issuecomment-3813260"""

hashes = {
    "sha160": "sha1=a2e4ff3da2627b92d6c6b34b33ca97ff739f080b",
    "sha256": "sha256=2bec855b24895f33f3fb2224adaeaef8d246d8df8f8e1634445c0e1ac293ff28",
}
