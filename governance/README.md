
#  Governance-Enforced CI/CD Deployment Pipeline

This project implements a secure CI/CD architecture with strict separation of concerns, governance enforcement, and policy-based deployment gating.

---

##  Branch Strategy

| Branch         | Purpose                                | Who Manages It       |
|----------------|----------------------------------------|-----------------------|
| `release/dev`  | Builds, scans, pushes images and scan results | Developers + CI      |
| `release/uat`  | Staging deployment only (no builds)     | DevOps                |
| `main`         | Production deployment only              | DevOps                |
| `ci-config`    | Source of truth for workflows, governance, and scripts | SecOps / Platform team |

---

##  Governance Sync PR Flow

When changes are made to:
- `governance/dispensations/*.yaml`
- `scripts/validate-scan.py`

A GitHub Actions workflow in `ci-config` will:
- Automatically create PRs to `release/uat` and `main`
- These PRs must be reviewed and approved
- Once merged, the governance rules are enforced during CD

---

##  Governance Enforcement

CD pipeline (in `cd.yaml`) will:
- Pull the image scan result from `release/dev/scan-results/`
- Run `scripts/validate-scan.py` before deployment
- If high/critical CVEs are found:
  -  Deployment is allowed only if a matching dispensation file exists
  -  Otherwise, deployment is blocked

---

##  Required Files Per Branch

###  `release/dev`
- `.github/workflows/ci.yaml`
- `app/`, `Dockerfile`
- `scan-results/`

### `release/uat` & `main`
- `.github/workflows/cd.yaml`
- `charts/helloworld/`
- `scripts/validate-scan.py`
- `governance/dispensations/`
-  NO build, app, or scan logic

### `ci-config`
- `.github/workflows/ci.yaml` (source)
- `.github/workflows/sync-governance.yml`
- `scripts/validate-scan.py`
- `governance/dispensations/`

---

## Sample Dispensation File Format

```yaml
approved_vulnerabilities:
  - CVE-2024-12345
  - CVE-2023-99999
reason: "Temporary approval for hotfix"
approved_by: "security-team"
expires: "2024-12-31"
```

---

## 👥 Access and Responsibility Separation

| Role       | Permissions                          |
|------------|--------------------------------------|
| Developer  | Works in `release/dev`, can't deploy |
| DevOps     | Monitors CD, deploys to UAT & main   |
| Security   | Owns `ci-config`, dispensation files |

---

## Test Deployment Flow

1. Build and scan in `release/dev`
2. Merge to `release/uat` → triggers CD
3. CD checks scan + governance and deploys
4. Promote to `main` via approved PR

---

## Secure by Default

- No CD without valid scan
- No production deployment without review
- No bypass of CVE check without documented approval

---


