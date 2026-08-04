---
title: "Workers, Durable Objects - Inspect Worker startup performance with Wrangler"
url: "https://developers.cloudflare.com/changelog/post/2026-07-31-wrangler-startup-profile-summary/"
date: "2026-07-31"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
wrangler check startup now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal. Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.
