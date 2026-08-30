---
title: "Cloudflare One, Access - MCP server portals support MCP 2026-07-28 specification"
url: "https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/"
date: "2026-08-25"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
MCP server portals support the stateless MCP 2026-07-28 specification for client and upstream server connections. The portal's /mcp endpoint automatically accepts stateless MCP 2026-07-28 requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP 2026-07-28 support and falls back to the 2025 handshake when needed.
