# Programmatic API Onboarding — Cloudflare

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for Cloudflare: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`cloudflare-api-auth.mjs`](cloudflare-api-auth.mjs)
- Run `node cloudflare-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/09/cloudflare-token-but-click-dashboard-first/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
