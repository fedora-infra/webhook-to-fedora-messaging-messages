# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "action run cancelled" event
"""

summary = "testuser-w2fm created action_run_cancelled on fedora/w2fm-test"

specification = """Event: Action Run Cancelled
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Workflow: security.yml
Run: Security Scan (https://codeberg.org/fedora/w2fm-test/actions/runs/12348)
Status: running → cancelled
Commit: d4e5f6a
Branch: feature/security-scan"""

hashes = {
    "sha160": "sha1=5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c",
    "sha256": "sha256=6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c5b",
}
