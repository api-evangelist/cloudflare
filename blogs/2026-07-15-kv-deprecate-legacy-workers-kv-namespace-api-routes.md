---
title: "KV - Deprecate legacy Workers KV namespace API routes"
url: "https://developers.cloudflare.com/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/"
date: "2026-07-15"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
The legacy Workers KV API routes under /accounts/{account_id}/workers/namespaces/* are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented Workers KV API routes under /accounts/{account_id}/storage/kv/namespaces/* before that date. The legacy and replacement routes are interchangeable.
