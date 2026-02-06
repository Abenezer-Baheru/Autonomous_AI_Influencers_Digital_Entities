# Tooling & MCP Strategy

Purpose
- Document the MCP servers and developer tools used to author, test, and run Project Chimera.

Recommended MCP servers (developer-facing)
- `git-mcp` — version-control bridge exposing commits, branches, diffs, and PR drafts. Use for programmatic patching and commit automation.
- `filesystem-mcp` — read/write access to the repository files; used for editing specs, tests, and implementations.
- `run-mcp` / `shell-mcp` — executes build/test commands in a sandboxed environment (e.g., `make test`, `pytest`).
- `container-mcp` / `docker-mcp` — builds and runs Docker images for integration testing and CI parity.
- `mcp-sense` (Tenx MCP Sense) — telemetry and health checks for MCP servers; connect early to log events and validate connections.

Configuration notes
- Principle: give each MCP the minimum privileges needed. For example, `git-mcp` may only need push rights on feature branches, not on `main`.
- Credentials / tokens: prefer short-lived tokens or OIDC where supported. Store any long-lived tokens in your secrets manager — never in repo files.

How to use (developer workflow)
1. Connect `mcp-sense` first to validate other MCP services (it will record discovery and connection logs).
2. Use `filesystem-mcp` for drafting specs and tests, then `git-mcp` to commit and push changes.
3. Run unit tests via `run-mcp` (e.g., `python -m pytest`) before building containers with `container-mcp`.

Example: quick connect checklist
- Start `mcp-sense` and confirm discovery of `git-mcp` and `filesystem-mcp`.
- Author or update `specs/` via `filesystem-mcp` and commit via `git-mcp`.
- Execute `make test` in `run-mcp` to validate tests pass in the configured environment.

Notes & guidance
- Map real-world tools to MCP implementations available in your environment (the names above are conceptual; your environment may provide specific plugin names).
- For CI, mirror MCP usage in GitHub Actions: use container build steps and a small test matrix that mimics developer `run-mcp` behavior.
