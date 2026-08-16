---
title: "Gateway, Cloudflare One - Traffic Source selector in Gateway policies"
url: "https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/"
date: "2026-08-12"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Gateway HTTP and Network policies now include a Traffic Source selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint. Available traffic source values UI name API value Description Device client device_client Traffic from the Cloudflare One Client (WARP) Mesh mesh Traffic from a Cloudflare Mesh connector Cloudflare WAN cloudflare_wan Traffic from Cloudfla
