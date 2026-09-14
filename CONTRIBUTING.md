# Contributing to ThoughtKhoral

Thank you for helping improve ThoughtKhoral. The project uses specifications as
durable memory and as the source of truth for implementation and generated
documentation.

## Start with an issue

Open an issue in the repository that owns the affected behavior. Use the issue
form that best matches the request:

- feature or capability request;
- defect or test failure;
- documentation correction;
- protocol or compatibility change;
- architecture or governance proposal; or
- deployment and operational problem.

Include the user outcome, affected repository, relevant version or contract,
reproduction details, and acceptance evidence where applicable. Maintainers may
move an issue to the repository with the correct ownership.

## Specification-first flow

1. Maintainers triage the issue and decide whether it is accepted, needs more
   evidence, deferred, or closed.
2. An accepted issue is converted into a maintainer-authored What, How, or
   Decision update.
3. The specification is reviewed and approved before implementation begins.
4. Implementation, tests, and generated documentation reference the issue and
   governing specification.
5. The change is released by the repository that owns the artifact.

Contributors do not need to edit `.ai/specs` directly. Maintainers may invite a
contributor to submit an implementation pull request after the issue and
specification are ready. Pull requests must reference the accepted issue and
governing specification.

## Pull requests

Use a focused branch and include tests or verification commands. Explain any
compatibility, security, operational, or documentation impact. Do not include
credentials, private data, generated artifacts that should be produced by CI,
or unrelated formatting changes.

## Security

Do not report vulnerabilities in a public issue. Follow [SECURITY.md](SECURITY.md)
for private reporting guidance.
