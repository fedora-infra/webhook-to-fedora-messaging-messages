# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "pull_request" event
"""

summary = "testuser-w2fm created pull_request on fedora/w2fm-test"

specification = """Event: Pull Request
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Title: Taking a dump with `json.dumps()` function
URL: https://codeberg.org/fedora/w2fm-test/pulls/7
Author: Akashdeep Dhar
Status: opened
Source Branch: pull
Destination Branch: main
Requested Reviewers: fedoraproject"""

hashes = {
    "sha160": "sha1=153ffb3c2836947af9e4e098b226a91e92fb3d56",
    "sha256": "sha256=62bda34321653279dea75ba57e25063c36672cb7128feb2aa8462f80da4b5e42",
}
