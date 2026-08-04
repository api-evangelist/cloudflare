---
title: "Cloudflare One, Gateway - Control Cloudflare Gateway DNS caching with a maximum TTL setting"
url: "https://developers.cloudflare.com/changelog/post/2026-07-28-gateway-maximum-dns-ttl/"
date: "2026-07-28"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.
