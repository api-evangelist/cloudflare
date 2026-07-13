---
title: "Cloudflare One, Access - Service token support for MCP server portals"
url: "https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/"
date: "2026-06-26"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now connect autonomous agents and bots to an MCP server portal using an Access service token . Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow. To set this up: Add a Service Auth policy that matches your service token to the portal's Access application.
