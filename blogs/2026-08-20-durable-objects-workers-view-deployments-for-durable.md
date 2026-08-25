---
title: "Durable Objects, Workers - View deployments for Durable Objects in the dashboard"
url: "https://developers.cloudflare.com/changelog/post/2026-08-20-durable-objects-deployments-tab/"
date: "2026-08-20"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Durable Object namespaces now have a Deployments tab in the Cloudflare dashboard, showing the versions of the backing Worker that are currently live and the traffic split between them. Go to Durable Objects ↗ A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a gradual deployment in progress for a Durable Object meant navigating to the backing Worker.
