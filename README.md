# Project Chimera

Project Chimera — Autonomous AI Influencer platform (spec-driven, agentic factory).

## Quick start

1. Create and activate a Python virtualenv:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Unix / Git Bash
source .venv/bin/activate
```

2. Install package and test deps:

```bash
pip install -e . pytest
```

3. Run tests:

```bash
pytest -q
```

## Tests

- `tests/test_skills_interface.py` defines interface tests (TDD).
- `tests/test_skills_realistic.py` contains realistic tests verifying `dry_run` behavior.
- Integration (real) tests are skipped by default. To enable them set the env var:

```bash
export RUN_REAL_SKILLS_TESTS=1
pytest -q
```

## Makefile

Use the provided `Makefile` to standardize local dev commands:

- `make setup` – create venv and install deps
- `make test` – run tests
- `make lint` – simple JSON lint check
- `make docker-build` / `make docker-run`

## CI & Release

We provide two GitHub Actions workflows:

- `.github/workflows/main.yml` — Runs `make setup` and `make test` on pushes and PRs to `main`. It caches `pip` to speed up dependency installs.
- `.github/workflows/release.yml` — Triggered on tag pushes (tags `v*`). It:
	- builds a multi-arch Docker image (`linux/amd64`, `linux/arm64`) using Buildx
	- uses GitHub Actions cache for Docker layers to speed repeated builds
	- pushes images to GitHub Container Registry (`ghcr.io/<owner>/project-chimera:<tag>` and `:latest`)
	- attempts keyless image signing with `cosign` (sigstore) and creates a GitHub Release containing the image digest

To create a release and publish images, tag a commit and push the tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Note: The release workflow signs images keylessly using OIDC; ensure repository settings and GHCR permissions permit this. The signing step is best-effort and will not fail the workflow if cosign/keyless signing isn't available.

## Security & Governance

- All runtime agents must read specs in `specs/` before implementing code.
- Tenx MCP Sense telemetry should remain connected to the IDE during development for traceability.

## Optional runtime dependencies

- For real downloads and transcription, optionally install extras:

```bash
pip install -e .[yt,transcribe]
```

This installs `yt-dlp` and `openai-whisper` (or similar) to enable real skill execution. CI disables network-heavy tests by default.

## Repository structure

Top-level layout (important files/folders):

- `pyproject.toml` — project metadata and optional extras
- `specs/` — spec-driven files: `_meta.md`, `functional.md`, `technical.md`, `openclaw_integration.md`
- `skills/` — skill contracts and implementations
	- `skills/impl/` — Python skill implementations (e.g., `skill_download_youtube.py`)
- `tests/` — pytest tests (interface + realistic dry_run tests)
- `Makefile` — `make setup`, `make test`, `make docker-build` targets
- `Dockerfile` — image build for runtime and CI
- `.github/workflows/` — CI and release workflows (`main.yml`, `release.yml`)
- `.coderabbit.yaml` — AI reviewer / policy simulation config
- `docs/AI_REVIEW_POLICY.md` — human-readable review policy
- `.gitignore` — excludes venvs, artifacts, and secrets
- `.vscode/mcp.json` — MCP Sense connection config

If you want a printable tree of the repo, run:

```bash
find . -maxdepth 2 -type d -or -type f | sed 's|^./||' | sort
```

