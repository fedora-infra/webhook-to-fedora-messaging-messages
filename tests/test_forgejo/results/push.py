# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "push" event
"""

summary = "testuser-w2fm created push on fedora/w2fm-test"

specification = """Event: Push
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Pusher: Akashdeep Dhar (https://codeberg.org/gridhead)
Branch: pull
Commits:
- 1c5ccba: Taking a dump with `json.dumps()` function by Akashdeep Dhar (https://codeberg.org/fedora/w2fm-test/commit/1c5ccba31592d36a7b999434768c7498edfec822)"""

hashes = {
    "sha160": "sha1=6e56d9e95c45eb93164c56b393bc3236cfd87f2d",
    "sha256": "sha256=014b6489921826f35b0bb367ea674822ac418e97d6b07ef2d11295e2199794af",
}
