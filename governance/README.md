Deployment Policy & Dispensation Guide (Simplified)
1. Purpose
This guide explains the rules we follow to deploy container images safely and what to do if we need to bypass those rules with proper approval.

2. Deployment Policy (Simple Rules)
We follow these basic rules during deployment:

a.Only allow images that were scanned in CI and saved with a unique image SHA.

b.Block any image that has critical or high vulnerabilities.

c.The scan must be recent — within 7 days.

d.The image used in Helm must exactly match what was scanned (based on SHA).

e.Even during rollbacks, only pre-scanned and compliant images can be deployed.

3. Dispensation Process (What to Do if You Need an Exception)
Sometimes, we may need to deploy even if the image has issues. In that case:

The developer creates a file (YAML) with the image SHA and justification.

This file is saved in a special GitHub folder: governance/.

Someone from the Security team must review and approve it (via Pull Request).

The CD pipeline checks this approval file and only allows deployment if it's valid.

4. Audit and Access Control
All exceptions (dispensations) are tracked in GitHub.

a.Only the Security team can approve or modify files in governance/.

b. This keeps everything transparent and auditable.

5. Optional Future Additions
We might later add:

a.Approvals through a form or ServiceNow

b. Alerts in Slack when a rule is bypassed

c. Auto-expiry for old approvals