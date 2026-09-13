---
title: "Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting)"
url: "https://blog.cloudflare.com/automatic-key-exchange-for-origins/"
date: "2026-09-08"
author: "Suleman Ahmad"
feed_url: "https://blog.cloudflare.com/rss/"
---
Automatic Key Exchange probes TLS 1.3-capable customer origins to learn which key agreement algorithms they support. We then lead with the most secure algorithm when connecting to the origin, preferring post-quantum connections wherever the origin supports it.
