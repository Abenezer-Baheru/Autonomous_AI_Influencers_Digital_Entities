# Frontend Specification

Purpose
- Provide a simple operator dashboard for Project Chimera to monitor agents, preview content, and approve or schedule posts.

Primary Users
- Operator: reviews trends, approves posts, monitors agent health.
- Auditor: inspects logs, decisions, and spec traceability.

Screens & Components
- Dashboard (Home)
  - Agent Health panel: live status from MCP Sense (up/down, last heartbeat).
  - Pending Approvals: list of content items requiring operator approval (title, preview, source skill).
  - Recent Activity: timeline of skill runs, downloads, transcriptions, and publish events.
- Content Preview
  - Media player for video/audio preview, transcript panel, metadata (title, duration, source URL).
  - Approve / Reject buttons with reason modal.
- Skill Inspector
  - View skill run details: input params, outputs, logs, referenced spec paths, and test evidence link.
- Settings
  - Connectors: configure social connectors (placeholder values stored in secrets manager).
  - MCP Config: view MCP endpoints and discovery status (read-only in UI).

User Flows
- Review & Approve
  1. Operator opens Dashboard → Pending Approvals shows new item from `skill_publish_social`.
 2. Click Preview → inspect media and transcript → click Approve → schedule time or publish immediately.
- Investigate Failure
  1. Operator opens Recent Activity, filters to failed runs → click run → open logs and spec reference → create an incident ticket.

Acceptance Criteria
- The dashboard shows live agent health within 10s of events emitted by MCP Sense.
- Approve/Reject actions create a signed audit record linking to the spec that permitted the action.
- Preview renders media thumbnails and at least the first 30s of video/audio inline.
- All connectors are configured via secrets (no plaintext keys in repo).

Tech Notes
- Frontend may be a lightweight React app communicating with a backend API defined in `specs/technical.md`.
- Authentication: integrate with org SSO; at minimum require a JWT issued by the backend for operator actions.
