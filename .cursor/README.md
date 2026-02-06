Cursor Rules — How to use `.cursor/rules`
======================================

Purpose
- Explain where `.cursor/rules` lives and how IDE agents should follow it.

Overview
- The file `.cursor/rules` contains the agent's Prime Directive, Traceability rules, and behavioral constraints.
- Agents must reference `specs/` files before authoring code and must include spec references in commit messages.

Demo guidance
- For demos, open `.cursor/rules` and read the Prime Directive and Traceability sections aloud to prove the agent will check specs first.

Location
- The primary rules file is at the repo root: `.cursor/rules`.
