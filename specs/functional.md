# Functional Specification

User stories (agent-centric):

- As an Agent, I need to fetch trending topics from multiple sources so I can propose content ideas.
- As an Agent, I need to generate a content plan (script, assets, publish schedule) from a brief.
- As an Agent, I need to transcode and tag produced videos with metadata for search and analytics.
- As an Agent, I need to surface high-confidence items for auto-publish and medium-confidence items for human review.

Acceptance criteria:
- Trend fetcher returns structured list: [{"topic","score","source","timestamp"}].
- Content plan includes: title, hooks[], segments[], required_assets[], publish_window.
