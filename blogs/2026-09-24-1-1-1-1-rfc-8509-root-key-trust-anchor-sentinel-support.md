---
title: "1.1.1.1 - RFC 8509 root key trust anchor sentinel support"
url: "https://developers.cloudflare.com/changelog/post/2026-09-24-root-key-trust-anchor-sentinel/"
date: "2026-09-24"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
1.1.1.1 now supports RFC 8509 ↗︎ root key trust anchor sentinels. They let you check whether the responding resolver trusts a DNSSEC root key ahead of a key rollover. To check for KSK-2024 (key tag 38696), query DNSSEC-signed names in dnstest.dev : # On a sentinel-aware resolver that trusts KSK-2024: # Returns NOERROR with an A answer.
