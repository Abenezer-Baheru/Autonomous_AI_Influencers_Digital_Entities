# AI Review Policy — Project Chimera

Overview
--------

This project enforces an AI Review Policy that ensures automated reviewers (e.g., CodeRabbit) and human reviewers validate changes for spec alignment, security, and test coverage.

Policy highlights
-----------------

- Spec-Driven Development: Any functional implementation must reference a ratified spec file under `specs/` before merge.
- Mandatory Tests: New features require tests that fail initially (TDD) or appropriate unit/integration tests.
- Security Scans: Dependency changes and code diffs are scanned for vulnerabilities and secrets.
- Human Oversight: For medium/low confidence AI suggestions, a human must approve before merging.

How the policy is enforced
--------------------------

- `.github/workflows/main.yml` runs `make test` on every push/PR.
- `.coderabbit.yaml` contains AI-reviewer rules for spec alignment and security checks (simulated configuration).
- Release workflows sign images with `cosign` and create GitHub Releases containing image digests.

Maintainers should configure repository secrets and organization policies to enable OIDC and cosign signing where required.
