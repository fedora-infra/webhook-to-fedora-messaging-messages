# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "issues" event
"""

summary = "testuser-w2fm created issues on fedora/w2fm-test"

specification = """Event: Issue
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Title: Sample issue for webhook trigger checking
URL: https://codeberg.org/fedora/w2fm-test/issues/5
Author: Akashdeep Dhar
Status: opened
Labels: Kind/Bug, Kind/Feature, Kind/Enhancement, Kind/Security, Kind/Testing, Kind/Documentation, Compat/Breaking, Reviewed/Invalid, Status/Need More Info, Priority/Critical"""

hashes = {
    "sha160": "sha1=f9a6aae9f318fffeaab18ecb093fd2a5867839b6",
    "sha256": "sha256=be7518b5453cb3a6626726d301b2c80d53c04246e5d9a8e454b616d15a5e0b66",
}
