Contributing to Project Chimera
===============================

Thanks for contributing. This project follows a Spec-Driven Development (SDD) workflow.

Quickstart
- Create a feature branch: `git checkout -b feat/your-feature`
- Run setup: `make setup`
- Run tests locally: `make test`

Spec-Driven Workflow
- Always consult and reference the relevant spec under `specs/` before implementing.
- Write a failing test that represents the "empty slot" in the spec.
- Implement the minimal code to make the test pass, and include the spec path in your commit message:

  feat: implement X — refs specs/functional.md#story-3

Testing
- Unit tests: `pytest` (run via `make test`).
- Integration tests that perform network calls are skipped by default. To run them, set `RUN_REAL_SKILLS_TESTS=1`.

Commit & PR
- Keep commits small and focused; include the spec reference in commits and PR descriptions.
- In the PR description list which spec sections are addressed and the failing test names that were satisfied.

Security & Secrets
- Never commit secrets or credentials. If you find secrets, stop and notify the maintainers immediately.

AI / Code Review
- This repository includes `.coderabbit.yaml` and `.cursor/rules` to guide AI-assisted contributions. Please follow those rules when using AI tools to author changes.

Maintainers
- Add contact instructions or a team alias here as needed.
