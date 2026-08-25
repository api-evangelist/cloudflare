---
title: "Analytics - WebSocket reporting now includes full connection data transfer"
url: "https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/"
date: "2026-08-14"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare has fixed an issue affecting WebSocket data transfer reporting. HTTP Traffic Analytics and HTTP request logs now correctly count data transferred throughout a WebSocket connection, restoring the correct behavior. During the affected period, reporting captured only the initial 101 Switching Protocols handshake for some WebSocket connections, which could underreport their data transfer.
