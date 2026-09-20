---
title: "Cache - Configure Origin Range Requests with the Rulesets API"
url: "https://developers.cloudflare.com/changelog/post/2026-09-02-origin-range-requests-rulesets-api/"
date: "2026-09-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The Rulesets API now supports Origin Range Requests in Cache Rules. This setting lets Cloudflare fetch large files from your origin in cache-aligned byte ranges. Cloudflare may expand a client range and issue several single-range origin requests.
