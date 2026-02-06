# Project Chimera Roadmap

0–1 month (stabilize)
- Finalize specs and fill any missing acceptance criteria.
- Ensure TDD tests are authoritative; remove demo failing test.
- Harden CI to run unit tests and linting on PRs.

1–3 months (integration)
- Implement frontend minimal dashboard (specs/frontend.md) and backend API endpoints.
- Add monitoring and observability (MCP Sense metrics → Prometheus/Grafana or equivalent).
- Integrate secrets manager for connectors.

3–6 months (scale)
- Add orchestration for scheduling and retry logic for skills.
- Build infra-as-code for production deployment (Terraform / GitHub Actions deploy).
- Implement signed image promotion flow (cosign + attestation).

6–12 months (production readiness)
- Run Canary deployments and automated rollback.
- SLA targets: < 1% publish failure rate; 99.9% uptime for control-plane services.
- Add automated content safety checks and compliance logging.

Long horizon
- Multi-tenant orchestration, role-based access, and economics (cost dashboards).
- Full audit trail with verifiable signatures for operator approvals.
