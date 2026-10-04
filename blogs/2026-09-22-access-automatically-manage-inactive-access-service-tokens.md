---
title: "Access - Automatically manage inactive Access service tokens"
url: "https://developers.cloudflare.com/changelog/post/2026-09-22-service-token-inactivity-cleanup/"
date: "2026-09-22"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Access administrators can now automatically disable or delete inactive service tokens. Administrators can set an inactivity period from 30 to 365 days and choose what Access does when a token reaches that limit. To be eligible for cleanup, a token must be older than the configured period, must not have successfully authenticated during that period, and must not be directly referenced by an Access policy rule.
