---
title: "A broken DNSSEC rollover took down .al. Now 1.1.1.1 tells you when validation is bypassed"
url: "https://blog.cloudflare.com/dnssec-nta-ede-33/"
date: "2026-07-14"
author: "Sebastiaan Neuteboom"
feed_url: "https://blog.cloudflare.com/rss/"
---
When a failed DNSSEC key rollover took down the .al TLD, we deployed a Negative Trust Anchor to restore resolution. This time, though, clients didn't have to take our word for it: 1.1.1.1 returned EDE 33, a new DNS error code that signals directly in the response that DNSSEC validation was bypassed.
