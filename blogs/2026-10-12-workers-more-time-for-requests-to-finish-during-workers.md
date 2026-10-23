---
title: "Workers - More time for requests to finish during Workers runtime updates"
url: "https://developers.cloudflare.com/changelog/post/2026-10-12-longer-runtime-update-grace-period/"
date: "2026-10-12"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Pending requests and connections to Workers now have a grace period of up to 20 minutes during Workers runtime updates. Previously, the grace period was up to 30 seconds. This gives long-running HTTP requests, streamed AI responses, and live WebSocket sessions more time to continue before an update interrupts them.
