---
title: "D1 - D1 enforces free tier daily query limits"
url: "https://developers.cloudflare.com/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/"
date: "2026-09-01"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Beginning September 1, 2026, D1 queries on the Workers Free plan will fail when an account exceeds the daily row read or row write limits . Queries via the Workers Binding API and the REST API will return errors until the limit resets at midnight UTC. Stored data is not affected.
