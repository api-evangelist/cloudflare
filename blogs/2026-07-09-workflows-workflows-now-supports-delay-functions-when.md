---
title: "Workflows - Workflows now supports delay functions when retrying"
url: "https://developers.cloudflare.com/changelog/post/2026-07-09-dynamic-retry-delays/"
date: "2026-07-09"
feed_url: "https://developers.cloudflare.com/changelog/rss/index.xml"
---
With Workflows , you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as constant , linear , or exponential . Step retries now support dynamic delay functions.
