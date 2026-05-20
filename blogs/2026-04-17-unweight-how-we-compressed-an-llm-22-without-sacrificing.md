---
title: "Unweight: how we compressed an LLM 22% without sacrificing quality"
url: "https://blog.cloudflare.com/unweight-tensor-compression/"
date: "Fri, 17 Apr 2026 13:00:00 GMT"
author: "Chris Branch"
feed_url: "https://blog.cloudflare.com/rss/"
---
Running LLMs across Cloudflare’s network requires us to be smarter and more efficient about GPU memory bandwidth. That’s why we developed Unweight, a lossless inference-time compression system that achieves up to a 22% model footprint reduction, so that we can deliver faster and cheaper inference than ever before.
