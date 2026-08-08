---
title: "Workers - AI agents can debug Workers with local tracing"
url: "https://developers.cloudflare.com/changelog/post/2026-08-04-local-tracing/"
date: "2026-08-04"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
wrangler dev and vite dev automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations. Debug with AI agents When the tooling detects an AI agent session, it prints a terminal hint pointing to the Local Explorer API at /cdn-cgi/explorer/api . The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.
