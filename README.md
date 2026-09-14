# ThoughtKhoral organization defaults

This repository is the GitHub organization control plane for ThoughtKhoral. It
provides the public organization profile and default community-health files for
repositories that do not define a more specific version.

Product architecture, specifications, repository status, and generated
cross-project content belong in the
[ThoughtKhoral project home](https://github.com/thoughtkhoral/thought-khoral),
not here.

## Contents

- `profile/README.md` — organization landing page;
- `CONTRIBUTING.md` — issue-first contribution workflow;
- `SECURITY.md` — private vulnerability reporting guidance;
- `SUPPORT.md` — repository routing for support issues;
- `ISSUE_TEMPLATE/` — structured issue intake;
- `labels.yml` — the versioned organization label catalog;
- `PULL_REQUEST_TEMPLATE.md` — issue and specification traceability checks.

Changes to these defaults should reference an issue in the `thought-khoral`
repository and be reviewed as organization-governance documentation.

GitHub labels are repository-local settings. Apply the names in `labels.yml` to
each public repository when enabling the issue forms; the issue forms reference
these names exactly.
