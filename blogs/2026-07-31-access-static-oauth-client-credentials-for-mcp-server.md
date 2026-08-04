---
title: "Access - Static OAuth client credentials for MCP server portals"
url: "https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/"
date: "2026-07-31"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
MCP server portals can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.
