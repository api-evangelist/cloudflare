---
title: "Workers AI - Reject busy synchronous inference requests"
url: "https://developers.cloudflare.com/changelog/post/2026-09-17-reject-if-busy/"
date: "2026-09-17"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The rejectIfBusy option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue. Pass the option as the third argument to the Workers AI binding: const response = await env.
