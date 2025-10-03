# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "action run success" event
"""

summary = "testuser-w2fm created action_run_success on fedora/w2fm-test"

specification = """Event: Action Run Success
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Workflow: ci.yml
Run: CI Pipeline (https://codeberg.org/fedora/w2fm-test/actions/runs/12345)
Status: running → success
Commit: a1b2c3d
Branch: main"""

hashes = {
    "sha160": "sha1=8a7b6c5d4e3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b",
    "sha256": "sha256=9f8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e",
}
