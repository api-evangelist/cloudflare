---
title: "When DNSSEC goes wrong: how we responded to the .de TLD outage"
url: "https://blog.cloudflare.com/de-tld-outage-dnssec/"
date: "2026-05-06"
author: "Sebastiaan Neuteboom"
feed_url: "https://blog.cloudflare.com/rss/"
---
On May 5, 2026, at roughly 19:30 UTC, DENIC, the registry operator for the .de country-code top-level domain (TLD), started publishing incorrect DNSSEC signatures for the .de zone. Any validating DNS resolver receiving these signatures was required by the DNSSEC specification to reject them and return SERVFAIL to clients, including 1.1.1.1, the public DNS resolver operated by Cloudflare. The country-code top-level domain for Germany, .de, is one of the largest on the Internet. On Cloudflare Radar, it consistently ranks among the most broadly queried TLDs globally.
