# Security and Acceptance Criteria

Threat Model (brief)
- Adversaries: Malicious content providers, compromised connectors, leaked credentials, or compromised CI runners.
- Assets: downloaded media, transcripts, publish connectors, and operator approvals.

Secrets & Credentials
- Never check secrets into the repo. Use an external secrets manager (Vault, GitHub Secrets) and reference keys in runtime config.
- CI runners must fetch secrets at runtime using short-lived credentials or OIDC.

CI Gating
- Pull requests must run `make test` and pass unit tests. Integration tests (network) are optional and must be gated behind `RUN_REAL_SKILLS_TESTS=1`.
- Merge to `main` requires review and a passing CI run.

Skill-specific Acceptance Criteria
- `skill_download_youtube`:
  - Input validation: rejects missing or non-HTTP(S) `url` with status `error`.
  - Dry-run: when `dry_run=true`, returns `status: skipped` and `expected_path`.
  - Real-run: when enabled, downloads a file to configured dir and returns `filepath` and `filesize`.
- `skill_transcribe_audio`:
  - Returns `transcript` (string) and `segments` (list of {start,end,text}).
  - Must respect `language` param when provided.
- `skill_publish_social`:
  - On success returns `post_id` and `url`.
  - On failure returns `status: error` and non-sensitive `error_code`.

Operational Requirements
- Logging: all skill runs must emit structured logs including `spec_ref` and `test_refs` when available.
- Monitoring: agent health metrics emitted to MCP Sense; alert if error rate > 5% over 1 hour.
- Storage: media files stored in a dedicated bucket with lifecycle policy (e.g., 30-day retention by default).

Acceptance checklist for release
- All unit tests pass.
- Security scan (dependabot or Snyk) shows no critical vulnerabilities.
- No secrets committed.
- Cosmosign or signing policy for images documented in `ROADMAP.md` and enabled in CI when org OIDC is configured.
