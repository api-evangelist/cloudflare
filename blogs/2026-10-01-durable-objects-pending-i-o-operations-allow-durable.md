---
title: "Durable Objects - Pending I/O operations allow Durable Objects to continue long-running work without a connected client"
url: "https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/"
date: "2026-10-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Durable Objects remain active while handling a request from a connected client. This change applies when no client is connected, such as when an agent continues a submitted job after its client disconnects. This behavior is the default for Workers with a compatibility date of 2026-10-01 or later.
