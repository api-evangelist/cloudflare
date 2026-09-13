---
title: "AI Gateway - AI Gateway custom costs support cache tokens"
url: "https://developers.cloudflare.com/changelog/post/2026-09-09-custom-cache-token-costs/"
date: "2026-09-09"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers. Add per_cache_read_token or per_cache_write_token to the cf-aig-custom-cost header: { "per_token_in" : 0.000001 , "per_token_out" : 0.000002 , "per_cache_read_token" : 0.0000001 , "per_cache_write_token" : 0.0000005 } Cache-token pricing activates when either cache rate is present.
