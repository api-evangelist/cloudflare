---
title: "Workers - Deploy larger Workers — up to 64 MiB for both free and paid plans"
url: "https://developers.cloudflare.com/changelog/post/2026-09-04-increased-worker-size-limit/"
date: "2026-09-04"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits. When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid).
