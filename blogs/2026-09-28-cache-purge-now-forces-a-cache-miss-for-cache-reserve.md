---
title: "Cache - Purge now forces a cache miss for Cache Reserve content"
url: "https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/"
date: "2026-09-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Purge requests now force a cache miss for Cache Reserve content, regardless of purge type. Previously, purging by cache tag, hostname, prefix, or everything marked matching Cache Reserve content for revalidation. Purging by URL already removed content from Cache Reserve and is unchanged.
