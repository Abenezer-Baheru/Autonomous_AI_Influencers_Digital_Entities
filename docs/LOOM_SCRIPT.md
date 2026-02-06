# Loom Recording Script — Project Chimera (max 5 minutes)

Purpose: Short guided script to follow during a 5-minute Loom walkthrough.

0:00–0:20 — Intro
- State your name and role.
- Show the repo URL: https://github.com/Abenezer-Baheru/Autonomous_AI_Influencers_Digital_Entities
- One-line purpose: "Project Chimera: a spec-driven autonomous influencer agent platform."

0:20–1:20 — Specs walkthrough
- Open `specs/_meta.md` and summarize vision & constraints (10s).
- Open `specs/functional.md` and read two user stories aloud (20s).
- Open `specs/technical.md` and point to the API contract section for agents (10s).
- (Optional) Open `specs/openclaw_integration.md` and mention how status will be published to OpenClaw (10s).

1:20–2:20 — TDD demo (show failing test)
- Open `tests/` and highlight `test_skills_interface.py` and `tests/test_demo_failing.py`.
- Run the intentional failing test only (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
python -m pytest tests/test_demo_failing.py -q
```

- Let the failing assertion be visible on-screen and explain: "This is the 'empty slot' the agent will fill using SDD."

2:20–3:20 — IDE Agent context demo
- Open `.cursor/rules` and read the Prime Directive line: "NEVER generate or commit production code without first locating and checking the relevant specification in the `specs/` directory."
- Ask your IDE/Co-pilot a short question aloud (example): "How should I implement `skill_download_youtube` to match the spec?"
- Show the agent responding and highlight where it cites `specs/` or follows the traceability rules.

3:20–4:30 — Connect specs → tests → impl
- Open `skills/impl/skill_download_youtube.py` (or one skill) and show how the `run(params)` contract aligns with `specs/technical.md`.
- Mention CI and governance briefly: `.github/workflows/`, `.coderabbit.yaml`, `.cursor/rules`.

4:30–5:00 — Wrap-up
- Re-state repo URL and where to find the specs and tests.
- Note: After recording, remove `tests/test_demo_failing.py` or we can revert the temporary commit.

Recording tips
- Keep code/editor zoomed so text is legible.
- Speak commands before running them and pause briefly after test output to let viewers read failure text.
