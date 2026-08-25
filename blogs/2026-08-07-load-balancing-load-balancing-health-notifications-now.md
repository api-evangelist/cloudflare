---
title: "Load Balancing - Load Balancing health notifications now resolve automatically"
url: "https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/"
date: "2026-08-07"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Load Balancing health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.
