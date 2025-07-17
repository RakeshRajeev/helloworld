# CI Configuration & Governance Branch

This `ci-config` branch manages pipeline templates and security governance rules.This approach ensures consistent enforcement across environments. The reuse of scan validation logic in CI and CD simulates a shared-library pattern—helping teams avoid duplicating logic across branches.


## Features

- Contains reusable CI/CD workflows
- Maintains governance exceptions under `governance/dispensations/`
- Hosts shared logic and helper scripts

## Folder Structure

- `.github/workflows/`: Centralized CI/CD YAMLs
- `governance/dispensations/`: Image-specific exceptions
- `scripts/`: Includes `validate-scan.py` for enforcement

## Note

This branch supports centralized policies and logic, reducing duplication across environments.
