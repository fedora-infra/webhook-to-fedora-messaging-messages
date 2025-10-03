# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "action run failure" event
"""

summary = "testuser-w2fm created action_run_failure on fedora/w2fm-test"

specification = """Event: Action Run Failure
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Workflow: test.yml
Run: Test Suite (https://codeberg.org/fedora/w2fm-test/actions/runs/12346)
Status: running → failure
Commit: b2c3d4e
Branch: feature/database-refactor"""

hashes = {
    "sha160": "sha1=7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e",
    "sha256": "sha256=8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d",
}
