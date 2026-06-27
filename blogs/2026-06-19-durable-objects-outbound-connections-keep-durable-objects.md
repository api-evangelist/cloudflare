---
title: "Durable Objects - Outbound connections keep Durable Objects alive"
url: "https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/"
date: "2026-06-19"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Active outbound connections via connect() or WebSocket now prevent Durable Object eviction during streaming operations like LLM responses. Objects remain alive for active connections up to 15 minutes, then standard eviction rules apply after connection closure.
