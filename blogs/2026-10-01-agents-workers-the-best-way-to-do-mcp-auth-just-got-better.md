---
title: "Agents, Workers - The best way to do MCP auth just got better: Workers OAuth Provider goes v1, with a new split API and full support for MCP 2026-07-28"
url: "https://developers.cloudflare.com/changelog/post/2026-10-01-workers-oauth-provider-1x/"
date: "2026-10-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
@cloudflare/workers-oauth-provider ↗︎ is now v1, with a new split API. One Worker acts as the authorization server: it signs users in and issues tokens. Your MCP server acts as the resource server, and can run in another Worker.
