---
title: "Logs, Log Explorer - Per-zone post-quantum visibility in Logpush and Log Explorer"
url: "https://developers.cloudflare.com/changelog/post/2026-08-20-pqc-key-exchange-visibility/"
date: "2026-08-20"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
Cloudflare Radar ↗ publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the http_requests Logpush dataset — also queryable in Log Explorer — includes a new ClientTLSKeyExchangeGroup field. The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name.
