import json
import os
import sys

SCAN_RESULTS_DIR = "scan-results"
DISPENSATION_DIR = "governance/dispensations"
IMAGE_NAME = os.environ.get("IMAGE_NAME")
IMAGE_TAG = os.environ.get("IMAGE_TAG")

if not IMAGE_NAME or not IMAGE_TAG:
    print("ERROR: IMAGE_NAME and IMAGE_TAG environment variables are required.")
    sys.exit(1)

scan_file = f"{SCAN_RESULTS_DIR}/{IMAGE_NAME}-{IMAGE_TAG}.json"
dispensation_file = f"{DISPENSATION_DIR}/{IMAGE_NAME}.yaml"

# Check if scan file exists
if not os.path.isfile(scan_file):
    print(f"ERROR: Scan result not found: {scan_file}")
    sys.exit(1)

# Parse the scan result
with open(scan_file, 'r') as f:
    scan_data = json.load(f)

vulnerabilities = []
for result in scan_data.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):
        if vuln["Severity"] in ("HIGH", "CRITICAL"):
            vulnerabilities.append(vuln)

if not vulnerabilities:
    print("No critical or high vulnerabilities found.")
    sys.exit(0)

# Check for dispensation file
if os.path.isfile(dispensation_file):
    print(f"Critical vulnerabilities found, but dispensation exists: {dispensation_file}")
    sys.exit(0)

print("BLOCKED: Critical/High vulnerabilities found and no dispensation present:")
for v in vulnerabilities:
    print(f"- {v['VulnerabilityID']} ({v['Severity']}): {v['PkgName']}")

sys.exit(1)
