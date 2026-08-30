---
title: "Workers, Durable Objects - Durable Objects can use up to ten Dynamic Workers concurrently"
url: "https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/"
date: "2026-08-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Durable Objects can have up to ten distinct Dynamic Workers with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.
