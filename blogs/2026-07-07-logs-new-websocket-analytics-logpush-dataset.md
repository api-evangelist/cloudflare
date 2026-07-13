---
title: "Logs - New WebSocket Analytics Logpush dataset"
url: "https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/"
date: "2026-07-07"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Enterprise customers can now push per-connection WebSocket analytics to any Logpush destination using the new websocket_analytics dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling. Key fields include: ConnectionCloseReason — why the connection ended: peerReset , peerNoError , timedOut , upstreamReset , protocolViolation , unspecifiedError , or none .
