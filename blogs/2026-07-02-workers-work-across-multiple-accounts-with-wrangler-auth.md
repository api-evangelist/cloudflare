---
title: "Workers - Work across multiple accounts with Wrangler auth profiles"
url: "https://developers.cloudflare.com/changelog/post/2026-07-02-wrangler-auth-profiles/"
date: "2026-07-02"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Wrangler CLI now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in. A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running wrangler login .
