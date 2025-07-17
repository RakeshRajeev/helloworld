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

---

### CI Pipeline

**Trigger:** Push to `release/dev`  
## Features

- Builds Docker images from `app/`
- Performs vulnerability scanning using Trivy
- Stores scan results under `scan-results/` folder
- Pushes validated images to Docker Hub

## Folder Structure

- `.github/workflows/ci.yaml`: CI pipeline logic
- `app/`: Source code and Dockerfile
- `scan-results/`: JSON reports of image scans
- `scripts/validate-scan.py`: Used later in CD pipeline
---
### Scan Results

All scan result files follow the naming pattern:  
`scan-results/helloworld-<git-sha>.json`

This allows traceability and consistent validation during promotions.


