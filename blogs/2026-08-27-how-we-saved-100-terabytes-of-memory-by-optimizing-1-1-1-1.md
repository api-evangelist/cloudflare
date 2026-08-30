---
title: "How we saved 100 terabytes of memory by optimizing 1.1.1.1’s DNS cache"
url: "https://blog.cloudflare.com/dns-cache-memory-optimization-1111/"
date: "2026-08-27"
author: "Sebastiaan Neuteboom"
feed_url: "https://blog.cloudflare.com/rss/"
---
Five Rust-level memory optimizations to the DNS cache layout of Big Pineapple cut per-entry memory by 56%, freeing approximately 100 TB of memory across Cloudflare's fleet.
