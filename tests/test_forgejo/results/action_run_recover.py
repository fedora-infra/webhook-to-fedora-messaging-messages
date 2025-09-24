# SPDX-FileCopyrightText: 2024-2025 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""
Result specification for Forgejo "action run recover" event
"""

summary = "testuser-w2fm created action_run_recover on fedora/w2fm-test"

specification = """Event: Action Run Recover
Repository: fedora/w2fm-test (https://codeberg.org/fedora/w2fm-test)
Workflow: deploy.yml
Run: Deploy to Staging (https://codeberg.org/fedora/w2fm-test/actions/runs/12347)
Status: failure → success (recovered)
Commit: c3d4e5f
Branch: main
Previous Run: 12344 (failed)"""

hashes = {
    "sha160": "sha1=6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d",
    "sha256": "sha256=7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c",
}
