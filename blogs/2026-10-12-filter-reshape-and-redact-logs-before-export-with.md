---
title: "Filter, reshape, and redact logs before export with Transformers"
url: "https://blog.cloudflare.com/transformers-on-logpush/"
date: "2026-10-12"
author: "Rob Taylor"
feed_url: "https://blog.cloudflare.com/rss/"
---
Logpush now supports Transformers, allowing teams to filter, redact, and reshape log streams using SQL before export. Powered by Apache DataFusion and Apache Arrow, Transformers apply those changes directly to log data before it reaches the destination.
