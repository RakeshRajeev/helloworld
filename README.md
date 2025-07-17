## CI/CD Governance Pipeline – Overview

This repository demonstrates a secure and governed CI/CD setup for a containerized application (`helloworld`) using GitHub Actions, Docker, and Helm. It integrates image scanning, promotion workflows, and policy-driven deployment decisions across different branches.

---

## Branching Strategy

| Branch         | Purpose                                  |
|----------------|-------------------------------------------|
| `release/dev`  | Dev build, image scan, and result storage |
| `release/uat`  | UAT deployment and scan result validation |
| `main`         | Production-ready deployment               |
| `ci-config`    | Centralized governance & reusable workflows/scripts |

# Helloworld App - UAT Environment

This `release/uat` branch handles Continuous Deployment (CD) for the UAT environment.

## Features

- Fetches and validates scan reports from `release/dev`
- Uses `validate-scan.py` for security gating
- Pulls approved Docker images
- Simulates deployment using Docker Desktop

## Folder Structure

- `.github/workflows/cd.yaml`: CD pipeline logic
- `charts/`: Helm chart for deployment
- `scripts/validate-scan.py`: Scan validation script
- `scan-results/`: Approved image scan results copied from dev
