# OpenClaw Integration Plan

Overview: Chimera will publish a minimal presence object to OpenClaw for discovery by other agents.

Presence schema:
- id: string (agent id)
- services: ["trend_fetch","content_creation","media_hosting"]
- status: {"uptime":float, "confidence_score":0.0}

Interaction patterns:
- Announce: POST presence to OpenClaw registry on startup and every 5 minutes.
- Offer/Request: Use standardized JSON-RPC over MCP for direct agent-to-agent exchanges.

Security:
- Use signed metadata and rotating keys; validate signatures before trusting external agents.
