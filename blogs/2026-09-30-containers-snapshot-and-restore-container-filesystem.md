---
title: "Containers - Snapshot and restore Container filesystem"
url: "https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/"
date: "2026-09-30"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Containers now support snapshot APIs in public beta for saving and restoring point-in-time filesystem state. Create a snapshot first, then pass it back to start() to restore files after container sleep, restart, or handoff to another Durable Object. Use snapshotContainer() through the Durable Object Container API to capture the full container filesystem.
